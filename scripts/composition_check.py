#!/usr/bin/env python3
"""Composition check: measures how a piece sits in its frame and fails the framings the client has rejected.

  python3 composition_check.py <image|video> [...] --format card|reel|still|square|detail|lineup|auto
                               [--set] [--allow-top] [--allow-bleed] [--json out.json] [--overlay dir]

  --format   which frame rules apply (references/composition.md, section 3). auto picks from the aspect ratio:
             9:16 -> reel, 4:5 -> card, 1:1 -> square, wide -> lineup.
  --set      the inputs are one set (site cards, a carousel, a lineup): also fail when they don't share one fill,
             one floor line and one centre (the "all over the place" check).
  --allow-top    the piece is ceiling-hung and its canopy is meant to run off the top edge (cards.json flush_top).
  --allow-bleed  a deliberate detail crop the client asked for; edge contact becomes a note, not a fail.
  --ignore x0,y0,x1,y1  leave a region out (fractions of the frame), e.g. a plinth that runs off the bottom of a reel:
             --ignore 0,0.66,1,1. Say why in the piece's notes. The studio overlay (green chips, crop marks, corner
             text) is stripped automatically.
  --overlay  writes each frame with the subject box, margins, safe zone and the centred square/3:4 grid crops drawn on.
  Videos: checks frames at 0, 25, 50, 75 % and the last frame, plus every 0.5 s for edge cuts (the widest pose).

Works on renders on white or light grey seamless (the studio look): the background is modelled from the frame border
(a smooth quadratic, so a seamless gradient and the floor falloff are background), soft contact shadows are dropped
(low contrast and no texture), and what is left is the subject. It does not judge the design, only the framing.

Exit 0 when every input passes, 1 on any FAIL. Prints one line per finding:
  FAIL CUT card.jpg: subject touches the left edge (piece cut off by the frame)
Codes: CUT EDGE SMALL BIG OFFCENTRE LOW HIGH SAFE SQUARE GRID3x4 SPREAD FLOOR STRAY SPARSE BUSY BORDER BALANCE TILT and, with --set,
SETFILL SETFLOOR SETCENTRE. Thresholds live in PROFILES below and are explained, with their sources, in
references/composition.md. Never loosen one to make a render pass: fix the camera.

Needs numpy, Pillow, scipy (ffmpeg on PATH for videos).
"""
import sys, os, json, math, subprocess, tempfile, glob
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi

Image.MAX_IMAGE_PIXELS = None

# Every number here is in references/composition.md with its reason. Fractions of the frame.
PROFILES = {
    # site index card, 4:5 720x900 loop (studio look section 9): subject fills 86 % on its limiting axis, centred,
    # floor line a little low, and it must survive the grid's centred square crop.
    'card':   dict(fill=(0.78, 0.90), margin=0.02, cx=0.04, cy=(0.48, 0.57), square=True, grid34=False, safe=None),
    # reel / TikTok frame 1080x1920: piece 40-60 % of frame height, inside the safe zone, centred.
    'reel':   dict(fill_h=(0.40, 0.60), margin=0.059, cx=0.05, cy=(0.40, 0.56), square=False, grid34=True,
                   safe=(220 / 1920, 380 / 1920, 64 / 1080)),
    # hero still / carousel frame 4:5: whole object 55-70 % of frame height with air (seamless above it).
    'still':  dict(fill_h=(0.50, 0.75), fill=(0.0, 0.85), margin=0.06, cx=0.06, cy=(0.47, 0.60), square=False,
                   grid34=False, safe=None),
    # square: grid cover, the reel's closing crop, IG square, spec squares on the page.
    'square': dict(fill=(0.66, 0.88), margin=0.05, cx=0.04, cy=(0.47, 0.56), square=False, grid34=False, safe=None),
    # detail / close-up: the feature whole with air (Moth reel critique); fill may be high but nothing cut.
    'detail': dict(fill=(0.45, 0.92), margin=0.03, cx=0.10, cy=(0.40, 0.62), square=False, grid34=False, safe=None),
    # lineup / banner / family frame: one floor line, nothing touching, nothing at the edges.
    'lineup': dict(fill_h=(0.35, 0.85), margin=0.04, cx=0.08, cy=(0.40, 0.62), square=False, grid34=False, safe=None),
}


def load_rgb(path, maxside=600):
    """RGB in 0-1, plus the alpha mask when the file carries real transparency (a render with Film > Transparent:
    the exact silhouette, best for white parts on white)."""
    src = Image.open(path)
    alpha = None
    if src.mode in ('RGBA', 'LA') or 'transparency' in src.info:
        a = src.convert('RGBA').getchannel('A')
        if a.getextrema()[0] < 250:
            alpha = a
    im = src.convert('RGBA')
    bgw = Image.new('RGBA', im.size, (243, 243, 243, 255))   # card fill under a transparent render
    im = Image.alpha_composite(bgw, im).convert('RGB')
    s = maxside / max(im.size)   # one working size, so gradient thresholds mean the same on every input
    if s != 1:
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        if alpha is not None:
            alpha = alpha.resize(im.size, Image.LANCZOS)
    load_rgb.alpha = None if alpha is None else (np.asarray(alpha) > 127)
    return np.asarray(im).astype(np.float32) / 255.0


def to_lab(rgb):
    c = np.where(rgb > 0.04045, ((rgb + 0.055) / 1.055) ** 2.4, rgb / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.9505, 1.0, 1.089])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def fit_background(lab, bgmask):
    """Quadratic surface per Lab channel fitted to background pixels: a seamless gradient and floor falloff stay bg."""
    H, W = lab.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W]
    x, y = xx / W - 0.5, yy / H - 0.5
    A = np.stack([np.ones_like(x), x, y, x * x, y * y, x * y], -1)
    idx = np.flatnonzero(bgmask.ravel())
    if len(idx) > 40000:
        idx = idx[np.random.default_rng(0).choice(len(idx), 40000, replace=False)]
    Af = A.reshape(-1, 6)
    out = np.empty_like(lab)
    for ch in range(3):
        coef, *_ = np.linalg.lstsq(Af[idx], lab.reshape(-1, 3)[idx, ch], rcond=None)
        out[..., ch] = (Af @ coef).reshape(H, W)
    return out


def subject_mask(rgb):
    lab = to_lab(rgb)
    H, W = lab.shape[:2]
    b = max(2, int(0.02 * min(H, W)))
    border = np.zeros((H, W), bool)
    border[:b], border[-b:], border[:, :b], border[:, -b:] = True, True, True, True
    # start from the border, then refit on everything that looks like background
    med = np.median(lab[border], 0)
    bg = np.linalg.norm(lab - med, axis=-1) < 6
    bg &= True
    model = fit_background(lab, bg | border & (np.linalg.norm(lab - med, axis=-1) < 10))
    for _ in range(2):
        d = np.linalg.norm(lab - model, axis=-1)
        model = fit_background(lab, d < 5)
    d = lab - model
    dE = np.linalg.norm(d, axis=-1)
    dL, dC = d[..., 0], np.hypot(d[..., 1], d[..., 2])
    # texture: local gradient of L. Contact shadows are soft (no texture), neutral and darker than the floor.
    gy, gx = np.gradient(ndi.gaussian_filter(lab[..., 0], 1.0))
    grad = ndi.maximum_filter(np.hypot(gx, gy), 3)
    strong = dE > 22
    shadowish = (dL < 0) & (dC < 6) & (grad < 2.2)
    textured = (dE > 7) & (grad > 2.2)
    # white-on-white parts: faint fill but crisp silhouette edges; close the edge outline and fill it
    edges = (dE > 1.8) & (grad > 1.1)
    m = (strong & ~(shadowish & (dE < 34))) | textured
    m = ndi.binary_opening(m, iterations=1)
    rr = max(2, int(0.006 * max(H, W)))
    outline = ndi.binary_fill_holes(ndi.binary_closing(edges | m, iterations=rr))
    outline = ndi.binary_opening(outline, iterations=rr)
    m = ndi.binary_closing(m | outline, iterations=2)
    m = ndi.binary_fill_holes(m)
    lbl, n = ndi.label(m)
    if n:
        sizes = ndi.sum(m, lbl, range(1, n + 1))
        keep = np.isin(lbl, 1 + np.flatnonzero(sizes >= 0.0004 * H * W))
        m = keep
    # background clutter: texture in what is left as background
    busy = float(((grad > 3.0) & ~ndi.binary_dilation(m, iterations=6)).mean())
    # boundary simplicity (FLMS, Fang et al. 2014): the frame edge should run through plain ground
    e = max(2, int(0.01 * min(H, W)))
    band = np.concatenate([grad[:e].ravel(), grad[-e:].ravel(), grad[:, :e].ravel(), grad[:, -e:].ravel()])
    subject_mask.border = float((band > 3.0).mean())
    return m, busy


def pieces(m):
    """Group mask blobs into pieces: parts closer than ~2.5 % of the frame diagonal are one piece."""
    H, W = m.shape
    r = max(2, int(0.025 * math.hypot(H, W) / 2))
    lbl, n = ndi.label(ndi.binary_dilation(m, iterations=r))
    out = []
    for i in range(1, n + 1):
        pm = m & (lbl == i)
        if not pm.any():
            continue
        ys, xs = np.nonzero(pm)
        out.append(dict(area=float(pm.mean()), box=(xs.min() / W, ys.min() / H, (xs.max() + 1) / W, (ys.max() + 1) / H)))
    out.sort(key=lambda p: -p['area'])
    return out


def strip_overlay(rgb, m):
    """Drop the studio overlay so it is not taken for the subject: accent chips (#1D847E and the white type on them),
    crop marks and corner text (anything small inside the 9 % corner boxes)."""
    H, W = m.shape
    acc = np.array([29, 132, 126]) / 255.0
    chip = np.linalg.norm(rgb - acc, axis=-1) < 0.16
    chip = ndi.binary_dilation(chip, iterations=4)
    m = m & ~ndi.binary_fill_holes(ndi.binary_closing(chip, iterations=3))
    lbl, n = ndi.label(m)
    if n:
        cy, cx = H * 0.09, W * 0.09
        for i, sl in enumerate(ndi.find_objects(lbl), 1):
            h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
            in_corner = ((sl[0].stop < cy or sl[0].start > H - cy) and (sl[1].stop < W * 0.35 or sl[1].start > W * 0.65)) or \
                        ((sl[1].stop < cx or sl[1].start > W - cx) and (sl[0].stop < H * 0.2 or sl[0].start > H * 0.8))
            if in_corner and h * w < 0.01 * H * W:
                m[lbl == i] = False
    return m


def measure(rgb, alpha=None, ignore=()):
    m, busy = subject_mask(rgb)
    if alpha is not None and alpha.shape == m.shape:
        m = alpha
    m = strip_overlay(rgb, m)
    H, W = m.shape
    for x0, y0, x1, y1 in ignore:
        m[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] = False
    H, W = m.shape
    if not m.any():
        return None, m
    ys, xs = np.nonzero(m)
    x0, x1, y0, y1 = xs.min() / W, (xs.max() + 1) / W, ys.min() / H, (ys.max() + 1) / H
    bw, bh = x1 - x0, y1 - y0
    cx_mass, cy_mass = xs.mean() / W, ys.mean() / H
    # principal axis of the silhouette (tilt of the long axis)
    cov = np.cov(np.stack([xs / W * (W / H), ys / H]))
    ev, evec = np.linalg.eigh(cov)
    ang = math.degrees(math.atan2(evec[1, 1], evec[0, 1]))
    elong = math.sqrt(ev[1] / max(ev[0], 1e-9))
    edge = dict(left=bool(m[:, :2].any()), right=bool(m[:, -2:].any()), top=bool(m[:2].any()), bottom=bool(m[-2:].any()))
    ps = pieces(m)
    gaps = []
    if len(ps) > 1:
        bx = sorted(ps, key=lambda p: p['box'][0])
        for a, b in zip(bx, bx[1:]):
            gaps.append(max(0.0, b['box'][0] - a['box'][2]))
    big = [p for p in ps if p['area'] >= 0.15 * ps[0]['area']]
    floor = [p['box'][3] for p in big]
    return dict(
        w=W, h=H, aspect=W / H, box=[round(v, 4) for v in (x0, y0, x1, y1)], fill_w=round(bw, 3), fill_h=round(bh, 3),
        fill=round(max(bw, bh * H / W if W < H else bh) if False else max(bw, bh), 3),
        area=round(float(m.mean()), 4), occupancy=round(float(m.mean()) / max(bw * bh, 1e-9), 3),
        margins=dict(left=round(x0, 3), right=round(1 - x1, 3), top=round(y0, 3), bottom=round(1 - y1, 3)),
        centre=[round((x0 + x1) / 2, 3), round((y0 + y1) / 2, 3)], mass=[round(cx_mass, 3), round(cy_mass, 3)],
        border_busy=round(getattr(subject_mask, 'border', 0.0), 4), edge=edge, tilt=round(ang, 1), elong=round(elong, 2), busy=round(busy, 4),
        pieces=len(ps), big_pieces=len(big), piece_boxes=[[round(v, 3) for v in p['box']] for p in big],
        gaps=[round(g, 3) for g in gaps], floor_spread=round(max(floor) - min(floor), 3) if len(floor) > 1 else 0.0,
        stray=sum(1 for p in ps if p['area'] < 0.15 * ps[0]['area'])), m


def guess_format(aspect):
    if aspect < 0.62:
        return 'reel'
    if aspect < 0.9:
        return 'card' if abs(aspect - 0.8) < 0.03 else 'still'
    if aspect < 1.12:
        return 'square'
    return 'lineup'


def judge(r, fmt, allow_top=False, allow_bleed=False):
    P = PROFILES[fmt]
    out = []  # (level, code, text)
    def add(level, code, text):
        out.append((level, code, text))
    mg = r['margins']
    # 1. cut by the frame (Nave "here specfically", Moth reel "crops cut things off", G10 whole work)
    for side, touch in r['edge'].items():
        if touch and not (side == 'top' and allow_top):
            add('NOTE' if allow_bleed else 'FAIL', 'CUT', f'subject touches the {side} edge (piece cut off by the frame)')
    for side, v in mg.items():
        if r['edge'][side] or (side == 'top' and allow_top):
            continue
        if v < P['margin']:
            add('FAIL', 'EDGE', f'{side} margin {v:.1%} < {P["margin"]:.1%}: the piece needs air on every side')
    # 2. size in frame
    if 'fill' in P:
        lo, hi = P['fill']
        f = max(r['fill_w'], r['fill_h'])
        if f < lo:
            add('FAIL', 'SMALL', f'subject fills {f:.0%} of the frame on its limiting axis; {fmt} wants {lo:.0%}-{hi:.0%}')
        elif f > hi:
            add('FAIL', 'BIG', f'subject fills {f:.0%} on its limiting axis; over {hi:.0%} it crowds the frame')
    if 'fill_h' in P:
        lo, hi = P['fill_h']
        f = r['fill_h']
        if f < lo and not (fmt == 'lineup'):
            add('FAIL', 'SMALL', f'subject is {f:.0%} of the frame height; {fmt} wants {lo:.0%}-{hi:.0%}')
        elif f < lo:
            add('WARN', 'SMALL', f'lineup is {f:.0%} of the frame height; under {lo:.0%} reads as a strip')
        elif f > hi:
            add('FAIL', 'BIG', f'subject is {f:.0%} of the frame height; {fmt} wants at most {hi:.0%}')
    # 3. placement: centred products (centre beats thirds for a lone object; composition.md section 2)
    cx, cy = r['centre']
    if abs(cx - 0.5) > P['cx']:
        add('FAIL', 'OFFCENTRE', f'subject centre at x {cx:.0%}; keep it within {P["cx"]:.0%} of the middle')
    lo, hi = P['cy']
    if cy < lo and not allow_top:
        add('FAIL', 'HIGH', f'subject centre at y {cy:.0%}; it floats high (floor line belongs a little low)')
    elif cy > hi:
        add('FAIL', 'LOW', f'subject centre at y {cy:.0%}; too much empty space above it')
    mx = r['mass'][0]
    if abs(mx - 0.5) > P['cx'] + 0.06:
        add('WARN', 'BALANCE', f'visual mass sits at x {mx:.0%}: the frame tips to one side')
    # 4. safe zone for vertical video
    if P['safe']:
        t, b, s = P['safe']
        if mg['top'] < t or mg['bottom'] < b or mg['left'] < s or mg['right'] < s:
            add('FAIL', 'SAFE', f'subject enters the reel safe zone (top {t:.0%}, bottom {b:.0%}, sides {s:.0%} are UI)')
    # 5. survives the crops the grid makes (cards: square; reels: the 3:4 profile-grid window)
    x0, y0, x1, y1 = r['box']
    if P['square'] and r['aspect'] < 1:
        hh = r['aspect']  # square side as a fraction of frame height
        top, bot = 0.5 - hh / 2, 0.5 + hh / 2
        if y0 < top + 0.01 and not allow_top or y1 > bot - 0.01:
            add('WARN', 'SQUARE', f'subject spans y {y0:.0%}-{y1:.0%}; the centred square crop keeps only {top:.0%}-{bot:.0%}')
    if P['grid34'] and r['aspect'] < 0.75:
        hh = r['aspect'] / 0.75
        top, bot = 0.5 - hh / 2, 0.5 + hh / 2
        if y0 < top or y1 > bot:
            add('WARN', 'GRID3x4', f'subject spans y {y0:.0%}-{y1:.0%}; the profile grid shows only {top:.0%}-{bot:.0%}')
    # 6. groups: one composition, not scattered (Rachis "distance between the two is a bit much"; Ogive, Bombyx)
    if r['big_pieces'] > 1:
        widths = [b[2] - b[0] for b in r['piece_boxes']]
        g = max(r['gaps']) if r['gaps'] else 0
        if g > 0.6 * (sum(widths) / len(widths)):
            add('FAIL', 'SPREAD', f'largest gap between pieces {g:.0%} of the frame width > 0.6x a piece: they read as separate pictures')
        if r['floor_spread'] > 0.04 and fmt in ('lineup', 'card', 'still'):
            add('WARN', 'FLOOR', f'piece bases differ by {r["floor_spread"]:.0%} of the frame height: put a lineup on one floor line')
    if r['stray'] and r['big_pieces'] >= 1 and fmt != 'detail':
        add('WARN', 'STRAY', f'{r["stray"]} small separate bit(s) in frame: a part or prop drifting away from the group')
    if r['occupancy'] < 0.18 and fmt != 'lineup':
        add('WARN', 'SPARSE', f'subject covers {r["occupancy"]:.0%} of its own box: scattered pieces with dead space between')
    # 7. clean ground
    if r['busy'] > 0.02:
        add('FAIL', 'BUSY', f'background texture {r["busy"]:.1%} of the frame: the studio ground must be clean')
    if r.get('border_busy', 0) > 0.08 and not any(c == 'CUT' for _, c, _ in out):
        add('WARN', 'BORDER', f'{r["border_busy"]:.0%} of the frame edge crosses detail: let the edge run through plain ground')
    # 8. diagonal subject in a reel (Nave: tilted diagonal framing rejected)
    if fmt == 'reel' and r['elong'] > 2.2 and 25 < abs(abs(r['tilt']) - 90) < 65:
        add('WARN', 'TILT', f'long axis at {r["tilt"]:.0f} deg: keep a long piece square-on, long axis on the frame long axis')
    return out


def overlay(path, rgb, r, fmt, outdir):
    im = Image.fromarray((rgb * 255).astype(np.uint8)).convert('RGB')
    d = ImageDraw.Draw(im)
    W, H = im.size
    x0, y0, x1, y1 = r['box']
    d.rectangle([x0 * W, y0 * H, x1 * W, y1 * H], outline=(29, 132, 126), width=2)
    for b in r['piece_boxes']:
        d.rectangle([b[0] * W, b[1] * H, b[2] * W, b[3] * H], outline=(160, 160, 160), width=1)
    if r['aspect'] < 1:
        s = W
        d.rectangle([0, (H - s) / 2, W - 1, (H + s) / 2], outline=(200, 60, 60), width=1)
    P = PROFILES[fmt]
    if P['safe']:
        t, b, s = P['safe']
        d.rectangle([s * W, t * H, (1 - s) * W, (1 - b) * H], outline=(230, 150, 0), width=1)
    d.line([W / 2, 0, W / 2, H], fill=(220, 220, 220))
    os.makedirs(outdir, exist_ok=True)
    im.save(os.path.join(outdir, os.path.splitext(os.path.basename(path))[0] + '_comp.jpg'), quality=85)


def video_frames(path, tmp):
    p = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                       capture_output=True, text=True)
    dur = float(p.stdout.strip() or 0)
    ts = sorted(set([0.0] + [dur * f for f in (0.25, 0.5, 0.75)] + [max(0, dur - 0.05)] +
                    [i * 0.5 for i in range(int(dur / 0.5))]))
    out = []
    for t in ts:
        f = os.path.join(tmp, f'f{t:07.2f}.png')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', path, '-frames:v', '1', f])
        if os.path.exists(f):
            out.append((t, f))
    return out


def main():
    a = sys.argv[1:]
    def opt(k, d=None):
        return a[a.index(k) + 1] if k in a else d
    flags = {'--set', '--allow-top', '--allow-bleed'}
    vals = {'--format', '--json', '--overlay', '--ignore'}
    files, i = [], 0
    while i < len(a):
        if a[i] in vals:
            i += 2; continue
        if a[i] in flags:
            i += 1; continue
        files.extend(sorted(glob.glob(a[i])) or [a[i]]); i += 1
    if not files:
        print(__doc__); sys.exit(2)
    fmt_opt = opt('--format', 'auto')
    allow_top, allow_bleed, is_set = '--allow-top' in a, '--allow-bleed' in a, '--set' in a
    ignore = [tuple(float(v) for v in a[i + 1].split(',')) for i, x in enumerate(a) if x == '--ignore']
    results, bad = [], False
    tmp = tempfile.mkdtemp()
    for f in files:
        frames = video_frames(f, tmp) if f.lower().endswith(('.mp4', '.mov', '.webm', '.m4v')) else [(None, f)]
        vid_find, vid_r = {}, None
        for t, fr in frames:
            rgb = load_rgb(fr)
            r, _ = measure(rgb, getattr(load_rgb, 'alpha', None), ignore)
            label = os.path.basename(f) + (f'@{t:.1f}s' if t is not None else '')
            if r is None:
                print(f"FAIL EMPTY {label}: no subject on a light ground (a blank frame, a full-colour card, or a dark set)"); bad = True; continue
            fmt = guess_format(r['aspect']) if fmt_opt == 'auto' else fmt_opt
            finds = judge(r, fmt, allow_top, allow_bleed)
            if t is not None:
                # video: CUT/EDGE/SAFE count on any sampled frame (the widest pose); the rest on the key frames
                key = t == 0.0 or any(abs(t - k) < 1e-6 for k in (frames[-1][0],)) or t in [fr_[0] for fr_ in frames[:1]]
                for lv, code, txt in finds:
                    if code in ('CUT', 'EDGE', 'SAFE') or key:
                        vid_find.setdefault(code, (lv, code, f'{txt} [{t:.1f}s]'))
                if t == 0.0:
                    vid_r = r
                if opt('--overlay') and t == 0.0:
                    overlay(f, rgb, r, fmt, opt('--overlay'))
                continue
            if opt('--overlay'):
                overlay(fr, rgb, r, fmt, opt('--overlay'))
            results.append(dict(file=f, format=fmt, metrics=r, findings=[dict(level=l, code=c, text=x) for l, c, x in finds]))
        if vid_find or vid_r:
            results.append(dict(file=f, format=fmt, metrics=vid_r, findings=[dict(level=l, code=c, text=x) for l, c, x in vid_find.values()]))
    if is_set and len(results) > 1:
        fills = [max(x['metrics']['fill_w'], x['metrics']['fill_h']) for x in results if x['metrics']]
        floors = [x['metrics']['box'][3] for x in results if x['metrics']]
        cys = [x['metrics']['centre'][1] for x in results if x['metrics']]
        setf = []
        if max(fills) - min(fills) > 0.14:
            setf.append(('FAIL', 'SETFILL', f'fill ranges {min(fills):.0%}-{max(fills):.0%} across the set: one tile tight, another floating small'))
        if max(floors) - min(floors) > 0.08:
            setf.append(('WARN', 'SETFLOOR', f'floor line ranges {min(floors):.0%}-{max(floors):.0%} across the set'))
        if max(cys) - min(cys) > 0.10:
            setf.append(('WARN', 'SETCENTRE', f'subject height in frame ranges {min(cys):.0%}-{max(cys):.0%} across the set'))
        results.append(dict(file='(set)', format='set', metrics=dict(fills=fills, floors=floors),
                            findings=[dict(level=l, code=c, text=x) for l, c, x in setf]))
    for x in results:
        fails = [y for y in x['findings'] if y['level'] == 'FAIL']
        bad |= bool(fails)
        m = x['metrics'] or {}
        head = 'PASS' if not fails else 'FAIL'
        summ = '' if not m or 'box' not in m else (f" fill {max(m['fill_w'], m['fill_h']):.0%} (h {m['fill_h']:.0%})"
                                                   f" centre {m['centre'][0]:.0%},{m['centre'][1]:.0%} pieces {m['big_pieces']}")
        print(f"{head} composition {os.path.basename(x['file'])} [{x['format']}]{summ}")
        for y in x['findings']:
            print(f"  {y['level']} {y['code']}: {y['text']}")
    if opt('--json'):
        json.dump(results, open(opt('--json'), 'w'), indent=1)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

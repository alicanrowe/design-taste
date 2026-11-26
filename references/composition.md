# Composition: how a piece sits in its frame (26 Nov 2026)

The client, 26 Nov 2026: "i think ur taste skill is not getting composition yet". This file is the composition part of
the taste: framing, air round the piece, camera height and lens, crops to square, and groups. Every rule is checkable,
and most are checked by `scripts/composition_check.py` (section 7).

**Order of authority.** The client's own critique (critique-log.md, principles.md, banned-moves.md) wins, then the
studio look (`studio-look.md` / brand LOOK.md), then this file's outside sources. Where outside practice disagrees with
the client, the client's rule stands and the conflict is listed in section 8. Outside numbers are paraphrased and
cited (section 9); no outside images or data are kept here.

## 1. The five things that decide a frame
1. **Whole and with air.** Every part of the piece is inside the frame with a clear margin on every side, in every
   pose of a move (check the widest pose: modules apart, doors open). The frame edge runs through plain ground, never
   through the piece. ("a few of your crops are pretty close and cut things off", Moth reel 23 Nov; "this framing is a
   bit awkward" + the tray cut at the edge, Nave 23 Nov; G10 whole work.) Outside agreement: crop research weights
   "the frame edge passes through simple areas" as its own term (FLMS, Fang et al. 2014).
2. **Size set by format, not by eye.** Each format has one fill band (section 3). Inside a set every frame uses the
   same band, so no tile is tight while its neighbour floats small ("these previews are actually all over the
   place", 26 Nov).
3. **Centred, floor line a little low.** A lone product sits on the vertical centre line, its box centre at 48 to 57 % (cards; other formats in section 3)
   of the frame height, so there is slightly more air above than below. Thirds placement is for scenes, not for a
   lone object on seamless (section 8).
4. **Square-on, long axis on the long axis.** The piece's long axis runs along the frame's long axis; no tilted or
   diagonal framing of the object in reels ("the tilted diagonal framing", Nave 23 Nov). The camera is level; verticals
   stay vertical.
5. **A group is one picture.** Several pieces sit close enough to read as one composition, on one floor line, at one
   real scale, nothing touching ("the distance between the too is a bit much", Rachis 23 Nov; "scale seems random",
   GitHub banner 25 Nov). A pendant never floats beside a floor piece (Rachis card, 26 Nov).

## 2. Camera height and lens
- **Lens: long, calm.** 85 to 105 mm full-frame equivalent for heroes and details (50 mm only when the room is the
  subject). The site cards are orthographic, which is the limit of a long lens. Wide angles exaggerate the near side:
  the enlargement of a feature standing h above the surface, seen from distance D, is about h / (D - h); a 48 mm tall
  object shot from 250 mm is drawn 24 % too big at its top, from 1 m only 5 % (PHOTARCH). So keep the camera far and the
  lens long. One lens, one distance, one aperture across every piece of a set (museum practice; G7 set parity).
- **Height by kind of piece** (outside practice, matched to our cards):
  | Piece | Camera | Why |
  |---|---|---|
  | Furniture (chairs, benches, cabinets) | lens at about half the piece's height, or a little above and tilted down 10 to 20 deg to show the seat or top | reads the proportion honestly; a high camera shrinks legs |
  | Jewelry rings | 3/4, from above 25 to 40 deg | shows the setting and the band (cards: 24 to 38 deg) |
  | Earrings, pendants | 3/4 or side, at the piece's height; drops get a side view | shows the hang |
  | Necklaces, sets of small pieces | straight on, or top-down for a laid group | a flat lay keeps a set tidy |
  | Lamps, standing pieces | at mid-height, level | no looking up a stem |
  | Hanging pieces | at eye level, canopy off the top edge or at the top margin | the client: hang it the way it is used |
  | Machines, robots | 3/4 at mid-height; low only when it must feel big | |
  | Site index cards | orthographic 3/4 from front left, az 214, el 17 (studio-look section 9) | one camera for all |
- **Three-quarter hero is 30 to 45 deg off the front**, elevation as above. Front, side and back views are square-on
  and level (they are the drawing's base).
- Depth of field: hero sharp front to back; details may soften the background, never the feature.

## 3. Fill bands by format (what the checker enforces)
Fractions are of the frame; "limiting axis" means whichever of width or height the piece fills more.
| Format | Fill | Margins | Centre | Extra |
|---|---|---|---|---|
| Site card 4:5 (720 x 900 loop) | 78 to 90 % on the limiting axis (target 86 %, studio look) | 2 % min each side | x within 4 % of centre, y 48 to 57 % | ceiling pieces may run off the top (`--allow-top`) |
| Reel / TikTok 9:16 | piece 40 to 60 % of frame height | outside the safe zone: top 220, bottom 380, sides 64 px of 1080 x 1920 | x within 5 %, y 40 to 56 % | warns if the piece leaves the 3:4 profile-grid window |
| Hero still / carousel 4:5 | 50 to 75 % of frame height, at most 85 % of width | 6 % min | x within 6 %, y 47 to 60 % | seamless above it |
| Square (grid cover, closing crop, spec squares) | 66 to 88 % | 5 % | x within 4 %, y 47 to 56 % | |
| Detail / close-up | 45 to 92 %: the whole feature (a casting, a joint) with air | 3 % | x within 10 % | a bleed crop only when the client asks (`--allow-bleed`) |
| Lineup / banner / family | 35 to 85 % of frame height | 4 % | x within 8 % | one floor line; gaps under 0.6 x a piece's width |
Outside cross-checks: marketplaces want the product to fill 75 to 90 % of a square main image (Google Merchant Center
best practice) or about 85 % (Amazon main image, from seller summaries); our card band sits inside both. In a study of
200+ professional photos the main subject covered about 0.56 or 0.82 of the frame for object shots (Liu et al. 2010);
our hero and card bands match those two peaks.

## 4. Crop to square
- The reel's closing crop and the grid cover: a centred square on white, the piece 66 to 88 % of the square, centred.
- A 4:5 card or still must keep the whole piece inside the centred square if the grid shows a square (the check warns
  with SQUARE). A tall piece filling 86 % of a 4:5 height cannot fit a 4:5 square window (it holds 80 %), so where the
  site shows the card uncropped, SQUARE is a warning only; G10 forbids any page from square-cropping a card that does
  not fit.
- A 9:16 reel shows on the profile grid as a centred 3:4 window (the middle 75 % of the height): the piece should sit in
  it on frame 1 and on the cover (GRID3x4 warning).
- Leave enough ground round a still that it can be cropped to square, portrait and landscape without touching the piece
  (marketplace practice, Etsy).

## 5. Groups and families
- One subject doing one thing, or a tight pair (banned-moves: too much going on). For a family card, all the family.
- Gap between neighbours: under about 0.6 x the mean piece width; nothing touching or overlapping in silhouette unless
  one sits in front of the other on purpose. Pieces share one floor line (bases within 4 % of the frame height), apart
  from a hanging piece, which is shot on its own.
- True relative scale, never each fitted to its own box. Jewelry with furniture: a small quiet pair, names only.
- Odd counts (3, 5) group into a triangle more easily than even ones; past six or seven items a group reads as a
  pattern, so lay it out as a pattern (a row, a grid) on purpose (outside practice).
- No stray bit: a ring, a prop or a part sitting far from the rest reads as dropped (STRAY).

## 6. Ground
- White or #F3F3F3 seamless with a soft contact shadow; nothing textured on the ground (BUSY). The shadow is part of
  the ground, not the subject: it may run to the edge.
- Background far enough behind that it stays plain (museum practice).

## 7. The automatic check
`python3 scripts/composition_check.py <files or videos> --format card|reel|still|square|detail|lineup|auto [--set]
[--allow-top] [--allow-bleed] [--overlay <dir>] [--json out.json]`

It models the ground from the frame border (a smooth fit, so a seamless gradient and the shadow stay ground), keeps
crisp silhouette edges so white parts on white are found, and uses the file's alpha when the render has one (render
with a transparent film for exact silhouettes). It then measures the subject box, fill, margins, centre, visual mass,
pieces and gaps. Videos: frames at 0, 25, 50, 75 %, the last frame, and every 0.5 s for cuts (the widest pose).
| Code | Level | Means |
|---|---|---|
| CUT | FAIL | the piece touches a frame edge |
| EDGE | FAIL | a margin under the format's minimum |
| SMALL / BIG | FAIL | outside the format's fill band |
| OFFCENTRE / HIGH / LOW | FAIL | box centre outside the format's band |
| SAFE | FAIL | a reel's piece enters the UI safe zone |
| SPREAD | FAIL | a group with a gap wider than 0.6 x a piece: separate pictures |
| BUSY | FAIL | textured ground |
| SETFILL | FAIL | with `--set`: fill varies more than 14 points across the set |
| SQUARE, GRID3x4, BALANCE, FLOOR, STRAY, SPARSE, BORDER, TILT, SETFLOOR, SETCENTRE | WARN | look again; fix unless there is a reason |
Use: every still, card, carousel frame and reel before showing (rubric gate G12), and give its output to the blind
reviewer with the images. The overlay draws the subject box, piece boxes, the centred square and the reel safe zone.
It measures framing only; it cannot tell a good piece from a bad one. Never loosen a threshold to pass a render: move
the camera. A threshold that is wrong for a whole format is changed here, with the reason, and in the script together.

Tested 26 Nov 2026. On the 24 site card loops (the card kit preview) it found the Ogive tweezers card's two pieces
set far apart in empty ground (SPREAD), tall pieces sitting on the bottom edge and wide ones pressed against the
right edge (EDGE, BIG), a few tiles off-centre, and fill running 71 to 94 % across the set (SETFILL): the same
"all over the place" the client saw. The card band was calibrated on that approved kit (centre y up to 57 %, 2 %
margin). On the 24 Nov lights reel preview it flagged a mid-move frame with a lamp pressed to the edge and a plinth
cut by the frame, and the retired green end card (EMPTY). It measures framing only; judge the rest by eye.

## 8. Where outside practice and the client disagree (the client wins)
- **Bleed crops** (the product running off two or three edges) are the signature detail shot of @productdesign and of
  many studios. The client rejected crops that cut the piece ("cut things off", "here specfically"). Ours frame the
  whole feature with air. A bleed is allowed only when the client asks for one.
- **Rule of thirds.** Crop and aesthetics research rewards thirds placement for scenes (Liu et al. 2010 weight it
  highest); none of the datasets reports that thirds beats centre for a lone object on seamless, and marketplaces and
  museums centre products. Ours centre the piece; thirds only for a room hero or a scene.
- **Tilted, floating or tumbling objects** (a common product-ad move) are out for reels after the Nave critique; a
  family card is a still group on one floor.
- **Black void and coloured seamless** backgrounds: D3 white stands (productdesign-account.md, conflicts).
- **Wide-angle "hero" low shots** for big objects: only for machines, and still level verticals.

## 9. Sources (public; used as paraphrased facts and numbers only)
- Liu, Chen, Wolf, Cohen-Or, "Optimizing Photo Composition", Computer Graphics Forum 2010: subject-size peaks
  (about 0.10, 0.56, 0.82 of the frame) from 200+ professional photos; thirds, diagonal, balance and size terms.
- Fang, Lin, Mech, Shen, "Automatic Image Cropping using Visual Composition, Boundary Simplicity and Content
  Preservation Models", ACM MM 2014 (FLMS): a crop keeps at least about 40 % of the saliency; the frame edge should
  pass through simple areas.
- Zhang, Niu, Zhang, "Composition-Aware Image Aesthetics Assessment" (CADB, SAMP-Net), BMVC 2021, arXiv 2104.03133:
  composition scores depend heavily on object category; 13 composition classes incl. centre, thirds, symmetric,
  fill-the-frame. Code MIT; images from AADB, research use only.
- Kong et al., AADB, ECCV 2016 (object emphasis, rule of thirds, balancing element attributes); Murray et al., AVA,
  CVPR 2012; Lee and Kim, KU-PCP, JVCIR 2018 (nine composition classes). Images in all of these are research-only or of
  unknown terms: none are kept or redistributed here, and nothing here is trained on them.
- Zeng et al., GAIC / GAICD grid-anchor cropping (CVPR 2019, TPAMI 2020): good crops keep at least half the image and
  an aspect between 1:2 and 2:1; many crops are acceptable, and what a crop cuts away matters as much as what it keeps.
- Chen et al., FCDB (WACV 2017): the best window keeps the salient subject in and the frame edge out of it.
- Luo and Tang, "Photo and Video Quality Evaluation", ECCV 2008: a simple background (few colours) and a subject box
  are among the strongest pro-vs-amateur cues (our BUSY and the subject box).
- Open code reviewed, not bundled: SAMP-Net (MIT, a 1-5 composition score), GAIC-PyTorch and CACNet-PyTorch (MIT),
  idealo NIMA and the LAION aesthetic predictor (Apache-2.0), U-2-Net (Apache-2.0) for subject masks. They are
  trained on natural photos, not products on seamless, so the gate uses the deterministic check above; a learned
  score may be used as a second opinion only, never as a pass. Avoid pyiqa (non-commercial licence) and rembg's
  default model (paid commercial licence).
- Google Merchant Center image requirements (product fills 75 to 90 % of the image; no borders, text or watermarks);
  Amazon main-image rules as summarised by sellers (pure white, about 85 % fill); Etsy photo guidance (leave ground to
  crop to square, portrait and landscape; centre the key part); eBay picture rules (no borders).
- PHOTARCH object-photography notes (near-side enlargement h / (D - h); one lens, distance and aperture per series).
- Museum object photography guides (lens at the object's middle height, levelled; the object nearly fills the view
  with a little background; background well behind the object; 50 mm standard, longer for small objects).
The research notes behind this file (with URLs) are kept in the project, not in this repo.

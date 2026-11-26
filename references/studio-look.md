# Studio look (copy of the brand kit's LOOK.md): the one guide for every reel, TikTok, video, post and still

The client, 26 Nov 2026: "I want to make sure everything we produce looks high quality and cohesive ... all of our projects
look like they're from the same studio ... consistent palette, fonts and logo sizes. We're not changing the logo size.
End cards usually look kind of cheap, so make those look good."

This page wins over any older note (STUDIO_LOOK.md v1, STUDIO_THEME.md "end card", the studio.py v1 docstring).
Tokens live in the brand kit's `theme.json`; the code is the studio finishing kit (`studio.py`). If something is not on this page, it is not allowed.

## 1. Fonts: two families, four cuts, nothing else
| Cut | File | Use |
|---|---|---|
| Newsreader 200 | `Newsreader-200-opsz13.ttf` (small) / `-opsz21` (large) | body, the piece name on the end card |
| Newsreader 300 | `Newsreader-300-opsz13.ttf` / `-opsz21` | titles, nav, uppercase labels |
| IBM Plex Mono 400 | `IBMPlexMono-Regular.ttf` | every tag, spec line, url, counter, caption, credit |
| IBM Plex Mono 700 | `IBMPlexMono-Bold.ttf` | the piece name inside a reel tag only |

- opsz13 below 16 site px, opsz21 above. Newsreader is never bold or italic.
- Not allowed: Plex Mono Light (one exception: the home tower's black server console, a machine screen, not studio output), any other font, system fallbacks (DejaVu, Arial, Helvetica), and the platforms'
  own text tools, stickers and auto-caption styles. Subtitles, when needed, are Plex Mono 400 lowercase in the tag slot.

## 2. Palette
| Token | Value | Where |
|---|---|---|
| page | `#FFFFFF` | site, end card, stills, carousels |
| ink / heading | `rgba(0,0,0,.75)` / `.68` (`#404040` / `#525252`) | all type on white |
| strong | `#000000` | logo, name labels |
| image fill | `#F3F3F3` | empty slots, seamless |
| accent | `#1D847E` (IKIYA lining green) | tag chips, the url chip on the end card, active nav. Nothing else |
| on accent | `#FFFFFF` | type on a chip |
| frame ink | warm white `#F6F3EE` on dark frames, `#282624` on pale | crop marks, node squares, hairlines |

- The world is grey (`unify`); the only saturated colour in a frame is the piece's own.
- Never: full-colour backgrounds or slabs, gradients, scrims, coloured type, a second accent. Firebrick is the
  home-page marquee only.

## 3. Logo: one size rule, never by eye
`logo px = 54 x (canvas width / reference width)`, reference 390 for phone formats, 1440 for screens.

| Format | Canvas | Logo |
|---|---|---|
| site header | 390 / 1440 | 54 px |
| reel, TikTok, Story, Short | 1080 x 1920 | 150 px |
| IG post / carousel | 1080 x 1350 or 1080 | 150 px |
| YouTube, X video, wall | 1920 x 1080 | 72 px |
| 4K | 3840 x 2160 | 144 px |
| banners (GitHub, LinkedIn) | width w | 54 x w / 1440 |

- Black on white only. Never on footage, never recoloured, outlined, boxed or tinted, never with a wordmark.
- Place: top-left, at the gutter, at the top of the safe zone (reels: x 78, y 250). `studio.LOGO_PX` holds the number.

## 4. Frame layout (1080 x 1920)
- Safe zone: nothing in the top 220 px or the bottom 380 px except crop marks; 64 px sides.
- Crop marks: 2 px, 34 px long, 54 px in, on every frame.
- Counter `04 / 10` on a chip, top-right at y 244. URL in tiny mono top-left, first frame only.
- Tags: bottom-left stack ending at `TAG_Y` (1500): name (mono 700) and one spec line (mono 400), lowercase, on chips.
- Nodes: 16 px hollow squares on real named parts, one hairline joining them, part names on small chips.
- The piece fills 40 to 60% of the frame height, with air around it.
- 16:9 and square crops keep the same marks and tag slot, scaled with `theme.scale()`.

## 5. Grade
`grade()` then `unify()` on every frame: one key light and its pool, soft shoulder, warm highs and cool shadows, fine
grain. Hero and Instagram stills must also pass as a photograph (photoreal.md).

## 6. Motion
- Frame 1 is the piece. No title card, no logo sting, no intro.
- One continuous camera move, or hard cuts between holds of about 1.5 s. No spins into odd compositions, no flicker,
  no random jump cuts, no zoom punches, slides, bounces or whip transitions.
- Tags and type fade in and out over 0.6 s, ease `cubic-bezier(.65,0,.35,1)`, 0.08 s stagger.
- Length: 20 to 30 s for reels and TikToks (50 s at most). YouTube films set their own length, same rules.
- Sound: real shop and material sound first. Trending audio only on TikTok, low under the real sound.

## 7. Endings: no card, the reel closes into a square (the client picked C, 26 Nov 12:41 AM ET)
the client on the site card: "still kind of feels like corporate ... slop", "your video shouldn't just end abruptly either".
Of the three in-world endings (samples in the brand kit), the client picked the crop: "3rd is the way to go and is also
wise because when the reels are on the main grid it ensures u get a good preview because of the crop".
- **Default, every reel and TikTok: Crop.** The last camera move eases to a stop (about 1.4 s, never a cut while
  moving), then the frame closes into a centred 760 px square on white over 0.9 s, hairline marks round it, and one
  mono line fades in under it (`name · url`). Holds 2 s, about 4.4 s in all. No logo, no spec stack, no chip.
- **The cover is that last frame.** Upload the crop's final frame as the reel's cover (Instagram and TikTok both show
  a centred 3:4 window on the profile grid; the square and its line sit inside it), so every grid tile is the piece in
  a square on white and the grid reads as one studio. `studio.cover(tail, name, url)` returns it.
- **The carousel's last slide** is the same still.
- Settle and Lights down stay in `studio.ending` only for a case the client asks for. `studio.endcard()` (the site
  card) and the green slab are retired.
- Code: `studio.ending('crop', tail_frames, name, url)`; tail = the last ~1 s of clean frames.
- Never: a card bolted on after the reel, a logo stack, specs paragraphs, "follow for more", arrows, stickers, a hard
  cut while the camera is still moving.

## 8. The gate (pass every line before anything is shown or posted)
1. Only the four font cuts above appear. No platform text or stickers.
2. Colours: white, the greys, `#1D847E` on chips only, and the piece's own colour.
3. Logo is the exact size for the format, black on white, top-left, and only on white surfaces.
4. Nothing but crop marks in the top 220 / bottom 380 px of a vertical frame.
5. Tags lowercase mono on chips, low-left; counter top-right; nodes only on real parts.
6. `grade` + `unify` ran; the world is grey and the piece carries the colour.
7. Frame 1 is the piece; no title card; no flicker, spins or jump cuts; length within the limit.
8. Ends on the crop (section 7) and the cover is its last frame; never a card or a cut while moving.
9. No clipping or interference in the piece (standing rule).
10. Checked side by side against the last approved reel: it looks like the same studio.

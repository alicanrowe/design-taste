# Rubric: score before showing

Run this on the real render of every design, before anyone else sees it. It needs three kinds of image:
- the main views (hero, plus the views the domain skill lists),
- a **part contact sheet**: one close-up per part in the piece's part inventory, at about 30 cm framing for
  furniture, 3 cm for jewelry, 15 cm for boots and garment details, side by side with a close-up of the piece's
  signature part,
- two or three **reference images** per lead influence, at the same size as the render.

Write the result into the piece's notes as one line plus the fixes:
`<piece>: gates OK | scores 2 2 1 2 2 2 2 1 2 2 2 2 = 22/24 | fixed: ...`

## Gates (any fail: fix and re-render; never show)
- **G1 Clipping.** Nothing passes through anything: metal through glass or leather, cords through ferrules,
  stitches into leather, body through garment, hardware through hardware. Run the domain skill's check; it reads 0.
- **G2 One body, nothing loose.** Castings are one connected body each; every strap, loop and wrap either opens or
  is sewn closed; no floating parts.
- **G3 Buildable and strong.** Real stock sizes (stones, leather thickness, wire, bought hardware named), casting
  minimums, no gaps that would snap, no part that would flop or fold under its own weight, seats carry their load.
- **G4 No banned move.** Go down `banned-moves.md` line by line against the main views and the part sheet.
- **G6 White background.** Every image that goes out sits on white unless the client asked otherwise (principles
  D3). Run the background check on the exported files themselves; a transparent render turns black on export.
- **G5 Current.** The render, page, GLB and sheet all show the newest version of the model.

## Scored criteria (0 = fails, 1 = passable, 2 = strong)
Bar to show: **no zeros, and at least 20 of 24.** For the client's own flagship pieces, aim for 22.

| # | Criterion | 2 looks like | 0 looks like | Principle |
|---|---|---|---|---|
| 1 | **Silhouette idea** | one idea you can name, visible in the main view's outline | a standard type (a plain chelsea, a plain bomber) with trims | A1, A8 |
| 2 | **Motif is structure** | delete the motif and the object no longer stands or closes | delete the motif and a normal object remains (gimmick test) | A2 |
| 3 | **One language** | part inventory: every part named in the same language; no odd one out on the part sheet | a smooth, stock or other-language part | A3 |
| 4 | **Even fidelity** | every close-up on the part sheet is equally modelled and finished | one part is a default shell, low poly, or a stitch line where others are relief | A4, B6 |
| 5 | **Surface** | surfaces modelled in depth (layers, relief, moulding, crimping); rest fields bounded and deliberate | large flat or blank panels | A5 |
| 6 | **Solidity** | details read thick, stiff, tied in; edges finished (turned, bound, boxed, filleted) | thin flaps, points, tails or wires that would hang or bend; knife points or square laser edges on anything handled daily (tip radius under 3 mm) | A6, B4, B5 |
| 7 | **Line** | strokes swell and taper, curves accelerate, tapers smooth, ends clean | even tubes, kinks, lumps, nubs, wobble | B1 to B4 |
| 8 | **Focus** | one focal point, three or four motifs, quiet around it | busy, noisy, competing centres | A9 |
| 9 | **Mood** | dark, gothic, considered; could only be this client's | pretty, cute, generic, costume | A7 |
| 10 | **Reference match** | at reference size it sits beside the references without looking like a render or a copy; for metal, it could pass beside a phone photo of real oxidised cast silver (dark recesses, bright worn highs, cast shadow) | the references make it look cheap, flat, or like plastic; uniform chrome silver floating on white | A10, B6, E5 |
| 11 | **Fit to world** | built from the host piece's or collection's own motifs; liked moves reused | ignores the host, or drops a pick the client loved | A3, E2, E3 |
| 12 | **Distinct** (for sets) | each variant has its own silhouette idea | variants differ by seed, colour or stone | A1 |

For a single piece with no set, score 12 as 2 if it is distinct from the client's earlier rejected rounds.
For a whole collection, 12 also covers the earlier collections: run the sameness check (sculpted-metal-casting,
`scripts/check_sameness.py`) against every earlier collection and any sibling being built at the same time. Any
SAME, ECHO, RESKIN or TYPES flag scores 0 ("make sure that they all like look different, so it looks not too samey
compared to the other ones", 21 Nov).

## The four questions to ask out loud
After scoring, answer these in the notes, in a sentence each. They catch what the table misses.
1. If the client covered the logo and the motif, would anything about this still be interesting?
2. Which part would the client pin first, and what would they write?
3. Is any detail here because it was easy to model rather than because it is right?
4. Would the best maker named in the brief put their name on it?

## When a critique gets past this rubric
Add the line that would have caught it, in the same session, and publish (see SKILL.md).

## Added 21 Nov 2026 (round 4 boots review)
- Before scoring Surface, put the largest plain panel (often the vamp) on screen at part-sheet size. If it is blank
  and the motif does not reach it, Surface is 1 at most, however rich the rest is.
- Many small soft lobes (feathers, scales, petals) score 0 to 1 on Solidity even when watertight: they read torn or
  floppy. Fewer, larger, stiff plates.

## Added 21 Nov 2026 (Bombyx live-page review)
- Even fidelity across a collection: put the collection's best-detailed piece (for Bombyx, the carved LOULAN
  feathers) next to each piece at the same size. Any piece whose surfaces are plainer (open outlines, smooth
  struts) scores Even fidelity 0 to 1, however clean it is.
- Solidity of heads: for every stone head, find the narrowest place where metal links the setting to the rest
  (sculpted-metal-casting `check_joints.py`), then look at it in the main view. One visible link, or members ending
  as stubs against the gallery, scores 0, whatever the numbers say.
- Line on contours and tips: trace every arc the eye reads as one curve (a crescent's inner edge) and every free
  tip. A knuckle on the arc or a rounded nub on a tip meant to be sharp scores Line 0.
- Bundles (ribbons, vines, strands): they share one rule (an even fan, a common wave). Random crossings or merges
  score Focus 0 to 1.

## Added 21 Nov 2026 (Bombyx review 2)
- Ends and junctions: zoom on every place a member ends or meets another (sculpted-metal-casting
  `check_members.py` lists them: NUB, CROSS, BOLT, HOLE). A round cap showing, a stem across a leaf face, a necked
  bolted-on point, or anything in a ring's finger hole is a G4 fail, whatever the clipping check says.
- Production: before a collection is called done, can each piece be sent to a jeweler as is? Watertight STL,
  stone list with cut and mm size, findings named (bought ear wires, posts, barrettes) on cast loops or pads.

## Added 22 Nov 2026 (form study before surface)
- Before any material, texture or colour goes on, render the form once in one matte neutral clay (light warm grey,
  so it reads on the white background) from a fixed set of named views: front, side, rear, top, three-quarter, a
  close-up of each main part, exploded, and assembled. Look at the sheet. Silhouette idea, Line and Solidity are
  scored on this clay sheet, because colour, shine and texture hide a weak outline, a lumpy curve or a thin leg.
  A form that fails in clay is reworked before surfacing, not rescued by the finish. Keep the clay sheet in the
  piece's notes; it is a check, not something to show the client unless they ask. (After a stool form study
  shown "in neutral clay white, one form, seven angles", 22 Nov.)

## Added 22 Nov 2026 (reel pacing)
- Pacing: play the cut at full speed once, start to finish, before showing it. Any stretch over about 2 s where
  nothing new enters the frame (no new piece, label, reveal or change of direction) is a fail; speed-ramp it or
  cut it. Each piece gets a short beat, not a long hold, and travel between pieces runs faster than the beat.
  A social reel of a collection lands around 40 to 50 s. (After "the timing seemed super awkwardly long pauses",
  on the 1:30 the jewelry line reel, 22 Nov.)

## Added 23 Nov 2026 (sculpture with a use)
- **Gate G-use (sculpture and objects):** name the job in five words (holds rings, stores keys, lights a corner,
  carries a tray). The job shows in the hero render (rings on the pins, light glowing, something in the bowl) and
  grows from the motif, not a tray or bulb stuck on. A purely decorative flat wall piece fails (Oculus, 23 Nov:
  "the dumbest thing ever").

## Added 23 Nov 2026 (cast chairs read as kitsch)
- **Depiction test (scored under 9, Mood):** describe the piece without naming anything it looks like. If the only
  honest description is "a chair shaped like a ___" (spine, window, halo, leaf, coil), score 0 on Mood: it is a
  themed prop. 2 looks like: the idea is a way of making (a fold, a lean, a pour, a counterweight) and the mood
  comes from proportion, mass and colour.
- **Five-word idea:** write the piece's one idea in five words in its notes. If it takes two ideas, cut one.


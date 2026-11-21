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
| 6 | **Solidity** | details read thick, stiff, tied in; edges finished (turned, bound, boxed, filleted) | thin flaps, points, tails or wires that would hang or bend | A6, B5 |
| 7 | **Line** | strokes swell and taper, curves accelerate, tapers smooth, ends clean | even tubes, kinks, lumps, nubs, wobble | B1 to B4 |
| 8 | **Focus** | one focal point, three or four motifs, quiet around it | busy, noisy, competing centres | A9 |
| 9 | **Mood** | dark, gothic, considered; could only be this client's | pretty, cute, generic, costume | A7 |
| 10 | **Reference match** | at reference size it sits beside the references without looking like a render or a copy | the references make it look cheap, flat, or like plastic | A10, E5 |
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

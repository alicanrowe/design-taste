# The taste in each medium

The principles are the same everywhere; what changes is how a medium breaks them. Each section says what has
already gone wrong and what passing looks like.

## Cast metal: jewelry
- Loved: open hind wings with loose, layered veins crossing over and under inside the rim; light aquamarine heads
  on wing-frame shanks; curl-tail drops; unequal chain-and-pear drops; open vein loops inside a band.
- Missed: vein fills that are dense, combed, random or noisy (a whole stud family "a mess"); bug bodies as spiky
  clusters; nubs on every tail; dark stones; ten near-identical cuffs.
- Every face of a ring carries detail. Wearables: no sharp points, wire and links at least 1.0 mm.
- Domain rules: sculpted-metal-casting `style-rules.md`, `client-picks.md`, `casting-rules.md`.

## Machined metal (jewelry as precision parts)
- The brief: "more masculine, maybe less gemstoned, more precise machining ... an ode to precise machining ...
  knurling elements or other like American industrial kind of things" (21 Nov).
- Every detail is a real part's real detail at its real proportion: cut knurl, involute teeth that mesh, threads
  under screw heads, springs with closed ends, chamfered edges. A detail that only looks mechanical is a fail.
- Two-tone by finish (bright, satin, oxidised black, stainless). Black parts get bright cut chamfers or they read
  as holes. Stones only where the real part has a ball.
- Piece types come from the parts, one per job, so the set reads as one machine and not as rings in a new metal.
  But every type must be something people actually wear now ("who the fuck wears bolo ties man", 21 Nov): no
  bolo ties, no novelty types picked only to avoid a repeat.
- The concept carrying the page is not enough ("i love this thinking but every piece in governor is ugly", 21 Nov).
  Round 1 failed because each piece was a literal, life-size diagram of the part: flat plates, square bars, a
  cutaway bore, plain bands, gadgets glued onto a shank. The machine is the source, not the object. Each piece has
  to be beautiful jewelry first (proportion, a flowing silhouette, volume that catches light, detail at jewelry
  scale) and read as the part second. Test: hide the story; would someone still want to wear it?
- Line (rubric 7) reads as: straight where the part is straight, true arcs, crisp edges, no wobble, no blobs.

## Cast metal: furniture-scale (sawhorses, case hardware, jail grilles, tools)
- Loved: Durumi's crane foot and bojagi seat, Thread's twisted-strand foot, Edge's tapered side profile, thorned
  vines up the posts, the carved-feather stretcher, the cast braided-lancet jail with the moth hanging like a bat,
  red stitched-cord leather grips ("perfect").
- Missed: smooth chrome parts on a carved piece, ball tips, literal butterflies, hexagon hubs, elf-shoe toes, flat
  laser-cut grilles, low-poly tools, metal through glass, spikes too thin to survive.
- Hardware for an existing piece starts from that piece's own motifs (list them first).
- Domain rules: sculpted-metal-casting `furniture-scale.md`, `design-coherence.md`, `buildable.md`.

## Wood furniture
- The bar is the client's own carving (Fawn Orchard): long gouge scoops along the grain, pierced lancets, oiled
  walnut. When asked for "only solid wood carving", every metal, ply or bought part goes (keep what the client
  names, like upholstered seats).
- Match photos one to one when modelling existing work; place every part exactly where the photo shows it.
- Render like Gregory Beson: soft high light, paper sweep or limewash room, colour measured against his photos.
- Domain rules: hardwood-furniture-cad, seating-load-check.

## Leather: boots and bags
Round 1 "all suck and feel unrealised", round 2 "super ugly and unoriginal", round 3 "simple ... details are
inconsistent in quality ... a lot of flat surfaces ... flimsy or floppy ... gimmicky". Only COAT, HALO and
GAUNTLET had ideas worth keeping. What round 3 looked like: nine near-identical plain black calf shells with the
same long point and the same block heel, each carrying one small attachment (stock rectangle buckles, a ring on
the ankle, a thin bracket heel, stitch-line vines, single-layer crown points).

What passing needs:
- **The idea in the structure.** The heel, counter, shaft or toe *is* the motif, built as a sculpted part that
  carries load (a cast heel cage that is the halo; lames that are the shaft; a horn that is the heel and counter
  sweeping up the back, not a ring on the side).
- **No plain shell.** Every boot gets modelled leather over most of its surface: layered and lapped panels with
  real edge thickness, moulded or wet-formed shapes, crimped fronts, channel quilting or couched cord in relief,
  boxed and piped edges, overlays with turned edges. A single smooth calf vamp is a flat surface.
- **Different silhouettes.** Nine boots share no default last, toe or heel unless the brief asks.
- **Hardware in the piece's language,** cast and big enough to read at sheet size, integrated with the leather
  (straps run through cast keepers that are part of the motif). Rectangle stock buckles fail.
- **Stiff where it stands up.** Points, flaps and crowns are double layers with turned or bound edges, stiffened
  (leatherboard, moulding) or carried by metal. Nothing single-layer sticks up or hangs.
- **Even fidelity.** If the hardware is jewelry-grade, the welt, sole edge, heel stack and topline are too.
- Domain rules: boots-and-bags `check-loop.md`, `construction.md`, `hardware.md`.

## Leather: jackets and garments
- Same critique as the boots (rejected together). Round 3 jackets read as glossy grey plastic with noisy
  wrinkles, one rich detail (sleeve lames, a collar) on an otherwise blank body, and thin skirts and tails that
  hang like sheet.
- Passing: matte leather that reads as hide; the motif carried by the cut and the seams across the whole garment
  (not one zone); structured parts (collars, peplums, tails, wings) built as stiffened double layers with finished
  edges; hardware cast in the motif and sized to read at full-garment view; each jacket the boot's twin at a
  glance.

## Machines (the Dancers)
- Real parts only, matched to their listings; no stand-in boxes. Saturated colours must survive the renderer.
- Look is engineered and honest; the taste rules on coherence and fidelity still apply (one part rendered
  rougher than the rest stands out).

## Site pages and renders
- White backgrounds by default (D3): every render, page image, teaser and part photo. Check the actual output
  file, not the render: a transparent PNG flattened with a plain RGB convert lands on black.
- Every page matches the newest page look (currently Nine Rests): same layout, type and theme. A page that passes
  the brand audit can still look old.
- Every image, GLB and spec shows the newest model version. Caching or a stale file reads as "not done".
- 3D viewers: no flicker, no shattered decimation, grain running along each part, stones in their colours.
- Interactive pieces feel like product pages: images act as controls where they look like buttons.
- Fractal and digital presets match their named artist until the render could pass as theirs.

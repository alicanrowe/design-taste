---
name: design-taste
description: The client's design taste across every project (jewelry, cast-metal furniture, wood furniture, leather boots, jackets and bags, machines, site pages, renders). Read it before designing anything, score every design against its rubric before showing it, and log every new critique so it keeps improving.
---

# Design taste

One shared, self-improving record of what the client approves, what they reject, and why, distilled from every
review across every project. Domain skills (sculpted-metal-casting, boots-and-bags, hardwood-furniture-cad,
concrete-mold-casting, shop-machine-cad, website-publishing and any new one) point here for taste and keep only
their own craft rules.

The point is to get it right before the client sees it, instead of finding taste by many rounds of edits.
Taste is the job, not a finishing pass: when anything can be built, knowing what is worth making and making it
look and feel great is the work (client reference, 25 Nov).

## Files
- `references/principles.md`: the taste itself. What the client likes and hates, as rules, each with the
  client's words behind it and how many times it has come up.
- `references/banned-moves.md`: moves that have been rejected outright. Any one of them fails a design.
- `references/rubric.md`: the scoring rubric. Gates plus scored criteria, run before anything is shown.
- `references/influences.md`: the named references and how each one is used (hand, not products).
- `references/domains.md`: how the principles translate into each medium (metal, wood, leather, garments,
  machines, renders and pages), including what went wrong in each.
- `references/critique-log.md`: every critique, verbatim, dated, by project and piece. Append-only.
- `references/instagram-saves.md`: patterns from the client's saved Instagram posts (about 2,500): materials,
  makers, surfaces, colours and staging they keep returning to. Lower weight than critique; use it to pick
  references and break ties. Where it conflicts with a principle, the principle wins.
- `references/productdesign-account.md`: how products are shot and rendered, from all 88 posts of the
  @productdesign account (25 Nov): the carousel frame order, camera angles, bleed crops, light recipes,
  backgrounds and material tells, plus our default shot plan. Read it before planning any render set, product page
  or IG carousel. Lower weight than critique and saves; D3 white still wins.

## Use it (every design task)
1. **Before sketching.** Read `principles.md`, `banned-moves.md`, the section of `domains.md` for your
   medium, and the matching signals in `instagram-saves.md` (for renders, pages and reels, also the shot plan in `productdesign-account.md`). Read the project's own brief and picks file. Write the brief in four lines: the one silhouette idea,
   the language every part is built from (named motifs, from the host piece if there is one), the focal point,
   and the two or three references you will hold it against.
2. **Design to the rubric, not to the checklist after.** The rubric's top failures are structural (a plain base
   object with a feature stuck on, flat dead surfaces, one part at lower fidelity than the rest). They can't be
   patched at the end. Decide how the motif *is* the structure before modelling.
   Check the bare form first: one matte clay render from every named view (rubric, "form study before surface")
   before any material goes on.
3. **Score before showing.** Run `rubric.md` on the real render, including a close-up of every part. Write the
   scores in the piece's notes. Anything that fails a gate or scores under the bar is fixed and re-rendered, not
   shown. Use the domain skill's own checks (clipping, casting, fit) as gate G1 to G3.
4. **Cross-check a set before picking (blind critique).** When a step makes several variants or a pick among
   options, don't let the maker grade its own work alone. Give each variant to a reviewer that did not make it
   (a separate agent with only the brief, `principles.md`, `banned-moves.md`, `rubric.md` and the renders, not
   the maker's notes). Each reviewer's job is to find what's wrong: rubric fails, banned moves, the weakest part
   at close-up. Fix what they find, carry a fix that wins on one variant across the others where it fits their
   motif, then re-score. Keep it small: one reviewer per variant, at most five, one round, two only if a gate
   still fails. Skip it for a single quick fix.
5. **Show only what passed**, with the score line. If the client asked not to review along the way, publish the
   passing set and report once.

## Excuses that don't count
Each of these is a shortcut that ends in a broken result. If you catch yourself thinking the left column, do the right column.

| The excuse | What to do instead |
|---|---|
| "The owner will like this one, it's close" | Score it on the rubric first. Anything under the bar goes back into the loop, not to the owner. |
| "The brief is about a process (engraving, casting), so the form can fall back on the house gothic" | Run banned-moves.md on the silhouette before any CAD. Spandrel (23 Nov) was a black lancet-window chair with spike posts and was pulled the same day. |
| "That critique is obvious, no need to log it" | Log the exact words in the critique log the same session and distil them into the principles. |
| "I scored it myself, it passes" | For a set or a pick, run the blind cross-critique in step 4; the maker misses its own flaws. |
| "The variants are different enough" | Run the sameness check; variants that differ only by colour, seed or stone fail. |
| "The finish will carry it" | Render it in plain clay from every side first; if the form doesn't hold up bare, rework the form. |

## Keep it improving (standing rule, every thread, every project)
Whenever the client gives design critique of any kind (a pin on a sheet, a word in chat, a reaction to a live
page, a pick between options), in the same session:
1. Append it to `references/critique-log.md`: date, project, piece and place, the client's exact words, and what
   was shown. Positive picks too ("love this", "fucking sick", "perfect") are as important as rejections.
2. Distil it. If it repeats an existing principle, raise that principle's strike count and sharpen its wording.
   If it is new, add a principle (or a banned move if it was rejected outright, or a rubric line if it is
   checkable). If it contradicts an older rule, the newer word wins: rewrite the rule and say what changed.
3. If the miss got past the rubric, add the check that would have caught it.
4. Publish: `bash ../_publish/sync.sh design-taste "<what changed>"` (see that folder's
   README). Commit to main, no PR, no private data.

Craft-only lessons (a kit bug, a casting minimum) stay in the domain skill; anything about how a thing looks or
feels comes here.

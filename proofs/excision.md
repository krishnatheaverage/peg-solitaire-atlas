# The Excision Lemma (Route B for the strip) - case analysis draft

**Goal.** For k >= K0 and p in the strip: any solving play on C(k;p)
can be transformed into a solving play on C(k-2;p). Contrapositive +
verified bases close Theorem 1's necessity for all k.

## Where to excise

By strip-closure L2/L3, at most E* = 46 jumps are "special" (gadget
interface or antipodal crossings). All other jumps are arc-internal.
A 2-block (x_a, x_{a+1}) in the far half is TOUCHED by a jump if the
jump's 3-cell path uses a or a+1. Every touching jump either lands in
the block (an import) or consumes >= 1 block peg. Global import
budget into the far half is bounded (antipode-weight ledger, L3
arithmetic), so, taking K0 large enough that the far half contains
more than (import budget) + E* + 1 disjoint 2-blocks, SOME block B
satisfies:

  (i)  no special jump touches B,
  (ii) no jump lands in B except as part of a same-visit sweep (see
       below),
  (iii) B does not hold the final peg.

## Local histories of such a block

With no imports and both cells eventually empty, the touching jumps
consume the 2 initial pegs. Complete enumeration (up to mirror):

  (H1) one jump (x_a > x_{a+1} > x_{a+2}): both pegs consumed,
       lands OUTSIDE at x_{a+2};
  (H2) one jump (x_{a+1} > x_a > x_{a-1}): mirror of H1;
  (H3) two jumps (x_a > x_{a-1} > x_{a-2}) and
       (x_{a+1} > x_{a+2} > x_{a+3}) in either order (block pegs
       exit in opposite directions as jumpers);
  (S)  sweep visit: (x_{a+2} > x_{a+1} > x_a) [lands at x_a: an
       import, but from the block's own neighborhood] followed
       later by (x_a > x_{a-1} > x_{a-2}); or the mirror.

## Excision rewrites

Remove cells x_a, x_{a+1}; x_{a-1} becomes adjacent to x_{a+2}.

  (S): replace the pair by the single jump
       (x_{a+2} > x_{a-1} > x_{a-2}), scheduled at the time of the
       SECOND jump. Soundness requires x_{a+2}'s peg to be untouched
       between the two jump times; since only these two jumps touch
       the block and x_{a+2}'s peg was consumed by the first, the
       merged jump is legal at the first jump's time iff
       (x_{a-1} pegged, x_{a-2} empty) then - the INTERFERENCE
       CONDITION. If other jumps touch x_{a-2}, x_{a-1} in between,
       choose a different block (interfering jumps touch the
       adjacent block, charging the budget; a counting argument
       picks a visit-coherent block).
  (H1): the landed peg at x_{a+2} must later be consumed by some
       jump J'. Pair (H1, J') and rewrite according to J's direction:
       if J' = (x_{a+2} > x_{a+3} > x_{a+4}) the pair becomes
       "x_a's peg jumps two blocks right"; in the compressed cycle
       the single jump (x_{a-1}... ) - CASE NOT CLOSED: H1 excision
       requires tracking one more jump; the rewrite exists in all
       sub-cases tried by hand but the enumeration is incomplete.
  (H3): both jumps survive verbatim in the compressed cycle (their
       paths avoid the seam); but each REQUIRED a hole at its
       landing time and consumed x_{a-1}/x_{a+2} pegs - paths
       (a,a-1,a-2) uses cells a-1, a-2 which persist; legal verbatim.
       The block pegs however disappear from the compressed board -
       these two jumps must be DELETED, and their side effects
       (consuming x_{a-1} and x_{a+2}, landing at x_{a-2} and
       x_{a+3}) compensated - NOT CLOSED; H3 blocks may need to be
       avoided via the choice argument instead (H3 consumes two
       outside pegs and creates two outside pegs: net local
       neutrality suggests a swap rewrite; unfinished).

## Status: honest

The sweep pattern (S) - empirically the dominant one in witnesses -
excises cleanly modulo the interference condition. H1/H3 rewrites are
unfinished; the choice argument ("enough blocks that some block's
history is type S") needs a proof that far-half consumption in a
solving play is sweep-like except boundedly often, which is plausible
(sweeps are the only weight-conserving way to consume far arc) but
not yet written. Machine support: check on witnesses for solvable
crowns k = 16..24 that type-S blocks exist in every play sampled.

This route stays elementary but needs one more working session; the
automaton route (strip-closure.md L5) remains the alternative.

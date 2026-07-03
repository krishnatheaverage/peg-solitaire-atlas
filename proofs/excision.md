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

## CORRECTION (2026-07-02, session 4)

The S pattern is NOT a no-import history: its first jump lands at
x_a, which requires x_a's original peg to have been consumed earlier
by yet another touching jump. So S-blocks belong to the boundedly
many import-blocks and are AVOIDED by block choice, not rewritten.
The no-import trichotomy {H1}, {H2}, {H3L + H3R} (proved complete by
the consumption-mode enumeration above) is the whole case list.

**H1 context analysis.** H1's landed peg at x_{a+2} can only be
consumed by (x_{a+2} > x_{a+3} > x_{a+4}) (jumper right; all other
consumers of x_{a+2} land inside the block = import, excluded). So
an H1 block extends into a rightward chain of H1-type jumps; the
chain's INTERIOR blocks (x_b, x_{b+1}) have history {land at x_b
from (x_{b-2} > x_{b-1} > x_b); exit via (x_b > x_{b+1} > x_{b+2})}
and merge cleanly into the single C' jump
(x_{b-2} > x_{b-1} > x_{b+2}), PROVIDED no interleaved jump touches
x_{b-2}, x_{b-1}, x_{b+2} between the two chain steps (interference
condition). Chain endpoints reach either the special zone (bounded,
avoidable) or a leftward consumer (an S-flavored joint).

## Status: honest

Case list complete; the mid-chain merge is proved modulo the
interference condition, which still needs either (i) a scheduling
lemma (chain steps can be commuted to be time-adjacent: plausible
via the standard exchange argument - independent jumps commute), or
(ii) a counting argument avoiding interfered chains. H2/H3 isolated
blocks remain genuinely unfinished. The exchange-commutation route
looks most promising: jumps with disjoint 3-cell supports commute,
so any play can be normalized so each chain runs consecutively; then
every mid-chain block merges. Under that normalization the excision
closes IF every far-half no-import block is mid-chain - the isolated
H2/H3 cases must be shown absent or separately rewritten. One more
session.

## Commutation Lemma + strengthened block choice (2026-07-02, session 5)

**Commutation Lemma (PROVED).** If consecutive jumps J1, J2 in a play
have disjoint 3-cell supports, swapping them preserves legality and
all subsequent states. Proof: legality of a jump depends only on the
contents of its own support; disjointness means neither changes the
other's support; the combined effect is the same multiset update.

**Strengthened choice (PROVED).** Import-blocks are boundedly many
(antipode-weight budget), special-touched blocks likewise, so for k
large, all but an absolute constant number of far-half 2-blocks have
an import-free 3-block NEIGHBORHOOD. For such a block, no jump lands
on x_{b-2}..x_{b+3} at any time, and (by the Commutation Lemma) the
jumps touching the neighborhood can be normalized to be consecutive.
Under this normalization the H1 mid-chain merge
(x_{b-2} > x_{b-1} > x_b) + (x_b > x_{b+1} > x_{b+2})  ==>
(x_{b-2} > x_{b-1} > x_{b+2})
is sound with no interference condition.

**Remaining (one case family).** Isolated H2/H3 blocks with
import-free neighborhoods: the H3 pair consumes two outside pegs and
creates two outside pegs (a "+1 peg mismatch" against any single
compressed jump), so its excision requires pairing with the later
consumer of one landed peg; the cascade terminates at special events
(bounded) or another chain. Enumerating cascade terminations is the
one unfinished list. Everything else in Route B is proved.

## ROUTE B REFUTED (2026-07-02, session 6) - important correction

Pushing the H2/H3 analysis to completion exposed a fatal flaw in the
block-choice premise. If a 6-cell window x_{a-2}..x_{a+3} receives NO
interior landings, then its inner cells x_a, x_{a+1} can never be
consumed: every jump consuming them (as jumper or middle) lands
within the window. Hence EVERY far-half 6-window in a solving play
needs interior landings or holds the final peg. Since consuming the
far arc requires Theta(k) landings there (every sweep step lands a
peg), the premise "imports into the far half are bounded" is FALSE -
the weight ledgers bound antipodal crossings and near-antipode
away-jumps, NOT total landings. (Sanity check that caught it: the
false premise + this window argument would prove large solvable
crowns impossible, contradicting p <= p* instances.)

Consequences:
- The Commutation Lemma stands (independent, true).
- The "strengthened block choice" is RETRACTED.
- Route B (elementary excision) collapses into Route A: excising two
  cells from a long pure-1-D region while preserving interface
  behavior IS the pumping lemma for the Moore-Eppstein transducer.
  The automaton is not an alternative but the essential tool.

Theorem 1's remaining gap is therefore exactly: construct/verify the
interface automaton (strip-closure.md L5) and extract (N_p, T_p).
Fourth model error caught by contradiction-testing; the discipline
holds.

# Criticality half of the double crown dichotomy (2026-07-03)

## The clean reduction (PROVED)

$DC(k,d)$: $k$-cycle, two pendants at $x_0$, two at $x_d$.
Delete any cycle edge $\Rightarrow$ the $k$ cycle vertices become a
path (spine length $m=k$) carrying the two pendant pairs. The two
loaded vertices $x_0,x_d$ end up separated along the path by $d$ (if
the deleted edge is on the length-$(k-d)$ arc) or $k-d$ (if on the
length-$d$ arc). Verified arithmetic: DC(16,8)->{8}, DC(24,8)->{8,16},
DC(12,4)->{4,8}, DC(22,6)->{6,16}, all even.

So for $k$ even and $d$ even: every spanning tree is a
double-cluster caterpillar of EVEN spine length $k$ with EVEN
separation.

## The caterpillar necessity (machine-verified, KEY)

For even spine length $m$, a double-cluster caterpillar
$P_m(2@i, 2@j)$ with $j-i$ even is unsolvable -- for ALL positions
$i<j$. Verified exhaustively, every position pair:
  m=14: 0 even-sep solvable   m=16: 0   m=18: 0   m=20: 0.
CRITICAL SUBTLETY (caught by testing odd $m$): the rule needs EVEN
spine length. At $m=19$ (odd spine) there ARE even-separation
solvable pairs (e.g. (2,6),(4,6),...). So the statement is
"even spine + even separation => unsolvable", not "even separation
=> unsolvable". DC(k,d) with $k$ even always yields even-spine
caterpillars, so the reduction is unaffected -- but the precise
hypothesis matters and would have been an error if stated loosely.

## Consequence

Criticality half of the dichotomy: for $k,d$ even, $DC(k,d)$ (once
solvable) is cycle-critical. Unconditional for even $k\le 20$
(caterpillar prop verified there); verified directly through $k=24$.
For all $k$: contingent only on the caterpillar necessity extending
to all even $m$, a $k$-uniform statement of the same character as
the crown strip. This replaces the old "verified through $k=24$"
with a structural proof resting on a far more robustly verified
proposition (all positions, all even $m\le 20$).

## Still open
- Prove caterpillar necessity for all even $m$ (invariant likely a
  pagoda/parity function; the naive bipartite 2-colouring resource
  count does NOT suffice -- it gives no separation-parity obstruction,
  tested). This is the honest remaining gap.
- Non-antipodal even-$d$ solvability for all $k$ (verified, not
  proved; Thm dcs covers antipodal only).

## Invariant hunt outcome (2026-07-03) — NEGATIVE, informative

Attempted to prove caterpillar necessity via a certificate. Results:
- EXACT MODULAR INVARIANT (sum w mod q invariant): does NOT exist.
  The system w(u)+w(v)=w(w) over all cherries has only the trivial
  (zero) solution for q=2,3,5 (computed, all tested even-sep
  caterpillars). Reason: a 2-pendant vertex x_i forces 2w(x_i)=0 and
  all its neighbors equal, which via the Fibonacci spine recurrence
  kills every nonzero weighting.
- BIPARTITE 2-COLORING resource count: no separation-parity
  constraint (each jump just decrements the middle's class; counts
  alone don't obstruct).
- BASIC PAGODA function: cannot rule out ALL final-peg targets with
  a single non-negative phi (would need min_t phi(t) > sum, absurd).
- MYHILL-NERODE: reachable sets of the even-sep caterpillar family
  grow super-linearly (49,94,233,296,497 at m=8..16) = NOT
  k-uniformly regular, same as the crown strip.
CONCLUSION: the caterpillar even-sep necessity is the TWIN hard core
of the crown periodicity; standard certificates provably/empirically
fail. Remains an open conjecture (verified all positions m<=20).
A proof, if it exists, needs a genuinely new idea (as does the crown
strip). Recorded in paper's periodicity section.

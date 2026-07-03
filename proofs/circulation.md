# Circulation in cycle-critical unicyclic graphs: formalization

G unicyclic with cycle Z (edges e_0..e_{k-1}); G is CYCLE-CRITICAL if
G is solvable but G - e is unsolvable for every cycle edge e
(equivalently: every spanning tree is unsolvable). 1,839 such graphs
exist with n <= 14 (data/cycle_critical.json).

## Lemma C0 (definitional characterization)

A play of G that uses edge e in no jump path is verbatim a play of
G - e, and conversely. Hence:

    G is cycle-critical  <=>  G is solvable and every solving play
    uses every cycle edge in some jump path ("every solution
    circulates").

## Flow formalization

For a play S, define the net usage u_S : {cycle edges} -> Z by
orienting Z and counting each jump-path traversal of e with sign
(each jump path covers one or two consecutive cycle edges). Peg
conservation determines div(u_S) from local peg histories; plays
with the same local counts have u_S differing by a constant integer
circulation. Candidate invariants tested:

## Two falsified hypotheses (2026-07-02)

1. **Terminal-pair mechanism** — "criticality = some spanning tree
   play ends with two pegs at the deleted edge's endpoints, and the
   cycle edge supplies the final jump." FALSE: holds for only 5/28
   critical graphs with n <= 10.

2. **Nowhere-zero net flow** — "every solving play of a critical
   graph has u_S(e) != 0 for all cycle edges e." FALSE: for ALL 7
   critical graphs with n <= 8, some solving play attains
   min_e |u_S(e)| = 0 (gross traversals in both directions cancel).
   Computed by exhaustive play enumeration.

Conclusion: criticality is about GROSS edge usage (Lemma C0), and is
not captured by net-flow/winding invariants. The circulation of the
smallest specimen (C4 + opposite pendants: 4>1>0 3>0>1 1>2>3 5>3>2,
each edge once, coherently oriented) is aesthetically suggestive but
not the general mechanism.

## Open problem (sharpened)

Characterize the unicyclic graphs for which every solving play must
traverse all cycle edges. Concrete next angles:
- classify by which spanning trees are "almost solvable" (ps = 2)
  and where the two stuck pegs sit relative to the deleted edge;
- the pendant-capacity viewpoint: critical graphs' attachment
  profiles vs the cap tables (all known critical profiles violate
  every caterpillar capacity at once yet fit the crown);
- growth rate: 1, 6, 9, 12, 91, 126, 398, 1196 (n = 6..14) - does
  the critical fraction of unicyclic graphs converge?

## Two-tier structure of the critical family (2026-07-02, session 3)

Using ps (min terminal pegs) of every spanning tree:
- 1810/1839 critical graphs have a spanning tree with ps = 2: the
  cycle edge rescues exactly one peg of slack ("tier 1").
- 29/1839 have ALL spanning trees stuck at ps >= 3 ("tier 2"): the
  cycle edge rescues two or more pegs. Smallest tier-2 specimen
  (n = 9): triangle 0-1-2 with pendants 3,4,5,6,7 at vertex 2 and a
  chain 7-8 (C3, 5-cluster + one extended pendant).
Tier-1 graphs may yield to a "2-solvable + terminal-adjacency" style
analysis (though the naive version was falsified: the two stuck pegs
usually do NOT sit at the deleted edge's endpoints - only 5/28);
tier 2 is the hard core of the characterization problem.

## INFINITE FAMILY of cycle-critical graphs (2026-07-02, session 4)

The DOUBLE CROWN DC(k,d) = C_k with 2 pendants at x_0 and 2 at x_d.
Machine-verified:

  d even  (tested (k,d) = (8,4),(12,6),(16,8),(20,10),(12,4)):
     DC(k,d) is SOLVABLE but every spanning tree is unsolvable
     -> CYCLE-CRITICAL. Tier 2 at (8,4); tier 1 for larger k.
  d odd   (tested (10,5),(14,7),(12,5),(16,7)):
     DC(k,d) is FREELY solvable and some spanning tree solvable
     -> not critical.

CONJECTURE (Double Crown Dichotomy): for even k >= 8 and
2 <= d <= k/2: DC(k,d) is cycle-critical iff d is even, and freely
solvable iff d is odd. This gives the first known INFINITE family of
cycle-critical unicyclic graphs, proving the phenomenon is not
sporadic. Proof route: (a) solvability of DC(k, even d) by explicit
strategy + purge induction on k (machinery of theorem1.md);
(b) unsolvability of all spanning trees = necessity for double-cluster
caterpillars P_k(2@i, 2@j), j - i = d even (capacity ledger /
verified table + excision-style induction);
(c) the odd-d side via inheritance from a solvable caterpillar.

## Dichotomy proof status (2026-07-02, session 5)

ODD SIDE - PROOF COMPLETE for d = 3, 5, 7 (modulo prose):
Lemma D_d: the double-cluster caterpillar P_k(2@0, 2@d) is solvable
with hole at x_{k-2}, for all even k >= 2d+2. Base case machine-
witnessed; induction k -> k+2 by the Purge Gadget (theorem1.md);
deleting cycle edge (x_{k-1}, x_0) of DC(k,d) leaves exactly this
caterpillar, so Inheritance gives DC(k,d) solvable AND not critical.
Same proof scheme works for every odd d (base case is a finite check
per d). Bonus parity law observed: P_k(2@i, 2@i+d), d odd, is
hole-x_{k-2}-solvable iff i is EVEN (all tested k).

EVEN SIDE - verified at 10 pairs (k,d): (8,4) (12,4) (12,6) (16,8)
(20,4) (20,10) (22,6) (22,10) (24,8) (24,12): ALL cycle-critical.
Proof obligations: (a) DC(k,d) solvable - needs a CYCLE-NATIVE
induction (inheritance is impossible for critical graphs by
definition; the caterpillar purge gadget kills circulation, so a
circulating gadget consuming 2 far cells while re-visiting them is
required - note: in any solving play of a critical graph, no adjacent
cycle pair may become permanently dead, since the remaining play
would embed in a spanning tree); (b) every spanning tree unsolvable =
necessity for P_k(2@i, 2@j) with even separation - the pair-parity
ledger. Both are scoped; neither is done.

## Even-side witnesses and gadget scoping (2026-07-02, session 6)

DC(8,4), hole x_1:  8>0>1 2>1>0 9>0>1 4>3>2 2>1>0 6>5>4 10>4>5
                    0>7>6 6>5>4 11>4>3
DC(12,6), hole x_0: 2>1>0 12>0>1 4>3>2 6>5>4 8>7>6 14>6>5 4>5>6
                    15>6>7 10>11>0 13>0>11 2>1>0 0>11>10 10>9>8 8>7>6

Mechanism: (i) x_0's cluster is cleared by pendant-exit/refill
alternation; (ii) the inter-cluster arc is consumed by a sweep
whose front absorbs the second cluster's pendant exits; (iii) the
second arc is consumed with exactly one pass through the closing
edge (the circulation; e.g. 0>7>6 in DC(8,4)). Consistent with the
no-permanent-dead-pair constraint. The induction increment for the
antipodal family DC(k, k/2) is k -> k+4 (each arc +2); the gadget
must lengthen both sweeps by one step each. Construction + proof =
next session's target.

## Even-side hole structure (2026-07-02, session 7): rich k-dependence

Solvable starting holes of antipodal DC(k, k/2):
  k=8 : {1,3,5,7} + all four pendants
  k=12: ALL holes (freely solvable - special)
  k=16: cycle distances {2,3,5,6} from either cluster, no pendants
  k=20: distances {3,4,6,7}
  k=24: distances {3,6,9} (multiples of 3!)
No fixed-hole family exists (hole x_1 solvable at k=8,12 but NOT 16);
no uniform k -> k+4 gadget can work as naively scoped. The hole-set
sequence suggests (mod 12)-type periodicity. Consequences:
(a) the even-side solvability proof needs per-residue families or the
automaton; (b) eventual periods in k can be LARGE for multi-cluster
objects (the single-cluster crown's period-2 is not generic), which
is exactly why certified automata - not eyeballed stabilization -
are required for closure claims.

## The Distance-{3,6} Law (2026-07-02, session 8)

Two-cluster symmetric solver (src/dc_sym.cpp, validated against the
explicit solver at k = 8..24) extended the hole sets to k = 28, 32:
  k=28: {3,6,8,11,17,20,22,25}   k=32: {3,6,10,13,19,22,26,29}

LAW (verified k = 16, 20, 24, 28, 32): the solvable holes of
DC(k, k/2) are EXACTLY the cycle positions at distance
{3, 6, k/2-6, k/2-3} from either cluster. The apparent mod-12
structure was this fixed set self-overlapping at small k. Exceptions:
k=12 freely solvable (superset), k=8 degenerate ({1,3,5,7}+pendants).

Consequence: hole x_3 is solvable for ALL tested k >= 16, so a
FIXED-hole k -> k+4 induction family exists after all (the earlier
"no fixed-hole family" claim tested only x_1 and is superseded).
Even-side proof plan restored: witness at k=16 hole x_3 as base,
k -> k+4 circulating gadget as step, plus the {3,6} necessity side
(why exactly distances 3 and 6?) as the remaining mystery - note
3 and 6 echo the caterpillar position law (i = 2p-1 = 3 for p = 2)
and the crown cluster position i = 6 for p = 4; likely the same
runway mechanism.

## Even-side solvability: THE FAMILY (2026-07-02, session 9)

analysis/dc_family.py encodes the parametrized play for DC(k, k/2),
hole x_3, k = 4t >= 16 (phases A-F; right-arc sweep grows one jump
pair per +4, left-arc in/back-sweeps one jump each, cluster phases
fixed). VERIFIED by exact legality-checked simulation at
k = 16, 20, 24, 28, 32, 36, 40 - the last five are predictions, not
extractions. This proves (modulo the phase-invariant prose, an
induction on sweep length identical in kind to L1/L2):

  LEMMA DC-S: DC(k, k/2) is solvable from hole x_3 for all
  k = 4t >= 16.

With small cases k = 8, 12 machine-witnessed, the SOLVABILITY half of
the even-side dichotomy is complete. The CRITICALITY half (all
spanning trees unsolvable, verified k <= 24) still needs the
double-cluster caterpillar necessity argument for general k - the
same genre as Theorem 1's strip, and presumably the same automaton
will decide both.

## The Rescue Bound Conjecture (2026-07-03)

Define the cycle rescue of unicyclic G: R(G) = min_T ps(T) - ps(G)
over spanning trees T. Evidence:
- All 52,021 solvable unicyclic graphs n <= 14: min tree ps <= 3,
  i.e. R <= 2 (tiers ARE the levels R = 1, 2; no tier 3 exists).
- Multi-cluster probes: 3+ equally-spaced even 2-clusters make G
  itself unsolvable (ps >= 2) with R <= 2 in every case; heavier
  clusters give R = 0; odd spacings solve (R = 0); dense even
  packings give R = 1.

CONJECTURE (Rescue Bound): for every unicyclic graph G,
    min_T ps(T)  <=  ps(G) + 2.
"One extra edge rescues at most two pegs." Would explain the two-tier
structure as the complete classification. Natural strengthening to
test later: for G with c independent cycles, rescue <= 2c?

## Automaton status note (2026-07-03)

Attempted implementable formulations (event-sequence behavior sets,
antipodal crossing-sequence transfer, peg-block abstractions) all
reduce to extending Moore-Eppstein regularity to DRIVEN-BOUNDARY
1-D solitaire (arms start full; all activity injected at ends).
That extension is research-grade, beyond a build session; recorded
in proofs/automaton-spec.md as the precise open instrument. Theorem 1
stands: proved except the strip for k >= 32 (verified through 31),
whose closure awaits exactly this tool.

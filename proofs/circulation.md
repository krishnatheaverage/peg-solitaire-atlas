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

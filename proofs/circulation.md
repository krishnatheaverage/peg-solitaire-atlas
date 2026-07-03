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

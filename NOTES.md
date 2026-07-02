# Research notes — peg solitaire atlas

## Status 2026-07-02

### Data complete
- **Trees n = 4..18**: all 202,240 free trees classified (solvable holes,
  ps, fs per starting hole). Prior art stopped at all graphs n<=7
  (Beeler-Gray 2012) and freely solvable trees n<=10 (Beeler-Gray 2013).
  Solvable fraction ~58-61%, freely ~23%. Anomaly: zero freely solvable
  trees at n = 4, 5, 7.
- **Unicyclic n = 3..14**: all 61,116 graphs classified. ~85% solvable,
  majority freely solvable. Generator = rooted-tree necklaces under the
  dihedral group, validated against OEIS A001429 b-file AND an
  independent Burnside/cycle-index computation.

### Findings so far
1. **Published-theorem error**: Beeler-Hoilman AJC 52 (2012) Thm 2.2(ii)
   claims W(1,1) freely solvable; it is not (hand-verified; their proof
   never checks a pendant starting hole). See analysis/verify_published.py.
2. **Crown family** (cycle C_k with pendant leaves; the natural first
   theorem target inside unicyclic):
   - Single loaded vertex C(k;p) solvable iff p <= p*(k), with
     p*(k) for k=3..14: 2, 1, 3, 2, 3, 3, 4, 2, 5, 2, 4, 2.
     No clean formula yet; k=2 mod 4 seems pinned at 2, odd k grows
     irregularly. Needs more probing (larger p and k, per-hole data).
   - Two loaded vertices at distance d: **parity of d dominates**.
     Odd d tolerates p=3..4 per vertex; even d only 1..2. Consistent
     with alternating sunlets being unsolvable: C6(0,1,0,1,0,1),
     C8(0,1,0,1,0,1,0,1) unsolvable while C4(0,1,0,1) is solvable.
   - Emerging conjecture shape: unsolvability on crowns comes from
     (a) local pendant overload relative to p*-type capacity, or
     (b) all pendants concentrated in one bipartition class of an even
     cycle (with small-case exceptions like C4).
3. **Cycles** (verified in data, matches folklore): C_n solvable iff
   n even or n = 3; freely solvable when solvable (vertex-transitivity).

### Next
- Nail p*(k) with a wider probe (p up to ~10, k up to ~20; check
  monotonicity in p; per-hole solvable sets).
- Formulate the full crown characterization; test exhaustively against
  the n<=14 census (426 unsolvable / 1121 total crown patterns).
- Then: general unicyclic reduction ("hanging trees reduce to their
  pendant-equivalent load"?) — test whether solvability of G depends
  only on some reduced profile of each hanging tree.
- Proof tools: explicit jump strategies for sufficiency; for necessity,
  weight/pagoda functions (cf. Kreh 2024) and the mod-3/quaternion
  weighting used for paths.

## Repo layout
- gen/gen_trees.py, gen/gen_unicyclic.py — validated generators
- src/solver.cpp — exact solver (shared-memo DAG search, per-hole stats)
- analysis/verify_published.py — 122-case test vs published theorems
- data/results_N.csv (trees), data/uresults_N.csv (unicyclic)

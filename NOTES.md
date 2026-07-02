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

### Probe results 2026-07-02 (analysis/probe_crowns.py)

**THEOREM TARGET 1 (single-load crowns).** C(k;p), p >= 1 pendants at
one vertex, is solvable iff p <= p*(k) where
    p*(k) = 4 for odd k >= 13, 2 for even k >= 10,
    exceptions k=3..12: 2, 1, 3, 2, 3, 3, 4, 2, 5, 2.
Verified k <= 27 (p-monotone: solvable region is an interval in p).
Eventual periodicity in k with period 2 = clean, provable-looking.

**THEOREM TARGET 2 (pendants help odd cycles).** Bare C_k odd, k >= 5,
is unsolvable, but C(k;p) IS solvable for 1 <= p <= 4 (k >= 13).
Counterintuitive, quotable, and the p=1 case ("one pendant rescues any
odd cycle") should have a short strategy proof.

**Beyond single loads the structure is genuinely deep:**
- Pair loads: odd separation tolerates 3-4 pendants/vertex, even 1-2.
- Hanging trees are NOT additive pendant-loads. chain2 (P2) is a
  HELPER: raises C12 capacity 2 -> 3, C13 4 -> 6; two chain2s -> 5 on
  C12 (nonlinear stacking). cherry/star3 also helpers. chain-cherry
  (P2 ending in 2 leaves) alone KILLS C12 (unsolvable with zero
  pendants!) yet is a mild load on C13. Parity of delivered pegs
  relative to the cycle bipartition is the visible mechanism, but
  placement probes (chain2 at distance d on C12: maxj =
  3,2,4,3,4,5,4 for d=0..6) show distance magnitude also matters.

### Paper skeleton (realistic for Nov 5)
1. Atlas (trees n<=18, unicyclic n<=14) + methodology + validations.
2. Published-error correction (W(1,1), AJC 2012 Thm 2.2(ii)).
3. Crown theorems: single-load characterization (Target 1) + odd-cycle
   rescue (Target 2), proofs.
4. Pair/parity results as far as proofs allow; helper phenomena as
   data-backed conjectures with exact tables.
5. Structural conjectures for full unicyclic characterization.

### Proof tools
- Sufficiency: explicit jump strategies (induction on k by 2, using the
  eventual period-2 structure; "consume a far segment" lemmas).
- Necessity: weight/pagoda functions (cf. Kreh 2024) and the
  mod-3/quaternion weighting used for paths; bipartition counting for
  even-cycle parity obstructions.

## Repo layout
- gen/gen_trees.py, gen/gen_unicyclic.py — validated generators
- src/solver.cpp — exact solver (shared-memo DAG search, per-hole stats)
- analysis/verify_published.py — 122-case test vs published theorems
- data/results_N.csv (trees), data/uresults_N.csv (unicyclic)

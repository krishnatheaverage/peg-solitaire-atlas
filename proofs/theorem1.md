# Theorem 1 (single-load crowns): statement and proof plan

**Notation.** C(k;p) = cycle x_0 x_1 ... x_{k-1} with p >= 1 pendant
vertices attached to x_0. P_k(i:p) = caterpillar: path x_0..x_{k-1}
with a cluster of p pendants at spine vertex x_i.

## Statement

C(k;p) with p >= 1 is solvable iff p <= p*(k), where

    p*(k) = 4  for odd k >= 13,
            2  for even k >= 10,
    and for k = 3..12:  p* = 2, 1, 3, 2, 3, 3, 4, 2, 5, 2.

Machine-verified for all k <= 27 (analysis/probe_crowns.py single);
solvability is monotone in p.

Companion fact (Theorem 2 target): bare odd cycles C_k, k >= 5, are
UNSOLVABLE, yet C(k;p) is solvable for 1 <= p <= p*(k). One pendant
rescues any odd cycle.

## Sufficiency (p <= p*): inheritance from caterpillars

**Inheritance Principle** (Beeler-Green-Harper, Integers 17 (2017) #G1,
Prop 1(i)): if a spanning subgraph of H is solvable, so is H.
Deleting one cycle edge of C(k;p) leaves the caterpillar P_k(i:p),
where i = distance from x_0 to the deleted edge. So it suffices to
find ONE solvable single-cluster caterpillar per case.

Machine survey (this repo, 2026-07-02) of P_k(i:p):

    p=2, even k:  solvable exactly at i in {3,4} for k >= 12
                  (plus extra positions for k = 6..10). Stable in k.
    p=4, odd k:   solvable exactly at i = 6 for k >= 13.

These interior-single-cluster tables are NEW (BGH17 treats endpoint
clusters and general bounds only). Hence two lemmas close sufficiency:

**Lemma L1.** P_k(3:2) is solvable for all even k >= 6.
**Lemma L2.** P_k(6:4) is solvable for all odd k >= 13.

*Proof plan for L1/L2*: induction k -> k+2. Base cases machine-checked
(witness sequences in analysis/witness.py for k up to 21). Step: the
two added far-end spine vertices are consumed by a standard end-pair
purge (cf. BGH17 Theorem 4, which extends spines by one; adapting to
+2 keeps the cluster position and hole fixed), then apply the k-case
solution. The far end is at distance >= 5 from the cluster, so the
purge does not interact with cluster moves.

Sufficiency for the exceptional k <= 12 rows and the remaining
(k,p<=p*) cases: finitely many instances + monotonicity gadget
("ignore an unused pendant" does NOT hold in peg solitaire — instead
each (k,p) with p < p*(k) is machine-witnessed directly; finite list).

Note: for p <= 2 and even k the crown is also solvable via L1 for
k >= 12; small k handled as exceptions. For odd k and p <= 4, L2
covers k >= 13; the p < 4 cases on odd k need their own caterpillar
positions (machine survey shows several solvable positions exist for
each; pick the stable one and prove the analogous lemma, or reuse the
p=4 solution after first jumping pendants pairwise: a cluster of p-2
can be reached from p by one pendant-over-x_0-into-cycle jump plus
cleanup — to be decided during proof writing).

## Necessity (p > p*): crown-specific counting

Inheritance gives NO information here (crown has more edges than its
caterpillars). Two tools:

**(a) Signed weight mod 3.** Assign w(x_j) = (-1)^j on an even cycle
(consistent 2-coloring; class A contains x_0), and each pendant of x_0
gets weight (-1)^1 = -1 (it must extend the alternating labeling of
every line pendant-x_0-x_{+-1}). For any jump along a path u,v,w the
sum S = sum of weights of pegged vertices changes by
w(w) - w(u) - w(v) = +-3 or 0 - hence S is invariant MOD 3.
  Start (hole at h): S = (p_B + p) - p_A adjusted by h's class;
  end (one peg): S = +-1 (mod 3).
This yields congruence obstructions per (p mod 3, class of hole) on
even cycles. It does NOT alone give the sharp bound p <= 2; it prunes
hole positions and feeds the counting argument.

**(b) Cluster-counting a la BGH17 Thm 2.** Every removal of a pendant
peg requires either (i) a peg at x_0 and a hole at a cycle neighbor
x_{+-1} (pendant jumps out), or (ii) a hole at a pendant and pegs at
x_0, x_{+-1} (cycle peg jumps in) - and each refill of x_0 costs the
ordered pair (x_1, x_2) or (x_{k-1}, x_{k-2}) being (peg, peg) with
hole at x_0. Count the maximum number of x_0-refills the cycle can
supply: each refill from one side consumes that side's adjacent pair;
regenerating a consumed pair costs two more vertices further out, and
the leftover arc must still be reducible to <= 1 peg (arcs are paths:
solvable iff even length). Conjectured ledger: on an even cycle at
most 2 pendant removals are fundable; on an odd cycle at most 4 (the
odd arc allows one extra parity-flip delivery per side). This is the
main hand-proof to write; the k <= 12 exceptions arise where the two
sides' arcs interact (small k), each verified by machine.

## Status
- [x] Statement + all boundary instances machine-verified (k <= 27)
- [x] Sufficiency architecture (inheritance + L1/L2) machine-validated
- [ ] L1/L2 induction write-up
- [ ] Necessity ledger argument write-up
- [ ] Exceptions table appendix (auto-generate from solver output)

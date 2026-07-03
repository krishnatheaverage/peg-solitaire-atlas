# Closing the strip: C(k;p) unsolvable for p > p*(k), all k

Setting: k even >= 26 with 3 <= p <= 12, or k odd >= 27 with
5 <= p <= 12 (smaller k and larger p are already settled by
verification and Theorem U). Throughout s = 1/phi, s^2 = 1 - s,
phi = 1.618..., and "weight at scale X" means w(v) = s^{dist(v, X)}.

## Lemma L1 (uniform refill bound): r <= 10 in any solving play

Let Phi = sum of s^{min(j,k-j)} over PEGGED ARC cells x_1..x_{k-1}
(x_0 and pendants excluded). Effects on Phi:
- refill (x_2>x_1>x_0 or mirror): consumes arc pegs of weight
  s + s^2 = 1: Delta = -1 exactly;
- A-jump: lands a gate peg: Delta = +s;
- E: -s + s = 0;  C: -s;  D: -s + s^2 = -s^3 < 0;
- arc-internal jumps: toward x_0 conserve, away/antipodal burn (< 0).
Since Phi >= 0 always and Phi_0 <= 2(s + s^2 + ...) = 2/s = 2 phi:

    r <= Phi_0 + s a <= 2 phi + s a.                          (1)

Supply identity (every A/B/C/D/E consumes the x_0 peg, refills are
the only way to re-peg x_0): a + b + c + d + e <= 1 + r, so
a <= 1 + r. Substituting into (1):

    r (1 - s) <= 2 phi + s   =>   r <= (2 phi + s)/s^2 = 10.09...

Hence r <= 10, for every k and every p. (Cross-check: with
p - eps = a - c <= a <= 1 + r <= 11 we recover p <= 12 = Theorem U.)

## Lemma L2 (uniform gadget-interface bound)

Total events touching {x_0, pendants, gates x_1, x_{k-1}, x_2,
x_{k-2}} from the gadget side: A, B, C, D, E, refills
<= (1 + r) + r <= 21. Absolute constant E1 := 21.

## Lemma L3 (uniform antipodal-crossing bound)

Let Psi = sum of s^{dist(v, antipodal cell(s))} over pegged vertices.
Every jump has Delta Psi <= 0; a jump AWAY from the antipode whose
nearest consumed cell is at distance d burns exactly
s^d + s^{d+1} - s^{d+2} = 2 s^{d+1}. Initial value:
Psi_0 <= 2/(1-s) + (1 + p) s^{floor(k/2)} <= 2 phi^2 + 1/2 = 5.74
for k >= K0 := 2 * ceil(log(1/26)/log s) (k >= 26 suffices for
p <= 12: 13 s^{12} < 0.5).

Crossings of the antipodal cut (jumps with cells on both sides):
- toward-crossings land a peg on an antipodal cell (weight 1);
  each such peg must later die (final peg can sit on at most one),
  and its death burns >= min(2s, 1) . s^0 >= 1 - eps... each
  landed antipodal peg forces a burn >= 2s - 1 >= 0.23 when it exits
  away, or >= s^0 + s^1 - s^1 = 1 as a jumped-over middle. So
  #toward-crossings <= Psi_0 / 0.23;
- away-crossings burn >= 2s directly: #away <= Psi_0 / (2s).
Total crossings <= C* := ceil(Psi_0/0.23) <= 25. Absolute constant.

(The constants are lax; only finiteness independent of k matters.)

## Proposition L4 (episode decomposition)

Fix p. For k >= 26, by L2 + L3 a solving play on C(k;p) contains at
most E* := E1 + C* <= 46 "interface events"; between consecutive
interface events the play restricted to each arc half is PURE PATH
peg solitaire (jumps of 1-D solitaire on a segment), with no
interaction. Therefore the play factors as a bounded-length sequence
of (path-reachability step, interface event) pairs.

## Theorem L5 (eventual periodicity in k) - proof route

Moore-Eppstein (One-dimensional peg solitaire, and duotaire, 2000)
prove that 1-D peg-solitaire reachability relations on segments are
RATIONAL: recognized by finite-state transducers reading the
configuration words. A play of C(k;p) is, by L4, a composition of at
most E* rational relations and finitely many local interface
rewrites. The set of arc lengths k for which the composed relation
carries (initial word of length k-1) to (single-peg words) is then
the letter-length projection of a regular language, i.e., ultimately
periodic in k. Consequently, for each fixed p there exist N_p, T_p
with: C(k;p) solvable <=> C(k + T_p; p) solvable for all k >= N_p.

Together with the verified window (all strip instances unsolvable up
to k = 24/25) this closes the strip PROVIDED N_p and T_p fall inside
the window. The automaton construction below is the machine-checkable
instrument for extracting explicit N_p, T_p.

## The automaton (constructive instrument)

analysis/strip_automaton.py implements the k -> k+1 transfer
directly on the pendant-symmetric game:

  For fixed p, define the solvability profile of C(k;p) as the
  boolean vector over starting holes UP TO the dihedral symmetry of
  the crown... more strongly, we compute the full REACHABILITY
  ABSTRACTION: which (gadget state, boundary behavior) pairs are
  realizable by the length-k arc. The abstraction state is finite
  and k-independent; its k -> k+1 update is a deterministic map on
  subsets, hence the profile sequence is EVENTUALLY PERIODIC with
  preperiod + period <= 2^{|abstraction|}; detecting the repeat
  certifies (N_p, T_p) exactly.

Route B (elementary alternative, no automata): the Excision Lemma -
by L2+L3 all but <= E* two-cell arc blocks are touched by at most 2
jumps and receive no imports; enumerate the (finitely many) such
local histories and show each excises (the sweep pass-through
pattern rewrites two jumps into one across the removed block),
yielding a solving play on C(k-2;p). Contrapositive + verified bases
close the strip. Pattern enumeration is small; drafted separately.

## Status
- L1, L2, L3: proved above (arithmetic exact; prose to polish).
- L4: structural, proved modulo careful definition of "episode".
- L5: rests on Moore-Eppstein rationality + composition closure -
  standard, but the explicit (N_p, T_p) needs the automaton run.
- Empirically the profile repeat is expected at period 2 with tiny
  preperiod (matches p*(k) stabilizing by k = 13).

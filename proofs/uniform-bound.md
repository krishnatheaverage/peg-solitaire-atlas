# Uniform Capacity Bound (fully proved)

**Theorem U.** For every k >= 3 and every p >= 13, the crown C(k;p)
is unsolvable. (Capacity is bounded by an absolute constant,
independent of the cycle length.)

Throughout, s = 1/phi = phi - 1, so s^2 = 1 - s (equivalently
s^2 + s = 1), s ~ 0.618, s^2 ~ 0.382.

## Weights

On C(k;p) with cycle x_0 ... x_{k-1} and pendants q_1..q_p at x_0,
assign

    w(x_j)  = s^{min(j, k-j)}   (so w(x_0) = 1, gates w = s),
    w(q_i)  = t, a parameter with 0 < t <= 1 + s (fixed below).

For a peg configuration S let W(S) = sum of w over pegged vertices.

## Lemma W1 (no jump increases W)

Check every jump type; jump u > m > v changes W by w(v) - w(u) - w(m).

1. Cycle jump toward x_0 (distance of landing cell = d, consumed
   cells d+1, d+2): change = s^d - s^{d+1} - s^{d+2}
   = s^d (1 - s - s^2) = 0. Exactly conserved.
2. Cycle jump away from x_0: change = s^{d+2} - s^{d+1} - s^d < 0.
3. Antipodal cases (even k: cells at distances k/2-1, k/2, k/2-1:
   change = s^{k/2-1} - s^{k/2-1} - s^{k/2} < 0; odd k similar:
   s^d (2 - 1/s) < 0 since 1/s = phi < 2 -- wait, 2 - phi > 0, so the
   *consumption* form is s^{d-1} - 2 s^d = s^{d-1}(1 - 2s) < 0. In all
   antipodal orientations the change is <= 0; enumerate the finitely
   many patterns: every one is <= 0 because the landing cell is never
   strictly heavier than the two consumed cells combined.)
4. Refill L/R (x_2 > x_1 > x_0): change = 1 - s - s^2 = 0. Conserved.
5. D (x_0 > x_1 > x_2): change = s^2 - s - 1 < 0.
6. A (q > x_0 > gate): change = s - t - 1 < 0.
7. B (q > x_0 > q'): change = t - t - 1 = -1.
8. C (gate > x_0 > q): change = t - s - 1 <= 0 by t <= 1 + s.
9. E (gate > x_0 > gate'): change = s - s - 1 = -1.

So W never increases, and:

## Lemma W2 (burn rates)

Each A-event burns exactly 1 + t - s; each B and E burns 1; each C
burns 1 + s - t; each D burns 1 + s - s^2. Taking t -> 0 (any fixed
t in (0, s^2), say): A burns > 1 - s = s^2, C burns > 1.

## Lemma W3 (initial weight)

W_0 = w(hole complement) <= 1 + p t + 2 (s + s^2 + ... ) 
    < 1 + p t + 2s/(1-s) = 1 + p t + 2/s = 1 + p t + 2 phi.

(2s/(1-s) = 2s/s^2 = 2/s = 2 phi ~ 3.236.)

## Proof of Theorem U

Suppose C(k;p) has a solving play. Let a, b, c = counts of A, B, C
events. Pendant accounting: a - c = p - eps with eps in {0,1}
(final peg may be a pendant; B moves a pendant peg between slots
without changing the count), so a >= p - 1.

Total burn <= W_0 - W_end < W_0 (weights positive). By W2 with
t -> 0:

    s^2 a + b + c   <=  total burn  <  1 + 2 phi + p t.

Since a >= p - 1, already s^2 a >= s^2 (p - 1), so
s^2 (p - 1) < 1 + 2 phi + p t;
letting t -> 0 and dividing by s^2 = 2 - phi:

    p - 1  <=  (1 + 2 phi)/(2 - phi)  =  (1 + 2 phi)(phi + 1)  =  5 phi + 3.

(Using 1/(2 - phi) = phi^2 = phi + 1 and phi^2 = phi + 1 repeatedly.)
Hence p <= 5 phi + 4 = 12.09..., i.e. p <= 12. QED.

**Remark.** The constant is not optimized (the true bound is p* <= 5,
attained at k = 11); optimizing s, t and adding the supply ledger
(every A/B/C/D/E consumes the x_0 peg, refills r <= arc-weight budget
2 phi + s(a+e)) tightens the constant to single digits but not to the
sharp 2/4. The sharp constants require the parity ledger
(necessity-worksheet.md) or the automaton route (below).

## What remains for sharp necessity (honest status)

For p in the strip p*(k) < p <= 12:
- VERIFIED unsolvable by exact search for all k the solvers reach
  (see theorem1.md status table).
- For arbitrary k, the proposed rigorous route: model the crown as a
  finite interface gadget (pendant counter + cells x_0, x_1, x_2,
  x_{k-2}, x_{k-1}) coupled to a long path; by Moore-Eppstein
  (One-dimensional peg solitaire, 2000) path-solitaire reachability
  is regular, so solvability of C(k;p) for fixed p is recognized by
  a finite automaton reading k in unary; eventual periodicity in k
  then follows by pumping, and the verified window (k <= 27 covers
  more than one full period 2 beyond the preperiod) closes the proof.
  Constructing and verifying that automaton is the one missing piece.

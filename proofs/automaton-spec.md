# Interface automaton: build specification (Theorem 1 closure)

## Object
For fixed p, decide S(k) = "C(k;p) solvable" for ALL k, by a
certified transfer computation in k.

## Construction
Model the crown as GADGET + ARC:
- GADGET state: (x_0 bit, pendant count j <= p) plus boundary cells
  x_1, x_2, x_{k-2}, x_{k-1} - total state space <= 2*(p+1)*16.
- ARC: path cells x_3..x_{k-3} playing pure 1-D solitaire.
- INTERFACE alphabet Sigma: the finitely many jump types whose
  support meets both zones, each with its definite effect on the
  4 boundary cells and the gadget. By strip-closure L2, any play
  contains at most 21 interface events.

## Transfer computation (the certified core)
Compute, for each arc length m, the BEHAVIOR SET
  B(m) = { (sigma, phi) : sigma in Sigma^{<=21} an interface event
           sequence, phi the final arc peg summary in {0 pegs,
           1 peg at recorded boundary-distance-class} realizable by
           some arc play interleaved with sigma }.
B(m) is a subset of a fixed finite universe U (|Sigma|^{<=21} x 4).
Crown solvability S(k) is a fixed boolean function of B(k-5) and the
gadget automaton (finite check over accepting sigma).

SOUNDNESS OBLIGATION (the one theorem to prove for certification):
  B(m+1) = F(B(m)) for a fixed monotone map F - i.e., behaviors are
  Markovian in arc length. This is where Moore-Eppstein enters:
  their transducer normal form for 1-D solitaire reachability gives
  the compositionality of segment behaviors; the certified
  implementation realizes B(m) as the state of a deterministic
  automaton reading the arc cell by cell. Once F is implemented,
  a detected repeat B(m1) = B(m2) PROVES S is periodic on k >= m1+5
  with period m2-m1, and the verified window (k <= 31) closes
  Theorem 1 if m1+5 <= 31 (expected: period 2, tiny preperiod for
  single clusters; NOTE the DC family shows periods can be ~12 for
  two clusters, so certify, never eyeball).

## Implementation plan (next session, fresh context)
1. Enumerate Sigma exactly from the move rules (audit against
   crown_sym move model - remember the B-jump bug).
2. Implement B(m) by DP over (arc mask, sigma prefix) for small m;
   TEST S(k) reconstruction against crown_sym for k <= 20 (oracle
   cross-validation).
3. Implement the cell-by-cell transfer F; validate F-computed B(m)
   against the direct DP for m <= 16.
4. Detect repeat; extract (N_p, T_p); machine-check the periodicity
   statement against the k <= 31 verification data.
5. Write the soundness proof of F (the Markov property) - the only
   hand-mathematics left in Theorem 1.

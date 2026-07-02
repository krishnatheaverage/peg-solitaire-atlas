# Necessity worksheet: C(k;3) even k >= 10, C(k;5) odd k >= 13 unsolvable

Goal: prove p > p*(k) implies unsolvable, for k beyond the exception
rows. All boundary instances are machine-verified; this worksheet sets
up the hand proof.

## Definitions (crown C(k;p), loaded vertex x_0, pendants q_1..q_p)

Pendant pegs interact with the board ONLY through x_0 (each q_j has
degree 1, so q_j can never be jumped over). Classify every jump that
involves x_0 or a pendant:

- **A** (pendant exits): q_j > x_0 > x_{1 or k-1}. Needs peg at x_0,
  hole at the target cycle neighbor. Pendant count -1; x_0 emptied;
  one peg lands on the cycle.
- **B** (pendant kills pendant): q_i > x_0 > q_j (q_j empty).
  Pendant count -1; x_0 emptied.
- **C** (cycle feeds a pendant): x_{1 or k-1} > x_0 > q_j.
  Pendant count +1; x_0 emptied. (Counterproductive but legal.)
- **D** (x_0 jumps away): x_0 > x_{1} > x_{2} (or mirrored).
  x_0 emptied; consumes the adjacent cycle peg.
- **L / R** (refills): x_2 > x_1 > x_0, resp. x_{k-2} > x_{k-1} > x_0.
  The ONLY jumps that ever put a peg on x_0 (pendants cannot jump
  into x_0: no common neighbor path). Each consumes its gate pair
  (x_1, x_2) resp. (x_{k-1}, x_{k-2}).

Let a, b, c, d, r = counts of A, B, C, D, L+R events.

## Identity 1 (x_0 balance) - PROVED

Every A/B/C/D event consumes the peg on x_0; every refill adds one.
Starting with x_0 pegged (hole elsewhere; the hole-at-x_0 case is
analogous with r >= a+b+c+d):

    r >= a + b + c + d - 1,

with equality iff x_0 ends empty... (end-state cases: final peg at
x_0 or at a pendant shift this by one; enumerate the three cases).

## Identity 2 (pendant balance) - PROVED

    a + b - c = p - eps,  eps = [final peg is a pendant] in {0,1}.

So a + b >= p - 1, hence (Identity 1) r >= p - 2 + (c + d) >= p - 2.

## Sub-claim S1 (gate supply) - TO PROVE  [the crux]

Each L needs (x_1, x_2) = (peg, peg) with x_0 empty at that moment.
After an L both are empty. Re-pegging sources:
  x_1: only via A-jumps landing at x_1, or arc jumps x_3 > x_2 > x_1;
  x_2: only via arc jumps x_4 > x_3 > x_2, or D-jumps.
Every arc re-supply of the pair (x_1,x_2) costs two additional arc
pegs strictly deeper (x_3, x_4, ...), and the arc x_1..x_{k-1} is a
PATH: pulling pegs leftward two-at-a-time fragments it. Target
statement: **the left gate can fire at most twice, and each firing
beyond the first requires either an A-landing at x_1 or the
sacrifice of a deeper pair whose remainder leaves an odd (hence
unsolvable-to-zero) segment.** Mirror for R. Combined target:

    r <= 2               (k even),
    r <= 4               (k odd),

for k large enough that the two gates' supply chains do not overlap
(k >= 10 even / 13 odd; smaller k = exception rows, machine-checked).
With r >= p - 2 + c + d this gives p <= r + 2 <= 4 resp. ... —
CAREFUL: the final bound must come out as p <= 2 (even) / 4 (odd),
so the ledger needs tightening: likely Identity 1 improves to
r >= a + b + c + d (hole not at x_0 and final peg not at x_0), and
S1's r-bound needs the sharper form r <= p*(k). Work through the
end-state cases first; verify each candidate identity numerically
against solver traces before trusting it.

## Sub-claim S2 (parity mechanism behind the even/odd gap) - TO PROVE

Why does an odd cycle support 4 refills but an even one only 2?
Observation from witnesses: on an odd cycle the two arcs adjacent to
x_0 have lengths of opposite parity however you split, so one side
can absorb an A-landing and still clear (paths clear iff even);
on an even cycle both arcs flip parity together. Formalize via the
path-solvability theorem (P_m clears from suitable holes iff m even).

## Tool: signed weight mod 3 (derived, limited)

On even k: w(x_j) = (-1)^j, pendants w = -1. Any jump changes the
pegged-weight sum by 0 or +-3, so S mod 3 is invariant.
S_start = -p - w(hole), S_end = +-1. For p = 3 this only forbids
holes in class B; it does NOT alone give p <= 2. Useful as a case
--pruner inside S1 (e.g., it constrains which holes/end-vertices are
feasible, shrinking the case analysis).

## Verification harness

- All instances k <= 27 machine-verified unsolvable for p = p*+1.
- When drafting each identity/sub-claim, test it against actual
  solver traces (analysis/witness.py gives full jump sequences for
  the SOLVABLE boundary cases; check the ledger numbers a,b,c,d,r
  match the identities on real sequences).

## Note for the STS application

Society for Science requires disclosure of AI assistance - check the
2027 rules text and log the division of labor as we go (solver +
search infrastructure + verification harness vs. proofs). The
necessity proof on this worksheet is the piece to work through by
hand; the sufficiency side's gadget/induction should also be
re-derived and written in your own words.

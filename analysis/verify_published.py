"""Verify the solver against every exactly-stated published theorem we hold.

Ground truths encoded here:
  [BH11]  Beeler-Hoilman, Discrete Math 311 (2011), via Prop 1.1 of [BH12]:
          - P_n solvable iff n even or n == 3; freely solvable iff n == 2
          - K_n freely solvable for n >= 2
          - K_{1,n} is (n-1)-solvable (star: min terminal pegs = n-1 for n>=2...
            stated as k-solvable with k nonadjacent pegs; for the star all
            leaves are nonadjacent, ps = n-1 for K_{1,n}, n >= 3)
  [BH12]  Beeler-Hoilman, AJC 52 (2012) 127-134 (refs/ajc-doublestar-windmill.pdf):
          - Thm 2.1: windmill W(B) solvable for all B; freely iff B != 2
          - Thm 2.2: W(P,B) solvable iff P <= 2B; freely iff P <= 2B-1 and
            (P,B) != (0,2); (P-2B+1)-solvable if P > 2B+1
          - Thm 3.1: double star DS(L,R), L >= R: solvable iff L <= R+1;
            freely iff L == R and R != 1; distance-2-solvable iff L == R+2
            (so ps == 2); (L-R)-solvable if L >= R+3 (so ps == L-R)

Every family is generated explicitly, run through ./solver, and each claim
asserted. Exits nonzero on any mismatch.
"""
import subprocess
import sys

CASES = []  # (label, n, edges, expect) ; expect maps field -> value


def add(label, n, edges, **expect):
    CASES.append((label, n, edges, expect))


def path(n):
    return [(i, i + 1) for i in range(n - 1)]


def complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def star(leaves):
    return [(0, i) for i in range(1, leaves + 1)]


def double_star(L, R):
    # vertices: 0 = u_l, 1 = u_r, 2..L+1 left pendants, L+2..L+R+1 right
    e = [(0, 1)]
    e += [(0, 2 + i) for i in range(L)]
    e += [(1, 2 + L + i) for i in range(R)]
    return e


def windmill(P, B):
    # vertex 0 = universal u; blades (1,2),(3,4),...; pendants after blades
    e = []
    for i in range(B):
        a, b = 1 + 2 * i, 2 + 2 * i
        e += [(0, a), (0, b), (a, b)]
    e += [(0, 1 + 2 * B + j) for j in range(P)]
    return e


# --- [BH11] paths and complete graphs -----------------------------------
for n in range(2, 21):
    solv = (n % 2 == 0) or n == 3
    add(f"P_{n}", n, path(n), solvable=solv, freely=(n == 2))
for n in range(2, 11):
    add(f"K_{n}", n, complete(n), solvable=True, freely=True)
# stars: K_{1,m} has n = m+1 vertices; ps = m-1 for m >= 2
for m in range(2, 12):
    add(f"K_1,{m}", m + 1, star(m), ps=(1 if m == 2 else m - 1),
        solvable=(m == 2))

# --- [BH12] double stars -------------------------------------------------
for L in range(0, 7):
    for R in range(0, L + 1):
        n = L + R + 2
        exp = dict(solvable=(L <= R + 1),
                   freely=(L == R and R != 1))
        if L >= R + 3:
            exp["ps"] = L - R
        if L == R + 2:
            exp["ps"] = 2
        add(f"DS({L},{R})", n, double_star(L, R), **exp)

# --- [BH12] windmills ----------------------------------------------------
for B in range(1, 7):
    add(f"W({B})", 1 + 2 * B, windmill(0, B), solvable=True,
        freely=(B != 2))
for B in range(1, 6):
    for P in range(0, 2 * B + 4):
        # NOTE: Thm 2.2(ii) as published claims W(1,1) is freely solvable.
        # It is not (verified by hand 2026-07-02): with the hole on the
        # pendant, both possible first jumps go over the universal vertex,
        # removing it and stranding two nonadjacent pegs. The published
        # sufficiency proof never considers a pendant starting hole. We
        # encode the corrected statement (extra exception at (P,B)=(1,1)).
        exp = dict(solvable=(P <= 2 * B),
                   freely=(P <= 2 * B - 1 and (P, B) not in [(0, 2), (1, 1)]))
        if P > 2 * B + 1:
            exp["ps"] = P - 2 * B + 1
        if P == 2 * B + 1:
            exp["ps"] = 2
        add(f"W({P},{B})", 1 + 2 * B + P, windmill(P, B), **exp)


def main():
    lines = []
    for _, n, edges, _ in CASES:
        flat = " ".join(f"{u} {v}" for u, v in edges)
        lines.append(f"{n} {flat}")
    out = subprocess.run(["./solver"], input="\n".join(lines) + "\n",
                         capture_output=True, text=True, check=True).stdout
    rows = out.strip().split("\n")[1:]
    assert len(rows) == len(CASES), (len(rows), len(CASES))

    failures = 0
    for (label, n, _, expect), row in zip(CASES, rows):
        f = row.split(",")
        got = dict(solvable=f[4] in "SF", freely=f[4] == "F", ps=int(f[5]),
                   fs=int(f[6]))
        for key, want in expect.items():
            if got[key] != want:
                failures += 1
                print(f"FAIL {label}: {key} expected {want}, got {got[key]}"
                      f"  (row: {row})")
    print(f"{len(CASES)} graphs checked against published theorems; "
          f"{failures} failures")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()

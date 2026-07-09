"""Verify solver against published theorems (BH11, BH12).
Usage: python3 analysis/verify_published.py
"""
import subprocess
import sys

CASES = []


def add(label, n, edges, **expect):
    CASES.append((label, n, edges, expect))


def path(n):
    return [(i, i + 1) for i in range(n - 1)]


def complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def star(leaves):
    return [(0, i) for i in range(1, leaves + 1)]


def double_star(L, R):
    e = [(0, 1)]
    e += [(0, 2 + i) for i in range(L)]
    e += [(1, 2 + L + i) for i in range(R)]
    return e


def windmill(P, B):
    e = []
    for i in range(B):
        a, b = 1 + 2 * i, 2 + 2 * i
        e += [(0, a), (0, b), (a, b)]
    e += [(0, 1 + 2 * B + j) for j in range(P)]
    return e


for n in range(2, 21):
    solv = (n % 2 == 0) or n == 3
    add(f"P_{n}", n, path(n), solvable=solv, freely=(n == 2))
for n in range(2, 11):
    add(f"K_{n}", n, complete(n), solvable=True, freely=True)
for m in range(2, 12):
    add(f"K_1,{m}", m + 1, star(m), ps=(1 if m == 2 else m - 1),
        solvable=(m == 2))

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

for B in range(1, 7):
    add(f"W({B})", 1 + 2 * B, windmill(0, B), solvable=True,
        freely=(B != 2))
for B in range(1, 6):
    for P in range(0, 2 * B + 4):
        # W(1,1) correction: published theorem claims freely solvable,
        # but pendant-hole start leaves two stranded pegs.
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
    print(f"{len(CASES)} graphs checked, {failures} failures")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()

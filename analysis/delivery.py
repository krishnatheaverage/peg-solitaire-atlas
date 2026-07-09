"""Delivery numbers of paths: max pegs a fully-pegged path can deliver
to an adjacent target cell. D(m), D_hole(m), D2(m) (two-sided).
Usage: python3 analysis/delivery.py [max_m]
"""
import sys
from functools import lru_cache


def delivery(m, holes=(), two_sided=False):
    n = m + (2 if two_sided else 1)
    targets = {0, m + 1} if two_sided else {0}
    start = 0
    for c in range(n):
        if c in targets:
            continue
        if c not in holes:
            start |= 1 << c
    moves = []
    for c in range(n - 2):
        moves.append((c, c + 1, c + 2))
        moves.append((c + 2, c + 1, c))

    sys.setrecursionlimit(1 << 20)

    @lru_cache(maxsize=None)
    def best(state):
        res = 0
        for t in targets:
            if (state >> t) & 1:
                res = max(res, best(state & ~(1 << t)))
        for u, v, w in moves:
            if (state >> u) & 1 and (state >> v) & 1 and not (state >> w) & 1:
                gain = 1 if w in targets else 0
                res = max(res, gain + best(state ^ (1 << u) ^ (1 << v)
                                           ^ (1 << w)))
        return res

    return best(start)


def main():
    mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    print(f"{'m':>3} {'D(m)':>5} {'D_hole(m)':>9} {'D2(m)':>6}")
    for m in range(1, mmax + 1):
        d = delivery(m)
        dh = max(delivery(m, holes=(h,)) for h in range(1, m + 1))
        d2 = delivery(m, two_sided=True)
        print(f"{m:>3} {d:>5} {dh:>9} {d2:>6}")


if __name__ == "__main__":
    main()

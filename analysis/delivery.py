"""Delivery numbers of paths: the crux quantity for crown necessity.

Model: path cells 1..m (all pegged unless a hole is specified) plus a
target cell 0 adjacent to cell 1. Jumps happen only along the line
(cells 0..m). The target cell is special: whenever it holds a peg, an
external process may remove it at any time (this models x_0's peg
being consumed by pendant events A/B/C/D/E). A DELIVERY is a jump
2 > 1 > 0.

D(m)      = max deliveries, path starts full.
D_hole(m) = max over starting hole positions h in 1..m of max
            deliveries when cell h starts empty.
D2(m)     = two-sided version: targets 0 and m+1 at both ends, path
            full; counts total deliveries into either target.

Exact search over states (peg bitmask on cells 1..m, target assumed
drained immediately - draining immediately is optimal for counting
deliveries only, EXCEPT the target peg can also jump back into the
path (D-type moves). To stay exact we keep the target's peg state in
the search and allow: keep it, drain it (external), or jump it back
0 > 1 > 2. Memoized max-delivery search.
"""
import sys
from functools import lru_cache


def delivery(m, holes=(), two_sided=False):
    # cells: 0 = left target, 1..m path, m+1 = right target (if two_sided)
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
        # external drain of a pegged target
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

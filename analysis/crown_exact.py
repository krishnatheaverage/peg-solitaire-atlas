"""Pendant-symmetric analysis of crowns C(k;p) with refill counting.
Usage: python3 analysis/crown_exact.py <k> <p>
"""
import sys
sys.setrecursionlimit(1 << 22)


def analyze(k, p):
    jumps = []
    for m in range(k):
        a, b = (m - 1) % k, (m + 1) % k
        jumps.append((a, m, b))
        jumps.append((b, m, a))

    memo = {}

    def reach(mask, j):
        key = (mask, j)
        if key in memo:
            return memo[key]
        pegs = bin(mask).count('1') + j
        if pegs == 1:
            memo[key] = (True, 0, 0)
            return memo[key]
        lo, hi, ok = None, None, False
        for u, v, w in jumps:
            if (mask >> u) & 1 and (mask >> v) & 1 and not (mask >> w) & 1:
                s, l, h = reach(mask ^ (1 << u) ^ (1 << v) ^ (1 << w), j)
                if s:
                    r = 1 if w == 0 else 0
                    ok = True
                    lo = l + r if lo is None else min(lo, l + r)
                    hi = h + r if hi is None else max(hi, h + r)
        x0 = (mask >> 0) & 1
        g1, g2 = 1, k - 1
        if x0:
            if j >= 1:
                for g in (g1, g2):
                    if not (mask >> g) & 1:
                        s, l, h = reach((mask & ~1) | (1 << g), j - 1)
                        if s:
                            ok = True
                            lo = l if lo is None else min(lo, l)
                            hi = h if hi is None else max(hi, h)
            if j >= 1 and (p - j) >= 1:
                s, l, h = reach(mask & ~1, j)
                if s:
                    ok = True
                    lo = l if lo is None else min(lo, l)
                    hi = h if hi is None else max(hi, h)
            if (p - j) >= 1:
                for g in (g1, g2):
                    if (mask >> g) & 1:
                        s, l, h = reach((mask & ~1) & ~(1 << g), j + 1)
                        if s:
                            ok = True
                            lo = l if lo is None else min(lo, l)
                            hi = h if hi is None else max(hi, h)
        memo[key] = (ok, lo or 0, hi or 0) if ok else (False, 0, 0)
        return memo[key]

    full = (1 << k) - 1
    out = {}
    for h in range(k):
        out[h] = reach(full ^ (1 << h), p)
    if p >= 1:
        out['q'] = reach(full, p - 1)
    return out


if __name__ == "__main__":
    k, p = int(sys.argv[1]), int(sys.argv[2])
    res = analyze(k, p)
    solv = [h for h, (s, _, _) in res.items() if s]
    if not solv:
        print(f"C({k};{p}): UNSOLVABLE from every hole")
    else:
        stats = {h: (l, hh) for h, (s, l, hh) in res.items() if s}
        rmin = min(l for l, _ in stats.values())
        rmax = max(h for _, h in stats.values())
        print(f"C({k};{p}): solvable holes {solv}; refills over all "
              f"solving plays: min={rmin} max={rmax}")
        for h, (l, hh) in sorted(stats.items(), key=str):
            print(f"   hole {h}: refills [{l},{hh}]")

"""The k -> k+4 play family for DC(k, k/2), hole x_3  (even-side gadget).

Generates the parametrized solving play inferred from the k=16 and
k=20 witnesses and validates it by exact simulation. Phases (d = k/2):

  A: 5>4>3  2>3>4  0>1>2
  B: pairs (2j+7 > 2j+6 > 2j+5), (2j+4 > 2j+5 > 2j+6)
     for j = 0 .. (d-8)/2                      [right arc, grows +1 pair per +4... wait: per +4 in k, d grows +2, so one extra pair]
  C: (k-2 > k-1 > 0), then (m > m+1 > m+2) descending:
     (k-4 > k-3 > k-2), (k-6 > k-5 > k-4), ... down to (d+4 > d+5 > d+6)
  D: q0>0>1   2>1>0   q0>0>(k-1)
  E: (k-1 > k-2 > k-3), (k-3 > k-4 > k-5), ... down to landing at d+5
  F: qd>d>(d-1)  (d+2)>(d+1)>d  qd>d>(d+1)  (d-2)>(d-1)>d
     d>(d+1)>(d+2)  (d+2)>(d+3)>(d+4)  (d+5)>(d+4)>(d+3)

Usage: python3 analysis/dc_family.py <k> [<k> ...]
"""
import sys


def family(k):
    d = k // 2
    mv = [(5, 4, 3), (2, 3, 4), (0, 1, 2)]
    for j in range(0, (d - 6) // 2):
        mv.append((2 * j + 7, 2 * j + 6, 2 * j + 5))
        mv.append((2 * j + 4, 2 * j + 5, 2 * j + 6))
    mv.append((k - 2, k - 1, 0))
    m = k - 4
    while m >= d + 4:
        mv.append((m, m + 1, m + 2))
        m -= 2
    mv += [("q0", 0, 1), (2, 1, 0), ("q0", 0, k - 1)]
    m = k - 1
    while m >= d + 7:
        mv.append((m, m - 1, m - 2))
        m -= 2
    mv += [("qd", d, d - 1), (d + 2, d + 1, d), ("qd", d, d + 1),
           (d - 2, d - 1, d), (d, d + 1, d + 2),
           (d + 2, d + 3, d + 4), (d + 5, d + 4, d + 3)]
    return mv


def simulate(k, moves, hole=3):
    d = k // 2
    pegs = set(range(k)) - {hole}
    q = {0: 2, d: 2}  # pendant counts

    def adj(a, b):
        return (b - a) % k in (1, k - 1)

    for t, (u, v, w) in enumerate(moves):
        if u == "q0" or u == "qd":
            c = 0 if u == "q0" else d
            assert q[c] >= 1 and c in pegs, (t, u, v, w)
            if w == "q0" or w == "qd":
                assert q[c] <= 1, (t,)
            else:
                assert v == c and adj(c, w) and w not in pegs, (t, u, v, w)
                q[c] -= 1
                pegs.discard(c)
                pegs.add(w)
                continue
        assert u in pegs and v in pegs and w not in pegs, (t, u, v, w)
        assert adj(u, v) and adj(v, w) and u != w, (t, u, v, w)
        pegs.discard(u)
        pegs.discard(v)
        pegs.add(w)
    total = len(pegs) + q[0] + q[d]
    return total, sorted(pegs), q


if __name__ == "__main__":
    for k in map(int, sys.argv[1:]):
        mv = family(k)
        try:
            total, pegs, q = simulate(k, mv)
            status = "SOLVED" if total == 1 else f"FAILED ({total} pegs left: {pegs} q={q})"
        except AssertionError as e:
            status = f"ILLEGAL MOVE at {e}"
        print(f"DC({k},{k//2}) hole=x_3, {len(mv)} moves: {status}")

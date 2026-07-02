"""Extract an explicit winning jump sequence for a graph + starting hole.

A jump is (u, v, w): peg at u jumps over v into hole w; u,v lose pegs,
w gains one. Prints the sequence reaching a single peg, or UNSOLVABLE.

Usage:
  python3 analysis/witness.py "<n> <edge list>" <hole>
  python3 analysis/witness.py crown <k> <p> [hole]   # C(k;p) helper
"""
import sys


def parse_graph(spec):
    tok = list(map(int, spec.split()))
    n, flat = tok[0], tok[1:]
    edges = list(zip(flat[::2], flat[1::2]))
    return n, edges


def crown_spec(k, p):
    edges = [(i, (i + 1) % k) for i in range(k)]
    edges += [(0, k + j) for j in range(p)]
    return k + p, edges


def solve(n, edges, hole):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    moves = []
    for mid in range(n):
        for u in adj[mid]:
            for w in adj[mid]:
                if u != w:
                    moves.append((u, mid, w))
    memo = {}

    def dfs(state):
        if state in memo:
            return memo[state]
        if bin(state).count('1') == 1:
            memo[state] = []
            return []
        for u, v, w in moves:
            if (state >> u) & 1 and (state >> v) & 1 and not (state >> w) & 1:
                rest = dfs(state ^ (1 << u) ^ (1 << v) ^ (1 << w))
                if rest is not None:
                    memo[state] = [(u, v, w)] + rest
                    return memo[state]
        memo[state] = None
        return None

    sys.setrecursionlimit(10000)
    full = (1 << n) - 1
    return dfs(full ^ (1 << hole))


def main():
    if sys.argv[1] == "crown":
        k, p = int(sys.argv[2]), int(sys.argv[3])
        n, edges = crown_spec(k, p)
        holes = [int(sys.argv[4])] if len(sys.argv) > 4 else range(n)
        label = f"C({k};{p})"
    else:
        n, edges = parse_graph(sys.argv[1])
        holes = [int(sys.argv[2])] if len(sys.argv) > 2 else range(n)
        label = "graph"
    for h in holes:
        seq = solve(n, edges, h)
        if seq is None:
            print(f"{label} hole={h}: UNSOLVABLE")
        else:
            pretty = "  ".join(f"{u}>{v}>{w}" for u, v, w in seq)
            print(f"{label} hole={h}: {pretty}")
            break
    else:
        return


if __name__ == "__main__":
    main()

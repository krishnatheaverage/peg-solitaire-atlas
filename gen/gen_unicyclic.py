"""Generate all non-isomorphic connected unicyclic graphs on n vertices.

A unicyclic graph is a cycle C_k (3 <= k <= n) with rooted trees hung on
the cycle vertices. Isomorphism classes = necklaces of rooted-tree
canonical codes under the dihedral group of the cycle.

Rooted trees are built recursively in canonical (AHU) form: a tree is the
sorted tuple of its children's codes. Around the cycle we keep a k-tuple
only if it is the lexicographic minimum over all rotations and
reflections.

Expected counts (OEIS A001429, verified against the b-file and an
independent Burnside/cycle-index computation): n=3:1, 4:2, 5:5, 6:13,
7:33, 8:89, 9:240, 10:657, 11:1806, 12:5026, 13:13999, 14:39260,
15:110381, 16:311465.

Output format (same as gen_trees.py): "n u1 v1 u2 v2 ..." per graph.
Cycle vertices come first (0..k-1, edges i-(i+1) and (k-1)-0).

Usage: python3 gen_unicyclic.py <n> [outfile]
"""
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


@lru_cache(maxsize=None)
def rooted_trees(size):
    """All canonical rooted trees on `size` vertices, as nested tuples."""
    if size == 1:
        return ((),)
    result = []

    # choose a non-decreasing sequence of children (by (size, code) order)
    # with sizes summing to size-1
    def extend(remaining, min_key, children):
        if remaining == 0:
            result.append(tuple(children))
            return
        for csize in range(1, remaining + 1):
            for code in rooted_trees(csize):
                key = (csize, code)
                if key < min_key:
                    continue
                children.append(code)
                extend(remaining - csize, key, children)
                children.pop()

    extend(size - 1, (0, ()), [])
    return tuple(result)


def tree_size(code):
    return 1 + sum(tree_size(c) for c in code)


def emit_edges(code, root, next_id, edges):
    """Assign vertex ids to a rooted tree; returns next free id."""
    for child in code:
        cid = next_id
        next_id += 1
        edges.append((root, cid))
        next_id = emit_edges(child, cid, next_id, edges)
    return next_id


def unicyclic(n):
    """Yield edge lists of all unicyclic graphs on n vertices."""
    for k in range(3, n + 1):
        # trees[i] available for each cycle slot, sizes sum to n
        choices = []
        for size in range(1, n - k + 2):
            for code in rooted_trees(size):
                choices.append((size, code))

        def assign(pos, remaining, tup):
            if pos == k:
                if remaining != 0:
                    return
                # canonical under dihedral group
                t = tuple(tup)
                cand = [tuple(t[(i + r) % k] for i in range(k))
                        for r in range(k)]
                rev = t[::-1]
                cand += [tuple(rev[(i + r) % k] for i in range(k))
                         for r in range(k)]
                if t != min(cand):
                    return
                edges = [(i, (i + 1) % k) for i in range(k)]
                nid = k
                for i, code in enumerate(tup):
                    nid = emit_edges(code, i, nid, edges)
                yield edges
                return
            budget = remaining - (k - pos - 1)  # others need >= 1 each
            for size, code in choices:
                if size > budget:
                    break
                # slot 0 must hold a minimal element of the tuple
                if pos > 0 and code < tup[0]:
                    continue
                tup.append(code)
                yield from assign(pos + 1, remaining - size, tup)
                tup.pop()

        # choices sorted by size then code so `break` on size works
        choices.sort()
        yield from assign(0, n, [])


def main():
    n = int(sys.argv[1])
    out = open(sys.argv[2], "w") if len(sys.argv) > 2 else sys.stdout
    count = 0
    for edges in unicyclic(n):
        flat = " ".join(f"{u} {v}" for u, v in edges)
        out.write(f"{n} {flat}\n")
        count += 1
    if out is not sys.stdout:
        out.close()
    print(f"n={n}: {count} unicyclic graphs", file=sys.stderr)


if __name__ == "__main__":
    main()

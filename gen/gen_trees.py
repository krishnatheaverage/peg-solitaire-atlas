"""Generate all non-isomorphic free trees on n vertices.
Usage: python3 gen_trees.py <n> [outfile]
"""
import sys
import networkx as nx


def main():
    n = int(sys.argv[1])
    out = open(sys.argv[2], "w") if len(sys.argv) > 2 else sys.stdout
    count = 0
    for tree in nx.nonisomorphic_trees(n):
        flat = " ".join(f"{u} {v}" for u, v in tree.edges())
        out.write(f"{n} {flat}\n")
        count += 1
    if out is not sys.stdout:
        out.close()
    print(f"n={n}: {count} trees", file=sys.stderr)


if __name__ == "__main__":
    main()

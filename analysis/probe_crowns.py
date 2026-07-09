"""Structured solver probes for the crown family C(k;p) and variants.
Usage: python3 analysis/probe_crowns.py <single|pair|subtree|helper>
"""
import subprocess
import sys

sys.path.insert(0, 'gen')
from gen_unicyclic import rooted_trees, emit_edges  # noqa: E402


def solve_all(lines):
    out = subprocess.run(['./solver'], input="\n".join(lines) + "\n",
                         capture_output=True, text=True, timeout=550).stdout
    return [row.split(",")[4] for row in out.strip().split("\n")[1:]]


def crown(k, loads=None, chains=None, subtrees=None):
    edges = [(i, (i + 1) % k) for i in range(k)]
    nid = k
    for v, c in (loads or {}).items():
        for _ in range(c):
            edges.append((v, nid))
            nid += 1
    for v, ln in (chains or []):
        prev = v
        for _ in range(ln):
            edges.append((prev, nid))
            prev = nid
            nid += 1
    for v, code in (subtrees or []):
        cid = nid
        nid += 1
        edges.append((v, cid))
        nid = emit_edges(code, cid, nid, edges)
    return f"{nid} " + " ".join(f"{u} {v}" for u, v in edges)


def probe_single():
    lines, meta = [], []
    for k in range(3, 28):
        for p in range(0, min(11, 31 - k) + 1):
            lines.append(crown(k, {0: p}))
            meta.append((k, p))
    cls = dict(zip(meta, solve_all(lines)))
    for k in range(3, 28):
        ps = [p for p in range(0, min(11, 31 - k) + 1)]
        s = "".join('S' if cls[(k, p)] != 'U' else 'U' for p in ps)
        pstar = max([p for p in ps if cls[(k, p)] != 'U'], default=-1)
        print(f"k={k:>2}: {s}  p*={pstar}")


def probe_pair():
    lines, meta = [], []
    for k in range(4, 13):
        for d in range(1, k // 2 + 1):
            for p in range(1, 5):
                lines.append(crown(k, {0: p, d: p}))
                meta.append((k, d, p))
    cls = dict(zip(meta, solve_all(lines)))
    for k in range(4, 13):
        row = []
        for d in range(1, k // 2 + 1):
            t = max([p for p in range(1, 5) if cls[(k, d, p)] != 'U'],
                    default=0)
            row.append(str(t))
        print(f"k={k:>2}: max p by d=1..{k//2}: {' '.join(row)}")


def probe_subtree():
    subs = [(s, code) for s in range(1, 5) for code in rooted_trees(s)]
    lines, meta = [], []
    for k in (12, 13):
        for s, code in subs:
            for j in range(0, 7):
                lines.append(crown(k, {0: j}, subtrees=[(0, code)]))
                meta.append((k, s, code, j))
    cls = dict(zip(meta, solve_all(lines)))
    for s, code in subs:
        mj = {k: max([j for j in range(7) if cls[(k, s, code, j)] != 'U'],
                     default=-1) for k in (12, 13)}
        print(f"subtree {code} size={s}: maxj k12={mj[12]} k13={mj[13]}")


def probe_helper():
    lines, meta = [], []
    for k in (12, 13):
        for j in range(0, 13):
            lines.append(crown(k, {0: j}, chains=[(0, 2)]))
            meta.append(('ceil', k, j))
    for d in range(0, 7):
        for j in range(0, 9):
            lines.append(crown(12, {0: j}, chains=[(d, 2)]))
            meta.append(('place', d, j))
    for j in range(0, 13):
        lines.append(crown(12, {0: j}, chains=[(0, 2), (0, 2)]))
        meta.append(('two', 12, j))
    cls = dict(zip(meta, solve_all(lines)))
    for k in (12, 13):
        mj = max([j for j in range(13) if cls[('ceil', k, j)] != 'U'],
                 default=-1)
        print(f"one chain2@v0 k={k}: maxj={mj}")
    mj = max([j for j in range(13) if cls[('two', 12, j)] != 'U'], default=-1)
    print(f"two chain2@v0 k=12: maxj={mj}")
    for d in range(0, 7):
        mj = max([j for j in range(9) if cls[('place', d, j)] != 'U'],
                 default=-1)
        print(f"chain2 at d={d} on C12: maxj={mj}")


if __name__ == "__main__":
    {"single": probe_single, "pair": probe_pair,
     "subtree": probe_subtree, "helper": probe_helper}[sys.argv[1]]()

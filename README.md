# peg-solitaire-atlas

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21285775.svg)](https://doi.org/10.5281/zenodo.21285775)

Exact solvers, graph generators, verification scripts, and exhaustive
solvability atlases for **peg solitaire on graphs** (in the sense of
Beeler and Hoilman), focused on trees and unicyclic graphs.

This is the code and data accompanying the paper *Peg solitaire on
unicyclic graphs: crowns, cycle-critical graphs, and two atlases*
(K. Harish).

## Contents

- `src/solver.cpp` — exact memoized solver; reports per-hole minimum and
  maximum terminal peg counts for each input graph.
- `src/crown_sym.cpp`, `src/dc_sym.cpp` — pendant-symmetric solvers for
  crowns `C(k;p)` and double crowns `DC(k,d)`.
- `gen/gen_trees.py`, `gen/gen_unicyclic.py` — non-isomorphic tree and
  unicyclic-graph generators (counts validated against OEIS A000055 and
  A001429).
- `analysis/` — verification against published theorems
  (`verify_published.py`), crown and double-crown probes, delivery-number
  computations, and an explicit-witness extractor.
- `data/` — the atlases (trees `n <= 18`, unicyclic `n <= 14`) and derived
  datasets, including the cycle-critical census.

## Quickstart

```sh
# build the solver
g++ -O2 -o solver src/solver.cpp

# reproduce the checks against published theorems (should report 0 failures)
python3 analysis/verify_published.py

# generate and solve all unicyclic graphs on 10 vertices
python3 gen/gen_unicyclic.py 10 | ./solver | head
```

The pendant-symmetric solvers build the same way:

```sh
g++ -O2 -o crown_sym src/crown_sym.cpp
g++ -O2 -o dc_sym   src/dc_sym.cpp
```

## Citation

If you use this repository, please cite the accompanying paper and the
archived release: Zenodo DOI
[10.5281/zenodo.21285776](https://doi.org/10.5281/zenodo.21285776)
(v1.0.0). See `CITATION.cff` for full metadata.

## License

Released under the MIT License (see `LICENSE`).

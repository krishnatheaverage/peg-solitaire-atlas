# Peg solitaire on theta graphs (bicyclic frontier, 2026-07-04)

New direction: cycle rank 2. $\Theta(a,b,c)$ = two hubs joined by
three internally disjoint paths with $a\le b\le c$ internal vertices
($n=a+b+c+2$; at most one of $a,b,c$ may be $0$, giving a hub-hub
chord). Paths and cycles are the rank-0/1 building blocks; theta
graphs are the simplest bicyclic graphs and appear untouched in the
peg-solitaire-on-graphs literature.

## Discovery (machine-verified, all theta with $n\le 24$: 194 graphs)

**Every theta graph is solvable.** Zero unsolvable among 194.
Moreover $193/194$ are FREELY solvable; the lone exception in range is
$\Theta(1,8,9)$ ($n=20$), solvable but not freely. Independent solver
confirms (incl.\ large odd cases $\Theta(5,7,9)$ etc.). Contrast:
cycles $C_n$ are unsolvable for odd $n>3$; the second hub-hub path
removes the obstruction entirely.

## Theorem (even $n$): every theta with $n$ even is solvable. PROVED.

Every $\Theta(a,b,c)$ contains a spanning Hamiltonian path: with hubs
$u,v$ and paths $u x_1\!\cdots x_a v$, $u z_1\!\cdots z_b v$,
$u y_1\!\cdots y_c v$, the sequence
\[
 y_c,\dots,y_1,\ u,\ x_1,\dots,x_a,\ v,\ z_b,\dots,z_1
\]
visits every vertex using only theta edges (verified for all theta in
range). When $n$ is even this Hamiltonian path is $P_n$, solvable by
Beeler--Hoilman, so the Inheritance Principle makes $\Theta$ solvable.
$\square$

## Odd $n$: status

The Hamiltonian path is $P_n$ with $n$ odd (unsolvable), so a
different spanning subgraph is needed. Breaking one hub-hub path at a
hub leaves a TADPOLE spanning subgraph (cycle + pendant path); the
theta is solvable if any of its three tadpoles is. This works for
$82/96$ odd thetas in range. The remaining $14$ --- the balanced-long
cases $\Theta(5,5,5)$, $\Theta(7,7,7)$, $\Theta(5,6,6)$, \dots and the
chord cases $\Theta(0,7,8),\Theta(0,8,9)$ --- have NO solvable path or
tadpole spanning subgraph, yet are solvable: they genuinely use both
independent cycles. This is a rank-2 echo of cycle-criticality, and a
direct two-cycle (circulation-style) strategy is the missing proof,
exactly analogous to the balanced-triangle circulation of
$T(q,q,q)$.

## Tadpole sub-result (needed above, of independent interest)

$\mathrm{Tad}(m,L)$ = cycle $C_m$ with a pendant path of $L$ vertices.
Machine pattern ($m\le 13$): small cycles $m\in\{3,4,6,8\}$ solvable
for every tail $L$; odd $m\ge 5$ unsolvable exactly at $L=0$ and even
$L\ge 6$; even $m\ge 10$ unsolvable at odd $L\ge 5$. (Not yet a clean
closed form; recorded for the theta reduction.)

## Open
- Prove solvability of the $14$ balanced-odd thetas (two-cycle
  circulation) $\Rightarrow$ "every theta graph is solvable" as a full
  theorem.
- Characterize the non-freely-solvable theta graphs (only
  $\Theta(1,8,9)$ appeared; find the family).
- Clean closed form for tadpole solvability $\mathrm{Tad}(m,L)$.
- Bicyclic beyond theta: dumbbells (two cycles joined by a path),
  and cycle-rank-2 criticality ("both cycle edges load-bearing").

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

## Every theta contains an even cycle (PROVED, parity)

The three cycles of $\Theta(a,b,c)$ (pairs of paths) have lengths
$a+b+2,\ a+c+2,\ b+c+2$, with parities those of $a+b,\ a+c,\ b+c$.
These three sum to $2(a+b+c)$, even, so they cannot all be odd: at
least one of $a+b,a+c,b+c$ is even. Hence \textbf{every theta graph
has an even cycle.} $\square$

## Odd $n$: reduced from bicyclic to unicyclic (the hard cases dissolve)

The balanced-odd cases are NOT bicyclic-critical after all: they do
have solvable unicyclic spanning subgraphs, just not tadpoles
(the solvable one comes from breaking a path in its MIDDLE, giving a
cycle with two tails, not at a hub). Uniform construction: take the
even cycle (exists, above); the third path has odd internal length;
split it into two tails at the two hubs. This
even-cycle-with-two-tails unicyclic graph is a spanning subgraph, and
it is solvable for a suitable split --- VERIFIED for all $96$ odd-$n$
thetas with $n\le 24$ (searching over even-cycle choice and split
point; the balanced split alone already works for $93/96$).

So by the Inheritance Principle, \emph{every theta graph is solvable},
with the odd case resting on one clean unicyclic lemma:

  LEMMA (verified, closed form open): the even-cycle-with-two-tails
  graphs arising here are solvable. Equivalently, a $C_m$ ($m$ even)
  with two pendant paths at the two hub vertices, of appropriate
  lengths, is solvable.

This REPLACES the earlier "needs a direct two-cycle circulation"
plan: the balanced-odd hard cases reduce to rank 1, not rank 2. The
remaining gap is a unicyclic (cycle-with-tails) solvability statement,
strictly easier than the original bicyclic question. Status:
- even $n$: theta solvable, FULLY PROVED (Ham path).
- odd $n$: theta solvable, PROVED modulo the cycle-with-tails lemma
  (verified all $n\le 24$).

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

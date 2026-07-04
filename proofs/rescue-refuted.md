# The Rescue Bound is FALSE: rescue is unbounded (2026-07-04)

We conjectured $R(G)=\min_T\ps(T)-\ps(G)\le 2$ ("one edge rescues at
most two pegs"), verified tight on all unicyclic $n\le 12$. That
verification range was too small. Pushing further refutes it.

## The counterexample family

$T(q)=T(q,q,q)$: a triangle $\{a,b,c\}$ with $q$ pendants at each
vertex ($n=3q+3$). Smallest explicit counterexample: $T(5)$, $n=18$,
$\ps=1$, every spanning tree $\ps=4$, so $R=3$. Verified by two
independent solvers (C++ memoized + Python memoized). $T(6)$ gives
$R=4$. In general $R(T(q))=q-2$ (computed $q\le 6$; proved $\ge q-4$).

## Theorem A: $\ps(T(q))=1$ (solvable), all $q$

*Proof (circulation induction).* Hole at $a$. The three jumps
$b_q\!>\!b\!>\!a$, $c_q\!>\!c\!>\!b$, $a_q\!>\!a\!>\!c$ are legal in
turn and return the triangle to (hole $a$, $b,c$ pegged) while
deleting one pendant from each vertex --- i.e.\ reduce $T(q)$ to
$T(q-1)$ with the hole again at $a$. Induct to $T(0)=K_3$, solved by
$b\!>\!c\!>\!a$. Verified by explicit simulation for $q\le 8$.
$\square$

## Theorem B: every spanning tree of $T(q)$ has $\ps\ge q-3$

*Proof (bipartite 2-colouring ledger).* A spanning tree deletes a
triangle edge, say $ab$, leaving spine $a\!-\!c\!-\!b$ with $q$
pendants at each. This tree is BIPARTITE; colour by distance parity
from $c$:
  EVEN $=\{c\}\cup\{a\text{-pendants}\}\cup\{b\text{-pendants}\}$,
       size $1+2q$;
  ODD  $=\{a,b\}\cup\{c\text{-pendants}\}$, size $2+q$.
Every jump $u\,v\,w$ has $u,w$ one colour and the middle $v$ the
other; it decrements the peg-count of $v$'s colour by exactly one and
leaves the other unchanged. The only non-leaf vertices (possible
middles) are $a,b,c$: $c$ is EVEN, $a,b$ are ODD. Hence:
- EVEN-class pegs are removed ONLY by $c$-middle jumps;
- a $c$-middle jump empties $c$, so between two of them $c$ must be
  refilled, and a peg lands on $c$ only via an $a$- or $b$-middle jump
  (its neighbours $a,b$ are the sole non-leaf neighbours of $c$).
So $\#\{c\text{-middle}\}\le 1+\#\{c\text{-refills}\}\le
1+\#\{a,b\text{-middle}\}$. Writing $P_e,P_o$ for the terminal peg
counts by colour and using
$\#\{c\text{-middle}\}=\text{init}_e-P_e$,
$\#\{a,b\text{-middle}\}=\text{init}_o-P_o$:
\[
\text{init}_e-P_e\ \le\ 1+(\text{init}_o-P_o).
\]
With the hole in either class, $\text{init}_e\ge 2q$ and
$\text{init}_o\le 2+q$, giving $P_e-P_o\ge q-3$, hence total terminal
pegs $P=P_e+P_o\ge q-3$. So $\ps(T(q)-e)\ge q-3$. (Machine value: exactly
$q-1$; the ledger is loose by $2$ because not every $a,b$-middle jump
lands on $c$.) $\square$

## Corollary: rescue is unbounded

$R(T(q)) = \ps(\text{tree})-\ps(T(q)) \ge (q-3)-1 = q-4 \to \infty$.
So no absolute bound $R\le B$ holds. The Rescue Bound conjecture is
false.

## Why the mechanism is clean

The obstruction in Theorem B is exactly non-bipartiteness. The
spanning tree is bipartite, so the colour ledger applies and strands
$\Theta(q)$ pegs. The triangle is an ODD cycle, NOT bipartite, so no
such ledger exists and the circulation of Theorem A wins. The cycle
edge is worth $\Theta(q)$ pegs, not a constant.

## Consequences for the paper (corrections)

1. Conjecture (Rescue bound) $R\le 2$: RETRACTED, replaced by
   "rescue is unbounded" (Theorems A,B).
2. The "two tiers" observation (all critical graphs on $n\le 14$
   strand 2 or 3 pegs) was also an $n\le 14$ artifact: $T(5)$ ($n=18$)
   strands 4, and $T(q)$ strands $q-1$, so the number of tiers is
   unbounded. Keep the $n\le 14$ census as a finite fact; drop the
   "exactly two tiers" framing.
3. $T(q)$, $q\ge 3$, is also a new infinite family of cycle-critical
   graphs (triangle-based), complementing the double crowns.
4. The Skip Identity lemma is unaffected (still true and useful).

Lesson (again): verify conjectures well past the range that first
suggested them.

## Follow-up (2026-07-04): what controls the rescue

**Non-uniform triangles T(a,b,c)** (a>=b>=c pendants). The rescue is
governed by cluster BALANCE, not size. The minimum spanning tree is
obtained by making the LARGEST cluster the spine middle (delete the
opposite edge); the bipartite ledger then strands ~ (b+c) - a - const
pegs. So:
  - balanced clusters (a~b~c=q): min tree ps ~ q, R ~ q  -> unbounded;
  - one dominant cluster (a >> b,c): b+c-a small/negative, R bounded
    (e.g. T(a,1,1) has R = min(a-2, 2), capped at 2).
The maximally balanced T(q,q,q) is the extremal case. Verified over
all a>=b>=c with 3+a+b+c<=22. This answers the "what parameter
controls R" question: the excess (b+c-a) of the two smaller clusters
over the largest.

**Uniform cycles C_k(q)** (q pendants at every vertex of C_k). Only
the TRIANGLE rescues: R(C_3(q)) = q-2 (unbounded), but R(C_k(q)) = 0
for k = 4,5,6,7 (all tested q). Reason: deleting a triangle edge
leaves the length-3 caterpillar P_3(q,q,q) where the single even-class
non-leaf (the middle) is a bottleneck; for k>=4 the spanning
caterpillar P_k(q,...,q) has >=2 even non-leaves, no bottleneck, and
is solvable, so R=0. (Being an odd cycle is NOT sufficient: C_5, C_7
are odd yet rescue 0. The triangle is special as the shortest cycle /
K_3, not merely as an odd cycle.)

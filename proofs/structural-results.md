# Structural results toward the two necessity conjectures (2026-07-03)

Genuine-proof attempts on (1) caterpillar even-separation necessity
and (2) the Rescue Bound. Clean lemmas proved; gaps stated honestly.

## 1. Refill Necessity Lemma (PROVED, pure logic)

**Lemma.** Let $v$ have exactly two pendant (leaf) neighbours
$p_1,p_2$. Any play that removes the pegs on both $p_1$ and $p_2$
contains a jump landing on $v$ (a "refill") that occurs after a
moment when $v$ is empty.

*Proof.* A leaf $p$ can be removed only as the JUMPER of a jump over
its unique neighbour $v$ into a hole: it cannot be a middle (degree
1), and it starts pegged so it is not created. Such a jump needs $v$
pegged just before and empties $v$ just after. Let $J_1$ (before
$J_2$) be the jumps removing $p_1,p_2$. After $J_1$, $v$ is empty;
just before $J_2$, $v$ is pegged. So between them a jump places a peg
on $v$; its middle is a non-leaf (hence spine) neighbour of $v$. This
is the refill. $\square$

**Consequence / where it stalls.** In the double-cluster caterpillar,
both $x_i$ and $x_j$ must be refilled from the spine (a jump
$x_{i\pm2}\,x_{i\pm1}\,x_i$). The inter-cluster segment
$x_{i+1},\dots,x_{j-1}$ has $j-i-1$ vertices, which is ODD when the
separation $j-i$ is even. The unproved step: two refills drawing on
an odd interior segment plus the outer segments cannot all be
financed while also clearing the spine to one peg. This is the exact
analogue of the crown refill ledger, and, like it, resists closure.

## 2. Directional golden pagodas for caterpillars (PROVED valid)

Assign coordinate $c(x_t)=t$ and $c(p)=i$ for a pendant $p$ at $x_i$.
With $s=1/\varphi$ ($s^2+s=1$), the resource $R=\sum_{\rm peg}s^{c(v)}$
is a valid pagoda (non-increasing): spine-left jumps conserve it,
everything else strictly decreases it. Check at a pendant vertex: all
cherries $p x_i x_{i\pm1}$, $p x_i p'$, $x_{i-1}x_i x_{i+1}$ satisfy
$s^{c(w)}\le s^{c(u)}+s^{c(v)}$ because $s^{i-1}\le 2s^i$ and
$s^i\le s^{i+1}+s^i$. The mirror resource $R'$ (coordinate
$m-1-c$) is non-increasing too. For a single final peg at $z$,
$R_{\rm end}R'_{\rm end}=s^{\,m-1}$, independent of $z$.

**Why it is not enough.** These give only inequalities
$R_{\rm end}\le R_{\rm start}$, easily satisfied; as for the bare odd
path $P_5$, real-valued directional pagodas bound but do not by
themselves forbid a single peg. A finer (non-real, or exact) invariant
is needed, and Section (periodicity) shows none of the standard ones
exist. Recorded as an honest dead-end-with-content.

## 3. Rescue Bound: universal verification + extremal structure

**Verified (machine).** $R(G)=\min_T\ps(T)-\ps(G)\in\{0,1,2\}$ for
ALL unicyclic $G$ on $n\le 12$ (solvable and unsolvable): $7437$ with
$R=0$, $421$ with $R=1$, exactly $13$ with $R=2$. So the bound
$R\le 2$ is not only true but TIGHT, and the tight cases are rare.

**Reduction (proved).** If $G$ is solvable and NOT cycle-critical it
has a solvable spanning tree, so $R=0$. Hence $R>0$ forces $G$ either
cycle-critical or unsolvable. The bound is interesting only there.

**Extremal family (identified).** All $13$ graphs with $R=2$ except
one are TRIANGLES carrying a heavy pendant cluster at a single vertex
(e.g.\ $C_3$ with a $k$-pendant star at one corner and a short tail);
the lone exception is a $C_8$ with two pendant pairs. Mechanism: a
triangle is $K_3$, and its third edge is worth exactly a two-peg
boost for clearing a large cluster (the corner can be refilled
"for free" across the clique), which a spanning path cannot match.
Longer cycles give a smaller boost, so $2$ is the maximum.

**Skip-surgery (framework + gap).** Given a solving play of a
critical $G$ (which uses every cycle edge), delete a cycle edge and
replay, skipping now-illegal jumps. Machine test: the result strands
$\le 3$ pegs on every critical graph $n\le 9$ (damage $\le 2$). A
proof needs to bound the skip cascade; the extremal analysis says the
worst case is exactly the triangle-plus-cluster, where the boost is
provably $2$. Closing the cascade bound in general is open.

## Status
- Refill Lemma: proved, in the paper.
- Rescue Bound: proved for non-critical solvable $G$; verified $R\le2$
  (tight) for all unicyclic $n\le12$; extremal family = triangle +
  heavy cluster. General proof open (skip-surgery cascade bound).
- Caterpillar necessity: refill engine + pagoda tool in hand, but the
  parity closure is the crown strip's twin and stays open.

## Skip-surgery: CLOSED as insufficient (2026-07-03, honest correction)

Tested the greedy skip-replay of a FIXED optimal play across 88
unicyclic graphs. Findings:
- Skip identity CONFIRMED: final pegs = r + (skips), exactly. Clean
  lemma (now Lemma "Skip identity" in the paper). Gives R<=0 when an
  optimal play omits a cycle edge (=> positive rescue forces every
  optimal play to use every cycle edge; for solvable G, criticality).
- BUT min_e (skips) over a single optimal play reaches 6, while true
  R stays <=2. So naive skip-surgery does NOT prove R<=2 -- the
  inherited play is too lossy; the tree needs its OWN optimal play.
- This RETRACTS the earlier optimism ("skeleton is there, damage <=2").
  The <=2 seen before came from searching over MANY plays, not a fixed
  one. The cascade is real.
CONCLUSION: Rescue Bound remains a conjecture (verified+tight n<=12).
The skip identity is the salvageable real result. Closing R<=2 needs
control of the tree's native optima, not play inheritance -- harder
than the "tractable skeleton" suggested. Recorded honestly.

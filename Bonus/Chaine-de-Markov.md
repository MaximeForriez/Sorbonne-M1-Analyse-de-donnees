# Chaînes de Markov

Le processus de J. Bernoulli est une chaîne de A. A. Markov[^1] particulière.

## Vecteurs de probabilité

On dit qu'un vecteur $u = \left( \begin{array}{c} u_1\\ u_2\\ \ldots{} \\ u_n \end{array} \right)$ est un **vecteur de probabilité** si :

1. ses composantes sont **positives ou nulles** ;

2. la somme de ces composantes est **égale à 1**.

Quelques exemples pour comprendre :

1. $u = \left( \begin{array}{cccc} \frac{3}{4} & 0 & -\frac{1}{4} & \frac{1}{2} \end{array} \right)$ n'est pas un vecteur de probabilité puisque sa troisième composante est négative, même si : $\frac{3}{4} + 0 - \frac{1}{4} + \frac{1}{2} = 1$.

2. $v = \left( \begin{array}{cccc} \frac{3}{4} & \frac{1}{2} & 0 & \frac{1}{4} \end{array} \right)$ n'est pas un vecteur de probabilité puisque $\frac{3}{4} + \frac{1}{2} + 0 + \frac{1}{4} = \frac{3}{2} \neq 1$.

3. $w = \left( \begin{array}{cccc} \frac{1}{4} & \frac{1}{4} & 0 & \frac{1}{2} \end{array} \right)$ est un vecteur de probabilité puisque $\frac{1}{4} + \frac{1}{4} + 0 + \frac{1}{2} = 1$ et toutes ses composantes sont positives.

4. $y = \left( \begin{array}{ccccc} 2 & 3 & 5 & 0 & 1 \end{array} \right)$ n'est pas un vecteur de probabilité puisque $2 + 3 + 5 + 0 + 1 = 11 \neq 1$, mais, comme ses composantes sont positives, il existe un unique réel $k$ tel que $ky$ est un vecteur dont la somme des composantes vaut 1.

$k \left( \begin{array}{ccccc} y_1 & y_2 & y_3 & y_4 & y_5 \end{array} \right) = 1 \Leftrightarrow k = \frac{1}{11}$

Le vecteur $ky$ est un vecteur de probabilité.

## Matrices stochastiques

On dit qu'un matrice carrée $P = \left( p_{ij} \right)$ est une **matrice stochastique** si chacune de ses **lignes** est un vecteur de probabilité.

**Théorème.** Si $A$ et $B$ sont des matrices stochastiques, alors le produit $A.B$ est une matrice stochastique. En particulier, toutes les puissances $A^n$ sont des matrices stochastiques.

## Matrices stochastiques régulières

On dit qu'une matrice stochastique $P$ est régulière si tous les éléments d'une puissance quelconque $p^m$ sont positifs.

Exemple. $A = \left( \begin{array}{cc} 0 & 1\\ \frac{1}{2} & \frac{1}{2} \end{array} \right)$

$A^2 = \left( \begin{array}{cc} 0 & 1\\ \frac{1}{2} & \frac{1}{2} \end{array} \right).\left( \begin{array}{cc} 0 & 1\\ \frac{1}{2} & \frac{1}{2} \end{array} \right)$

$\Leftrightarrow A^2 = \left[ \begin{array}{cc} \left( \begin{array}{cc} 0 & 1 \end{array} \right).\left( \begin{array}{c} 0\\ \frac{1}{2} \end{array} \right) & \left( \begin{array}{cc} 0 & 1 \end{array} \right).\left( \begin{array}{c} 1\\ \frac{1}{2} \end{array} \right)\\ \left( \begin{array}{cc} \frac{1}{2} & \frac{1}{2} \end{array} \right).\left( \begin{array}{c} 0\\ \frac{1}{2} \end{array} \right) & \left( \begin{array}{cc} \frac{1}{2} & \frac{1}{2} \end{array} \right).\left( \begin{array}{c} 1\\ \frac{1}{2} \end{array} \right) \end{array} \right]$

$\Leftrightarrow A^2 = \left[ \begin{array}{cc} 0 \times 0 + \frac{1}{2} & 0 \times 1 + 1 \times \frac{1}{2}\\ \frac{1}{2} \times 0 + \frac{1}{2} \times \frac{1}{2} & \frac{1}{2} \times 1 + \frac{1}{2} \times \frac{1}{2} \end{array} \right]$

$\Leftrightarrow A^2 = \left( \begin{array}{cc} \frac{1}{2} & \frac{1}{2}\\ \frac{1}{4} & \frac{3}{4} \end{array} \right)$

$\Leftrightarrow A^3 = \left( \begin{array}{cc} \frac{1}{4} & \frac{3}{4}\\ \frac{3}{8} & \frac{5}{8} \end{array} \right)$

$\Leftrightarrow A^4 = \left( \begin{array}{cc} \frac{3}{8} & \frac{5}{8}\\ \frac{5}{16} & \frac{11}{16} \end{array} \right)$

La matrice est régulière, puisqu'elle a tous ses éléments positifs.

$\Leftrightarrow B = \left( \begin{array}{cc} 1 & 0\\ \frac{1}{2} & \frac{1}{2} \end{array} \right)$

$\Leftrightarrow B^2 = \left( \begin{array}{cc} 1 & 0\\ \frac{3}{4} & \frac{1}{4} \end{array} \right)$

$\Leftrightarrow B^3 = \left( \begin{array}{cc} 1 & 0\\ \frac{7}{8} & \frac{1}{8} \end{array} \right)$

$\Leftrightarrow B^4 = \left( \begin{array}{cc} 1 & 0\\ \frac{15}{16} & \frac{1}{16} \end{array} \right)$
	
...
	
$\left( \begin{array}{cc} 1 & 0 \end{array} \right)$ est conservé pour toute puissance $m$ de $B.B$ n'est pas une matrice stochastique régulière.

## Points fixes et matrices stochastiques régulières

**Théorème.** Soit $P$ une matrice stochastique régulière $P$ a alors les propriétés suivantes.

1. $P$ contient un vecteur de probabilité $t$ constant et un seul, dont les composantes sont toutes positives.

2. La suite $P^1, P^2, P^2, \ldots{}$ des puissances de $P$ converge vers la matrice $T$ dont les lignes sont toutes le **point fixe** $t$.

3. Si $p$ est un vecteur de probabilité quelconque, la suite des vecteurs $pP, pP^2, pP^3, \ldots{}$ converge vers le point fixe $t$.

**N.B.** Lorsque l'on dit que $P^n$ converge vers $T$, cela signifie que chaque élément de $P^n$ converge vers la composante correspondante $t$.

## Chaînes de Markov

Soit une suite d'**épreuves** dont les résultats $X_1, X_2, \ldots{}$ satisfont les deux propriétés suivantes.

1. Chaque résultat appartient à un ensemble fini de résultats $\left\lbrace a_1, a_2, \ldots{}, a_n \right\rbrace$ que l'on appelle l'**espace des états** du système. Si le résultat de la $n$-ième épreuve est $a_i$, on dit que le système est dans l'état $a_i$ au temps $n$ ou à la $n$-ième transition.

2. Le résultat d'une épreuve dépend **au plus** du résultat de l'épreuve qui a immédiatement précédé, et d'**aucun autre résultat antérieur**. Pour chaque couple d'état $\left( a_i, a_j \right)$, on donne la probabilité $p_{ij}$ pour que $a_j$ se produise immédiatement après l'état $a_i$.

On dit qu'un tel processus stochastique est une **chaîne de Markov** (finie). Les nombres $p_{ij}$ sont les probabilités de transition et peuvent être rangés sous la forme d'une matrice $P$.

$P = \left(  \begin{array}{ccc} p_{11} & \ldots{} & p_{1m}\\ p_{21} & \ldots{} & p_{2m}\\ \ldots{} & \ldots{} & \ldots{}\\ p_{m1} & \ldots{} & p_{mm} \end{array} \right)$

qu'on appelle la **matrice de transition**.

À chaque état $A_i$ correspond la $i$-ième ligne $\left( \begin{array}{cccc} p_{i1} & p_{i2} & \ldots{} & p_{im} \end{array} \right)$ de la matrice de transition $P$. Si le système est dans l'état $a_i$, ce vecteur ligne est un vecteur de probabilité représentant tous les états possibles de l'**épreuve suivante**.

**Théorème.** La matrice $P$ d'une chaîne de Markov est une matrice stochastique.

## Probabilité de transition d'ordre supérieur

L'élément $p_{ij}$ de la matrice de transition $P$ d'une chaîne de Markov est la probabilité pour que le système passe de l'état $a_i$ à l'état $a_j$ en transition : $a_i \rightarrow a_j$.

Quelle est la probabilité ${p_{ij}}^{\left( n \right)}$ pour que le système évolue de l'état $a_i$ à l'état $a_j$ **en exactement** $n$ **transitions** ?

$a_i \rightarrow a_{k_1} \rightarrow \underbrace{a_{k_2} \rightarrow \ldots{} \rightarrow a_{k_{n - 1}} \rightarrow a_{j}}_{n \textrm{ transitions}}$

Les $p_{ij}^{\left( n \right)}$ sont rangés sous la forme d'une matrice de transition $P^{\left( n \right)}$ que l'on appelle la **matrice de transition d'ordre** $n$.

**Théorème.** Soit $P$ la matrice de transition d'un processus de Markov. La matrice de transition d'ordre $n$ est alors égale à la $n$-ième puissance $P$,  et l'on a $P^{\left( n \right)} = P^n$.

Si, à un instant arbitraire, la probabilité pour que le système soit dans l'état $a_i$ est $p_i$. Soit $p = \left( p_1, p_2, \ldots{}, p_m \right)$ le vecteur de probabilité qu'on appelle **distribution de probabilité** du système à cet instant. En particulier,

$p^{\left( 0 \right)} = \left( p_1^{\left( 0 \right)}, p_2^{\left( 0 \right)}, \ldots{}, p_m^{\left( 0 \right)} \right)$

est la **distribution de probabilité initiale**, c'est-à-dire celle à l'origine du processus. On écrira sous la forme :
	$p^{\left( n \right)} = \left( \begin{array}{cccc} p_1^{\left( n \right)}, p_2^{\left( n \right)}, \ldots{}, p_n^{\left( n \right)} \end{array} \right)$

la **distribution de probabilité à la** $n$**-ième transition**.

**Théorème.** Soit $P$ la matrice de transition d'un processus de Markov. Si $p = \left( p_i \right)$ est la distribution de probabilité du système une transition après et $pP^m$ est la distribution de probabilité $n$ transitions plus loin. En particulier :
	$p^{\left( 1 \right)} = p^{\left( 0 \right)} P$
	$p^{\left( 2 \right)} = p^{\left( 1 \right)} P$
	$p^{\left( 3 \right)} = p^{\left( 2 \right)} P$
	$\ldots{}$
	$p^{\left( n \right)} = p^{\left( 0 \right)} P^n$

## Distribution stationnaire des chaînes de Markov régulière

Soit une chaîne de Markov **régulière**, dont la matrice de transition $P$ est régulière. La suite $P^n$ des matrices de transition d'ordre $n$ converge vers la matrice $T$ dont les lignes sont toutes égales à l'unique vecteur de probabilité constant $t$ de $P$. Par conséquent, la probabilité $P_{ij}^{\left( n \right)}$ pour que $a_j$ se réalise pour des valeurs suffisamment grandes de $n$ est indépendante de l'état initial $a_i$ et converge vers le composant $t_j$ de $t$.

**Théorème.** Soit $P$ la matrice de transition d'une chaîne de Markov régulière. La probabilité pour qu'un état $a_i$ finisse par être réalisé est **approximativement égale** à la composante $t_j$ de l'unique vecteur de probabilité constant $t$ de $P$.

Dit autrement, l'effet de l'état initial ou la distribution de probabilité initiale du processus s'atténue lorsque le nombre de transitions du processus croît.

Toute suite de distributions de probabilité converge vers le vecteur de probabilité constant $t$ de $P$, qu'on appelle **distribution stationnaire** de la chaîne de Markov.

## États absorbants

On dit qu'un état $a_i$ d'une chaîne de Markov est un **état absorbant** si le système reste dans l'état $a_i$ une fois qu'il y est entré. Un état $a_i$ est absorbant si et seulement si la $i$-ième ligne de la matrice de transition $P$ a un $1$ sur la diagonale principale et zéros ailleurs.

La diagonale principale d'une matrice carrée $A = \left( a_{ij} \right)$ d'ordre $n$ est formée des éléments $a_{11}, a_{22}, \ldots{}, a_{nn}$.

Soit $a_i$ un état absorbant d'une chaîne de Markov ayant la matrice de transition $P$, alors, pour $j \neq i$, la probabilité de transition d'ordre $n$, $p_{ij}^{\left( n \right)} = 0$ pour tout $n$. Il en résulte que toute puissance de $P$ a un élément nul et que par conséquent $P$ n'est pas régulière.

**Théorème.** Si l'un des éléments de la diagonale principale d'une matrice stochastique $P$ est égal à $1$, $P$ n'est pas régulière, sauf si $P$ est une matrice $1 \times 1$.

## Notes de bas de page

[^1]: Andreï Andraïevitch Markov (1856-1922)

Adrien-Marie Legendre (1752-1833)

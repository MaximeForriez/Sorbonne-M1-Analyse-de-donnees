# Valeurs et vecteurs propres dans $\mathbb{R}^n$

## Pré-requis

Le déterminant d'ordre $n$ d'une matrice carrée vaut :

$\det \left( A \right) = \sum_{i = 1}^{n} \left( -1 \right)^{i + 1} a_{1i} D_{i1}$

avec $D_{i1}$ l'un des déterminants d'ordre $n - 1$.

La matrice identité $I_n$ d'ordre $n$ est une matrice carrée $n \times n$ telle que :

$I_n = \left[ \begin{array}{cccc} 1 $0$ \ldots{} & 0 \\ 0 $1$ \ldots{} & 0 \\ \ldots{} $\ldots{}$ \ldots{} & \ldots{} \\ 0 $0$ \ldots{} & 1 \\ \end{array} \right]$

Valeurs propres et vecteurs propres ne peuvent se calculer qu'\'{a} partir d'une matrice carrée.

## Valeurs propres

Les valeurs propres ${\lambda}_n$ de la matrice $A$ sont déterminées par la relation de colinéarité suivante :

$\det \left( A - {\lambda}_n I_n \right) = 0$

avec $I_n$ la matrice identité d'ordre $n$ et $\det$ le déterminant :

$\det \left( A - {\lambda}_n I_n \right) = \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right] = ad - bc$

**Exemple.** Calculer les vecteurs propres de $A = \left[ \begin{array}{cc} 5 & -3 \\ 6 & -4 \end{array} \right]$

1. Calculer $A - {\lambda}_n I_n$

$A - {\lambda}_n I_n = \left[ \begin{array}{cc} 5 & -3 \\ 6 & -4 \end{array} \right] - \left[ \begin{array}{cc} {\lambda}_n & 0 \\ 0 & {\lambda}_n \end{array} \right] = \left[ \begin{array}{cc} 5 - {\lambda}_n & -3 \\ 6 & - 4 {\lambda}_n \end{array} \right]$

2. Calculer $\det \left( A - {\lambda}_n I_n \right)$

$\det \left( A - {\lambda}_n I_n \right) = \left( 5 - {\lambda}_n \right) \left( -4 - {\lambda}_n \right) + 18 = {{\lambda}_n}^2 - {\lambda}_n - 2$

3. Résoudre $\det \left( A - {\lambda}_n I_n \right) = 0$

${{\lambda}_n}^2 - {\lambda}_n - 2 = 0 \Leftrightarrow \left\lbrace \begin{array}{c} {\lambda}_1 = \frac{1 + \sqrt{9}}{2} = 2 \\ {\lambda}_2 = \frac{1 - \sqrt{9}}{2} = -1 \end{array} \right.$

## Vecteurs propres

À chaque valeur propre, on associe un vecteur $x_n$ tel que $A.X = {{\lambda}_n}.X$

$A.X = {{\lambda}_n}.X \Leftrightarrow \left[ \begin{array}{c} 0 \\ 0 \\ \ldots{} \\ 0 \end{array} \right]$

Si l'on reprendre l'exemple précédent, il existe deux cas possibles.

- **Cas n°1. ${\lambda}_1 = 2$** 

$\begin{array}{l} \left( A - {\lambda}_1 I_2 \right) X_1 = 0 \\ \Leftrightarrow \left( A - 2 I_2 \right) X_1 = 0 \\ \Leftrightarrow \left( \left[ \begin{array}{cc} 5 & -3 \\ 6 & -4 \end{array} \right] - \left[ \begin{array}{cc} 2 & 0 \\ 0 & 2 \end{array} \right] \right).X_1 = 0 \\ \Leftrightarrow \left( \left[ \begin{array}{cc} 3 & -3 \\ 6 & -6 \end{array} \right] . \left[ \begin{array}{c} x_{11} \\ x_{12} \end{array} \right] \right) = 0 \\ \Leftrightarrow x_{11} = x_{12} \\ X_1 = \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] \end{array}$

- **Cas n°2. ${\lambda}_2 = -1$**

$\begin{array}{l} \left( A - {\lambda}_2 I_2 \right) X_2 = 0 \\ \Leftrightarrow \left( A + I_2 \right) X_2 = 0 \\ \Leftrightarrow \left( \left[ \begin{array}{cc} 5 & -3 \\ 6 & -4 \end{array} \right] - \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right] \right).X_2 = 0 \\ \Leftrightarrow \left( \left[ \begin{array}{cc} 6 & -3 \\ 6 & -3 \end{array} \right] . \left[ \begin{array}{c} x_{21} \\ x_{22} \end{array} \right] \right) = 0 \\ \Leftrightarrow x_{21} = \frac{1}{2} x_{22} \\ \Leftrightarrow \textrm{Il existe une infinité de vecteurs propres.} \\ X_2 = \left[ \begin{array}{c} 1 \\ 2 \end{array} \right] \textrm{ par exemple} \end{array}$

On obtient la matrice finale $F$ des vecteurs propres :

$F = \left[ \begin{array}{cc} 1 & 1 \\ 1 & 2 \end{array} \right]$

Il faut calculer le déterminant de $F$

$\det \left( F \right) = \det \left( \left[  \begin{array}{cc} 1 & 1 \\ 1 & 2  \end{array} \right] \right) = 2 - 1 = 1$

Comme $\det \left( F \right) \neq 0$, les vecteurs propres sont bien non colinéaires dans $\mathbb{R}^2$.

De manière plus générale, soit $A$ une matrice de l'application $f$ dans la base $\mathcal{B}$ de l'espace vectoriel $\mathbb{R}^n$, et soit $X$ un vecteur propre $x$ dans $\mathcal{B}$.

$A = \left[ \begin{array}{ccc} a_{11} & \ldots{} & a_{1n} \\ \ldots{} & \ldots{} & \ldots{} \\ a_{n1} & \ldots{} & a_{nn} \\ \end{array}\right]$

et

$\begin{array}{l} f \left( x \right) = {\lambda}_n x \\ \Leftrightarrow A.X = {{\lambda}_n}.X \\ \Leftrightarrow \left( A - {\lambda}_n I_n \right).X = 0 \\ \Leftrightarrow \left\lbrace \begin{array}{l} \left( a_{11} - {\lambda}_n \right) x_1 + a_{12} x_2 + \ldots{} + a_{1n} x_n = 0 \\ a_{21} x_1 + \left( a_{22} - {\lambda}_n \right) x_2 + \ldots{} + a_{2n} x_n = 0 \\ \ldots{} \\ a_{n1} x_1 + a_{n2} x_2 + \ldots{} + \left( a_{nn} - {\lambda}_n \right) x_n = 0 \\ \end{array}\right.  \end{array}$

Les valeurs propres sont les scalaires ${\lambda}_n$. Ils permettent d'écrire l'**équation caractéristique de degré $n$ en ${\lambda}_n$**.

$\det \left( A - {{\lambda}_n}.{I_n} \right) = 0$

## Diagonalisation d'une matrice carrée

La diagonalisation par la matrice $D$ de la matrice $A$ s'effectue par l'intermédiaire d'une **matrice de passage $P$** correspondant aux vecteurs propres, c'est-à-dire $F$.

$D = P^{-1} . A . P$

Si l'on reprend l'exemple précédent la matrice de passage correspond aux vecteurs propres calculés, d'où :

$\begin{array}{l} P = F \\ P^{-1} = \left[ \begin{array}{cc} 2 & -1 \\ -1 & 1 \end{array}\right] \\ D = \left[ \begin{array}{cc} 2 & -1 \\ -1 & 1 \end{array}\right] . \left[ \begin{array}{cc} 5 & -3 \\ 6 & -4 \end{array}\right] . \left[ \begin{array}{cc} 1 & 1 \\ 1 & 2 \end{array}\right] = \left[ \begin{array}{cc} 2 & 0 \\ 0 & -1 \end{array}\right] \end{array}$

> [!NOTE]
> $A^n = \left( P.D.{P^{-1}} \right) \left( P.D.{P^{-1}} \right) \ldots{} \left( P.D.{P^{-1}} \right) = P.{D^n}.{P^{-1}}$

## Matrices orthogonales

Lorsque la matrice carrée $U$ est réelle, on dit que $U$ est orthogonal si :

${{}^t}U.U = I_n$

$U$ appartient à l'espace vectoriel $E^{m \times n}$ avec $m \geq n$.

**Propriété.** ${{}^t}U = U^{-1}$

## Changement de coordonnées

Soit $E$ un **espace vectoriel** muni d'une base $e = \left\lbrace e_1, e_2, \ldots{}, e_n \right\rbrace$ que l'on qualifie d'ancienne base. On choisit dans $E$ une autre base $f = \left\lbrace f_1, f_2, \ldots{}, f_n \right\rbrace$ appelée nouvelle base.

On appelle **matrice de passage** de la base $e$ à la base $f$, la matrice carrée $P$ d'ordre $n$, dont les colonnes expriment les coordonnées des vecteurs de $f$ dans la base $e$. Cette matrice est régulière. La matrice de passage de $f$ à $e$ est la matrice $P^{-1}$.

Soit $x$ un élément de $E$ dont les coordonnées dans les deux bases $e$ et $f$ sont stockées dans des matrices colonnes $X$ et $Y$, alors :

$X = P.X$

et

$Y = {P^{-1}}.X$

## Liens

- [Topo en format P.D.F.](./PDF/08-Valeurs-et-vecteurs-propres-dans-R-n.pdf)

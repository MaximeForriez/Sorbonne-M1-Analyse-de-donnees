# Calcul matriciel

## Tutoriels

- [Matrices](https://www.youtube.com/watch?v=Sdg9O-HqSN0&list=PL024XGD7WCIHDg6tgbbb9Xa18cPq7eSpg)

- [Matrices et applications linéaires](https://www.youtube.com/watch?v=ozMEF87Gf_U&list=PL024XGD7WCIFrKp0wE8DwPmaDAv3tNBna)

- [Déterminants](https://www.youtube.com/watch?v=llMn-67irWo&list=PL024XGD7WCIGNiu5N6GPuLXQVgsHzCM2Q)

## Éléments du calcul matriciel

### Définition

Les matrices sont des tableaux de nombres. Beaucoup de problèmes en algèbre linéaire se ramènent à des calculs matriciels, notamment pour résoudre les systèmes linéaires.

Soit $\mathbb{K}$ un corps $\left( \mathbb{Q}, \mathbb{R}, \mathbb{C} \right)$, une **matrice $A$** est un tableau rectangulaire d'éléments de $\mathbb{K}$. $A$ est dite de **taille $n \times p$** si elle a $n$ lignes et $p$ colonnes. Les nombres $a_{ij}$ de tableau sont appelés les **coefficients de $A$** dans lesquelles $i$ est la i-ème ligne, et $j$ la j-ième colonne.

Il existe deux notations :

$A = \left[ \begin{array}{ccccc} a_{11} & \ldots{} & a_{1j} & \ldots{} & a_{1p} \\ a_{21} & \ldots{} & a_{2j} & \ldots{} & a_{2p} \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ a_{i1} & \ldots{} & a_{ij} & \ldots{} & a_{ip} \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ a_{n1} & \ldots{} & a_{nj} & \ldots{} & a_{np} \end{array} \right] = \left( a_{ij} \right)_{{\tiny \begin{array}{c} 1 \leq i \leq n \\ 1 \leq j \leq p \end{array}}}$

La seconde forme $\left( a_{ij} \right)$ est appelée le **terme général**.

Deux matrices sont **égales** si elles ont la même taille et les mêmes coefficients.

L'ensemble des matrices à $n$ lignes et $p$ colonnes à coefficients dans $\mathbb{K}$ est notée :

$M_{n, p} \left( \mathbb{K} \right)$

Par exemple, les matrices $M_{n, p} \left( \mathbb{R} \right)$ sont appelées **matrices réelles**.

Si $n = p$ alors la **matrice** est dite **carrée**.

$M_n \left( \mathbb{K} \right) = M_{n, n} \left( \mathbb{K} \right)$

$a_{1, 1}, a_{2, 2}, a_{3, 3}, \ldots{}, a_{i, i}, \ldots{}, a_{n, n}$ forment la **diagonale principale**.

Si $n = 1$ alors il s'agit d'une **matrice ligne** (ou un **vecteur ligne**).

$A = \left[ a_{1, 1}, a_{1, 2}, a_{1, 3}, \ldots{}, a_{1, j}, \ldots{}, a_{1, p} \right]$

Si $p = 1$ alors il s'agit d'une **matrice colonne** (ou un **vecteur colonne**).

$A = \left[ \begin{array}{c} a_{1, 1} \\ a_{1, 2} \\ a_{1, 3} \\ \ldots{} \\ a_{1, j} \\ \ldots{} \\ a_{1, p} \end{array} \right]$

La matrice dont tous les coefficients sont nuls, est appelée **matrice nulle**. Elle se note :

$0_{n, p}$

ou

$0$

La matrice nulle joue le rôle des zéros pour les nombres réels.

### Opérations

#### La somme des matrices

Soient $A$ et $B$, deux matrices de **même taille** $n \times p$, la somme $C = A + B$ est la matrice $n \times p$ définie par :

$c_{ij} = a_{ij} + b_{ij}$

#### Le produit d'une matrice par un scalaire

Le produit $A = \left( a_{ij} \right) \in M_{n, p} \left( \mathbb{K} \right)$ par $\alpha \in \mathbb{K}$ est la matrice

${\alpha}.A = \left( {\alpha}a_{ij} \right)$

#### L'opposé et la différence d'une matrice

$- A = \left( -1 \right) A$ est l'**opposé** de $A$.

La différence $A - B$ est définie par $A + \left( -B \right)$.

#### L'algèbre des matrices

Soient $A, B, C \in M_{n, p} \in \mathbb{K}$ et $\alpha, \beta \in \mathbb{K}$.

- Commutativité : $A + B = B + A$

- Associativité : $A + \left( B + C \right) = \left( A + B \right) + C$

- Élément neutre de l'addition : $A + 0 = A$

- Distributivité : $\left( \alpha + \beta \right) A = {\alpha}A + {\beta}A$

### Multiplication de matrices

$A = \left( a_{ij} \right)$ une matrice $n \times \mathbf{p}$ et $B = \left( b_{ij} \right)$ une matrice $\mathbf{p} \times q$, alors le produit $C = A.B$ est une matrice $n \times q$ définie par :

$c_{ij} = \sum_{k = 1}^{p} a_{ik} b_{kj}$

Le **produit scalaire** $u$ et $v$ est une matrice $1 \times 1$

$\begin{array}{l}u.v = \left[ a_1, a_2, a_3, \ldots{}, a_n \right] . \left[ \begin{array}{c} b_1 \\ b_2 \\ b_3 \\ \ldots{} \\ b_n \end{array} \right] \\u.v = \left[ a_1 b_1, a_2 b_2, a_3 b_3, \ldots{}, a_n b_n \right]\end{array}$

En général, $A.B \neq B.A$ ; le produit de matrice vérifie une propriété de **non commutativité**

$A.B = 0$ n'implique pas $\left\lbrace \begin{array}{l} A = 0 \\ \textrm{ou} \\ B = 0 \end{array} \right.$.

Exemple. $A = \left[ \begin{array}{cc} 0 & -1 \\ 0 & 5 \end{array} \right]$ et $B = \left[ \begin{array}{cc} 2 & -3 \\ 0 & 0 \end{array} \right]$, donc $A.B = \left[ \begin{array}{cc} 0 & 0 \\ 0 & 0 \end{array} \right]$.

$A.B = A.C$ n'implique pas $B = C$. Dit autrement, la simplification par l'élément neutre $1$ n'existe pas.

L'algèbre du produit matriciel vérifie trois propriétés.

- Associativité du produit. $A.\left( B.C \right) = \left( A.B \right) .C$

- Distributivité du produit. $\left\lbrace \begin{array}{l} A. \left( B + C \right) = A.B + A.C \\ \left( B + C \right) . A = B.A + C.A \end{array} \right.$

- $A.0 = 0$ et $0.A = 0$

### La matrice identité

La matrice carrée, notée $I_n$, ou $I$

$I_n = \left[ \begin{array}{cccc}1 & 0 & \ldots{} & 0 \\0 & 1 & \ldots{} & 0 \\\ldots{} & \ldots{} & \ldots{} & \ldots{} \\0 & 0 & \ldots{} & 1\end{array} \right]$

est la **matrice carrée**.

On définit le **symbole de Kronecker**[^1] ${\delta}_{i, j} \in \mathbb{R}$ pour $i$ et $j$ entiers.

${\delta}_{i, j} = \left\lbrace \begin{array}{lc} 0 & \textrm{si } i \neq j \\ 1 & \textrm{si } i = j \end{array} \right.$

alors $I_n = \left( {\delta}_{i, j} \right)_{1 \leq i, j \leq n}$.

La matrice identité joue un rôle analogue au nombre $1$ dans les réels pour la multiplication.

**Proposition.** Si $A$ est une matrice $n \times p$, alors $I_n . A = A$ et $A . I_p = A$

### La puissance d'une matrice

Dans $M_n \left( \mathbb{R} \right)$, la multiplication des matrices est une **opération interne**.

- Si $A, B \in M_n \left( \mathbb{K} \right)$ alors $A \times B \in M_n \left( \mathbb{K} \right)$.

- Cas particuliers.
    - $A^2 = A.A$
    - $A^3 = A.A.A$
    - *etc*.
    - $A^p = \underbrace{A \times A \times \ldots{} \times A}_{p \textrm{ facteurs}}$

Par définition, $A^0 = I_n$.

Par observation, on conjoncture[^2] que :

$A^p = \left[ \begin{array}{ccc}1 & 0 & 2^p - 1 \\0 & \left( -1 \right)^p & 0 \\ 0 & 0 & 2^p\end{array} \right]$

La démonstration s'effectue par récurrence.

> [!NOTE]
> Comme la multiplication n'est pas commutative.
> $\left( A + B \right)^2 = A^2 + A.B + B.A + B^2 \neq A^2 + 2 A.B + B ^2$
> Dit autrement, le binôme de Newton est en général faux.

**Proposition.** Soient $A, B \in M_n \left( \mathbb{K} \right)$ tels que $A$ et $B$ commutent

$A.B = B.A$

alors pour tout entier $p \geq 0$

$\left( A + B \right)^p = \sum_{k = 0}^{p} \left( \begin{array}{c} p \\ k \end{array} \right) A^{p - k} . B^k$

où $\left( \begin{array}{c} p \\ k \end{array} \right)$ désigne le coefficient du binôme.

S'il existe un entier $k$ tel que $N^k = 0$ la matrice $N$ est dite **nilpotente**.

###### Méthode de calcul du $A^p$

1. On pose $N = A - I_n$.

2. On calcule $N^2, N^3, \ldots{}, N^k$ jusqu'à trouver une matrice nilpotente.

3. Comme $A = I_n + N$ (ou $N + I_n$), la commutativité se vérifie :

$A^p = \sum_{l = 0}^{p} \left( \begin{array}{c} p \\ k \end{array} \right) N^l {I_n}^{p - l} = \sum_{k = 0}^{p} \left( \begin{array}{c} p \\ n \end{array} \right) N^k$

car les puissances de l'identité valent l'identité, or si $p = k$ la matrice $N$ est nilpotente, donc le calcul de $A^p$ s'arrête pour $p = k - 1$.

$\begin{array}{l} A^p = \sum_{l = 1}^{k - 1} \left( \begin{array}{c} k - 1 \\ n \end{array} \right) N^l \\ A^p = I_n + pN + \frac{p \left( p - 1 \right)}{2!} N^2 + \frac{p \left( p - 1 \right) \left( p - 2 \right)}{3!} N^3 + \ldots{} + \frac{p \left( p - 1 \right) \ldots{} \left( p - k + 1 \right)}{l!} N^{k - 1} \end{array}$

### L'inverse d'une matrice

Soit $A \in M_n \left( \mathbb{K} \right)$, s'il existe une matrice $B \in M_n \left( \mathbb{K} \right)$ telle que

$A.B = I_n$

et

$B.A = I_n$

alors $A$ est dite **inversible**. $B$ est la matrice **inverse** de $A$, et est notée $A^{-1}$.

Il suffit de vérifier l'une des deux conditions.

Lorsque $A$ est inversible pour $p \in \mathbb{N}$, on note

$A^{-p} = \left( A^{-1} \right)^{p} = \underbrace{A^{-1} \times A^{-1} \times \ldots{} \times A^{-1}}_{p \textrm{ facteurs}}$

L'ensemble des matrices inversibles de $M_n \left( \mathbb{K} \right)$ est noté $G L_n \left( \mathbb{K} \right)$

Exemple. Soit $A = \left[ \begin{array}{cc} 1 & 2 \\ 0 & 3 \end{array} \right]$, on cherche une matrice $B$ telle que $A.B = I_2$ et $B.A = I_2$. On pose $B = \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right]$.

- $A.B = \left[ \begin{array}{cc} 1 & 2 \\ 0 & 3 \end{array} \right] . \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right] = \left[ \begin{array}{cc} a + 2c & b + 2d \\ 3c & 3d \end{array} \right]$

$\begin{array}{l} A.B = I_2 \Leftrightarrow \left[ \begin{array}{cc} a + 2c & b + 2d \\ 3c & 3d \end{array} \right] = \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right] \\ A.B = I_2 \Leftrightarrow \left\lbrace \begin{array}{l} a + 2c = 1 \\ b + 2d = 0 \\ 3c = 0 \\ 3d = 1 \end{array} \right.  \end{array}$

Il existe une unique solution $B = \left[ \begin{array}{cc} 1 & -\frac{2}{3} \\ 0 & \frac{1}{3} \end{array} \right]$.

- $B.A = \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right] . \left[ \begin{array}{cc} 1 & 2 \\ 0 & 3 \end{array} \right] = \left[ \begin{array}{cc} a & 2a + 3b \\ c & 2c + 3d \end{array} \right]$

$B.A = I_2 \Leftrightarrow \left\lbrace \begin{array}{l} a = 1 \\ 2a + 3b = 0 \\ c = 0 \\ 2c + 3d = 1  \end{array} \right.$

Il existe une unique solution $B = \left[ \begin{array}{cc} 1 & -\frac{2}{3} \\ 0 & \frac{1}{3} \end{array} \right]$.

- $A.B = I_2$ et $B.A = I_2$ donc $A$ est inversible

$A^{-1} = \left[ \begin{array}{cc} 1 & -\frac{2}{3} \\ 0 & \frac{1}{3} \end{array} \right]$

**Contre-exemple.** $A = \left[ \begin{array}{cc} 3 & 0 \\ 5 & 0 \end{array} \right]$ n'est pas **inversible**. Pour $B = \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right]$, $B.A = \left[ \begin{array}{cc} 3a + 5b & 0 \\ 3c + 5d & 0 \end{array} \right] \neq \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right]$.

$I_n$ est inversible

${I_n}^{-1} = I_n$

${I_n} {I_n} = I_n$

La matrice nulle n'est pas inversible. Pour tout $B \in M_n \left( \mathbb{K} \right)$, on a

$B.{0_n} = 0_n \neq I_n$

- **Proposition 1.** Si $A$ est inversible, alors son inverse est **unique**.

- **Proposition 2.** Soit $A$ une matrice inversible, alors $A^{-1}$ est aussi inversible

$\left( A^{-1} \right)^{-1} = A$

- **Proposition 3.** Soient $A$ et $B$ deux matrices inversibles de même taille, alors $A.B$ est inversible

$\left( A.B \right)^{-1} = B^{-1} . A^{-1}$

L'ordre s'inverse aussi. De façon analogue, si $A_1, \ldots{}, A_m$ sont inversibles, alors

$\left[ A_1, A_2, \ldots{}, A_m \right]^{-1} = {A_m}^{-1} \ldots{} {A_2}^{-1} {A_1}^{-1}$

- **Proposition 4.** Soient $A, B \in M_n \left( \mathbb{K} \right)$ et $C$ une matrice inversible de $M_n \left( \mathbb{K} \right)$, alors

$A.C = B.C \Rightarrow A = B$

#### Méthode de calcul. Exemple des matrices $2 \times 2$

Soit $A = \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right]$ une matrice $2 \times 2$.

**Proposition.** Si $ad - bc \neq 0$ alors $A$ est inversible.

$A^{-1} = \frac{1}{ad - bc} \left[ \begin{array}{cc} d & -b \\ -c & 0 \end{array} \right]$

#### Méthode de Gauss pour inverser les matrices

1. Par des opérations élémentaires sur les lignes de $A$, transformer $A$ en la matrice identité $I_n$.

2. Par des opérations élémentaires sur les lignes de $A$, faire simultanément les mêmes opérations sur $I_n$.

3. À la fin, $A$ est transformée en $I_n$, et $I_n$ est transformée en $A^{-1}$.

On note $A$, matrice augmentée par $I_n$ :

$\left( A | I_n \right) \rightarrow \left( I_n | B \right) = \left( I_n | A^{-1} \right)$

On compte trois opérations élémentaires sur les lignes.

1. $L_i \leftarrow \lambda L_i$ avec $\lambda \neq 0$ : on peut multiplier une ligne par un réel non nul.

2. $L_i \leftarrow L_i + \lambda L_j$ avec $\lambda \in \mathbb{K}$ et $j \neq i$ : on peut ajouter à la ligne $L_i$ un multiple de $L_j$.

3. $L_i \leftrightarrow L_j$ : on peut échanger deux lignes.

> [!WARNING]
> Tout ce qui est fait à droite sur la matrice augmentée doit l'être à gauche.

Exemple. $A = \left[ \begin{array}{ccc} 1 & 2 & 1 \\ 4 & 0 & -1 \\ -1 & 2 & 2 \end{array} \right]$

$\begin{array}{l}\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 4 & 0 & -1 & | & 0 & 1 & 0 \\ -1 & 2 & 1 & | & 0 & 0 & 1 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \right) \\ \left( L_3 \right) \end{array} \\ \left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 0 & -8 & -5 & | & -4 & 1 & 0 \\ -1 & 2 & 1 & | & 0 & 0 & 1 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \leftarrow L_2 - 4 L_1 \right) \\ \left( L_3 \right) \end{array} \\\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 0 & -8 & -5 & | & -4 & 1 & 0 \\ 0 & 4 & 3 & | & 1 & 0 & 1 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \right) \\ \left( L_3 \leftarrow L_3 + L_1 \right) \end{array} \\\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & \frac{5}{8} & | & \frac{1}{2} & -\frac{1}{8} & 0 \\ 0 & 4 & 3 & | & 1 & 0 & 1 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \leftarrow -\frac{1}{8} L_2 \right) \\ \left( L_3 \right) \end{array} \\\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & \frac{5}{8} & | & \frac{1}{2} & -\frac{1}{8} & 0 \\ 0 & 0 & \frac{1}{2} & | & -1 & \frac{1}{2} & 1 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \right) \\ \left( L_3 \leftarrow L_3 - 4 L_2 \right) \end{array} \\\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & \frac{5}{8} & | & \frac{1}{2} & -\frac{1}{8} & 0 \\ 0 & 0 & 1 & | & -2 & 1 & 2 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \right) \\ \left( L_3 \leftarrow 2 L_3 \right) \end{array} \\\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 0 & 1 & 0 & | & \frac{7}{4} & -\frac{3}{4} & -\frac{5}{4} \\ 0 & 0 & 1 & | & -2 & 1 & 2 \end{array} \right] \begin{array}{r} \left( L_1 \right) \\ \left( L_2 \leftarrow L_2 - \frac{5}{8} L_3 \right) \\ \left( L_3 \right) \end{array} \\\left( A | I_3 \right) = \left[ \begin{array}{ccccccc} 1 & 0 & 0 & | & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 0 & | & \frac{7}{4} & -\frac{3}{4} & -\frac{5}{4} \\ 0 & 0 & 1 & | & -2 & 1 & 2 \end{array} \right] \begin{array}{r} \left( L_1 \leftarrow L_1 - 2 L_2 - L_3\right) \\ \left( L_2 \right) \\ \left( L_3 \right) \end{array}\end{array}$

donc $A^{-1} = \frac{1}{4} \left[ \begin{array}{ccc} -2 & 2 & 2 \\ 7 & -3 & -5 \\ -8 & 4 & 8 \end{array} \right]$.

Pour conclure, il faut vérifier $A \times A^{-1} = I_3$.

#### Matrices et systèmes linéaires

Soit le système linéaire à $n$ lignes et $p$ inconnues.

$\left\lbrace \begin{array}{l}a_{11} x_1 + \ldots{} + a_{1p} x_p = b_1 \\\ldots{} \\a_{n1} x_1 + \ldots{} + a_{np} x_p = b_n\end{array}\right. \Leftrightarrow A.X = B$

avec $A = \left[ \begin{array}{ccc} a_{11} & \ldots{} & a_{1p} \\ \ldots{} & \ldots{} & \ldots{} \\ a_{n1} & \ldots{} & a_{np} \end{array} \right]$, $B = \left[ \begin{array}{c} x_1 \\ \ldots{} \\ x_p \end{array} \right]$ et $B = \left[ \begin{array}{c} b_1 \\ \ldots{} \\ b_n \end{array} \right]$.

**Rappel.** Un [système d'équations linéaires](./05-Algebre%20lineaire.md) n'a soit aucune solution, soit une seule solution, soit une infinité de solution.

Dans le cas où le nombre d'équations est égal au nombre d'inconnues, on pose que : $A$ est une **matrice carrée** : $A = M_n \left( \mathbb{K} \right)$ ; $X$ est un **vecteur colonne** : $X = M_{n1} \left( \mathbb{K} \right)$ ; $B$ est un **vecteur colonne** : $B = M_{n1} \left( \mathbb{K} \right)$.

- **Proposition.** Si la matrice $A$ est **inversible**, alors la solution du système $A.X = B$ est unique et vaut :

$X = A^{-1} . B$

- **Démonstration.** $A.X = B \Leftrightarrow A^{-1} .A.X = A^{-1} .B$, or $A^{-1} .A = I_n$, donc $X = A^{-1} . B$.

> [!NOTE]
> Le produit est non commutatif, la multiplication a ainsi un sens soit on multiplie à gauche (comme dans la démonstration), soit on multiplie à droite (et dans ce sans on ne démontre rien). Dans le second cas, on place $A^{-1}$ à droite : $A.X = B \Leftrightarrow A \times A.X.A^{-1} = B.X^{-1}$. Il faut prendre cette habitude lors des calculs matriciels.

**Pour calculer l'inverse de $A$, il existe trois opérations élémentaires.**

1. $L_i \leftarrow \lambda L_i$ avec $\lambda \neq 0$.

2. $L_i \leftarrow L_i + \lambda L_j$ avec $\lambda \in \mathbb{K}$ et $i \neq j$.

3. $L_i \leftrightarrow L_j$.

Elles permettent de proposer **trois matrices élémentaires $E$**.

1. $E_{L_i \leftarrow \lambda L_i}$

2. $E_{L_i \leftarrow L_i + \lambda L_j}$

3. $E_{L_i \leftrightarrow L_j}$

Le produit $E \times A$ correspond à l'**opération élémentaire sur $A$**. Il faut bien noter que les opérations élémentaires sur les lignes sont réversibles, ce qui entraîne que les **matrices élémentaires** sont **inversibles**.

###### $L_i \leftarrow \lambda L_i$ avec $\lambda \neq 0$

La matrice $E_{L_i \leftarrow \lambda L_i}$ est la matrice obtenue en multipliant par $\lambda$ la i-ème ligne de la matrice identité $I_n$.

$E_{L_2 \leftarrow 5 L_2} = \left[ \begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right]$

La matrice $E_{L_i \leftarrow \lambda L_i} \times A$ est la matrice obtenue en multipliant par $\lambda$ la i-ème ligne de $A$.

$E_{L_2 \leftarrow \frac{1}{3} L_2} \times A = \left[ \begin{array}{ccc} 1 & 0 & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 1 \end{array} \right] \times \left[ \begin{array}{ccc} x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{array} \right] = \left[ \begin{array}{ccc} x_1 & x_2 & x_3 \\ \frac{1}{3} y_1 & \frac{1}{3} y_2 & \frac{1}{3} y_3 \\ z_1 & z_2 & z_3 \end{array} \right]$

###### $L_i \leftarrow L_i + \lambda L_j$ avec $\lambda \in \mathbb{K}$ et $i \neq j$

La matrice $E_{L_i \leftarrow L_i + \lambda L_j}$ est la matrice obtenue en ajoutant $\lambda$ fois la j-ème ligne de $I_n$ à la i-ème ligne de $I_n$

$E_{L_2 \leftarrow L_2 - 3 L_1} = \left[ \begin{array}{cccc}1 & 0 & 0 & 0 \\3- & 1 & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1\end{array} \right]$

car $-3L_1 \rightarrow \left[ -3, 0, 0, 0 \right]$ et $L_2 - 3 L_1 \rightarrow \left[ -3, 1, 0, 0 \right]$.

La matrice $E_{L_i \leftarrow L_i + \lambda L_j} \times A$ est la matrice obtenue en ajoutant $\lambda$ fois la j-ème ligne de $A$ à la i-ème de $A$.

$E_{L_1 \leftarrow L_1 - 7 L_3} \times A = \left[ \begin{array}{ccc} 1 & 0 & -7 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \times \left[ \begin{array}{ccc} x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{array} \right] = \left[ \begin{array}{ccc} x_1 -7z_1 & x_2 - 7z_2 & x_3 -7x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{array} \right]$

$\begin{array}{l}-7 L_3 \rightarrow \left[ \begin{array}{ccc} 0 & 0 & -7 \end{array}\right] \\- L_1 - 7 L_3 \rightarrow \left[ \begin{array}{ccc} 1 & 0 & -7 \end{array}\right] \\-7 \left[ \begin{array}{ccc} z_1 & z_2 & z_3 \end{array}\right] = \left[ \begin{array}{ccc} -7 y_1 & -7 y_2 & -7 y_3 \end{array}\right]\end{array}$

###### $L_i \leftrightarrow L_j$

La matrice $E_{L_i \leftrightarrow L_j}$ est la matrice obtenue en permettant les i-ème et les j-ème lignes de $I_n$.

$E_{L_2 \leftrightarrow L_4} = E_{L_4 \leftrightarrow L_2} = \left[ \begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right]$

La matrice $E_{L_i \leftrightarrow L_j} \times A$ est la matrice obtenue en permettant les i-ème et j-ème lignes de $A$.

$E_{L_2 \leftrightarrow L_3} \times A = \left[ \begin{array}{ccc} 1 & 0 & 0  \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right] \times \left[ \begin{array}{ccc} x_1 & x_2 & x_3  \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{array} \right] = \left[ \begin{array}{ccc} x_1 & x_2 & x_3  \\ z_1 & z_2 & z_3 \\ y_1 & y_2 & y_3 \end{array} \right]$ 

$\begin{array}{cccccc}& \left[ \begin{array}{c} \\  \\  \end{array} \right.  & \begin{array}{c} x_1 \\ y_1 \\ z_1 \end{array} & \begin{array}{c} x_2 \\ y_2 \\ z_2 \end{array} & \begin{array}{c} x_3 \\ y_3 \\ z_3 \end{array} & \left. \begin{array}{c} \\  \\  \end{array} \right] \\\left[ \begin{array}{ccc} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] & & \begin{array}{c} x_1 + 0 + 0 \\ 0 + 0 + z_1 \\ 0 + y_1 + 0 \end{array} & \begin{array}{c} x_2 + 0 + 0 \\ 0 + 0 + z_2 \\ 0 + y_2 + 0 \end{array} & \begin{array}{c} x_3 + 0 + 0 \\ 0 + 0 + z_3 \\ 0 + y_3 + 0 \end{array} &  \end{array}$

#### Matrices échelonnées et équivalentes

**Définition.** Une matrice est **échelonnée** si le nombre de zéros commençant une ligne croît strictement ligne par ligne, et s'arrête s'il n'y a plus de zéros.

$\left[ \begin{array}{ccccccc}+ & * & * & * & * & * & * \\0 & 0 & + & * & * & * & * \\0 & 0 & 0 & + & * & * & * \\0 & 0 & 0 & 0 & 0 & 0 & + \\0 & 0 & 0 & 0 & 0 & 0 & 0 \\0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array}\right]$

**Définition.** Une matrice est **échelonnée réduite** si :
    1. le premier coefficient non nul d'une ligne vaut 1 ;
    2. c'est le seul élément non nul de la colonne.

$\left[ \begin{array}{ccccccc}1 & * & 0 & 0 & * & * & 0 \\0 & 0 & 1 & 0 & * & * & 0 \\0 & 0 & 0 & 1 & * & * & 0 \\0 & 0 & 0 & 0 & 0 & 0 & 1 \\0 & 0 & 0 & 0 & 0 & 0 & 0 \\0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array}\right]$

**Théorème.** Étant donnée une matrice $A \in M_{n, p} \left( \mathbb{K} \right)$, il existe une unique matrice échelonnée réduite $U$ obtenue à partir de $A$ par des opérations élémentaires sur les lignes. Il s'agit de la méthode du pivot de Gauss :

1. Choix du pivot (matrice échelonnée)

2. Élimination (matrice échelonnée)

3. Boucle (matrice échelonnée)

4. Homothétie (matrice échelonnée réduite)

5. Élimination (matrice échelonnée réduite)

**Cas des matrices carrées.** Soit $A \in M_n \left( \mathbb{K} \right)$
 
- **Théorème.** La matrice $A$ est inversible si et seulement si sa forme échelonnée réduite est la matrice identité $I_n$.

> [!NOTE]
> Il justifie la méthode de calcul de l'inverse par la matrice augmentée.

- **Corollaire.** Les assertions suivantes sont équivalentes.

1. La matrice $A$ est inversible.

2. Le système linéaire $A.X = \left[ \begin{array}{c} 0 \\ 0 \\ \ldots{} \\ 0 \end{array} \right]$ a une unique solution $X = \left[ \begin{array}{c} 0 \\ 0 \\ \ldots{} \\ 0 \end{array} \right]$.

3. Pour tout second membre $B$, le système linéaire $A.X = B$ a une unique solution $X$.

**Exemple.** $A = \left[ \begin{array}{cccc} 1 & 2 & 3 & 4 \\ 0 & 2 & 4 & 6 \\ -1 & 0 & 1 & 0 \end{array} \right]$.

1. Passage à une matrice échelonnée

$\left\lbrace  \begin{array}{lc} {a_{11}}^1 = 1 & \\ L_3 \leftarrow L_3 + L_1 & A \sim \left[ \begin{array}{cccc} 1 & 2 & 3 & 4 \\ 0 & 2 & 4 & 6 \\ 0 & 2 & 4 & 4 \end{array} \right] \end{array} \right.$

$\left\lbrace  \begin{array}{lc} {a_{22}}^2 = 2 & \\ L_3 \leftarrow L_3 - L_2 & A \sim \left[ \begin{array}{cccc} 1 & 2 & 3 & 4 \\ 0 & 2 & 4 & 6 \\ 0 & 0 & 0 & -2 \end{array} \right] \end{array} \right.$

2. Passage à une forme échelonnée réduite

$\left\lbrace  \begin{array}{lc} L_2 \leftarrow \frac{1}{2} \textrm{ et } L_3 \leftarrow -\frac{1}{2} L_3 & A \sim \left[ \begin{array}{cccc} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 1 \end{array} \right] \end{array} \right.$

$\left\lbrace  \begin{array}{lc} L_2 \leftarrow L_2 - 3 L_3 \textrm{ et } L_1 \leftarrow L_1 - 4 L_3 & A \sim \left[ \begin{array}{cccc} 1 & 2 & 3 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right] \end{array} \right.$

$\left\lbrace  \begin{array}{lc} L_1 \leftarrow L_1 - 2 L_2 & A \sim \left[ \begin{array}{cccc} 1 & 0 & -1 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right] \end{array} \right.$

3. Conclusion

$\left[ \begin{array}{cccc} 1 & 2 & 3 & 4 \\ 0 & 2 & 4 & 6 \\ -1 & 0 & 1 & 0 \end{array} \right] \sim \left[ \begin{array}{cccc} 1 & 0 & -1 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right]$

### Matrices triangulaires, matrices diagonales

Soit $A$ une matrice carrée de taille $n \times n$.

La diagonale est l'ensemble des valeurs $\left[ \begin{array}{cccc} a_{11} & a_{22} & \ldots{} a_{nn} \end{array} \right]$.

$A$ est une **triangulaire inférieure** si ses éléments **au-dessus** de la diagonale sont nuls : $i < j \Rightarrow a_{ij} = 0$.

$A$ est une **triangulaire supérieure** si ses éléments **en-dessous** de la diagonale sont nuls : $i > j \Rightarrow a_{ij} = 0$.

**Théorème.** Une matrice $A$ de taille $n \times n$ est inversible si et seulement si ses éléments diagonaux sont tous non nuls.

Une matrice qui est transformée inférieure **et** supérieure est une **matrice diagonale** : $i \neq j \Rightarrow a_{ij} = 0$.

**Puissance $p$ d'une matrice diagonale**

$D = \left[  \begin{array}{ccccc} {{\alpha}_1} & 0 & \ldots{} & 0 & 0 \\ 0 & {{\alpha}_2} & \ldots{} & 0 & 0 \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ 0 & 0 & \ldots{} & {{\alpha}_{n - 1}} & 0 \\ 0 & 0 & \ldots{} & 0 & {{\alpha}_{n}}  \end{array} \right]$

$D^p = \left[  \begin{array}{ccccc} {{\alpha}_1}^p & 0 & \ldots{} & 0 & 0 \\ 0 & {{\alpha}_2}^p & \ldots{} & 0 & 0 \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ 0 & 0 & \ldots{} & {{\alpha}_{n - 1}}^p & 0 \\ 0 & 0 & \ldots{} & 0 & {{\alpha}_{n}}^p  \end{array} \right]$

### Matrice transposée

Soit $A = \left( a_{ij} \right)$ une matrice de taille $n \times p$, la **matrice transposée** de $A$, notée ${{}^t}A$, est la matrice de taille $p \times n$ définie par :

$A = \left[ \begin{array}{ccc}a_{11} & \ldots{} & a_{1p} \\a_{21} & \ldots{} & a_{2p} \\\ldots{} & \ldots{} & \ldots{} \\a_{n1} & \ldots{} & a_{np} \\\end{array}\right]$

et

${{}^t}A = \left[ \begin{array}{ccc}a_{11} & \ldots{} & a_{n1} \\a_{12} & \ldots{} & a_{n2} \\\ldots{} & \ldots{} & \ldots{} \\a_{1p} & \ldots{} & a_{np} \\\end{array}\right]$

Les coefficients de la diagonale reste sur la diagonale. Le coefficient $a_{ij}$ se retrouve à la place $\left( j, i \right)$ dans ${{}^t}A$. Dit autrement, la i-ème ligne de $A$ devient la i-ème colonne de ${{}^t}A$.

> [!WARNING]
> Il existe plusieurs notations pour la matrice transposée : ${{}^t}A = A^T = A^t = {{}^T}A$.

La transposée d'une matrice carrée est aussi une matrice carrée.

La transposée d'un vecteur ligne est un vecteur colonne.

- **Théorème 1.** ${{}^t}\left( A + B \right) = {{}^t}A + {{}^t}B$

- **Théorème 2.** ${{}^t}{\left( \alpha A \right)} = {\alpha}{\left( {{}^t}A\right)}$

- **Théorème 3.** ${{}^t}{\left( {{}^t}A \right)} = A$

- **Théorème 4.** ${{}^t}{\left( A.B \right) } = {{}^t}B.{{}^t}A$

> [!WARNING]
> L'ordre du produit matriciel s'inverse.

- **Théorème 5.** Si $A$ est inversible alors ${{}^t}A$ l'est aussi, et $\left( {{}^t}A \right)^{-1} = {{}^t}{\left( A^{-1} \right)}$.

### La trace d'une matrice

Soit $A = \left( a_{ij} \right)$ une matrice carrée de taille $n \times n$.

Les éléments $a_{11}, a_{22}, \ldots{}, a_{nn}$ sont les **éléments diagonaux**.

La **diagonale principale** est la diagonale $\left[ \begin{array}{cccc} a_{11} & a_{22} & \ldots{} & a_{nn} \end{array} \right]$.

La **trace** de la matrice $A$ est la somme des éléments diagonaux de $A$.

$\mathrm{tr} A = a_{11} + a_{22} + \ldots{} + a_{nn}$

Soient $A$ et $B$ deux matrices $n \times n$ alors :

- **Théorème 1.** $\mathrm{tr} \left( A + B \right) = \mathrm{tr} A  + \mathrm{tr} B$

-**Théorème 2.** Pour tout $\alpha \in \mathbb{K}$, $\mathrm{tr} \left( \alpha A \right) = \alpha \mathrm{tr} A$ 

- **Théorème 3.** $\mathrm{tr} \left( {{}^t}A \right) = \mathrm{tr} A$ 

- **Théorème 4.** $\mathrm{tr} \left( A.B \right) = \mathrm{tr} \left( B.A \right)$

### Matrice symétrique

Une **matrice carrée** $A$ de taille $n \times n$ est **symétrique** si elle est égale à $n$ transposée.

$A = {{}^t}A$

Dit autrement, si $a_{ij} = a_{ji}$ pour tout $i, j = 1, \ldots{}, n$, c'est-à-dire que les coefficients sont symétriques par rapport à la diagonale.

> [!NOTE]
> Il n'existe aucune contrainte sur $a_{11}, a_{22}, \ldots{}, a_{nn}$.

Pour une matrice $B$ quelconque, les matrices $B.{{}^t}B$ et ${{}^t}B.B$ sont symétriques.

$\begin{array}{l}{{}^t}{\left( B.{{}^t}B \right)} = {{}^t}{\left( {{}^t}B\right)}.{{}^t}B = B.{{}^t}B \\{{}^t}{\left( {{}^t}B.B \right)} = {{}^t}B.{{}^t}{\left( {{}^t}B \right)} = {{}^t}B.B\end{array}$

Une **matrice carrée** $A$ de taille $n \times n$ est **antisymétrique** si

${{}^t}A = - A$

Les éléments diagonaux d'une matrice antisymétrique sont toujours tous nuls. Si $i = j$, alors $a_{ii} = - a_{ii}$.

## Matrice et applications linéaires

### Rang d'une famille de vecteurs

Dans le cadre d'un espace vectoriel de dimension finie, l'étude des applications linéaires se ramènent à l'étude des matrices.

#### Définition

Le rang d'une famille de vecteurs est la dimension du plus petit sous-espace vectoriel contenant tous ces vecteurs.

Soient $E$ un $\mathbb{K}$-espace vectoriel et une famille de vecteurs $\left\lbrace v_1, \ldots{}, v_p \right\rbrace$ des vecteurs de $E$.

- Le sous-espace vectoriel $\mathrm{Vect} \left( v_1, \ldots{}, v_p \right)$ engendré par $\left\lbrace v_1, \ldots{}, v_p \right\rbrace$ est de dimension finie.

- Le **rang** de la famille $\left\lbrace v_1, \ldots{}, v_p \right\rbrace$ est la dimension du sous-espace vectoriel engendré par les vecteurs $v_1, \ldots{}, v_p$.

$\mathrm{rg} \left( v_1, \ldots{}, v_p \right) = \dim \left( \mathrm{Vect} \left( v_1, \ldots{}, v_p \right) \right)$

- **Proposition 1.** $0 \leq \mathrm{rg} \left( v_1, \ldots{}, v_p \right) \leq p$

    - Le rang vaut $0 \Leftrightarrow$ Tous les vecteurs sont nuls.
    
    - Le rang vaut $p \Leftrightarrow$ La famille de vecteurs est libre.

- **Proposition 2.** $\mathrm{rg} \left( v_1, \ldots{}, v_p \right) \leq \dim E$

Quel est le rang de $\left\lbrace v_1, v_2, v_3 \right\rbrace$ dans l'espace vectoriel $\mathbb{R}^4$ ? Avec $v_1 = \left( \begin{array}{c} 1 \\ 0 \\ 1 \\ 0 \end{array} \right)$, $v_2 = \left( \begin{array}{c} 0 \\ 1 \\ 1 \\ 1 \end{array} \right)$ et $v_3 = \left( \begin{array}{c} -1 \\ 1 \\ 0 \\ 1 \end{array} \right)$.

- Dans $\mathbb{R}^4$, $\mathrm{rg} \left( v_1, v_2, v_3 \right) \leq 4$, mais il n'y a que trois vecteurs, donc $\mathrm{rg} \left( v_1, v_2, v_3 \right) \leq 3$.

- $v_1 \neq 0$, donc $\mathrm{rg} \left( v_1, v_2, v_3 \right) \geq 1$.

- $\mathrm{rg} \left( v_1, v_2, v_3 \right) \geq \mathrm{rg} \left( v_1, v_2 \right) = 2$, car $v_1$ et $v_2$ ne sont pas colinéaires.

- Le rang de la famille de vecteurs est soit $2$, soit $3$. La famille est-elle libre ou liée ?

$\begin{array}{cl} & {\lambda}_1 v_1 + {\lambda}_2 v_2 + {\lambda}_3 v_3 = 0 \\ \Leftrightarrow & v_1 - v_2 + v_3 = 0 \\ \Leftrightarrow & \textrm{La famille est liée.} \\ \Leftrightarrow & \mathrm{Vect} \left( v_1, v_2, v_3 \right) = \mathrm{Vect} \left( v_1, v_2 \right) \end{array}$

$\mathrm{rg} \left( v_1, v_2, v_3 \right) = \dim \left( \mathrm{Vect} \left( v_1, v_2, v_3 \right) \right) = 2$

#### Rang d'une matrice

**Définition.** Le rang d'une matrice est le rang de ses **vecteurs colonnes**.

**Exemple.** Calculer le rang de la matrice $A$ :

$A = \left(  \begin{array}{cccc} 1 & 2 & -\frac{1}{2} & 0 \\ 1 & 4 & -1 & 0  \end{array} \right) \in M_{2, 4} \left( \mathbb{K} \right)$

Le rang de $A$ est le rang des vecteurs de $\mathbb{R}^2$

$\left\lbrace v_1 = \left( \begin{array}{c} 1 \\ 2 \end{array} \right), v_2 = \left( \begin{array}{c} 2 \\ 4 \end{array} \right), v_3 = \left( \begin{array}{c} -\frac{1}{2} \\ -1 \end{array} \right), v_4 = \left( \begin{array}{c} 0 \\ 0 \end{array} \right) \right\rbrace$

Tous les vecteurs sont colinéaires à $v_1$. On en déduit que $\mathrm{rg} \left\lbrace v_1, v_2, v_3, v_4 \right\rbrace = 1$.

$\mathrm{rg} A = 1$

**Définition.** Une matrice est échelonnée par rapport aux colonnes si le nombre de zéros commençant une colonne croît strictement colonne après colonne, jusqu'à ce qu'il ne reste plus que des zéros.

$\left(  \begin{array}{cccccc} + & 0 & 0 & 0 & 0 & 0 \\ * & 0 & 0 & 0 & 0 & 0 \\ * & + & 0 & 0 & 0 & 0 \\ * & * & + & 0 & 0 & 0 \\ * & * & * & 0 & 0 & 0 \\ * & * & * & + & 0 & 0 \\ \end{array} \right)$

avec $*$ des coefficients quelconques et $+$ des coefficients non nuls.

**Proposition.** Le rang d'une matrice échelonnée par colonnes est égal au nombre de colonnes non nulles.

$\textrm{Ici } \mathrm{rg} = 4$

#### Opérations conservant le rang

**Proposition.** Le rang d'une matrice est conservé par les opérations élémentaires suivantes sur les colonnes $C_1, C_2, \ldots{}, C_p$.

1. $C_i  \leftarrow {\lambda} C_i$ avec ${\lambda} \neq 0$.

2. $C_i  \leftarrow C_i + {\lambda} C_j$ avec ${\lambda} \in \mathbb{K}$ et $j \neq i$.

3. $C_i \leftrightarrow C_j$.

**Plus généralement, l'opération $C_i \leftarrow C_i + {\lambda}_1 C_1 + \ldots{} + {\lambda}_p C_p$ conserve le rang de la matrice**.

**Méthodologie.** Comment calculer le rang d'une matrice ?

1. Appliquer la méthode de Gauss sur les colonnes de la matrice $A$.

2. Appliquer les opérations élémentaires permettant la transformation de $A$.

3. Transformer la matrice $A$ en une matrice échelonnée.

4. Le rang de la matrice est le nombre de colonnes non nulles.

**Exemple.** Quel est le rang de la famille des cinq vecteurs suivants de $\mathbb{R}^4$ ?

$v_1 = \left( \begin{array}{c} 1 \\ 1 \\ 1 \\ 1 \end{array} \right)$

$v_2 = \left( \begin{array}{c} -1 \\ 2 \\ 0 \\ 1 \end{array} \right)$

$v_3 = \left( \begin{array}{c} 3 \\ 2 \\ -1 \\ -3 \end{array} \right)$

$v_4 = \left( \begin{array}{c} 3 \\ 5 \\ 0 \\ -1 \end{array} \right)$

$v_5 = \left( \begin{array}{c} 3 \\ 8 \\ 1 \\ 1 \end{array} \right)$

Cela revient à calculer le rang de la matrice

$\left( \begin{array}{ccccc} 1 & -1 & 3 & 3 & 3 \\ 1 & 2 & 2 & 5 & 8 \\ 1 & 0 & -1 & 0 & 1 \\ 1 & 1 & -3 & -1 & 1 \end{array} \right)$

Avec la méthode de Gauss, on obtient une matrice échelonnée.

- 1<sup>ère ligne. $C_2 \leftarrow C_2 + C_1$, $C_3 \leftarrow C_3 - 3 C_1$, $C_4 \leftarrow C_4 - 3 C_1$ et $C_5 \leftarrow C_5 - 3 C_1$

$\sim \left( \begin{array}{ccccc} 1 & 0 & 0 & 0 & 0 \\ 1 & 3 & -1 & 2 & 5 \\ 1 & 1 & -4 & -3 & -2 \\ 1 & 2 & -6 & -4 & -2 \end{array} \right)$

- 2<sup>e ligne. $C_2 \leftrightarrow C_3$ pour mettre $-1$ en pivot et éviter d'introduire des fractions, $C_3 \leftarrow C_3 + 3 C_2$, $C_4 \leftarrow C_4 + 2 C_2$ et $C_5 \leftarrow C_5 + 5 C_2$.

$\sim \left( \begin{array}{ccccc} 1 & 0 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 & 0 \\ 1 & -4 & -11 & -11 & -22 \\ 1 & -6 & -16 & -16 & -32 \end{array} \right)$

- 3<sup>e ligne. $C_4 \leftarrow C_4 - C_3$ et $C_5 \leftarrow C_5 - 2 C_3$.

$\sim \left( \begin{array}{ccccc} 1 & 0 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 & 0 \\ 1 & -4 & -11 & 0 & 0 \\ 1 & -6 & -16 & 0 & 0 \end{array} \right)$

Le rang de la famille de vecteurs est $3$.

#### Rang et matrice inversible

**Théorème.** Une matrice carrée de taille $n$ est inversible si et seulement si elle est de rang $n$.

#### Rang engendré par les vecteurs lignes

Une matrice $A$ est une superposition de vecteurs lignes $\left( w_1, \ldots{}, w_n \right)$.

**Proposition.** $\mathrm{rg} A = \dim \left( \mathrm{Vect} \left( w_1, \ldots{}, w_n \right) \right)$.

- Cela signifie que l'espace vectoriel engendré par les vecteurs colonnes et l'espace engendré par les vecteurs lignes sont de même dimension.

- Le rang d'une matrice est égal au rang de sa transposée.

$\mathrm{rg} A = \mathrm{rg} {{}^t}A$

### Applications linéaires en dimension finie

#### Construction et caractérisation

Soient $E$ et $F$ deux espaces vectoriels sur un même corps $\mathbb{K}$.

**Théorème de la construction d'une application linéaire.** Soient $E$ de dimension finie $n$ et $\left( e_1, \ldots{}, e_n \right)$ une base de $E$, alors pour tout choix $\left( v_1, v_2, \ldots{}, v_n \right)$ de $n$ vecteurs de $F$, il existe une et une seule application linéaire $f : E \rightarrow F$ telle que pour tout $i = 1, \ldots{}, n$.

$f \left( e_i \right) = v_i$

#### Rang d'une application linéaire

**Proposition.** Soit $f : E \rightarrow F$ une application linéaire :

$\mathrm{Im } f = f \left( E \right) = \left\lbrace f \left( x \right) \backslash x \in E \right\rbrace$

$\mathrm{Im } f$ est l'image de $f$. Si $E$ est de dimension finie alors :

- $\mathrm{Im } f = f \left( E \right)$ est un espace vectoriel de dimension finie.

- Si $\left( e_1, \ldots{}, e_n \right)$ est une base de $E$, alors

$\mathrm{Im } f = \mathrm{Vect} \left( f \left( e_1 \right), \ldots{}, f \left( e_n \right) \right)$

La dimension de cet espace vectoriel $\mathrm{Im } f$ est appelée **rang de $f$**.

$\mathrm{rg} \left( f \right) = \dim \left( \mathrm{Im } f \right) = \dim \left( \mathrm{Vect} \left( f \left( e_1 \right), f \left( e_2 \right), \ldots{}, f \left( e_n \right) \right) \right)$

**Proposition.** Si $E$ et $F$ sont de dimension finie, alors

$\mathrm{rg} \left( f \right) \leq \min \left( \dim E, \dim F \right)$

**Exemple.** Calcul du rang de $F$ :

$f : \left\lbrace \begin{array}{l} \mathbb{R}^3 \rightarrow \mathbb{R}^2 \\ \left( x, y, z \right) \mapsto \left\lbrace \begin{array}{l} 3x - 4y - 2z \\ 2x - 3y - z \end{array} \right.  \end{array} \right.$

On pose la base canonique $\left( e_1, e_2, e_3 \right)$ de $\mathbb{R}^3$.

$e_1 = \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right)$

$e_2 = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right)$

$e_3 = \left( \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right)$

On calcule l'image des trois vecteurs canoniques :

$f \left( e_1 \right) = \left( \begin{array}{c} 3 \\ 2 \end{array} \right)$

$f \left( e_2 \right) = \left( \begin{array}{c} -4 \\ -3 \end{array} \right)$

$f \left( e_3 \right) = \left( \begin{array}{c} 2 \\ -1 \end{array} \right)$

On pose $A = \left( \begin{array}{ccc} 3 & -4 & 2 \\ 2 & -3 & -1 \end{array} \right)$.

$\mathrm{rg } f = \mathrm{rg } A = 2$

#### Théorème du rang

$f : E \rightarrow F$ est une application linéaire entre deux $\mathbb{K}$-espaces vectoriels.

$E$ est de dimension finie.

Le **noyau** de $f$ est $\ker f = \left\lbrace x \in E \backslash f \left( x \right) = 0_F \right\rbrace$.

L'**image** de $f$ est $\mathrm{Im } f = f \left( E \right) = \left\lbrace f \left( x \right) \backslash x \in E \right\rbrace$.

**Théorème du rang.** $\dim E = \dim \left( \ker f \right)  + \dim \left( \mathrm{Im } f \right)$

$\dim E = \dim \left( \ker f \right)  + \mathrm{rg } f$

**Exemple.** $f : \left\lbrace \begin{array}{l} \mathbb{R}^4 \rightarrow \mathbb{R}^3 \\ \left( x_1, x_2, x_3, x_4 \right) \mapsto \left\lbrace \begin{array}{l} x_1 - x_2 + x_3 \\ 2 x_1 + 2 x_2 + 6 x_3 + 4 x_4 \\ -x_1 - 2 x_3 - x_4 \end{array} \right. \end{array} \right.$

- **Première méthode : calculer le noyau.** $\left( x_1, x_2, x_3, x_4 \right) \in \ker f$

$\begin{array}{cl} \Leftrightarrow & f \left( x_1, x_2, x_3, x_4 \right) = \left( 0, 0, 0 \right) \\ \Leftrightarrow & \left\lbrace \begin{array}{l} x_1 - x_2 + x_3 = 0 \\ 2 x_1 + 2 x_2 + 6 x_3 +4 x_4 = 0 \\ -x_1 - 2 x_3 - x_4 = 0 \end{array} \right. \\ \Leftrightarrow & \left\lbrace \begin{array}{l} x_1 - x_2 + x_3 = 0 \\ x_2 + x_3 + x_4 = 0 \end{array} \right. \\ \end{array}$

On choisit $x_3$ et $x_4$ comme paramètres :

$\begin{array}{l} \ker f = \left\lbrace \left( -2 x_3 - x_4, -x_3 - x_4, x_3, x_4 \right) \backslash x_3, x_4 \in \mathbb{R} \right\rbrace \\ \ker f = \left\lbrace \left( x_3 \left( \begin{array}{c} -2 \\ -1 \\ 1 \\ 0 \end{array} \right) + x_4 \left( \begin{array}{c} -1 \\ -1 \\ 0 \\ 1 \end{array} \right) \right) \backslash x_3, x_4 \in \mathbb{R} \right\rbrace \\ \ker f = \mathrm{Vect} \left( \left( \begin{array}{c} -2 \\ -1 \\ 1 \\ 0 \end{array} \right), \left( \begin{array}{c} -1 \\ -1 \\ 0 \\ 1 \end{array} \right) \right) \\ \dim \left( \ker f \right) = 2 \\ \Rightarrow \dim \left( \mathrm{Im } f \right) = 4 - 2 = 2 = \mathrm{rg} f \end{array}$

- **Seconde méthode : calculer l'image.** Soit $\left( e_1, e_2, e_3, e_4 \right)$ la base canonique de $\mathbb{R}^4$.

$\begin{array}{l} v_1 = f \left( e_1 \right) = \left( \begin{array}{c} 1 \\ -2 \\ -1 \end{array} \right) \\ v_2 = f \left( e_2 \right) = \left( \begin{array}{c} -1 \\ 2 \\ 0 \end{array} \right) \\ v_3 = f \left( e_3 \right) = \left( \begin{array}{c} 1 \\ 6 \\ -2 \end{array} \right) \\ v_4 = f \left( e_4 \right) = \left( \begin{array}{c} 0 \\ 4 \\ -1 \end{array} \right) \end{array}$

$A = \left( \begin{array}{cccc} 1 & -1 & 1 & 0 \\ 2 & 2 & 6 & 4 \\ -1 & 0 & -2 & -1 \end{array} \right) \sim \left( \begin{array}{cccc} 1 & 0 & 0 & 0 \\ 2 & 4 & 0 & 0 \\ -1 & -1 & 0 & 0 \end{array} \right)$

$\mathrm{rg} A = 2$

$\mathrm{rg} f = \dim \left( \mathrm{Im} f \right) = 2$

$\Rightarrow \dim \left( \ker \left( f \right) \right) = \dim \mathbb{R}^4 - \mathrm{rg} f = 4 - 2 = 2$

#### Entre espaces de même dimension

Un **isomorphisme** est une application linéaire bijective.

**Proposition.** Si $f : E \rightarrow F$ un isomorphisme entre espaces vectoriels de dimension finie, alors :

$\dim E = \dim F$

**Théorème.** Soit $f : E \rightarrow F$ une application linéaire où $E$ et $F$ de dimension finie. Si $\dim E = \dim F$, alors les assertions suivantes sont équivalentes :

1. $f$ est bijective ;

2. $f$ est injective ;

3. $f$ est surjective.

### Matrice d'une application linéaire

#### Matrice associée à une application

Soient $E$ et $F$ deux $\mathbb{K}$-espaces vectoriels de dimension finie, $\mathcal{B} = \left( e_1, \ldots{}, e_p \right)$ une base de $E$ avec $p$ sa dimension, $\mathcal{B}' = \left( f_1, \ldots{}, f_n \right)$ une base de $F$ avec $n$ sa dimension, et $f : E \rightarrow F$ une application linéaire :

1. $f$ est déterminée de manière unique par l'image d'une base de $E$, donc par les vecteurs $f \left( e_1 \right), \ldots{}, f \left( e_p \right)$.

2. Pour $j \in \left[ 1, p \right]$, $f \left( e_j \right)$ se décompose de manière unique comme une combinaison linéaire dans la base $\mathbb{B}'$.

3. Il existe $n$ scalaires uniques $a_{1,j}, a_{2,j}, \ldots{}, a_{n,j} \in \mathbb{K}$ tels que :

$f \left( e_j \right) = a_{1,j} f_1 + a_{2,j} f_2 + \ldots{} + a_{n,j} f_n = {\left( \begin{array}{c} a_{1,j} \\ \ldots{} \\ a_{n,j} \end{array} \right) }_{\mathbb{B}'}$ 

L'application linéaire $f$ est entièrement déterminée par les $f \left( e_j \right)$.

**Définition.** La matrice de $f$ par rapport aux bases $\mathcal{B}$ et $\mathcal{B}'$ est la matrice $\left( a_{ij} \right) \in M_{n,p} \left( \mathbb{K} \right)$

${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( f \right) = \begin{array}{cccc}  &  & \begin{array}{cccccc} f \left( e_1 \right) & f \left( e_2 \right) & \ldots{} & f \left( e_j \right) & \ldots{} & f \left( e_p \right) \end{array} &  \\ \begin{array}{c} f_1 \\ f_2 \\ \ldots{} \\ f_n \end{array} & \left( \begin{array}{c} \\  \\ \\  \end{array} \right. & \begin{array}{cccccc} a_{11} & a_{12} & \ldots{} & a_{1j} & \ldots{} & a_{1p} \\ a_{21} & a_{22} & \ldots{} & a_{2j} & \ldots{} & a_{2p} \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ a_{n1} & a_{n2} & \ldots{} & a_{nj} & \ldots{} & a_{np} \end{array} & \left. \begin{array}{c} \\  \\ \\  \end{array} \right) \end{array}$

${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}$ se lit « matrice de $f$ par rapport aux bases $\mathcal{B}$ et $\mathcal{B}'$ ».

- La $j$-ème colonne est constituée des coordonnées du vecteur $f \left( e_j \right)$ dans la base $\mathcal{B}' = \left( f_1, f_2, \ldots{}, f_n \right)$.

- Les vecteurs colonnes sont l'image par $f$ des vecteurs de la base de départ $\mathcal{B}$, exprimée dans la base d'arrivée $\mathcal{B}'$.

- La taille de ${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}$ dépend uniquement de la taille de l'espace de départ et de l'espace d'arrivée.

- Les coefficients de ${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}$ dépendent du choix de base $\mathcal{B}$ de $E$ et de la base $\mathcal{B}'$ de $F$.

**Exemple.** $f : \left\lbrace \begin{array}{l} \mathbb{R}^3 \rightarrow \mathbb{R}^2 \\ \left( x_1, x_2, x_3 \right) \mapsto \left( x_1 + x_2 - x_3, x_1 - 2 x_2 + 3 x_3 \right) \end{array} \right.$

- On pose $\mathcal{B} = \left( e_1, e_2, e_3 \right)$ la base canonique de $\mathbb{R}^3$. On pose $\mathcal{B}' = \left( f_1, f_2 \right)$ la base canonique de $\mathbb{R}^2$.

$e_1 = \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right)$

$e_2 = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right)$

$e_3 = \left( \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right)$

$f_1 = \left( \begin{array}{c} 1 \\ 0 \end{array} \right)$

$f_2 = \left( \begin{array}{c} 0 \\ 1 \end{array} \right)$

Pour trouver la matrice $f$ dans les bases $\mathcal{B}$ et $\mathcal{B}'$, on calcule les images de $e_1$, $e_2$ et $e_3$.

$\begin{array}{l} f \left( e_1 \right) = f \left( 1, 0, 0 \right) = \left( 1, 1 \right) = f_1 + f_2 \\ f \left( e_2 \right) = f \left( 0, 1, 0 \right) = \left( 1, -2 \right) = f_1 - 2 f_2 \\ f \left( e_3 \right) = f \left( 0, 0, 1 \right) = \left( -1, 3 \right) = -f_1 + 3 f_2  \end{array}$

${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} = \begin{array}{cccc} &  & \begin{array}{ccc} f \left( x_1 \right) & f \left( x_2 \right) & f \left( x_3 \right) \end{array} &  \\ \begin{array}{c} f_1 \\ f_2 \end{array} & \left( \begin{array}{c} \\  \\ \\  \end{array} \right. & \begin{array}{ccc} 1 & 1 & -1 \\ 1 & -2 & 3 \end{array} & \left. \begin{array}{c} \\  \\ \\  \end{array} \right) \end{array}$

- On peut échanger les bases de départ et d'arrivée.

${\varepsilon}_1 = \left( \begin{array}{c} 1 \\ 1 \\ 0 \end{array} \right)$

${\varepsilon}_2 = \left( \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right)$

${\varepsilon}_3 = \left( \begin{array}{c} 0 \\ 1 \\ 1 \end{array} \right)$

${\phi}_1 = \left( \begin{array}{c} 1 \\ 0 \end{array} \right)$

${\phi}_2 = \left( \begin{array}{c} 0 \\ 1 \end{array} \right)$

Soient la nouvelle base de départ ${\mathcal{B}}_0 = \left( {\varepsilon}_1, {\varepsilon}_2, {\varepsilon}_3 \right)$ et la nouvelle base d'arrivée ${\mathcal{B}'}_0 = \left( {\phi}_1, {\phi}_2 \right)$, on calcule :

$\begin{array}{l} f \left( {\varepsilon}_1 \right) = f \left( 1, 1, 0 \right) = \left( 2, -1 \right) = 3 {\phi}_1 - {\phi}_2 \\ f \left( {\varepsilon}_2 \right) = f \left( 1, 0, 1 \right) = \left( 0, 4 \right) = -4 {\phi}_1 + 4 {\phi}_2 \\ f \left( {\varepsilon}_3 \right) = f \left( 0, 1, 1 \right) = \left( 0, 1 \right) = -{\phi}_1 + {\phi}_2  \end{array}$

${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} = \begin{array}{cccc} &  & \begin{array}{ccc} f \left( {\varepsilon}_1 \right) & f \left( {\varepsilon}_2 \right) & f \left( {\varepsilon}_3 \right) \end{array} &  \\ \begin{array}{c} {\phi}_1 \\ {\phi}_2 \end{array} & \left( \begin{array}{c} \\  \\ \\  \end{array} \right. & \begin{array}{ccc} 3 & -4 & -1 \\ -1 & 4 & 1 \end{array} & \left. \begin{array}{c} \\  \\ \\  \end{array} \right) \end{array}$

La matrice de $f$ dépend du choix des bases.

#### Opérations sur les applications linéaires et les matrices

Soient $f, g : E \rightarrow F$ deux applications linéaire, $\mathcal{B}$ une base de $E$, et $\mathcal{B}'$ une base de $F$.

- **Proposition 1.** ${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( f + g \right) = {\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( f \right) + {\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( g \right)$

- **Proposition 2.** ${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( {\lambda} f \right) = {\lambda} {\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( f \right)$

- **Proposition : composition des applications linéaires.** Soient $f : E \rightarrow F$ et $g : F \rightarrow G$ deux applications linéaires, $\mathcal{B}$ une base de $E$, $\mathcal{B}'$ une base de $F$ et $\mathcal{B}"$ une base de $G$, alors :

${\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}"} \left( g \circ f \right) = {\mathrm{Mat}}_{\mathcal{B}', \mathcal{B}"} \left( g \right) \times {\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'} \left( f \right)$

Le produit matriciel correspond ainsi à la composition deux applications linéaires.

#### Matrice d'un endomorphisme

Dans un endomorphisme, l'espace d'arrivée et l'espace de départ sont identiques : $f : E \rightarrow E$. On pose une base identique $\mathcal{B}$ pour les deux ensembles de départ et d'arrivée : ${{\mathrm{Mat}}_{\mathcal{B}}} \left( f \right)$, ce qui se lit « matrice de $f$ dans $\mathcal{B}$ ».

> [!NOTE]
> Il est possible de poser deux bases distinctes $\mathcal{B}$ et $\mathcal{B}'$.

Exemples d'applications endomorphiques :

- L'identité $\mathrm{id} : \left\lbrace \begin{array}{l} E \rightarrow E \\ x \mapsto \mathrm{id} \left( x \right) = x \end{array} \right.$ a pour matrice associée : ${{\mathrm{Mat}}_{\mathcal{B}}} \left( \mathrm{id} \right) = I_n$.

- L'homothétie $h_{\lambda} : \left\lbrace \begin{array}{l} E \rightarrow E \\ x \mapsto h_{\lambda} \left( x \right) = {\lambda}x \end{array} \right.$ a pour matrice associée : ${{\mathrm{Mat}}_{\mathcal{B}}} \left( h_{\lambda} \right) = {\lambda} I_n$.

- La symétrie centrale $s : \left\lbrace \begin{array}{l} E \rightarrow E \\ x \mapsto s \left( x \right) = -x \end{array} \right.$ a pour matrice associée : ${{\mathrm{Mat}}_{\mathcal{B}}} \left( s \right) = -I_n$.

- La rotation d'angle $\theta$ centrée à l'origine 

$r_{\theta} : \left\lbrace \begin{array}{l} \mathbb{R}^2 \rightarrow \mathbb{R}^2 \\ \left( x, y \right) \mapsto r_{\theta} \left( x, y \right) = \left( x \cos \theta - y \sin \theta, x \sin \theta + y \cos \theta \right) \end{array} \right.$

avec $\mathbb{R}^2$ muni de la base canonique $\mathcal{B}$ a pour matrice associée : ${{\mathrm{Mat}}_{\mathcal{B}}} \left( r_{\theta} \right) = \left( \begin{array}{cc} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{array} \right)$.

**Corollaire.** Soient $E$ un espace vectoriel de dimension finie, $f : E \rightarrow E$ une application linéaire et $\mathcal{B}$ une base de $E$ :

$\forall p \in \mathbb{N}, {{\mathrm{Mat}}_{\mathcal{B}}} \left( f^p \right) = \left( {{\mathrm{Mat}}_{\mathcal{B}}} \left( f \right) \right)^p$

#### Matrice d'un isomorphisme

$f : E \rightarrow F$ est une application linéaire bijective.

Soient $E$ et $F$ deux espaces vectoriels de même dimension finie, $f : E \rightarrow F$ une application linéaire, $\mathcal{B}$ une base de $E$ et $\mathcal{B}'$ une base de $F$, $A = {{\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}} \left( f \right)$.

**Théorème.** $f$ est bijective. $\Leftrightarrow$ La matrice associée $A$ est inversible.

- $f : E \rightarrow F$ est bijective. $\Rightarrow$ La matrice $f^{-1} : F \rightarrow E$ est la matrice $A^{-1}$.

- ${{\mathrm{Mat}}_{\mathcal{B}', \mathcal{B}}} \left( f^{-1} \right) = \left( {{\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}} \left( f \right) \right)^{-1}$.

$f : E \rightarrow E$, $\mathcal{B}$ est la même base de départ et d'arrivée, et $A = {{\mathrm{Mat}}_{\mathcal{B}}} \left( f \right)$.

**Corollaire.** $f$ est bijective. $\Leftrightarrow$ La matrice associée $A$ est inversible.

- $f$ est bijective. $\Rightarrow$ La matrice associée à $f^{-1}$ dans la base $\mathcal{B}$ est $A^{-1}$.

- ${{\mathrm{Mat}}_{\mathcal{B}}} \left( f^{-1} \right) = \left( {{\mathrm{Mat}}_{\mathcal{B}}} \left( f \right) \right)^{-1}$.

### Changement de bases

#### Application linéaire, matrice, vecteur

Soient $E$ un espace vectoriel de dimension finie, $\mathcal{B} = \left( e_1, e_2, \ldots{}, e_p \right)$ une base de $E$, pour $x \in E$, $x = x_1 e_1 + \ldots{} + x_p e_p$.

La matrice de $x$ dans $\mathcal{B}$ est ${{\mathrm{Mat}}_{\mathcal{B}}} \left( x \right) = {\left( \begin{array}{c} x_1 \\ x_2 \\ \ldots{} \\ x_p \end{array} \right)}_{\mathcal{B}}$.

**Proposition.** On pose $f : \left\lbrace \begin{array}{l} E \rightarrow F \\ x \mapsto f \left( x \right) = y \end{array} \right.$, $\mathcal{B}$ la base de $E$ et $\mathcal{B}'$ la base de $F$. On note $A = {{\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}} \left( f \right)$. On note un vecteur $x$ de $E$ :

$X = {{\mathrm{Mat}}_{\mathcal{B}}} \left( x \right) = {\left( \begin{array}{c} x_1 \\ x_2 \\ \ldots{} \\ x_p \end{array} \right)}_{\mathcal{B}}$

et un vecteur $y$ de $F$ :

$Y = {{\mathrm{Mat}}_{\mathcal{B}'}} \left( y \right) = {\left( \begin{array}{c} y_1 \\ y_2 \\ \ldots{} \\ y_n \end{array} \right)}_{\mathcal{B}'}$

si $y = f \left( x \right)$ on a alors :

$Y = A.X$

${{\mathrm{Mat}}_{\mathcal{B}'}} \left( f \left( x \right) \right) = {{\mathrm{Mat}}_{\mathcal{B}, \mathcal{B}'}} \left( f \right) \times {{\mathrm{Mat}}_{\mathcal{B}}} \left( x \right)$

#### Matrice de passage d'une base à l'autre

Soient $E$ un espace vectoriel de dimension $n$, $\mathcal{B}$ et $\mathcal{B}'$ deux bases de $E$.

- **Définition.** La **matrice de passage** de la base $\mathcal{B}$ vers la base $\mathcal{B}'$, notée $P_{\mathcal{B}, \mathcal{B}'}$ et se lisant « $\mathcal{B}$ vers $\mathcal{B}'$ », est la matrice dont la j-ème colonne est formée des coordonnées du j-ème vecteur de la base $\mathcal{B}'$ par rapport à la base $\mathcal{B}$. Dit autrement, la matrice de passage $P_{\mathcal{B}, \mathcal{B}'}$ est constituée – en colonne – des coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ exprimés dans l'ancienne base $\mathcal{B}$.

- **Proposition 1.** La matrice de passage $P_{\mathcal{B}, \mathcal{B}'}$ est la matrice associée à l'identité ${\mathrm{id}}_E : \left( E, \mathcal{B}' \right) \rightarrow \left( E, \mathcal{B} \right)$.

$P_{\mathcal{B}, \mathcal{B}'} = {{\mathrm{Mat}}_{\mathcal{B}', \mathcal{B}}} \left( {\mathrm{id}}_E \right)$

- **Proposition 2.** Une matrice de passage est inversible

$P_{\mathcal{B}', \mathcal{B}} = \left( P_{\mathcal{B}, \mathcal{B}'} \right)^{-1}$

- **Proposition 3.** Si $\mathcal{B}$, $\mathcal{B}'$, $\mathcal{B}"$ sont trois bases, alors :

$P_{\mathcal{B}, \mathcal{B}"} = P_{\mathcal{B}, \mathcal{B}'} \times P_{\mathcal{B}', \mathcal{B}"}$

###### Effet du changement de base sur les coordonnées d'un vecteur

Soient $\mathcal{B} = \left( e_1, e_2, \ldots{}, e_n \right)$ et $\mathcal{B}' = \left( {e'}_1, {e'}_2, \ldots{}, {e'}_n \right)$ deux bases de $E$, $P_{\mathcal{B}, \mathcal{B}'}$ la matrice de passage de la base $\mathcal{B}$ vers la base $\mathcal{B}'$, pour $x \in E, x = \sum_{i = 1}^{n} x_i e_i$.

On note $X = {{\mathrm{Mat}}_{\mathcal{B}}} \left( x \right) = {\left( \begin{array}{c} x_1 \\ x_2 \\ \ldots{} \\ x_n \end{array} \right)}_{\mathcal{B}}$.

$x$ s'écrit aussi : $x' = \sum_{i = 1}^{n} {x'}_i {e'}_i$. On note $X' = {{\mathrm{Mat}}_{\mathcal{B}'}} \left( x' \right) = {\left( \begin{array}{c} {x'}_1 \\ {x'}_2 \\ \ldots{} \\ {x'}_n \end{array} \right)}_{\mathcal{B}'}$.

**Proposition.** $X = P_{\mathcal{B}, \mathcal{B}'} .X'$ et $X' = \left( P_{\mathcal{B}, \mathcal{B}'} \right)^{-1} .X$.

#### Formule de changement de base

Dans le cas d'un endomorphisme, soient $f : E \rightarrow E$ une application linéaire, deux bases $\mathcal{B}$ et $\mathcal{B}'$ de $E$, la matrice de l'application $f$ dans la base $\mathcal{B}$ $A = {{\mathrm{Mat}}_{\mathcal{B}}} \left( f \right)$, on pose $B = {{\mathrm{Mat}}_{\mathcal{B}'}} \left( f \right)$ la matrice de l'application $f$ dans la base $\mathcal{B}'$, et $P = {P_{\mathcal{B}, \mathcal{B}'}}$ la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$.

**Théorème.** $B = P^{-1} .A.P$.

Soient deux matrices carrées $A$ et $B$ de taille $n$ :

$M_n \left( \mathbb{K} \right)$

- **Définition.** $B$ est **semblable** à la matrice $A$ s'il existe une matrice inversible $P \in M_n \left( \mathbb{K} \right)$ telle que $B = P^{-1} .A.P$.

- **Propositions.** « Être semblable » est une relation d'équivalence.

1. La **réfléxivité.** Une matrice $A$ est semblable à elle-même.

2. La **symétrie.** Si $A$ est semblable à $B$, alors $B$ est semblable à $A$.

3. La **transitivité.** Si $A$ est semblable à $B$, et Si $B$ est semblable à $C$, alors Si $A$ est semblable à $C$. 

- **Corollaire** Deux matrices semblables représentent le même endomorphisme, mais exprimé dans des bases différentes.

#### Méthode pour opérer un changement de base

Dans $\mathbb{R}^2$, on considère $e_1 = \left( \begin{array}{c} 1 \\ 0 \end{array} \right)$, $e_2 = \left( \begin{array}{c} 1 \\ 1 \end{array} \right)$, ${\varepsilon}_1 = \left( \begin{array}{c} 1 \\ 2 \end{array} \right)$, et ${\varepsilon}_2 = \left( \begin{array}{c} 5 \\ 4 \end{array} \right)$. On pose deux bases $\mathcal{B} = \left( e_1, e_2 \right)$ et $\mathcal{B}' = \left( {e'}_1, {e'}_2 \right)$. Pour trouver la matrice de passage de la base $\mathcal{B}$ vers la base $\mathcal{B}'$, il faut exprimer ${\varepsilon}_1$ et ${\varepsilon}_2$ en fonction de $\left( e_1, e_2 \right)$. 

${\varepsilon}_1 = -e_1 + 2 e_2 = {\left( \begin{array}{c} -1 \\ 2 \end{array} \right)}_{\mathcal{B}}$

et

${\varepsilon}_2 = e_1 + 4 e_2 = {\left( \begin{array}{c} 1 \\ 4 \end{array} \right)}_{\mathcal{B}}$

La matrice de passage est :

${P_{\mathcal{B}, \mathcal{B}'}} = \left( \begin{array}{cc}-1 & 1 \\2 & 4\end{array} \right)$

De même

$e_1 = -\frac{2}{3} {\varepsilon}_1 + \frac{1}{3} {\varepsilon}_2 = {\left( \begin{array}{c} -\frac{2}{3} \\ \frac{1}{3} \end{array} \right)}_{\mathcal{B}}$

et

$e_2 = \frac{1}{6} {\varepsilon}_1 + \frac{1}{6} {\varepsilon}_2 = {\left( \begin{array}{c} \frac{1}{6} \\ \frac{1}{6} \end{array} \right)}_{\mathcal{B}}$

La matrice de passage est :

${P_{\mathcal{B}', \mathcal{B}}} = \left( \begin{array}{cc}-\frac{2}{3} & \frac{1}{3} \\\frac{1}{6} & \frac{1}{6}\end{array} \right)$

## Déterminants

Le déterminant est un **nombre** associé à une matrice carrée qui permet de savoir si la matrice est inversible (ou non). De manière générale, il joue un rôle important dans la résolution des systèmes linéaires.

### Dimensions 2 et 3

Soit un corps $\mathbb{K} \left( \mathbb{R} \textrm{ ou } \mathbb{C} \right)$.

#### Matrice $2 \times 2$

$\det{\left( \begin{array}{cc} a & b \\ c & d \end{array} \right)} = ad - bc$

#### Matrice $3 \times 3$

Soit $A = \left[ \begin{array}{ccc} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{array} \right]$, alors :

$\det A = a_{11} a_{22} a_{33} + a_{12} a_{23} a_{31} +a_{13} a_{21} a_{32} - a_{31} a_{22} a_{13} - a_{32} a_{23} a_{11} - a_{33} a_{21} a_{12}$

Pour les matrices $3 \times 3$, on peut appliquer la **règle de Sarrus**[^3]. Elle consiste à reproduire les deux premères colonne de la matrice $A$ en fin de celle-ci. Le produit des éléments des diagonales contenant trois éléments en partant de la gauche vers la droite fournit les coefficients ayant une valeur positive (en rouge), tandis que le produit des éléments des diagonales contenant trois éléments en partant de la droite vers la gauche fournit les coefficients ayant une valeur négative (en vert).

$\left[ \begin{array}{ccccc} \textcolor{red}{a_{11}} & \textcolor{red}{a_{12}} & \textcolor{red}{a_{13}} & a_{11} & a_{12} \\ a_{21} & \textcolor{red}{a_{22}} & \textcolor{red}{a_{23}} & \textcolor{red}{a_{21}} & a_{22} \\ a_{31} & a_{32} & \textcolor{red}{a_{33}} & \textcolor{red}{a_{31}} & \textcolor{red}{a_{32}}\end{array} \right]$

$\left[ \begin{array}{ccccc} a_{11} & a_{12} & \textcolor{green}{a_{13}} & \textcolor{green}{a_{11}} & \textcolor{green}{a_{12}} \\ a_{21} & \textcolor{green}{a_{22}} & \textcolor{green}{a_{23}} & \textcolor{green}{a_{21}} & a_{22} \\ \textcolor{green}{a_{31}} & \textcolor{green}{a_{32}} & \textcolor{green}{a_{33}} & a_{31} & a_{32}\end{array} \right]$

#### Interprétation géométrique du déterminant

Pour une matrice $2 \times 2$, le déterminant est l'aire du parallélogramme formée par deux vecteurs $v_1 = \left( \begin{array}{c} a \\ c \end{array} \right)$ et $v_2 = \left( \begin{array}{c} b \\ d \end{array} \right)$ du plan $\mathbb{R}^2$.

**Proposition.** L'aire du parallélogramme est égale à la valeur absolue du déterminant.

$\mathcal{A} = \left| \det \left( v_1, v_2 \right) \right| = \left| \det \left( \begin{array}{cc} a & b \\ c & d \end{array} \right) \right| = \left| ad - bc \right|$

Une unité d'aire dans $\mathbb{R}^2$ est une aire du carré unité.

Pour une matrice $3 \times 3$, le déterminant est le volume d'un parallépipède, obtenu par trois vecteurs $v_1 = \left( \begin{array}{c} a_{11} \\ a_{21} \\ a_{31} \end{array} \right)$, $v_2 = \left( \begin{array}{c} a_{12} \\ a_{22} \\ a_{32} \end{array} \right)$ et $v_3 = \left( \begin{array}{c} a_{13} \\ a_{23} \\ a_{33} \end{array} \right)$ du volume $\mathbb{R}^3$.

**Proposition.** Le volume du parallépipède est égal à la valeur absolue du déterminant.

$\mathcal{V} = \left| \det \left( v_1, v_2, v_3 \right) \right|$

Une unité de volume dans $\mathbb{R}^3$ est un volume du cube unité.

Si $\det A = 0$, alors les vecteurs sont colinéaires.

### Définition générale du déterminant

Le déterminant est une application qui, à une matrice carrée, associe un scalaire : $\det : M_n \left( \mathbb{K} \right) \rightarrow \mathbb{K}$.

**Théorème.** Il existe une unique application $M_n \left( \mathbb{K} \right)$ dans $\mathbb{K}$, appelée **déterminant** telle que :

1. le déterminant est linéaire par rapport à chaque vecteur colonne, les autres étant fixés ;

2. si une matrice $A$ a deux colonnes identiques, alors son déterminant est nul ;

3. le déterminant de la matrice identité $I_n$ vaut $1$.

> [!NOTE]
> Une application satisfaisant le point 1. est appelée **forme multilinéaire**.

> [!NOTE]
>  Si elle satisfait le point 2., on dit qu'elle est **alternée**.

On note le déterminant d'une matrice $A = \left( a_{ij} \right)$ par :

$\det A$

et

$\left| \begin{array}{cccc}a_{11} & a_{12} & \ldots{} & a_{1n} \\a_{21} & a_{22} & \ldots{} & a_{2n} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{n1} & a_{n2} & \ldots{} & a_{nn} \\\end{array} \right|$

Si on note $C_i$ la $i$-ème colonne de $A$, alors :

$\det A = \left| \begin{array}{cccc} C_1 & C_2 & \ldots{} & C_n \end{array} \right| = \det \left( C_1, C_2, \ldots{}, C_n \right)$

La propriété du point 1. s'écrit :

$\begin{array}{l}\det \left( C_1, C_2, \ldots{}, {\lambda}C_j + {\mu}{C'}_j, \ldots{}, C_n \right) \\= {\lambda} \det \left( C_1, C_2, \ldots{}, C_j, \ldots{}, C_n \right) + {\mu} \det \left( C_1, C_2, \ldots{}, {C'}_j, \ldots{}, C_n \right) \end{array}$

c'est-à-dire

$\begin{array}{l}\left| \begin{array}{ccccc}a_{11} & \ldots{} & {\lambda}a_{1j} + {\mu}{a'}_{1j} & \ldots{} & a_{1n} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{i1} & \ldots{} & {\lambda}a_{ij} + {\mu}{a'}_{ij} & \ldots{} & a_{in} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{n1} & \ldots{} & {\lambda}a_{nj} + {\mu}{a'}_{nj} & \ldots{} & a_{nn} \end{array} \right| \\= {\lambda} \left| \begin{array}{ccccc}a_{11} & \ldots{} & a_{1j} & \ldots{} & a_{1n} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{i1} & \ldots{} & a_{ij} & \ldots{} & a_{in} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{n1} & \ldots{} & a_{nj} & \ldots{} & a_{nn} \end{array} \right| + {\mu} \left| \begin{array}{ccccc}a_{11} & \ldots{} & {a'}_{1j} & \ldots{} & a_{1n} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{i1} & \ldots{} & {a'}_{ij} & \ldots{} & a_{in} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{n1} & \ldots{} & {a'}_{nj} & \ldots{} & a_{nn} \end{array}  \right|\end{array}$

- **Exemple 1.** La deuxième colonne est un multiple de $5$.

$\left| \begin{array}{ccc} 6 & 5 & 4 \\ 7 & -10 & -3 \\ 12 & 25 & -1 \end{array} \right| = 5 \times \left| \begin{array}{ccc} 6 & 1 & 4 \\ 7 & -2 & -3 \\ 12 & 5 & -1 \end{array} \right|$

- **Exemple 2.** La troisième colonne est une soustraction

$\left| \begin{array}{ccc} 3 & 2 & 4 - 3 \\ 7 & -5 & 3 - 2 \\ 9 & 2 & 10 - 4 \end{array} \right| = \left| \begin{array}{ccc} 3 & 2 & 4 \\ 7 & -5 & 3 \\ 9 & 2 & 10 \end{array} \right| -\left| \begin{array}{ccc} 3 & 2 & 3 \\ 7 & -5 & 2 \\ 9 & 2 & 4 \end{array} \right|$

#### Première propriétés

- **Propriété 1.** $\det 0_n = 0$.

- **Propriété 2.** $\det I_n = 1$.

- **Proposition.** Soient $A = \left( C_1, C_2, \ldots{}, C_n \right) \in M_n \left( \mathbb{K} \right)$ et $A' \in M_n \left( \mathbb{K} \right)$ obtenue par opération élémentaire sur les colonnes.
    
    1. Si $C_i \leftarrow {\lambda} C_i$ avec $\lambda \neq 0$, alors $\det A' = {\lambda} \det A$.
    
    2. Si $C_i \leftarrow C_i + {\lambda} C_j$ avec $\lambda \in \mathbb{K}$ et $j \neq i$, alors $\det A' = \det A$. Plus généralement, $C_i \leftarrow C_i \sum_{i = 1}^{n} {\lambda}_j C_j$ conserve le déterminant.
    3. Si $C_i \leftrightarrow C_j$ alors $\det A' = -\det A$.

**Corollaire.** Si une colonne de $A$ est combinaison linéaire des autres, alors $\det A = 0$.

**Proposition.** Le déterminant d'une matrice triangulaire supérieure (ou inférieure) est égal au produit des termes diagonaux.

**Corollaire.** Le déterminant d'une matrice diagonale est égal au produit des termes diagonaux.

#### Démonstration de l'existence du déterminant

Il s'agit de poser les bases de cette démonstration. L'unicité du déterminant est admise.

Pour $A \in M_n \left( \mathbb{K} \right)$, on note $A_{ij}$ la matrice obtenue en supprimant la i-ème ligne et la j-ème colonne de $A$.

**Théorème.** Les formules suivantes définissent par récurrence pour $n \geq 1$, l'application déterminant de $M_n \left( \mathbb{K} \right)$ dans $\mathbb{K}$ qui satisfait aux trois propriétés de la définition du déterminant.

1. Le déterminant d'une matrice $1 \times 1$. Si $A = \left( a \right)$, alors $\det A = a$.

2. La formule de récurrence. Si $A = \left( a_{ij} \right) \in M_n \left( \mathbb{K} \right)$, alors pour tout $i$ :

$\det A = \left( -1 \right)^{i + 1} a_{i1} \det A_{i1} + \ldots{} + \left( -1 \right)^{i + n} a_{in}$


**Le déterminant peut se concevoir comme une généralisation à l'espace de dimension $n$ de la notion d'aire et de volume orientés**.

### Propriétés du déterminant

#### Déterminant et matrices élémentaires

À chaque opération élémentaire, on associe une matrice $E_1$ dite élémentaire telle que $A' = A \times E$.

1. $C_i \leftarrow {\lambda} C_i$ avec $\lambda \neq 0$

$E_{C_i \leftarrow {\lambda} C_i} = \mathrm{diag} \left( 1, \ldots{}, 1, \lambda, 1 \ldots{}, 1 \right)$

$\lambda$ se situe dans la colonne $i$.

2. $C_i \leftarrow C_i + {\lambda} C_j$ avec $\lambda \in \mathbb{K}$ et $j \neq i$.

$E_{C_i \leftarrow C_i + {\lambda} C_j} = \left( \begin{array}{ccccc} 1 & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \lambda & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & 1 & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & 1 \end{array} \right)$

$\lambda$ se situe dans la case $ij$.

3. $C_i \leftrightarrow C_j$

$E_{C_i \leftrightarrow C_j} = \left( \begin{array}{cccccccc} 1 & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & 1 & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & 0 & \ldots{} & 1 & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & 1 & \ldots{} & 0 & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & 1 & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & 1 \end{array} \right)$

Les cases $ii$ et $jj$ valent $0$. Les cases $ij$ et $ji$ valent $1$.

- **Proposition 1.** $\det E_{C_i \leftarrow {\lambda} C_i} = \lambda$.
- **Proposition 2.** $\det E_{C_i \leftarrow C_i + {\lambda} C_j} = +1$.
- **Proposition 3.** $\det E_{C_i \leftrightarrow C_j} = -1$.
- **Proposition 4.** Si $E$ est une matrice élémentaire, alors

$\det \left( A \times E \right) = \det A \times \det E$

Avec ces propositions, on peut calculer le déterminant $A$ par l'**algorithme de Gauss**. Il s'agit de multiplier $A$ par des matrices élémentaires $E_i$ afin de trouver une matrice triangulaire $T$.

$T = A.{E_1} {\ldots{}} {E_r}$

et

$\det T = \det \left( A.{E_1} {\ldots{}} {E_r} \right) = \det A \det E_1 \ldots{} \det E_r$

Le $\det T$ et les $\det E_i$ sont connus. On peut alors en déduire $\det A$.

#### Déterminant d'un produit

**Théorème.** $\det \left( A \times B \right) = \det A \times \det B$.

#### Déterminant des matrices inversibles

**Théorème.** Une matrice carrée $A$ est inversible si et seulement si son déterminant est non nul. De plus, si $A$ est inversible, alors :

$\det \left( A^{-1} \right) = \frac{1}{\det A}$

#### Déterminant de la transposée

$\det {{}^t}A = \det A$

> [!NOTE]
> Les opérations élémentaires sur les lignes :
> 1. $L_i \leftarrow {\lambda} L_i$ avec $\lambda \neq 0$ : le déterminant est multiplié par $\lambda$.
> 2. $L_i \leftarrow L_i + {\lambda} L_j$ avec $\lambda \in \mathbb{K}$ et $j \neq i$ : le déterminant ne change pas.
> 3. $L_i \leftrightarrow L_j$ : le déterminant change de signe.

### Calculs de déterminants

#### Cofacteur

**Définition.** Soit $A = \left( a_{ij} \right) \in M_n \left( \mathbb{K} \right)$ une matrice carrée.

1. $A_{ij}$ est la matrice extraite obtenue en effaçant la ligne $i$ et la colonne $j$ de $A$.

2. Le nombre $\det A_{ij}$ est un **mineur d'ordre $n - 1$** de la matrice $A$.

3. Le nombre $C_{ij} = \left( -1 \right)^{i + j} \det A_{ij}$ est le **cofacteur** de $A$ relatif au coefficient $a_{ij}$.

Quel est le signe de $C_{ij}$ ? $C_{ij} = + \det A_{ij}$ ou $C_{ij} = -\det A_{ij}$. Pour le savoir, on associe $A_{ij}$ à une matrice exposant les signes :

$\left( \begin{array}{ccccc}+ & - & + & - & \ldots{} \\ - & + & - & + & \ldots{} \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\\end{array} \right)$

#### Développement suivant une ligne ou une colonne

- **Théorème.** Formule de développement par rapport à la ligne $i$ :

$\det A = \sum_{j = 1}^{n} \left( -1 \right)^{i + j} a_{ij} \det A_{ij} = \sum_{j = 1}^{n} a_{ij} C_{ij}$

- **Théorème.** Formule de développement par rapport à la colonne $j$ :

$\det A = \sum_{i = 1}^{n} \left( -1 \right)^{i + j} a_{ij} \det A_{ij} = \sum_{i = 1}^{n} a_{ij} C_{ij}$

> [!NOTE]
> Par le développement par rapport à une ligne, on se ramène à $n$ déterminants $\left( n - 1 \right) \times \left( n - 1 \right)$, et par récurrence à $n!$ sous-déterminants.

> [!NOTE]
>  Il faut que $A$ ait beaucoup de zéros.

> [!NOTE]
>  On commence par faire apparaître des zéros par des opérations élémentaires sur les lignes et les colonnes.

#### Inverse d'une matrice

Soit $A \in M_n \left( \mathbb{K} \right)$, la **comatrice** $C$ est la matrice des cofacteurs.

$C = \left( C_{ij} \right) = \left( \begin{array}{cccc}C_{11} & C_{12} & \ldots{} & C_{1n} \\ C_{21} & C_{22} & \ldots{} & C_{2n} \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} \\C_{n1} & C_{n2} & \ldots{} & C_{nn} \\\end{array} \right)$

**Théorème.** Soient $A$ une matrice inversible et $C$ sa comatrice. On a alors :

$A^{-1} = \frac{1}{\det A} {{}^t}C$

### Applications des déterminants

#### Méthode de Cramér

Soit $n$ équations linéaires à $n$ inconnues. Il peut s'écrire sous forme matrice $A.X = B$.

La matrice $A_j \in M_n \left( \mathbb{K} \right)$ vaut :

$A_j = \left( \begin{array}{ccccccc}a_{11} & \ldots{} & a_{1, j - 1} & b_1 & a_{1, j + 1} & \ldots{} & a_{1n} \\a_{21} & \ldots{} & a_{2, j - 1} & b_2 & a_{2, j + 1} & \ldots{} & a_{2n} \\\ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\a_{n1} & \ldots{} & a_{n, j - 1} & b_n & a_{n, j + 1} & \ldots{} & a_{nn} \\\end{array}\right)$

**Théorème : la règle de Cramér.** Soit un système de $n$ équations à $n$ inconnues :

$A.X = B$

On suppose que $\det A \neq 0$, alors l'unique solution $\left( x_1, x_2, \ldots{}, x_n \right)$ du système est donné par :

$\begin{array}{c} x_1 = \frac{\det A_1}{\det A} \\  x_2 = \frac{\det A_2}{\det A} \\  \ldots{} \\ x_n = \frac{\det A_n}{\det A}  \end{array}$

Ce n'est pas la méthode la plus efficace, mais elle est utile si le système contient des paramètres.

#### Déterminant et base

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n$ et $\mathcal{B}$ une base de $E$. Les $v_1, v_2, \ldots{}, v_n$ vecteurs de $E$ forment-ils une base ?

On définit $A \in M_n \left( \mathbb{K} \right)$ la matrice dont la j-ème colonne est formée des coordonnées du vecteur $v_j$ dans $\mathcal{B}$.

**Théorème.** Les vecteurs $\left( v_1, v_2, \ldots{}, v_n \right)$ forment une base de $E$ si et seulement si $\det A \neq 0$.

**Corollaire.** Une famille de $n$ vecteurs de $\mathbb{R}^n$

$\left( \begin{array}{cccc} \begin{array}{c} a_{11} \\ a_{21} \\ \ldots{} \\ a_{n1} \end{array} & \begin{array}{c} a_{12} \\ a_{22} \\ \ldots{} \\ a_{n2} \end{array} & \ldots{} & \begin{array}{c} a_{1n} \\ a_{2n} \\ \ldots{} \\ a_{nn} \end{array} \\ \end{array} \right)$

forme une base si et seulement si $\det \left( a_{ij} \right) \neq 0$.

#### Mineurs d'une matrice

Soient $A = \left( a_{ij} \right) \in M_{n, p} \left( \mathbb{K} \right)$ une matrice à $n$ lignes et $p$ colonnes, et $k$ un entier inférieur à $n$ et à $p$.

**Définition.** On appelle **mineur d'ordre $k$** le déterminant de toute matrice carrée de taille $k$ extraite de $A$. Une telle matrice est obtenue en supprimant $n - k$ lignes et $p - k$ colonnes de $A$. $A$ n'a pas besoin d'être une matrice carrée.

#### Calcul du rang d'une matrice

- **Définition.** Le rang d'une matrice est la dimension de l'espace vectoriel engendré par les vecteurs colonnes.

- **Théorème.** Le rang d'une matrice $A \in M_{n, p} \left( \mathbb{K} \right)$ est le plus grand entier $r$ tel qu'il existe un mineur d'ordre $r$ extrait de $A$ non nul.

#### Rang d'une transposée

**Proposition.** Le rang de $A$ est égal au rang de sa transposée ${{}^t}A$.

## Liens

- [Topo en format P.D.F.](./PDF/04-Calcul%20matriciel.pdf)

## Notes de bas de page

[^1]: Leopold Kronecker (1823-1891)

[^2]: **Conjoncture :** assertion que l'on pense être vraie et qu'il faut démontrer

[^3]: Pierre-Frédéric Sarrus (1798-1861)

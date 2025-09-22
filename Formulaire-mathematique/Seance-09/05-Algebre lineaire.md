# Algèbre linéaire

## Tutoriels

- [Applications linéaires](https://www.youtube.com/watch?v=4CS7MiS5AQA&list=PL024XGD7WCIH8m2216FggDVanYWEbZqS6)

- [Systèmes linéaires](https://www.youtube.com/watch?v=0uYJ3RNL5SU&list=PL024XGD7WCIFSxatDf77naZwvNPiPbAe4)

## Systèmes linéaires

Les systèmes linéaires forment la base calculatoire de l'algèbre linéaire. Ils permettent de traiter les cas de l'algèbre linéaire de dimension fini.

### Introduction générale

Une **équation** est dite **linéaire** en variable[^1] $x$ et en variable $y$, car il n'y a pas de carré, de cube, *etc*.

- **Exemple 1.** Dans le plan $\left( O, x, y \right)$, l'équation d'une droite s'écrit :

$ax + by= e$

avec $a, b, e$ des constantes réelles.

- **Exemple 2.** Intersection de deux droites $D_1$ et $D_2$. Un point $\left( x, y \right)$ est dans l'intersection $D_1 \cap D_2$ s'il est solution du système :

$S : \left\lbrace \begin{array}{l} ax + by = e \\ cx + dy = f \end{array} \right.$

Géométrique, seuls trois cas sont possibles : soit $D_1 \cap D_2$, dans ce cas $S$ a une solution ; soit $D_1 // D_2$, dans cas $S$ n'a pas de solution, soit $D_1 = D_2$, dans ce cas $S$ a une infinité de solutions.

#### Méthode de la substitution

$S : \left\lbrace \begin{array}{l}3x + 2y = 1 \\2x - 7y = -2\end{array} \right.$

$\begin{array}{l}\Leftrightarrow \left\lbrace \begin{array}{l}y = \frac{1}{2} - \frac{3}{2} x \\2x - 7 \left( \frac{1}{2} - \frac{3}{2} x \right)  = -2\end{array} \right. \\\Leftrightarrow \left\lbrace \begin{array}{l}y = \frac{1}{2} - \frac{3}{2} x \\\left( 2 + 7 \frac{3}{2} \right)x  = -2 + \frac{7}{2}\end{array} \right. \\\Leftrightarrow \left\lbrace \begin{array}{l}y = \frac{1}{2} - \frac{3}{2} x \\\frac{25}{2} x  = \frac{3}{2}\end{array} \right. \\\Leftrightarrow \left\lbrace \begin{array}{l}y = \frac{1}{2} - \frac{3}{2} \frac{3}{25} = \frac{8}{25} \\x  = \frac{3}{25}\end{array} \right. \end{array}$

L'ensemble des solutions du système est un singleton :

$S = \left\lbrace \left( \frac{3}{25}, \frac{8}{25} \right) \right\rbrace$

Dans l'espace $\left( O, x, y, z \right)$, une équation linéaire

$ax + by + cz = d$

avec $\left( a, b, c \right) \neq \left( 0, 0, 0 \right)$ est l'**équation d'un plan**.

Les triplets $\left( x, y, z \right)$ solutions du système à deux équations et à trois inconnues suivant :

$\left\lbrace \begin{array}{l}ax + by + cz = d \\a'x + b'y + c'z = d'\end{array}\right.$

ce sont les coordonnées des points dans l'intersection de deux plans dans l'espace.

Trois solutions sont possibles :

- Si $P_1 // P_2$ alors le système n'a aucune solution.

- Si $P_1 = P_2$ alors le système a une infinité de solutions. 

- Si $P_1 \cap P_2$ alors le système a une infinité de solutions (sous la forme d'une droite).

1. Cas de deux équations incompatibles

$\left\lbrace  \begin{array}{l} 2x + 3y - 4z = 7 \\ 4x + 6y - 8z = -1 \end{array} \right. \Leftrightarrow S = \varnothing$

2. Cas de deux équations équivalentes

$\left\lbrace  \begin{array}{l} 2x + 3y - 4z = 7 \\ 4x + 6y - 8z = -14 \end{array} \right. \Leftrightarrow S = \left\lbrace \left( x, y, \frac{1}{2} x + \frac{3}{4} y - \frac{7}{4} \backslash x, y \in \mathbb{R} \right) \right\rbrace$

La solution dépend d'un paramètre.

3. Choix du paramètre $x$.

$\left\lbrace  \begin{array}{l} 7x + 2y - 2z = 1 \\ 2x + 3y + 2z = 1 \end{array} \right. \Leftrightarrow S = \left\lbrace \left( x, -\frac{9}{5} x + \frac{2}{5}, - \frac{17}{10} x - \frac{1}{10} \backslash x \in \mathbb{R} \right) \right\rbrace$

Il offre une **description de la droite d'intersection de $P_1$ et $P_2$**.

4. Choix du paramètre $y$.

$\left\lbrace  \begin{array}{l} 7x + 2y - 2z = 1 \\ 2x + 3y + 2z = 1 \end{array} \right. \Leftrightarrow S = \left\lbrace \left( -\frac{10}{9} y +\frac{8}{9}, y, - \frac{7}{18} y - \frac{7}{18} \backslash y \in \mathbb{R} \right) \right\rbrace$

5. Choix du paramètre $z$.

$\left\lbrace  \begin{array}{l} 7x + 2y - 2z = 1 \\ 2x + 3y + 2z = 1 \end{array} \right. \Leftrightarrow S = \left\lbrace \left( 2 + \frac{20}{7} z, -\frac{18}{7} z - 1, z \backslash z \in \mathbb{R} \right) \right\rbrace$

Les systèmes à trois équations à trois inconnues ont en général pour solution un point.

#### Méthode de Cramér

La méthode de Cramér s'utilise dans le cas d'un système d'équation à deux inconnues.

$\left\lbrace \begin{array}{l}ax + by = e \\cx + dy = f\end{array}\right.$

- **Étape 1.** On calcule le **déterminant** du système.

$\left|   \begin{array}{cc} a & b \\ c & d  \end{array} \right| = ad - bc$

- **Étape 2.** Si le déterminant est non nul $\left( ad - bc \neq 0 \right)$, alors il existe **une unique solution** $\left( x, y \right)$ telle que :

$x = \frac{\left| \begin{array}{cc} e & b \\ f & d \end{array} \right|}{\left| \begin{array}{cc} a & b \\ c & d \end{array} \right|}$

et

$y = \frac{\left| \begin{array}{cc} a & e \\ c & f \end{array} \right|}{\left| \begin{array}{cc} a & b \\ c & d \end{array} \right|}$

ou

$x = \frac{ed - bf}{ad - bc}$

ou

$y = \frac{af - ec}{ad - bc}$

On place la colonne du second membre et la seconde colonne de coefficients ensemble.

On place la première colonne de coefficients et la colonne du second membre ensemble.

**La méthode de Cramér est bien adaptée pour les systèmes à un ou deux paramètres**. Par exemple,

$\left\lbrace \begin{array}{c}tx - 2y = 1 \\3x + ty = 1\end{array}\right.$

avec $t \in \mathbb{R}$.

On calcule dans un premier temps :

$\left| \begin{array}{cc}t & -2 \\3 & t\end{array}\right| = t^2 + 6$

$t^2 + 6 \neq 0 \Leftrightarrow t^2 \neq - 6$, or $t^2$ est strictement positif, donc $t^2 - 6 \neq 0$, c'est-à-dire $t^2 - 6 > 0$. 

On calcule dans un second temps :

$x = \frac{\left| \begin{array}{cc} 1 & 2 \\ 1 & t \end{array} \right|}{t^2 + 6} = \frac{t - 2}{t^2 + 6}$

et

$y = \frac{\left| \begin{array}{cc} t & 1 \\ 3 & 1 \end{array} \right|}{t - 3} = \frac{t - 2}{t^2 + 6}$

#### Résolution par inversion des matrices

La résolution par inversion des matrices intervient dans le cas du système de deux équations à deux inconnues.

**Tout système linéaire admet une traduction matricielle**.

Soit le système linéaire :

$\left\lbrace \begin{array}{l}ax + by = e \\cx + dy = f\end{array}\right.$

$\Leftrightarrow A.X = Y$

avec $A = \left[ \begin{array}{cc} a & b \\ c & d \end{array} \right]$, $X = \left[ \begin{array}{c} x \\ y \end{array} \right]$, et $Y = \left[ \begin{array}{c} e \\ f \end{array} \right]$.

Si le déterminant de la matrice $A$ est non nul, c'est-à-dire si $ad - bc \neq 0$, alors la matrice $A$ est **inversible** et ;

$A^{-1} = \frac{1}{ad - bc} \left[ \begin{array}{cc} d & -b \\ -c & a \end{array} \right]$

et l'unique solution $X = \left[ \begin{array}{c} x \\ y \end{array} \right]$ du système est donnée par :

$X = A^{-1} .Y$

Exemple.

$\left\lbrace \begin{array}{l}x + y = 1 \\x + t^2 y = t\end{array}\right.$

avec $t \in \mathbb{R}$.

On pose $A = \left[ \begin{array}{cc} 1 & 1 \\ 1 & t^2 \end{array} \right]$, $X = \left[ \begin{array}{c} x \\ y \end{array} \right]$ et $Y = \left[ \begin{array}{c} 1 \\ t \end{array} \right]$.

On calcule dans un premier temps :

$\left| \begin{array}{cc}1 & 1 \\1 & t^2\end{array}\right| = t^2 - 1$

$t^2 - 1 = 0 \Leftrightarrow t^2 = 1 \Leftrightarrow \left\lbrace \begin{array}{l} t = 1 \\ \textrm{ou} \\ t = -1 \end{array} \right.$ 

On étudie dans un deuxième temps le cas où $\left| t \right| \neq 1$.

$\begin{array}{l}A^{-1} = \frac{1}{t^2 - 1} \left[ \begin{array}{cc} t^2 & -1 \\ -1 & 1 \end{array} \right] \\A^{-1} = \left[ \begin{array}{cc} \frac{t^2}{t^2 - 1} & -\frac{1}{t^2 - 1} \\ -\frac{1}{t^2 - 1} & \frac{1}{t^2 - 1} \end{array} \right]\end{array}$

L'unique solution $X$ du système est donnée par :

$X = A^{-1}.Y = \left[ \begin{array}{cc} \frac{t^2}{t^2 - 1} & -\frac{1}{t^2 - 1} \\ -\frac{1}{t^2 - 1} & \frac{1}{t^2 - 1} \end{array} \right] . \left[ \begin{array}{c} 1 \\ t \end{array} \right] = \left[ \begin{array}{c} \frac{1}{t + 1} \\ \frac{1}{t + 1} \end{array} \right]$

Pour $t \neq \pm 1$, l'ensemble des solutions est :

$S = \left\lbrace \left( \frac{t}{t + 1}, \frac{1}{t + 1} \right) \right\rbrace$

On étudie dans un troisième temps le cas où $t = 1$.

$\left\lbrace \begin{array}{l}x + y = 1 \\x + y = 1\end{array}\right.$

Les deux équations sont **identiques**.

$S = \left\lbrace \left( x, 1 - x \right) \right\rbrace$

Puis, le cas où $t = -1$.

$\left\lbrace \begin{array}{l}x + y = 1 \\x + y = -1\end{array}\right.$

Les deux équations sont **incompatibles**.

$S = \varnothing$

### Théorie des systèmes linéaires

On appelle **système linéaire** dans les $p$ variables (ou inconnues) $x_1, \ldots{}, x_p$ toute relation de la forme :

$a_1 x_1 + \ldots{} + a_p x_p = b$

avec $a_1, \ldots{}, a_p$ des nombres réels donnés.

Un **système de $n$ équations linéaires à $p$ inconnues** est une liste de $n$ équations linéaires.

$\left\lbrace \begin{array}{ll}a_{11} x_1 + a_{12} x_2 + \ldots{} + a_{1p} = b_1 & \textrm{équation 1} \\a_{21} x_1 + a_{22} x_2 + \ldots{} + a_{2p} = b_2 & \textrm{équation 2} \\\ldots{} & \\a_{i1} x_1 + a_{i2} x_2 + \ldots{} + a_{ip} = b_i & \textrm{équation } i \\\ldots{} & \\a_{n1} x_1 + a_{n2} x_2 + \ldots{} + a_{np} = b_n & \textrm{équation } n \\\end{array}\right.$

Les nombres $a_{ij}$ avec $i = 1, \ldots{}, n$ (le numéro de ligne) et $j = 1, \ldots{}, p$ (le numéro de colonne) sont les **coefficients**.

Les nombres $b_i$ avec $i = 1, \ldots{}, n$ constituent le **second membre**.

Une **solution** du système linéaire est une liste de $p$ nombres réels $\left( s_1, s_2, \ldots{}, s_p \right)$ tels que si l'on remplace $x_1$ par $s_1$, $x_2$ par $s_2$, *etc*., dans le système linéaire, on obtient une égalité.

L'**ensemble des solutions du système** est l'ensemble des $p$-uplets.

**Résoudre** un système consiste à déterminer l'ensemble des solutions du système.

Deux systèmes linéaires sont **équivalents** s'ils ont le même ensemble de solutions.

Résoudre un système linéaire donné consistera à le transformer en un système équivalent dont la résolution sera plus simple que celle du système de départ.

- **Théorème.** Un système d'équations linéaires a :
    
    - soit aucune solution dans le cas d'un système linéaire incompatible ;
    
    - soit une seule solution ;
    
    - soit une infinité de solutions. Si l'on trouve deux solutions à un système linéaire alors il en existe une infinité.

Les **systèmes homogènes** sont des systèmes sans second membre, c'est-à-dire avec $b_1 = b_2 = \ldots{} = b_n = 0$.

- Un tel système est toujours **compatible**, car $s_1 = s_2 = \ldots{} = s_p = 0$ est toujours la **solution triviale** du système.

- Exemple. L'intersection de deux droites d'équation $ax + by = 0$ et $cx + dy = 0$ représente l'origine $\left( 0, 0 \right)$.

### Le pivot de Gauss

#### Systèmes échelonnés

Un **système** est **échelonné** si le nombre de coefficients nuls commençant une ligne croît strictement ligne après ligne.

Un **système** est **échelonné réduit** si, en plus :

- le premier coefficient non nul d'une ligne vaut 1 ;

- 1 est le seul élément non nul de sa colonne.

Exemple d'un système échelonné (non réduit car les premiers coefficients sont différents de 1).

$\left\lbrace \begin{array}{ccccccccc}2x_1 & + & 3x_2 & + & 2x_3 & - & x_4 & = & 5 \\& - & x_2 & - & 2x_3 &  &  & = & 4 \\&  &  &  &  &  & 3x_4 & = & 1 \\\end{array}\right.$

Exemple d'un système non échelonné (car il n'y a pas de coefficient nul en dernière ligne pour le premier coefficient).

$\left\lbrace \begin{array}{ccccccccc}2x_1 & + & 3x_2 & + & 2x_3 & - & x_4 & = & 5 \\&  &  & - & 2x_3 &  &  & = & 4 \\&  &  &  & x_3 & + & x_4 & = & 1 \end{array}\right.$

**Les systèmes échelonnés réduits sont particulièrement simples à résoudre**.

#### Opérations sur les équations d'un système

Trois opérations élémentaires permettent d'obtenir des systèmes équivalents.

- $L_i \leftarrow {\lambda} L_i$ avec $\lambda \neq 0$ c'est-à-dire on peut multiplier une équation par un réel non nul.

- $L_i \leftarrow L_i + {\lambda} L_j$ avec $\lambda \in \mathbb{R}$ et $i \neq j$ c'est-à-dire on peut ajouter à l'équation $L_i$ un multiple d'une autre équation $L_j$.

- $L_i \leftrightarrow L_j$ c'est-à-dire on peut échanger deux équations.

Exemple

$\left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\2x & - & y & + & 5z & = & -5 & \left( L_2 \right) \\-x & - & 3y & - & 9z & = & -5 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\& - & 3y & - & 9z & = & -3 & \left( L_2 \leftarrow L_2 - 2 L_1 \right) \\-x & - & 3y & - & 9z & = & -5 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\& - & 3y & - & 9z & = & -3 & \left( L_2 \right) \\& - & 2y & - & 2z & = & -6 & \left( L_3 \leftarrow L_3 + L_1 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\&  & y & + & 3z & = & 1 & \left( L_2 \leftarrow \frac{1}{3} L_2 \right) \\& - & 2y & - & 2z & = & -6 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\&  & y & + & 3z & = & 1 & \left( L_2 \right) \\&  &  &  & 4z & = & -4 & \left( L_3 \leftarrow L_3 + 2 L_2 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\&  & y & + & 3z & = & 1 & \left( L_2 \right) \\&  &  &  & z & = & -1 & \left( L_3 \leftarrow \frac{1}{4} L_3 \right)\end{array}\right.$

On obtient un système échelonné non réduit.

$S = \left\lbrace \left( 2, 4, -1 \right) \right\rbrace$

Pour arriver à un système échelonné réduit

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y & + & 7z & = & -1 & \left( L_1 \right) \\&  & y &  &  & = & 4 & \left( L_2 \leftarrow L_2 - 3 L_3 \right) \\&  &  &  & z & = & -1 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x & + & y &  &  & = & 6 & \left( L_1 \leftarrow L_1 - 7 L_3 \right) \\&  & y &  &  & = & 4 & \left( L_2 \right) \\&  &  &  & z & = & -1 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccr}x &  &  &  &  & = & 2 & \left( L_1 \leftarrow L_1 - L_2 \right) \\&  & y &  &  & = & 4 & \left( L_2 \right) \\&  &  &  & z & = & -1 & \left( L_3 \right)\end{array}\right.$

cette forme n'était pas utile pour résoudre l'exemple.

#### Méthode de résolution par le pivot de Gauss

Elle permet de trouver la solution de n'importe quel système linéaire. C'est un algorithme. Le processus aboutit toujours, et assez rapidement. Pour le comprendre, on peut illustrer par un exemple.

$\left\lbrace \begin{array}{cccccccccr}& - & x_2 & + & 2x_3 & + & 13x_4 & = & 5 & \left( L_1 \right) \\x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_2 \right) \\-x_1 & + & 3x_2 & - & 3x_3 & - & 20x_4 & = & -1 & \left( L_3 \right)\end{array}\right.$

##### Étape 1. Passage à une forme échelonnée

Pour appliquer le pivot de Gauss, il faut que le premier coefficient de la première ligne soit non nul.

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_1 \leftrightarrow L_2 \right) \\& - & x_2 & + & 2x_3 & + & 13x_4 & = & 5 & \left( L_2 \right) \\-x_1 & + & 3x_2 & - & 3x_3 & - & 20x_4 & = & -1 & \left( L_3 \right)\end{array}\right.$

En première ligne, on a un coefficient 1 ; on dit que l'on a un pivot en position $1, 1$. Il sert de base pour éliminer tous les autres termes sur la même colonne.

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_1 \right) \\& - & x_2 & + & 2x_3 & + & 13x_4 & = & 5 & \left( L_2 \right) \\&  & x_2 &  &  & - & 3x_4 & = & 3 & \left( L_3 \leftarrow L_3 + L_1 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_1 \right) \\&  & x_2 & - & 2x_3 & - & 13x_4 & = & -5 & \left( L_2 \leftrightarrow -L_2 \right) \\&  & x_2 &  &  & - & 3x_4 & = & 3 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_1 \right) \\&  & x_2 & - & 2x_3 & - & 13x_4 & = & -5 & \left( L_2 \right) \\&  &  &  & 2x_3 & + & 10x_4 & = & 8 & \left( L_3 \leftarrow L_3 - L_2 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_1 \leftrightarrow L_2 \right) \\&  & x_2 & - & 2x_3 & - & 13x_4 & = & -5 & \left( L_2 \right) \\&  &  &  & x_3 & + & 5x_4 & = & 4 & \left( L_3 \leftarrow \frac{1}{2} L_3 \right)\end{array}\right.$

##### Étape 2. Passage à une forme réduite

Il faut faire apparaître des zéros au-dessus des pivots.

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 & + & 3x_3 & + & 17x_4 & = & 4 & \left( L_1 \right) \\&  & x_2 &  &  & - & 3x_4 & = & 3 & \left( L_2 \leftarrow L_2 - L_3 \right) \\&  &  &  & x_3 & + & 5x_4 & = & 4 & \left( L_3 \right)\end{array}\right.$

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 & - & 2x_2 &  &  & + & 2x_4 & = & -8 & \left( L_1 \leftarrow L_1 - 3 L_3 \right) \\&  & x_2 &  &  & - & 3x_4 & = & 3 & \left( L_2 \right) \\&  &  &  & x_3 & + & 5x_4 & = & 4 & \left( L_3 \right)\end{array}\right.$

> [!WARNING]
> Il faut toujours partir de la dernière ligne, puis remonter vers l'équation à réduire.

$\Leftrightarrow \left\lbrace \begin{array}{cccccccccr}x_1 &  &  &  &  & - & 4x_4 & = & -2 & \left( L_1 \leftarrow L_1 - 2 L_2 \right) \\&  & x_2 &  &  & - & 3x_4 & = & 3 & \left( L_2 \right) \\&  &  &  & x_3 & + & 5x_4 & = & 4 & \left( L_3 \right)\end{array}\right.$

##### Étape 3. Conclusion

$x_4$ est une variable libre.

$\Leftrightarrow \left\lbrace \begin{array}{l}x_1 = 4x_4 - 2 \\x_2 = 3x_4 + 3 \\x_3 = -5x_4 + 4\end{array}\right.$

$S = \left\lbrace \left( 4x_4 - 2, 3x_4 + 3, -5x_4, x_4 \backslash x_4 \in \mathbb{R} \right) \right\rbrace$

Le fait que l'on puisse toujours se ramener à un système échelonné réduit implique que :

- **Théorème.** Tout système homogène d'équations linéaires dont le nombre d'inconnus est strictement plus grand que le nombre d'équations a une infinité de solution.

## Notes de bas de page

[^1]: ou inconnue

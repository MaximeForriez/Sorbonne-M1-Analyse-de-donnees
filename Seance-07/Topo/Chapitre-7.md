# Relation entre deux variables quantitatives

Pour les relations entre deux variables quantitatives, la notion de probabilités conditionnelles intervient. L'objectif de ce chapitre est d'expliquer la manière de les obtenir et de les étudier. Soient $X$ et $Y$ les deux caractères quantitatifs étudiés, $p$ le nombre de modalités prises par $X$, $q$ le nombre de modalités prises par $Y$, et $n$ le nombre total d'observations.

## Couple de variables aléatoires discrètes

Soient $X$ et $Y$ des variables aléatoires définies sur un même univers $S$, et ayant pour espaces images respectifs :

$X \left( S \right) = \left\lbrace x_1, x_2, \ldots{}, x_n \right\rbrace$

et

$Y \left( S \right) = \left\lbrace y_1, y_2, \ldots{}, y_n \right\rbrace$

On transforme l'ensemble produit :

$X \left( S \right) \times Y \left( S \right) = \left\lbrace \left( x_1, y_1 \right), \left( x_2, y_2 \right), \ldots{}, \left( x_n, y_n \right) \right\rbrace$

en un espace probabilisé, en définissant la probabilité du couple ordonné $\left( x_i, y_i \right)$ par $\Pr \left( X = x_i, Y = y_i \right)$, que l'on écrit $k \left( x_i, y_i \right)$. Cette fonction $h$ sur $X \left( S \right) \times Y \left( S \right)$, définie par $h \left( x_i, y_i \right) = \Pr \left( X = x_i, Y = y_i \right)$ est appelée la **distribution jointe**, où la loi de probabilité produit de $X$ et $Y$, et est habituellement représentée sous la forme d'un tableau (Tab. 1).

|  | $y_1$ | $y_2$ | $\ldots{}$ | $y_n$ | **SOMME** |
| :-: | :-: | :-: | :-: | :-: | :-: |
| $x_1$ | $h \left( x_1, y_1 \right)$ | $h \left( x_1, y_2 \right)$ | $\ldots{}$ | $h \left( x_1, y_n \right)$ | **$f \left( x_1 \right)$** |
| $x_2$ | $h \left( x_2, y_1 \right)$ | $h \left( x_2, y_2 \right)$ | $\ldots{}$ | $h \left( x_2, y_n \right)$ | **$f \left( x_2 \right)$** |
| $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ |
| $x_n$ | $h \left( x_n, y_1 \right)$ | $h \left( x_n, y_2 \right)$ | $\ldots{}$ | $h \left( x_n, y_n \right)$ | **$f \left( x_n \right)$** |
| **SOMME** | **$g \left( y_1 \right)$** | **$g \left( y_2 \right)$** | $\ldots{}$ | **$g \left( y_n \right)$** |  |

**Tableau 1. Loi de probabilité produit entre deux variables aléatoires X et Y**

Les fonctions $f$ et $g$ sont définies par :

$f \left( x_i \right) = \sum_{j = 1}^{q} = h \left( x_i, y_j \right)$

et

$g \left( y_j \right) = \sum_{i = 1}^{p} = h \left( x_i, y_j \right)$

La loi du couple $\left( X, Y \right)$ est également appelée **loi de probabilité simultanée** (ou loi conjointe). Elle est définie par l'ensemble des nombres $n_{ij} = h \left( x_i, y_j \right)$  avec $\left( 0 < n_{ij} < 1 \right)$ tels que :

$n_{ij} = \Pr \left( X = x_j \textrm{ et } Y = y_j \right)$

Les lois de probabilités $n_{ij} = h \left( x_i, y_i \right)$ vérifient les relations :

1. $h \left( x_i, y_i \right) \geq 0$ ;

2. $\sum_{i = 1}^{p} \sum_{j = 1}^{q} h \left( x_i, y_i \right) = 1$

Dans le cas fini, la loi conjointe est affichable sous la forme d'un **tableau de contingence**. Les probabilités $n_{ij}$ y figurant définissent la loi du couple et toutes les lois associées.

Dans le tableau 1, $f \left( x_i \right)$ est la somme des éléments de la $i$-ième ligne, tandis que $g \left( y_j \right)$ est la somme des éléments de la $j$-ième colonne. Ces fonctions portent le nom de **lois de probabilités marginales**. Ce sont les distribution individuelles respectives de $X$ et $Y$.

Les **lois de probabilité marginales** sont les lois de probabilité des variables $X$ et $Y$ prises séparément. Par définition, il en existe deux :

1. la loi de probabilité marginale de la variable $X$ : $\Pr \left( X = x_i \right) = \sum_{j = 1}^{q} n_{ij} = p_{i.}$ ;

2. la loi de probabilité marginale de la variable $Y$ : $\Pr \left( Y = y_j \right) = \sum_{i = 1}^{p} n_{ij} = p_{.j}$.

Les quantités $p_{i.}$ et $p_{.j}$ constituent les marges du tableau de contingence et vérifient les relations :

$\sum_{i = 1}^{p} n_{i.} = \sum_{j = 1}^{q} n_{.j} = 1$

Les **lois conditionnelles** sont les deux familles de lois suivantes :

1. la loi conditionnelle de $X$ sachant $Y = y_j$ c'est-à-dire que la valeur de la variable $Y$ est connue :

$\Pr \left( X = x_i \setminus Y = y_j \right) = \frac{n_{ij}}{n_{.j}} = \frac{\Pr \left( X = x_i \textrm{ et } Y = y_j \right)}{\Pr \left( Y = y_j \right)}$

2. la loi conditionnelle de $Y$ sachant $X = x_i$ c'est-à-dire que la valeur de la variable $X$ est connue :

$\Pr \left( Y = y_j \setminus X = x_i \right) = \frac{n_{ij}}{n_{i.}} = \frac{\Pr \left( X = x_i \textrm{ et } Y = y_j \right)}{\Pr \left( X = x_i \right)}$
	
> [!NOTE]
> Ces lois sont parfaitement définies si les quantités $\Pr \left( Y = y_j \right)$ ou $\Pr \left( X = x_i \right)$ sont différentes de 0.
	
> [!NOTE]
>  Si on connaît les lois conditionnelles, on peut inversement en déduire la loi du couple.
	
> [!NOTE]
>  Grâce à la formule de Bayes, on peut exprimer une loi conditionnelle en fonction de l'autre. Par exemple :
> $\Pr \left( X = x_i \setminus Y = y_j \right) = \frac{\Pr \left( X = x_i \textrm{ et } Y = y_j \right) \Pr \left( X = x_i \right)}{\sum_{i = 1}^{p} \Pr \left( Y = y_j \setminus X = x_i \right) \Pr \left( X = x_i \right)}$

### Propriétés des couples de variables aléatoires discrètes

Si $X$ et $Y$ sont des variables aléatoires définies sur le même univers $S$, $X + Y$, $X + k$, $kX$ et $XY$ avec $k \in \mathbb{R}$, sont des fonctions sur $S$ définies par :

- $\left( X + Y \right) \left( s \right) = X \left( s \right) + Y \left( s \right)$ ;

- $\left( kX \right) \left( s \right) = k X \left( s \right)$ ;

- $\left( X + k \right) \left( s \right) = X \left( s \right) + k$ ;

- $\left( XY \right) \left( s \right) = X \left( s \right) Y \left( s \right)$ ;

avec $\forall s \in S$.

> [!NOTE]
> Toutes ces fonctions sont également des variables aléatoires.

### Tableaux statistiques

Dans le cas de deux variables quantitatives discrètes, les tableaux statistiques portent le nom de **tableaux croisés** ou **tableaux de contingence** (Tab. 2). Dans chaque case du tableau, on inscrit l'effectif $n_{ij}$ de l'échantillon, c'est-à-dire le nombre de données tel que $X = x_i$ et $Y = y_i$.

On définit les fréquences absolues suivantes.

1. L'**effectif** et la **fréquence marginale** $n_i$ est le nombre d'individus possédant la modalité $i$ du caractère $X$ quelle que soit la distribution du caractère $Y$.

$n_{i.} = \sum_{j = 1}^{q} n_{ij}$

et

$f_{i.} = \frac{n_{i.}}{n}$
De même, $n_j$ est le nombre d'individus possédant la modalité $j$ du caractère $Y$ quelle que soit la distribution du caractère $X$.

$n_{.j} = \sum_{i = 1}^{p} n_{ij}$

et

$f_{.j} = \frac{n_{.j}}{n}$
	
2. L'**effectif** et la **fréquence conditionnelle** $n_{j \setminus i}$ est la distribution de la variable $Y$ lorsque l'on a fixé la modalité $i$ pour la variable $X$. Elle est définit par :

$n_{j \setminus i} = \frac{n_{ij}}{n_{i.}}$

On définit de la même façon la fréquence conditionnelle $n_{i \setminus j}$ par :

$n_{i \setminus j} = \frac{n_{ij}}{n_{.j}}$

On définit les **fréquences relatives** $f_{ij}$, $f_{i.}$ et $f_{.j}$ par la division des effectifs $n_{ij}$ et les **fréquences marginales** $n_{i.}$ et $n_{.j}$ par l'effectif total $n$.

| $XY$ | $x_1$ | $\ldots{}$ | $x_i$ | $\ldots{}$ | $x_p$ | **Effectif marginal** |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| $y_1$ | $n_{11}$ | $\ldots{}$ | $n_{j1}$ | $\ldots{}$ | $n_{p1}$ | $n_{.1}$ |
| $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ |
| $y_j$ | $n_{1j}$ | $\ldots{}$ | $n_{ij}$ | $\ldots{}$ | $n_{pj}$ | $n_{.j}$ |
| $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ | $\ldots{}$ |
| $y_q$ | $n_{1q}$ | $\ldots{}$ | $n_{iq}$ | $\ldots{}$ | $n_{pq}$ | $n_{.q}$ |
| **Effectif marginal** | $n_{1.}$ | $\ldots{}$ | $n_{i.}$ | $\ldots{}$ | $n_{p.}$ | $n$ |
 
**Tableau 2. Tableau de contingence entre la variable aléatoire $ X $ et la variable aléatoire $ Y $**

Le tableau de contingence permet de vérifier si les deux variables sont bien dépendantes l'une de l'autre. Toutefois, pour représenter graphiquement deux variables quantitatives, on utilise un nuage de points dans $\mathbb{R}^2$. 

### Les caractéristiques marginales

#### Moyennes marginales

La moyenne arithmétique, c''est-à-dire l'espérance mathématique, de $X$ vaut :

$\mathbb{E} \left( X \right) = \frac{1}{n} \sum_{i = 1}^{p} n_{i.} x_i$

La moyenne arithmétique, c''est-à-dire l'espérance mathématique, de $Y$ vaut :  

$\mathbb{E} \left( Y \right) = \frac{1}{n} \sum_{j = 1}^{q} n_{.j} y_j$

Le point G de coordonnées $\left( \mathbb{E} \left( X \right), \mathbb{E} \left( Y \right) \right)$ est appelé **point moyen**.

#### Variances marginales

La variance de $X$ vaut :  

$\mathbb{V} \left( X \right) = \frac{1}{n} \sum_{i = 1}^{p} n_{i.} \left( x_i - \mathbb{E} \left( X \right) \right)^2 = \left[ \frac{1}{n} \sum_{i = 1}^{p} n_{i.} {x_i}^2 \right] - \mathbb{E} \left( X \right)$

La variance de $Y$ vaut :  

$\mathbb{V} \left( Y \right) = \frac{1}{n} \sum_{j = 1}^{q} n_{.j} \left( y_j - \mathbb{E} \left( Y \right) \right)^2 = \left[ \frac{1}{n} \sum_{j = 1}^{q} n_{.j} {y_j}^2 \right] - \mathbb{E} \left( Y \right)$

### Les caractéristiques conditionnelles

#### Moyennes conditionnelles

$\mathbb{E} \left( X_j \right) = \frac{1}{n_{.j}} \sum_{i = 1}^{p} n_{ij} x_i$

et

$\mathbb{E} \left( Y_i \right) = \frac{1}{n_{i.}} \sum_{j = 1}^{q} n_{ij} y_j$

#### Variances conditionnelles

$\mathbb{V} \left( X_j \right) = \frac{1}{n_{.j}} \sum_{i = 1}^{p} n_{ij} \left( x_i - \mathbb{E} \left( X_j \right) \right)^2$  

et 

$\mathbb{V} \left( Y_i \right) = \frac{1}{n_{i.}} \sum_{j = 1}^{q} n_{ij} \left( y_j - \mathbb{E} \left( Y_i \right) \right)^2$  

### Les relations entre les caractéristiques marginales et les caractéristiques conditionnelles

#### Moyenne

La moyenne marginale est la moyenne pondérée des moyennes conditionnelles :

$\mathbb{E} \left( X \right) = \frac{1}{n} \sum{j = 1}{q} n_{.j} \mathbb{E} \left( X_j \right)$

et

$\mathbb{E} \left( Y \right) = \frac{1}{n} \sum{i = 1}{p} n_{i.} \mathbb{E} \left( Y_i \right)$

C'est le **théorème de la moyenne conditionnée**.

#### Variance

La variance marginale est la somme de la moyenne pondérée des variances conditionnelles et de la variance pondérée des moyennes conditionnelles.

$\mathbb{V} \left( X \right) = \bar{\mathbb{V} \left( X \right)} + \mathbb{V} \left( {\bar{X}}_j \right)$

$\mathbb{V} \left( X \right) = \frac{1}{n} \sum_{j = 1}^{q} n_{.j} \mathbb{V} \left( X_j \right) + \frac{1}{n} \sum_{j = 1}^{q} n_{.j} \left( {\bar{X}}_j - \bar{X} \right)^2$
	
et

$\mathbb{V} \left( Y \right) = \bar{\mathbb{V} \left( Y \right)} + \mathbb{V} \left( {\bar{Y}}_i \right)$

C'est le **théorème de la variance conditionnée**.

La variance traduit la dispersion de la distribution. Dans le cas de la distribution marginale de $X$ ou de $Y$, la dispersion résulte de deux facteurs :

1. la dispersion des distribution conditionnées autour de leurs moyennes $\bar{\mathbb{V} \left( X \right)}$ ou $\bar{\mathbb{V} \left( Y \right)}$ que l'on appelle **variance intra-population** (ou variance résiduelle) que l'on note souvent $s_w^2 \left( X \right)$ ou $s_w^2 \left( Y \right)$, $w$ signifiant *within*.

2. la dispersion des moyennes conditionnelles autour de la moyenne $\mathbb{V} \left( {\bar{Y}}_i \right)$ ou $\mathbb{V} \left( {\bar{X}}_j \right)$ que l'on appelle **variance inter-population** (ou variance expliquée) que l'on note $s_b^2 \left( X \right)$ ou $s_b^2 \left( Y \right)$, $b$ signifiant *between*.

### Covariance

Lors du chapitre exposant les paramètres statistiques, la notion de **covariance** avait été posée sans être définie clairement. Cette partie propose de préciser la signification de cette notion importante.

La covariance entre deux variables aléatoires mesure la façon dont deux variables aléatoires $X$ et $Y$ varient **simultanément**. Si elle est nulle, cela signifie que les deux variables ne sont pas corrélées, c'est-à-dire qu'elles sont indépendantes.

La covariance correspond au paramètre suivant :

$\mathrm{cov} \left( X, Y \right) = \frac{1}{n} \sum_{{\tiny \begin{array}{c} 1 \leq i \leq p \\ 1 \leq j \leq q \end{array} }}^{{\tiny \begin{array}{c} p \\ q \end{array} }} n_{ij} \left( x_i - \mathbb{E} \left( X \right) \right) \left( y_j - \mathbb{E} \left( Y \right) \right) = \left[ \frac{1}{n} \sum_{{\tiny \begin{array}{c} 1 \leq i \leq p \\ 1 \leq j \leq q \end{array} }}^{{\tiny \begin{array}{c} p \\ q \end{array} }} n_{ij} x_i y_j \right] - \mathbb{E} \left( X \right) \mathbb{E} \left( Y \right)$

ou

$\mathrm{cov} \left( X, Y \right) = \mathbb{E} \left[ \left( X - \mathbb{E} \left( X \right) \right) \left( Y - \mathbb{E} \left( Y \right) \right) \right] = \mathbb{E} \left( XY \right) - \mathbb{E} \left( X \right) \mathbb{E} \left( Y \right)$

- **Propriété 1.** $\mathrm{cov} \left( aX + b, cY + d \right) = {ac} \mathrm{cov} \left( X, Y \right)$

- **Propriété 2.** $\mathrm{cov} \left( X, X \right) = \mathbb{V} \left( X \right)$

- **Propriété 3.** $\left| \mathrm{cov} \left( X, Y \right) \right| = \sigma \left( X \right) \sigma \left( Y \right)$

- **Propriété 4.** Si les variables $X$ et $Y$ sont indépendantes, alors $\mathrm{cov} \left( X, Y \right)  = 0$. Par contre, la réciproque est fausse.

La covariance est une notion fondamentale qui permet l'étude d'une corrélation à $n$ variables. C'est grâce à elle que l'on sait immédiatement si les variables étudiées sont corrélées, ou pas. Cet aspect fera l'objet d'un chapitre spécifique.

### Corrélation

On définit la **corrélation** de $X$ et $Y$, que l'on écrit $\rho \left( X, Y \right)$, par :

$\rho \left( X, Y \right) = \frac{\mathrm{cov} \left( X, Y \right)}{{\sigma}_X {\sigma}_Y}$

$\rho$ est une quantité sans dimension. $\rho$ a les propriété suivantes :

1. $\rho \left( X, Y \right) = \rho \left( Y, X \right)$ ;

2. $\rho \in \left[ -1, +1 \right]$ ;

3. $\rho \left( X, X \right) = 1$ et $\rho \left( X, -X \right) = -1$ ;

4. $\rho \left( aX + b, cY + d \right) = \rho \left( X, Y \right)$ si $a \neq 0$ et $c \neq 0$.

Covariance et corrélation sont des mesures de la relation qui existe entre $X$ et $Y$.

> [!NOTE]
> La notion de loi de probabilité produit se généralise à un nombre fini quelconque de variables aléatoires $X$, $Y$, \ldots{}, $Z$. $h$ est alors une fonction sur l'ensemble produit $X \left( S \right) \times Y \left( S \right) \times \ldots{} \times Z \left( S \right)$, définie par :
> $h \left( x_i, y_j, \ldots{}, z_k \right) = \Pr \left( X = x_i, Y = y_j, \ldots{}, Z = z_k \right)$

Cela sera développé dans le cadre des analyses multivariées.

### Mesure de la dépendance

À l'aide de différents coefficients, l'étude de la distribution simultanée de deux variables permet de préciser le **type de liaison** pouvant exister entre ces deux variables, la nature et l'intensité de cette liaison.

On dit qu'un nombre fini des variables aléatoires $X$, $Y$, \ldots{}, $Z$ sur un univers $S$ sont **indépendantes** si :

$\Pr \left( X = x_i, Y = y_j, \ldots{}, Z = z_k \right) = \Pr \left( X = x_i \right) \Pr \left( Y = y_j \right) \ldots{} \Pr \left( Z = z_k \right)$

pour toutes les valeurs $x_i$, $y_j$, \ldots{}, $z_k$. En particulier, $X$ et $Y$ sont indépendants si :

$\Pr \left( X = x_i, Y = y_j \right) = \Pr \left( X = x_i \right) \Pr \left( Y = y_j \right)$

Le cadre multivarié sera utilisé plus tard. En attendant, voici quelques particuliers du cadre bivarié.

Si $X$ et $Y$ ont des distributions respectives $f$ et $g$, et une loi de probabilité produit $h$, l'équation peut s'écrire :

$h \left( x_i, y_j \right) = f \left( x_i \right) g \left( y_j \right)$

Dit autrement, $X$ et $Y$ sont indépendants si chaque élément $h \left( x_i, y_j \right)$ est le produit de ses éléments marginaux.

**Théorème.** Soient $X$ et $Y$ des variables aléatoires indépendantes, on a alors :

1. $\mathbb{E} \left( XY \right) = \mathbb{E} \left( X \right) \mathbb{E} \left( Y \right)$ ;

2. $\mathbb{V} \left( X + Y \right) = \mathbb{V} \left( X \right) + \mathbb{V} \left( Y \right)$ ;

> [!NOTE]
> Cela se généralise dans le cas multivarié. Soient $X_1$, $X_2$, \ldots{}, $X_n$ des variables aléatoires, alors :
> $\mathbb{V} \left( X_1 + X_2 + \ldots{} + X_n \right) = \mathbb{V} \left( X_1 \right) + \mathbb{V} \left( X_2 \right) + \ldots{} + \mathbb{V} \left( X_n \right)$

3. $\mathrm{cov} \left( X, Y \right) = 0$.

Corollairement, les distributions $X$ et $Y$ sont **statistiquement indépendantes** si et seulement si :

$f_{ij} = f_{i.} f_{.j}$

pour toutes les valeurs des indices $i$ et $j$. Dit autrement,

$n_{ij} = \frac{n_{i.} n_{.j}}{n}$

Pour qu'il y ait indépendance, il faut que l'égalité ait toujours lieu. Pour démontrer qu'il a **dépendance**, il suffit de fournir un seul cas pour lequel l'égalité n'a pas lieu. Mathématiquement, l'indépendance statistique correspond au fait que les lignes sont proportionnelles, ainsi que les colonnes. L'indépendance statistique de $X$ et de $Y$ correspond à la fois : 

1. à l'indépendance de $Y$ par rapport à $X$ c'est-à-dire que les fréquences conditionnelles de $Y$ pour $X = x_i$ ne dépendent pas de $i$ ; 

2. à l'indépendance de $X$ par rapport à $Y$ c'est-à-dire que les fréquences conditionnelles de $X$ pour $Y = y_j$ ne dépendent pas de $j$.

Différents **tests statistiques** peuvent être mis en œuvre pour vérifier l'indépendance de deux variables statistiques. Le plus utilisé est le test du ${\chi}^2$.

### Fonctions d'une variable aléatoire

Soient $X$ et $Y$ des variables aléatoires sur le même univers $S$, on dit alors que $Y$ est une fonction de $X$ si $Y$ peut se mettre sous la forme $Y = \Phi \left( X \right)$ pour une certaine fonction $\Phi$ d'une variable réelle à valeurs réelles, c'est-à-dire si $Y \left( s \right) = \Phi \left[ X \left( X \right) \right]$ pour tout $s \in S$. Par exemple, $kX$, $X^2$, $X + k$ et $\left( X + k \right)^2$ sont toutes des fonctions de $X$ avec respectivement $\Phi \left( x \right) = kx$, $x^2$, $x + k$ et $\left( x + k \right)^2$.

**Théorème.** Soient $X$ et $Y$ des variables aléatoires sur un même univers $S$ avec $Y = \Phi \left( x \right)$, on a alors :

$\mathbb{E} \left( Y \right) = \sum_{i = 1}^{n} \Phi \left( x \right) f \left( x_i \right)$

avec $f$ la fonction de distribution de $X$.

De la même manière, on dit qu'une variable aléatoire $Z$ est une fonction de $X$ et $Y$ si l'on peut représenter $Z$ sous la forme $Z = \Phi \left( X, Y \right)$ avec $\Phi$ une fonction à valeurs réelles de deux variables réelles, c'est-à-dire si :

$Z \left( s \right) = \Phi \left[ X \left( s \right), Y \left( s \right) \right]$

pour tout $s \in S$.

**Théorème.** Soient $X$, $Y$ et $Z$ des variables aléatoires sur un même univers $S$ avec $Z = \Phi \left( X, Y \right)$, on a alors :

$\mathbb{E} \left( Z \right) = \sum_{i, j}^{p, q} \Phi \left( x_i, y_j \right) h \left( x_i, y_j \right)$

avec $h$ la loi de probabilité produit de $X$ et $Y$.

### Combinaison linéaire de deux variables aléatoires

La combinaison linéaire de deux variables aléatoires a des conséquences sur la moyenne, la variance et l'écart type. Les propriétés ont été vues lors du chapitre exposant les paramètres statistiques.

## Couple de variables aléatoires continues

### Lois associées

La fonction de répartition conjointe $F$ du couple $\left( X, Y \right)$ est une application de $\mathbb{R}^2$ dans $\left[ 0, 1 \right]$ définie par :

$\forall \left( a, b \right) \in \mathbb{R}^2, F \left( a, b \right) = \Pr \left( X < a \textrm{ et } Y < b \right)$

Le couple $\left( X, Y \right)$ est absolument continu, s'il existe une fonction $f$ continue des deux variables $X$ et $Y$, appelée **densité de probabilité conjointe du couple $\left( X, Y \right)$** telle que, pour tout domaine $D$ du plan, on ait :

$\Pr \left[ \left( X, Y \right) \in D \right] = \int_D \int f \left( x, y \right) \mathrm{d} x \mathrm{d} y$

Si le domaine $D$ est l'ensemble des couples $\left( x, y \right)$ tels que $x \leq a$ et $y \leq b$, on obtient :

$F \left( a, b \right) = \int_{-\infty}^{b} \mathrm{d} y \int_{a}^{-\infty} f \left( x, y \right) \mathbb{d} x$

Entre la densité $f$ et la fonction de répartition $F$, il existe la relation suivante :

$f \left( x, y \right) = \frac{\mathrm{d}^2 F \left( x, y \right)}{\mathrm{d} x \mathrm{d} y}$

Les **lois marginales** sont les lois des variables aléatoires $X$ et $Y$ prises séparément.

1. La fonction de répartition marginale de la variable $X$ vaut :

$\Pr \left( -\infty < X < a \textrm{ et } -\infty < Y < +\infty \right) = H \left( a \right) = \int_{-\infty}^{a} \mathrm{d} x \int_{-\infty}^{+\infty} f \left( x, y \right) \mathrm{d} y$

2. La fonction de répartition marginale de la variable $Y$ vaut :

$\Pr \left( -\infty < Y < b \textrm{ et } -\infty < Y < +\infty \right) = G \left( b \right) = \int_{-\infty}^{b} \mathrm{d} y \int_{-\infty}^{+\infty} f \left( x, y \right) \mathrm{d} x$

> [!NOTE]
> On peut aussi écrire les lois marginales tels que :
> $H \left( a \right)  = F \left( a, +\infty \right)$
> et
> $G \left( b \right)  = F \left( -\infty, b \right)$

Il est alors possible de calculer les **densités marginales** :

$h \left( x \right) = \int_{-\infty}^{+\infty} f \left( x, y \right) \mathrm{d} y$

et

$g \left( y \right) = \int_{-\infty}^{+\infty} f \left( x, y \right) \mathrm{d} x$

Il est alors possible de calculer les **densités conditionnelles** :

$h \left( x \setminus y \right) = \frac{f \left( x, y \right)}{g \left( y \right)}$

et

$g \left( y \setminus x \right) = \frac{f \left( x, y \right)}{h \left( x \right)}$

### Indépendance

Soient $f$, $h$ et $g$ les densités de probabilités du couple $\left( X, Y \right)$ et des variables $X$ et $Y$ prises séparément, alors les variables aléatoires continues $X$ et $Y$ sont indépendantes si et seulement si :

$f \left( x, y \right) = h \left( x \right) g \left( y \right)$

En analyse statistique, la question qui se pose souvent est de savoir, à la vue d'un tableau répartissant une population de taille $n$ selon des modalités définies par deux variables aléatoires $X$ et $Y$, si ces variables sont indépendantes ou non. Le test le plus utilisé est le test du ${\chi}^2$ qui consiste à comparer le tableau observé et le tableau théorique que l'on obtiendrait si les variables $X$ et $Y$ étaient indépendantes.

### Moments d'une distribution d'un couple de deux variables aléatoires

Le moment d'ordre $p$ par rapport à la variable $X$ et d'ordre $q$ par rapport à la variable $Y$ est l'espérance mathématique $m_{pq}$ de la variable aléatoire $X^p Y^q$. Il est défini, sous réserve de l'existence de l'intégrale et en désignant par $D$ le domaine de définition des variables aléatoires $X$ et $Y$, par :

$m_{pq} = \int_D \int x^p y^q f \left( x, y \right) \mathrm{d} x \mathrm{d} y$

Dans les relations de dépendance, il apparaît souvent clairement que l'une des variables permet d'estimer l'autre. On établit de fait une relation fonctionnelle entre les deux dont il convient d'estimer et de tester la nature (droite, parabole, *etc*.). C'est là qu'intervient la notion de régression, dont la principale méthode est celle des moindres carrés.

## Liens

- [Topo en format P.D.F.](./PDF/Seance-07-Chapitre-07.pdf)

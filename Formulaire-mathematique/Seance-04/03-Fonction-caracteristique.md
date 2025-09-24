# Fonction caractéristique

La **fonction caractéristique** (f.c. en abrégé) d'une variable aléatoire est l'espérance mathématique de la variable $\mathbb{E} \left( e^{itx} \right)$ ; elle est définie par :

$\forall t \in \mathbb{R}, {\varphi}_x \left( t \right) = \mathbb{E} \left( e^{itx} \right) = \int_{\mathbb{R}} e^{itx} \mathrm{d} {\Pr}_x$  

Elle correspond à la transformée de Fourier-Streltjes de sa mesure de probabilité.

Elle est utilisée pour étudier le comportement asymptotique de la somme de variables aléatoires indépendantes, car des théorèmes d'analyse permettent de remplacer l'étude de la convergence en loi par l'étude de la convergence des fonctions caractéristiques.

## Principales propriétés

Elles se déduisent des propriétés de la transformée de Fourier d'une fonction intégrable.

- **Propriété 1.** La fonction caractéristique d'une variable aléatoire détermine sans ambiguïté sa loi de probabilité. Deux variables aléatoires ayant la même fonction caractéristique ont la même loi de probabilité. Cela justifie l'emploi du terme « caractéristique » donné à la fonction $\varphi$.

-**Propriété 2.** Comme ${\Pr}_X$ est une mesure bornée et que $\left| e^{itx} \right| = 1$, la fonction ${\varphi}_X \left( t \right)$ existe, est bornée et continue pour toutes les valeurs de $t$.

- **Propriété 3.** Si la loi de la variable $X$ possède une densité, la fonction caractéristique s'obtient par l'intégrale :

$\forall t \in \mathbb{R}, {\varphi}_x \left( t \right) = \int_{\mathbb{R}} e^{itx} f \left( x \right) \mathrm{d} x$

-**Propriété 4.** Les propriétés de linéarité sont vérifiées.

${\varphi}_{\lambda X} \left( t \right) = {\varphi}_{X} \left( \lambda t \right)$

et

${\varphi}_{X + \alpha} \left( t \right) = {\varphi}_{X} \left( t \right) e^{it{\alpha}}$

- **Propriété 5.** En particulier, si $U$ est la variable aléatoire centrée réduite associée à la variable $X$, $U = \frac{X - \mu}{\sigma}$, on obtient :

${\varphi}_{U} \left( t \right) = e^{-\frac{itm}{\sigma}} {\varphi}_X \left( \frac{t}{\sigma} \right)$

et

${\varphi}_{U} \left( t \right) = e^{itm} {\varphi}_U \left( {\sigma}t \right)$

- **Propriété 6.** Si $\varphi$ est une fonction caractéristique, il en est de même de :
    - ${\varphi}^n$ avec $n \in \mathbf{N}$ ;

	- $\bar{\varphi}$ ;

	- $\left| \varphi \right|^2$ ;

	- la partie réelle de $\varphi$.

- **Propriété 7.** Soient deux variables aléatoires indépendantes $X$ et $Y$, il en est de même des variables aléatoires $e^{itX}$ et $e^{itY}$. La fonction caractéristique de la somme de deux variables aléatoires indépendantes est :

${\varphi}_{X + Y} \left( t \right) = \mathbb{E} \left( e^{it \left( X + Y \right)} \right) = {\varphi}_X \left( t \right) {\varphi}_Y \left( t \right)$

La fonction caractéristique de la somme de deux variables aléatoires indépendantes est égale au produit de leurs fonctions caractéristiques. Par exemple, la somme de deux variables aléatoires normales indépendantes est une variable aléatoire normale.

## Fonction caractéristique et moments

- **Propriété 1.** Si $\mathbb{E} \left( X^k \right)$ est finie pour un entier $k \geq 1$, alors $\varphi$ est continûment dérivable jusqu'à l'ordre $k$ inclus. On peut calculer ses dérivées par dérivation sous le signe d'intégration. On obtient :

${\varphi}_X \left( 0 \right) = 1$

et

${\varphi}_{X^k} \left( t \right) = i^k \mathbb{E} \left( X^k \right)$

- **Propriété 2.** Si ${\varphi}_X \left( t \right)$ est de classe $C^{\infty}$, la formule de Mac-Laurin donne :

${\varphi}_X \left( t \right) = \sum_{k = 0}^{+\infty} \frac{t^k}{k!} i^k \mathbb{E} \left( X^k \right)$

**Exemple.** Les moments de la loi normale centrée réduite.

${\varphi}_U \left( t \right) = e^{-\frac{t^2}{2}} = 1 - \frac{t^2}{2} + \frac{1}{2!} \left( -\frac{t^2}{2} \right)^2 + \ldots{} + \frac{1}{k!} \left( -\frac{t^2}{2} \right)^k + \ldots{}$

${\varphi}_U \left( t \right) = \sum_{k = 0}^{+\infty} \frac{t^k}{k!} i^k \mathbb{E} \left( X^k \right)$

$\Rightarrow \left\lbrace  \begin{array}{l} \textrm{Les moments d'ordre impair sont nuls.} \\ \textrm{Les moments d'ordre pair sont égaux à } {\mu}_{2k} = \frac{\left( 2k \right)!}{{2^k} k!} \end{array} \right.$

## Inversion de la fonction caractéristique

Les formules d'inversion de la transformée de Fourier permettent d'obtenir la densité de la loi $X$ connaissant ${\varphi}_X \left( t \right)$.

1. $X$ admet une densité $f \left( x \right)$, continue, définie par l'intégrale :

$f \left( x \right) = \frac{1}{2\pi} \int_{\mathbb{R}} {\varphi}_{X} \left( t \right) e^{-itx} \mathrm{d} t$

2. Sinon, le résultat est le suivant :

$f \left( b \right) - f \left( a \right) = \frac{1}{2\pi} \lim_{T \rightarrow +\infty} \int_{-T}^{T} {\varphi}_{X} \left( t \right) \frac{e^{-itb} - e^{-ita}}{it} \mathrm{d} t$

## Exemples de fonctions caractéristiques

| **Loi** | **Fonction caractéristique** |
| --- | :-: |
| Loi de Bernoulli | ${\varphi}_X \left( t \right) = {\rho}e^{-it} + q$ avec $q = 1 - p$ |
 | Loi binomiale $B \left( n, p \right)$ | ${\varphi}_X \left( t \right) = \left( {\rho}e^{-it} + q \right)^n$ |
 | Loi de Poisson $P \left( \lambda \right)$ | ${\varphi}_X \left( t \right) = e^{{\lambda}t \left( e^{-it} - 1 \right)}$ |
 
**Tableau 1. Fonctions caractéristiques des lois discrètes**

| **Loi** | **Fonction caractéristique** |
| --- | :-: |
| Loi  uniforme sur $\left[ a, b \right]$ | ${\varphi}_X \left( t \right) = \frac{\sin \left( at \right)}{at}$ |
 | Loi gamma $\Gamma \left( 1 \right)$ | ${\varphi}_X \left( t \right) = \frac{1}{1 - it}$ |
 | Loi gamma $\Gamma \left( r \right)$ | ${\varphi}_X \left( t \right) = \frac{1}{\left( 1 - it \right)^r}$ |
 | Loi normale réduite $N \left( 0, 1 \right)$ | ${\varphi}_X \left( t \right) = e^{-\frac{t^2}{2}}$ |
 | Loi normale réduite $N \left( \mu, \sigma \right)$ | ${\varphi}_X \left( t \right) = e^{itm} e^{-\frac{t^2 {\sigma}^2}{2}}$ |
 | Loi de Cauchy de densité $f \left( x \right) = \frac{1}{\pi} \frac{1}{1 + x^2}$ | ${\varphi}_X \left( t \right) = e^{- \mathrm{abs} \left( t \right)}$ |
 
**Tableau 2. Fonctions caractéristiques des lois continues**

## Liens

- [Topo en format P.D.F.](./PDF/03-Fonction-caracteristique.pdf)

# Produit de convolution de deux variables aléatoires

Le **produit de convolution** répond au problème suivant : connaissant la loi des variables aléatoires $X$ et $Y$, indépendantes ou non, quelle est la loi de la somme $Z = X + Y$ de ces deux variables.

## Cas de deux variables aléatoires discrètes

Le théorème de probabilités totales donne la solution.

$\begin{array}{l} \Pr \left( Z = z \right) = \sum_{i = 1}^{n} \Pr \left[ \left( X = x_i \right) \textrm{ et } \left( Y = z_i - x_i \right) \right] \\ \Pr \left( Z = z \right) = \sum_{i = 1}^{n} \Pr \left[ \left( Y = y_i \right) \textrm{ et } \left( X = z_i - y_i \right) \right] \end{array}$

On note deux cas possibles :

1. Si $X$ et $Y$ sont indépendantes alors :

$\begin{array}{l} \Pr \left( Z = z \right) = \sum_{i = 1}^{n} \Pr \left( X = x_i \right) \Pr \left( Y = z_i - x_i \right) \\ \Pr \left( Z = z \right) = \sum_{i = 1}^{n} \Pr \left( Y = y_i \right) \Pr \left( X = z_i - y_i \right) \end{array}$

2. Si $X$ et $Y$ ne sont pas indépendantes alors :

$\begin{array}{l} \Pr \left( Z = z \right) = \sum_{i = 1}^{n} \Pr \left( X = x_i \right) \Pr \left( Y = z_i - x_i \setminus X = x_i \right) \\ \Pr \left( Z = z \right) = \sum_{i = 1}^{n} \Pr \left( Y = y_i \right) \Pr \left( Y = z_i - y_i \setminus Y = y_i \right) \end{array}$

> [!WARNING]
> Les limites des variables $X$ et $Y$ doivent être compatibles avec la condition $Z = z$.

**Exemple.** La loi de Poisson est stable pour l'addition de variables aléatoires indépendantes.

## Cas de deux variables continues

La loi de probabilité de la variable $Z = X + Y$ est la mesure image ${\Pr}_{XY}$, loi de probabilité du couple $\left( X, Y \right)$ par l'application de $\mathbb{R}^2$ dans $\mathbb{R}$ définie par $\left( x, y \right) \rightarrow x + y$.

Si les variables aléatoires $X$ et $Y$ sont indépendantes, la loi de probabilité $\Pr \left( Z \right)$ de la variable aléatoire $Z = X + Y$ est la mesure image de ${\Pr}_X \otimes {\Pr}_Y$ par l'application de $\mathbb{R}^2$ dans $\mathbb{R}$ définie par $\left( x, y \right) \rightarrow x + y$. ${\Pr}_Z$ est le produit de convolution de ${\Pr}_X$ et ${\Pr}_Y$.

Pour tout borélien $B$ de $\mathbb{R}^2$, cette probabilité est définie par :

${\Pr}_z \left( B \right) = \int_{\mathbb{R}^2} {**1**}_B \left( x + y \right) \mathrm{d} {\Pr}_X \otimes {\Pr}_Y$

Les variables $X$ et $Y$ jouent des rôles symétriques.

Si les lois de probabilités des variables aléatoires indépendantes $X$ et $Y$ admettent des densités $f$ et $g$, l'expression précédente s'écrit :

${\Pr}_z \left( B \right) = \int_{\mathbb{R}^2} {**1**}_B \left( x + y \right) f \left( x \right) g \left( y \right) \mathrm{d} x \mathrm{d} y$

On pose $x + y = z$, $x = u$ et on applique le théorème de G. Fubini[^1] :

$\begin{array}{c} {\Pr}_z \left( B \right) = \int_{\mathbb{R}^2} {**1**}_B \left( z \right) f \left( u \right) g \left( z - u \right) \mathrm{d} u \mathrm{d} z \\ {\Pr}_z \left( B \right) = \int_{\mathbb{R}} {**1**}_B \left( z \right)\mathrm{d} z \int_{D_x} f \left( u \right) g \left( z - u \right) \mathrm{d} u \end{array}$

d'où la densité de la variable aléatoire $Z$ :

$k \left( z \right) = \int_{D_x} f \left( x \right) g \left( z - x \right) \mathrm{d} x = \int_{D_y} f \left( z - y \right) g \left( y \right) \mathrm{d} y$

dans laquelle $D_x$ et $D_y$ désignent les domaines de variables des variables aléatoires $X$ et $Y$, compatibles avec la condition $Z = z$.

Par intégration, on obtient la fonction de répartition de la variable $Z$ :

$K \left( z \right) = \Pr \left( Z < z \right) = \int_{D_x} f \left( x \right) G \left( z - x \right) \mathrm{d} x = \int_{D_y} F \left( z - y \right) g \left( y \right) \mathrm{d} y$

dans laquelle $F$ et $G$ désignent les fonctions de répartition des variables $X$ et $Y$.

\item[**Exemple.**] La loi gamma est stable pour l'addition des variables aléatoires indépendantes.

## Liens

- [Topo en format P.D.F.](./PDF/01-Produit-de-convolution-de-deux-variables-aleatoires.pdf)

## Notes de bas de page

[^1]: Guido Fubini (1879-1943)

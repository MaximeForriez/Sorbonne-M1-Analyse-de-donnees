# Produit scalaire et statistique

## Cas avec deux variables

On appelle $\mathbb{R}^n$ l'espace des individus et $\mathbb{R}^2$ l'espace des variables.

On pose :

$D_{\frac{1}{n}} = \frac{1}{n} I_n$

avec $I_n$ la matrice unité à $n$ lignes et $n$ colonnes.

$D_{\frac{1}{n}}$ est inclus dans l'espace des variables.

Le produit scalaire vaut :

${\left\langle X | Y \right\rangle}_{D_{\frac{1}{n}}} = {\left\langle X | D_{\frac{1}{n}} | Y \right\rangle} = \sum_{i = 1}^{n} \frac{1}{n} x_i y_i = \frac{1}{n} \left\langle X | Y \right\rangle$

avec $\left\langle X | Y \right\rangle$ le produit scalaire canonique de $\mathbb{R}^n$.

On note ${\mathbf{1}}_n = \left( \begin{array}{c} 1 \\ \ldots{} \\ 1 \end{array} \right)$ le vecteur dont toutes les coordonnées sont égales à 1, appelé le **vecteur unité de $\mathbb{R}^n$**. Ce vecteur est normé. Sa longueur est ${\left| \left| {\mathbf{1}}_n \right| \right|}_{D_{\frac{1}{n}}} = \frac{1}{n} \sum_{i = 1}^{n} 1 \times 1 = \frac{1}{n} n = 1$.

### Moyenne d'une variable statistique

La moyenne $\bar{X}$ de la variable statistique $X$ est donnée par :

$\bar{X} = \frac{1}{n} \sum_{i = 1}^{n} x_i = \frac{1}{n} \sum_{i = 1}^{n} x_i \times 1 = {\left\langle X | D_{\frac{1}{n}} | {\mathbf{1}}_n \right\rangle} = {\left\langle X | {\mathbf{1}}_n \right\rangle}_{D_{\frac{1}{n}}}$

La moyenne de $X$ est le produit scalaire de $X$ par le vecteur unité ${\mathbf{1}}_n$.

Soit $X_0 = X - \bar{X}$ la variable centrée correspondant à $X$. Pour chaque individu $i$ de la population :

$\begin{array}{l} X_0 = \left( \begin{array}{c} x_1 - \bar{X} \\ \ldots{} \\ x_n - \bar{X} \end{array} \right) = \left( \begin{array}{c} x_1 \\ \ldots{} \\ x_n \end{array} \right) - \bar{X} {\mathbf{1}}_n \\ X_0 = X - \bar{X} {\mathbf{1}}_n \\ \Leftrightarrow X = X_0 - \bar{X} {\mathbf{1}}_n \end{array}$

$X = X_0 - {\left\langle X | {\mathbf{1}}_n \right\rangle}_{D_{\frac{1}{n}}} {\mathbf{1}}_n$

### Variance d'une variable statistique

$s^2 \left( X \right) = \bar{{X_0}^2} = \frac{1}{n} \sum_{i = 1}^{n} \left( x_i - \bar{X} \right)^2 = \left\langle X_0 | D_{\frac{1}{n}} | X_0 \right\rangle$

$s^2 \left( X \right) = \left| \left| X_0 \right| \right|^2$

La variance de $X$ est le carré de la norme de la variable centrée.

### Covariance

La covariance de deux variables quantitatives réelles $X$ et $Y$ définies sur $\mathbb{R}^2$ est la moyenne du produit des variables centrées.

$\mathrm{cov} \left( X, Y \right) = \frac{1}{n} \sum_{i = 1}^{n} \left( x_i - \bar{X} \right) \left( y_i - \bar{Y} \right) = \left\langle X_0 | D_{\frac{1}{n}} | Y_0 \right\rangle = {\left\langle X_0 | Y_0 \right\rangle}_{D_{\frac{1}{n}}}$

On pose $Z$ la matrice des variables centrées $Z = \left[ X_0, Y_0 \right]$. La matrice de covariance $C$ vaut alors :

$C = {{}^t} Z.D_{\frac{1}{n}}.Z$

et, dans ce cas :

$C = \frac{1}{n} {{}^t} Z.Z$

La covariance est le produit scalaire des variables centrées.

### Coefficient de corrélation linéaire

$r_{X, Y} = \frac{\mathrm{cov} \left( X, Y \right)}{s \left( X \right) s \left( Y \right)} = \frac{\left\langle X_0 | D_{\frac{1}{n}} | Y_0 \right\rangle}{{\left| \left| X_0 \right| \right|}_{\phi} {\left| \left| Y_0 \right| \right|}_{\phi}} = \cos \left( X_0, Y_0 \right)$

Le coefficient de corrélation linéaire est le cosinus de l'angle des variables centrées.

## Prédicteur linéaire d'une régression linéaire

Soient $Y$ la variable à expliquer, $X$ la variable explicative, $X_0$ et $Y_0$ les variables centrées.

Le prédicteur linéaire ${\Delta}_{Y | X}$ est :

$y^{*} = a + bx$

c'est-à-dire

$y^{*} - \bar{Y} = b \left( x - \bar{X} \right)$

soit ${y_0}^{*} = b x_0$. Il est représenté par la droite de régression de $Y$ en $X$ dans l'espace des individus.

$b = \frac{\mathrm{cov} \left( X, Y \right)}{s^2 \left( X \right)} = \frac{{\left\langle X_0 | Y_0 \right\rangle}_{\frac{1}{n}}}{{{\left| \left| X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2}$

$b X_0 = \frac{{\left\langle X_0 | Y_0 \right\rangle}_{D{\frac{1}{n}}}}{{{\left| \left| X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2} X_0$ est le projeté orthogonal de $Y_0$ sur $X_0$, $Y_0 - b X_0$ est orthogonal à $X_0$, et **$b$ est la valeur minimisant l'expression** :

$\begin{array}{l} S^2 = \frac{1}{n} \sum_{i = 1}^{n} \left( Y_{0i} - b X_{0i} \right)^2 \\ S^2 = {{\left| \left| Y_0 - b X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2 \\ S^2 = s^2 \left( Y - bX \right) \\ S^2 = s^2 \left( Y - a - bX \right) \\ S^2 = s^2 \left( Y - Y^{*} \right) \\ S^2 = s^2 \left( Y_0 - {Y_0}^{*} \right)  \end{array}$

**Le prédicteur linéaire de la variable centrée $Y_0$ est le projeté orthogonal de $Y_0$ sur $X_0$ dans $\mathbb{R}^n$, c'est-à-dire la variable ${Y_0}^{*}$ minimisant la variance $Y_0 - {Y_0}^{*}$**.

$\begin{array}{l} s^2 \left( Y \right) = {{\left| \left| Y_0 \right| \right| }_{D_{\frac{1}{n}}}}^2 = {{\left| \left| Y_0 - b X_0 + b X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2 \\ s^2 \left( Y \right) = {{\left| \left| Y_0 - b X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2 + {{\left| \left| b X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2 \end{array}$

or ${{\left| \left| Y_0 - b X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2 = {S_{\min}}^2$ 

$s^2 \left( Y \right) = {S_{\min}}^2 + b^2 {{\left| \left| X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2$

or ${{\left| \left| X_0 \right| \right|}_{D_{\frac{1}{n}}}}^2 = s^2 \left( X \right)$

$\begin{array}{l} s^2 \left( Y \right) = {S_{\min}}^2 + b^2 s^2 \left( X \right) \\ s^2 \left( Y \right) = {S_{\min}}^2 + \left( \frac{\mathrm{cov} \left( X, Y \right)}{s^2 \left( X \right)} \right)^2 s^2 \left( X \right) \\ s^2 \left( Y \right) = {S_{\min}}^2 + \left( \frac{\mathrm{cov} \left( X, Y \right) s \left( X \right)}{s^2 \left( X \right)} \right)^2 \\ s^2 \left( Y \right) = {S_{\min}}^2 + \left( \frac{\mathrm{cov} \left( X, Y \right) s \left( Y \right)}{s \left( X \right) s \left( Y \right)} \right)^2 \\ s^2 \left( Y \right) = {S_{\min}}^2 + \left( \frac{\mathrm{cov} \left( X, Y \right)}{s \left( X \right) s \left( Y \right)} \right)^2 s^2 \left( Y \right) \\ \end{array}$

d'où

$s^2 \left( Y \right) = {S_{\min}}^2 + {r_{XY}}^2 s^2 \left( Y \right)$

${S_{\min}}^2$ correspond à la **variance résiduelle**. ${r_{XY}}^2 s^2 \left( Y \right)$ est la **variance expliquée par la régression**.
	
De manière symétrique, si $Y$ est la variable explicative et $X$ la variable à expliquer, on a :

$s^2 \left( X \right) = {S'_{\min}}^2 + {r_{XY}}^2 s^2 \left( X \right)$

## Cas généralisé avec plusieurs variables

On appelle $\mathbb{R}^n$ l'espace des individus et $\mathbb{R}^m$ l'espace des variables.

Un $n$-uplet de variables est un vecteur dans l'espace des individus.

Un $m$-uplet de variables est un vecteur dans l'espace des variables.

## Liens

- [Topo en format P.D.F.](./PDF/07-Produit-scalaire-et-statistique.pdf)

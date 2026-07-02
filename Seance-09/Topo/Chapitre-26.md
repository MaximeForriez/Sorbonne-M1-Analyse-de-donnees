# Analyse canonique

Pour conclure le cours sur les analyses statistiques multivariées, ce chapitre propose une petite synthèse sur ce que l'on appelle l'**analyse canonique**. Elle opère la synthèse entre les méthodes exploratoires et les méthodes explicatives. Ce chapitre est large inspiré par [^1] (p. 63-82).

L'analyse canonique fut inventée par Harold Hotelling en 1969[^2]. Elle constitue la base théorique de la plupart des méthodes d'analyse de données :

1. la régression multiple ;

2. l'analyse de la variance ;

3. l'analyse des correspondances ;

4. l'analyse discriminante.

**La méthode est difficilement interprétable**.

« Le but de l'analyse canonique est d'étudier les relations linéaires existant entre deux groupes de caractères qualitatifs observés sur un même ensemble d'individus. De façon plus précis, on cherche une combinaison linéaire des caractères du premier ensemble et une combinaison linéaire des caractères du deuxième qui soient les plus corrélées possibles »[^1] (p. 64).

On pose $n$ le nombre d'observations dans ${\mathbb{R}}^n$.

- Soient $p$ caractères du groupe 1 : $x^1$, $\ldots{}$, $x^j$, $\ldots{}$, $x^p$.

- Soient $q$ caractères du groupe 2 : $y^1$, $\ldots{}$, $y^k$, $\ldots{}$, $y^q$.

On établit des combinaisons linéaires des caractères des deux groupes :

$\xi = a_1 x^1 + \ldots{} + a_j x^j + \ldots{} + a_p x^p$

$\eta =  = b_1 y^1 + \ldots{} + b_k y^k + \ldots{} + b_q y^q$

> [!WARNING]
> $x^1$, $y^1$, $\ldots{}$, utilisent des **indices** en exposant.

On isole les coefficients.

${{}^t}a = \left( \begin{array}{ccccc} a_1 & \ldots{} & a_j & \ldots{} & a_p \end{array} \right)$

${{}^t}b = \left( \begin{array}{ccccc} b_1 & \ldots{} & b_k & \ldots{} & b_q \end{array} \right)$

Ils maximisent le carré de corrélation entre $\xi$ et $\eta$.

On appelle **caractères canoniques** les vecteurs $\xi$ et $\eta \in {\mathbb{R}}^n$, **facteurs canoniques** les vecteurs de coefficient $a \in {\mathbb{R}}^p$ et $b \in {\mathbb{R}}^q$, et **corrélation canonique** le coefficient de corrélation entre $\xi$ et $\eta$.

L'ensemble des caractères $\xi$, combinaisons linéaires des $x^1, \ldots{}, x^j, \ldots{}, x^p$, forme un sous-espace vectoriel $W_1$ de ${\mathbb{R}}^n$ que l'on appelle **potentiel de précision** du premier groupe.

L'ensemble des caractères $\eta$, combinaisons linéaires des $y^1, \ldots{}, ykj, \ldots{}, y^q$, forme un sous-espace vectoriel $W_2$ de ${\mathbb{R}}^n$ que l'on appelle **potentiel de précision** du deuxième groupe.

La question revient à déterminer deux vecteurs $\xi \in W_1$ et $\eta \in W_2$ faisant un **angle minimal**.
> [!NOTE]
> Si les caractères sont centrées, cosinus et corrélation sont liés. Il existe une solution triviale : ${\eta}^1$ et ${\xi}^1$ tels que ${\cos}^2 \left( {\eta}^1, {\xi}^1 \right) = 1$. Lorsqu'un premier couple de variables canoniques a été obtenu, on recherche un autre couple de caractères ${\eta}^2$ et ${\xi}^2$ tels que $\rho \left( {\eta}^2, {\xi}^2 \right)$ soit maximal et tel que ${\eta}^1$ et${\eta}^2$, et ${\xi}^1$ et ${\xi}^2$, aient chacun une **corrélation nulle**. On répète le processus jusqu'à $p$ ou $q$ caractères.

> [!NOTE]
> Le problème de l'analyse canonique peut être rapproché de celui de la régression multiple.

## Formulation géométrique de l'analyse canonique

### Projection orthogonale sur un sous-espace vectoriel

Avant de résoudre le problème de l'analyse canonique, on pose celui de la régression multiple. Soit un caractère « à expliquer » $y$ et de $p$ caractères « explicatifs » $x^1$, $\ldots{}$, $x^j$, $\ldots{}$, $x^p$, on suppose que les $p + 1$ caractères sont observés sur le même ensemble de $n$ individus, chaque individu étant muni du poids $p_i > 0$ avec $\sum_{i = 1}^{n} p_i = 1$. à partir de là, il s'agit de déterminer une combinaison linéaire des $p$ caractères explicatifs :

$\xi = a_1 x^1 + \ldots{} + a_j x^j + \ldots{} + a_p x^p$

telle que $\xi$ soit le plus proche possible de $y$ au sens de la distance dans l'espace des caractères, c'est-à-dire le **critère des moindres carrés**.

Chacun des $p + 1$ caractères peut être représenté par un vecteur de ${\mathbb{R}}^n$ :

$y = \left( \begin{array}{c} y_1 \\ \ldots{} \\ y_i \\ \ldots{} \\ y_n \end{array} \right) \in {\mathbb{R}}^n$

et

$x^j = \left( \begin{array}{c} x_1^j \\ \ldots{} \\ y_i^j \\ \ldots{} \\ y_n^j \end{array} \right) \in {\mathbb{R}}^n$

avec $j = 1, 2, \ldots{}, p$.

On suppose que les $p + 1$ caractères sont centrés :

$\sum_{i = 1}^{n} p_i y_i = 0$

et

$\sum_{i = 1}^{n} p_i x_i^j = 0$

avec $j = 1, 2, \ldots{}, p$.

Soit le sous-espace vectoriel $W$ de ${\mathbb{R}}^n$ engendré par les combinaisons linéaires des caractères $x^j$ :

$\xi \in W \Leftrightarrow \xi = a_1 x^1 + \ldots{} + a_j x^j + \ldots{} + a_p x^p$

On suppose que la dimension de $W$ est égale à $p$, ce qui revient à dire que les $p$ caractères $x^j$ forme une base de $W$, ou encore que le rang de la matrice :

$X_{np} = \left(  \begin{array}{ccccc} x_1^1 & \ldots{} & x_1^j & \ldots{} & x_1^p \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ x_i^1 & \ldots{} & x_i^j & \ldots{} & x_i^p \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  x_n^1 & \ldots{} & x_n^j & \ldots{} & x_n^p \\ \end{array} \right)$

est égal à $p$.

> [!NOTE]
> En notation abrégée, on pose :
> $W = \left\lbrace \xi \in {\mathbb{R}}^n / \xi = Xa \textrm{ avec } a \in {\mathbb{R}}^p \right\rbrace$

On suppose que l'espace des caractères est muni du produit scalaire associé à la matrice diagonale des poids :

$D = \left(  \begin{array}{ccccc} p_1 & \ldots{} & 0 & \ldots{} & 0 \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\ 0 & \ldots{} & p_i & \ldots{} & 0 \\ \ldots{} & \ldots{} & \ldots{} & \ldots{} & \ldots{} \\  0 & \ldots{} & 0 & \ldots{} & p_n \\ \end{array} \right)$

Sur l'espace des caractères centrés, le produit scalaire et la covariance sont **identiques** :

${{}^t}x^i.D.x^k = s_{jk}$

De même, la norme et la variance sont **identiques** :

$\left| \left| x^j \right| \right|^2 = s_j^2$

La distance entre deux caractères est donnée par :

$d^2 \left( x^i, x^k \right) = \left| \left| x^i - x^k \right| \right|^2 = {{}^t}\left( x^j - x^k \right).D.\left( x^i - x^k \right)$

$y \in {\mathbb{R}}^n$ est donné. On cherche $\xi \in W$ tel que la distance entre $y$ et $\xi$ soit minimale. En appliquant le critère des moindres carrés, on peut écrire :

$\min_{\xi \in W} \left| \left| y - \xi \right| \right|^2$

Cela permet de détermine $\hat{y}$, le point de $W$ le plus proche de $y$. $\hat{y}$ **est la projection orthogonale de** $y$ **sur** $W$.

### Recherche du projecteur orthogonal sur $W$

Le **projecteur orthogonal** sur $W$ est l'application linéaire de ${\mathbb{R}}^n$ dans ${\mathbb{R}}^n$ faisant correspondre à tout vecteur de ${\mathbb{R}}^n$ sa projection orthogonale sur $W$. On note $A$ la matrice de cette application :

$y \rightarrow A.y = \hat{y}$

avec la condition d'orthogonalité vérifiée ${{}^t}\left( y - \hat{y} \right).D.\hat{y} = 0$.

**Comment construire** $A$ **à partir des vecteurs** $x^1$, $\ldots{}$, $x^j$, $\ldots{}$, $x^p$**, base de** $W$** ?** Tout vecteur $\xi \in W$ peut s'écrire sous la forme : $\xi = X.a$, en particulier $\hat{y} \in W$, pour lequel on pose : $\hat{y} = X.\hat{a}.\left( y - \hat{y} \right)$ est orthogonal à tout vecteur de $W$, donc, en particulier, aux vecteurs de base. Par conséquent, il existe $p$ équations : ${{}^t}x^j.D.\left( y = \hat{y} \right) = 0$ avec $j = 1, 2, \ldots{}, p$, ou, puisque $\hat{y} = X.\hat{a}$ :

${{}^t}x^j.D.y = {{}^t}x^j.D.X.\hat{a}$

avec $j = 1, 2, \ldots{}, p$. Cela peut s'écrire sous la forme d'une seule équation matricielle :

${{}^t}X.D.X.\hat{a} = {{}^t}X.D.y$

Puisque le rang de $X$ vaut $p$, la matrice ${{}^t}X.D.X$ est **inversible**, ce qui permet de déterminer $\hat{a}$ en application des systèmes linéaires :

$\hat{a} = \left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D.y$

Le vecteur $\hat{a}$ contient les $p$ coefficients de la combinaison linéaire $\hat{y} = {\hat{a}}_1 x^1 + \ldots{} + {\hat{a}}_j x^j + \ldots{} + {\hat{a}}_p x^p \in W$ **la plus proche** de $y$.

De l'expression de $\hat{a}$, on trouve l'expression recherchée de $\hat{y} = X.\hat{a}$

$\hat{y} = X.\left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D.y$

La matrice $X.\left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D$ fait correspondre à $y$ sa projection orthogonale sur $W$. On déduit la matrice recherchée $A$ :

$A = X.\left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D$

### Recherche de la droite $W$ faisant un angle minimal

**Comment prouver que** $\hat{y}$ **est un vecteur de** $W$ **faisant un angle minimal avec** $y$** ?** D'après le théorème de Pythagore, $\left| \left| y \right| \right|^2 = \left| \left| y - \hat{y} \right| \right|^2 + \left| \left| \hat{y} \right| \right|^2$, donc minimiser $\left| \left| y - \hat{y} \right| \right|^2$ revient à maximiser $\left| \left| \hat{y} \right| \right|^2$ puisque $\left| \left| \hat{y} \right| \right|^2$ est une constante. $\hat{y}$ est le vecteur $W$ maximisant :

${}^2 \left( y, \hat{y} \right) = \frac{\left| \left| \hat{y} \right| \right|^2}{\left| \left| y \right| \right|^2}$

ce qui est par conséquent l'angle minimal entre $y$ et $\hat{y}$.

> [!NOTE]
> Comme $y$ et $x^i$ sont centrés, le cosinus entre $y$ et $\hat{y}$ est le **coefficient de corrélation** entre les caractères $y$ et $\hat{y}$.

## Recherche des caractères canoniques

### Présentation géométrique

Soient deux ensemble de caractères : $x^1$, $\ldots{}$, $x^j$, $\ldots{}$, $x^p$ et $y^1$, $\ldots{}$, $y^k$, $\ldots{}$, $y^q$, on suppose que les $p + q$ caractères sont observés sur le même ensemble de $n$ individus munis de poids $p_i > 0$ avec $i = 1, 2, \ldots{}, n$ et $\sum_{i = 1}^{n} p_i = 1$. On suppose que les $p + q$ caractères sont centrés. Chacun des $p + q$ caractères peut être représenté par un vecteur de ${\mathbb{R}}^n$. :

$x^j = \left( \begin{array}{c} x_1^j \\ \ldots{} \\ y_i^j \\ \ldots{} \\ y_n^j \end{array} \right)$

avec $j = 1, \ldots{}, p$, et

$y = \left( \begin{array}{c} y_1^k \\ \ldots{} \\ y_i^k \\ \ldots{} \\ y_n^k \end{array} \right)$
	
avec $k = 1, \ldots{}, q$.

Aux vecteurs, $x^j$ et $y^k$, on associe respectivement les sous-espaces vectoriels de ${\mathbb{R}}^n$, $W_1$ et $W_2$ :

$W_1 = \left\lbrace \xi \in {\mathbb{R}}^n / \xi = X.a, a \in {\mathbb{R}}^p \right\rbrace$

$W_2 = \left\lbrace \eta \in {\mathbb{R}}^n / \eta = X.b, b \in {\mathbb{R}}^q \right\rbrace$

avec $X_{np}$ et $Y_{nq}$ les matrices contenant respectivement en colonnes les vecteurs $x^i$ et $y^k$ étant centrés, leurs sous-espaces vectoriels respectifs $W_1$ et $W_2$ contiennent des vecteurs centrés.

On suppose que les $X^j$ et les $y^k$ forment respectivement une base de $W_1$ et une base de $W_2$, donc :

$\dim \left( W_1 \right) = p$

et

$\dim \left( W_2 \right) = q$

et

$\mathrm{rg } \left( X \right) = p$

et

$\mathrm{rg } \left( Y \right) = q$

Cela permet de formuler **géométriquement** le problème de l'analyse canonique. Il s'agit de détermine $\xi \in W_1$ et $\eta \in W_2$ tels que :

${\cos}^2 \left( \eta, \xi \right) = \rho \left( \xi, \eta \right)$

soit un **maximum**.

> [!NOTE]
> Les vecteurs centrés ou **centrés réduits** ont un angle $\xi = X.a$ et $\eta = X.b$ **identique**. En pratique, on effectue généralement les calculs sur des caractères centrés **et** réduits.

En analyse canonique, on recherche **simultanément** une combinaison linéaire des variables du premier groupe, notée $\xi$, et une combinaison linéaire des variables du second groupe, notée $\eta$, telles que le coefficient de corrélation entre $\xi$ et $\eta$ soit maximal. Ce couple étant trouvé, on en recherche un deuxième orthogonal au premier qui satisfait le même critère, *etc*.

### Recherche des caractères canoniques

Si les caractères ${\xi}^1$ et ${\eta}^1$ sont solutions du problème de l'analyse canonique, puisque l'angle entre $\xi$ et $\eta$ ne dépend pas de leur norme, on suppose que $\left| \left| \xi \right| \right| = \left| \left| \eta \right| \right| = 1$.

${\eta}^1$ doit être colinéaire avec la projection orthogonale de ${\xi}^1$ sur $W_2$ qui est le vecteur de $W_2$ faisant un angle minimal avec ${\xi}^1$. Cette condition s'écrit :

$A_2.{\xi}^1 = {\rho}_1.{\eta}^1$

avec ${\rho}_1 = \cos \left( {\xi}^1, {\eta}^1 \right)$ et $A_2$ l'opérateur de projection orthogonale sur $W_2$. De même, on a :

$A_1.{\eta}^1 = {\rho}_1 {\xi}^1$

On en déduit le système linéaire :

$A_1.A_2.{\xi}^1 = {\lambda}_1.{\xi}^1$

$A_2.A_1.{\xi}^1 = {\lambda}_1.{\xi}^1$

avec ${\lambda}_1 = {{\rho}_1}^2 = {\cos}^2 \left( {\xi}^1, {\eta}^1 \right)$. On en déduit que ${\xi}^1$ et ${\eta}^1$ sont respectivement **vecteurs propres** des opérateurs $A_1.A_2$ et $A_2.A_1$ associés à la même plus grande **valeur propre** ${\lambda}_1$, égale à leur cosinus carré, c'est-à-dire à leur corrélation au carré.

Les caractères ${\xi}^1$ et ${\eta}^1$ se déduisent l'un de l'autre par une simple application linéaire :

${\eta}^1 = \frac{1}{\sqrt{{\lambda}_1}}.A_2.{\xi}^1$

${\xi}^1 = \frac{1}{\sqrt{{\lambda}_1}}.A_1.{\eta}^1$

Les caractères canoniques suivants sont les vecteurs propres de $A_1.A_2$ et $A_2.A_1$ associés avec des valeurs propres rangées par ordre décroissant. On peut prouver que les vecteurs propres de $A_1.A_2$ sont orthogonaux pour $D$, et que, par conséquent, ${\cos}^2 \left( {\xi}^i, {\xi}^j \right) = {\cos}^2 \left( {\eta}^i, {\eta}^j \right) = 0$ lorsque $i \neq j$. **À chaque étape, on choisit le couple de caractères canoniques** ${\xi}^i$**,** ${\eta}^i$ **associé à la plus grande valeur propre** ${\lambda}_i$ **non encore sélectionnée**.

> [!NOTE]
> Le nombre maximal de caractères canoniques est égal à $\min \left( p, q \right)$. En supposant $p < q$, les ${\xi}^i$ avec $i = 1, \ldots{}, p$, forment une base $W$ dans laquelle il est impossible d'obtenir d'autres vecteurs appartenant à $W_1$ et orthogonaux aux ${\xi}^i$.

### Recherche des facteurs canoniques

Puisque $\xi \in W_1$, $\xi$ peut s'écrire comme une combinaison linéaire des caractères $x^1$, $\ldots{}$, $x^j$, $\ldots{}$, $x^p$ :

$\xi = a_1 x^1 + \ldots{} + a_j x^j + \ldots{} + a_p x^p$

Si on pose ${{}^t}a = \left( \begin{array}{ccccc} a_1 & \ldots{} & a_j & \ldots{} & a_p \end{array} \right)$, on peut l'écrire plus simplement :

$\xi = X.a$

et

$\eta = X.b$

Les facteurs canoniques $a$ et $b$ peuvent être calculés **directement**. En posant :

$A_1 = X.\left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D$

et

$A_2 = Y.\left( {{}^t}Y.D.Y \right)^{-1}.{{}^t}Y.D$

et en remplaçant dans les équations donnant $\xi$ et $\eta$, on obtient :

$X.\left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D.Y.\left( {{}^t}Y.D.Y \right)^{-1}.{{}^t}Y.D.a = {\lambda}.X.a$

$Y.\left( {{}^t}Y.D.Y \right)^{-1}.{{}^t}Y.D.X.\left( {{}^t}X.D.X \right)^{-1}.{{}^t}X.D.b = {\lambda}.X.b$

Pour rendre plus lisible les équations, on pose :

- les variances :

$V_{11} = {{}^t}X.D.X$

$V_{22} = {{}^t}Y.D.Y$

- les covariances :

$V_{12} = {{}^t}X.D.Y$

$V_{21} = {{}^t}X.D.Y$

ce qui devient :

$X.V_{11}^{-1}.V_{12}.V_{22}^{-1}.V_{21}.a = {\lambda}.X.a$

$Y.V_{22}^{-1}.V_{21}.V_{11}^{-1}.V_{12}.b = {\lambda}.X.b$

**Les facteurs canoniques correspondent aux vecteurs propres de produits de matrices de covariance**.

Les conditions de normalisation $\left| \left| \xi \right| \right|^2 = \left| \left| \eta \right| \right|^2 = 1$ deviennent :

${{}^t}\xi.D.\xi = {{}^t}a.{{}^t}X.D.X.a = {{}^t}a.V_{11}.a = 1$

${{}^t}\eta.D.\eta = {{}^t}b.{{}^t}X.D.X.b = {{}^t}b.V_{22}.b = 1$

Pour finir, $a$ et $b$ se déduisent l'un de l'autre par transformation linéaire. $\eta = \frac{1}{\sqrt{\lambda}} A_2.\xi$ devient $Y.b = \frac{1}{\sqrt{\lambda}} Y.\left( {{}^t}Y.D.Y \right)^{-1}.{{}^t}Y.D.X.a$, et en simplifiant, on peut écrire :

$b = \frac{1}{\sqrt{\lambda}} {V_{22}}^{-1}.V_{21}.a$

et, de même, pour $a$, on peut écrire :

$a = \frac{1}{\sqrt{\lambda}} {V_{11}}^{-1}.V_{12}.b$

En pratique, on recherche $a$ si $p < q$ afin de travailler sur la matrice de plus petite taille, puis on déduira $b$.

## Conclusion générale

**L'intérêt de l'analyse canonique réside essentiellement dans ses aspects méthodologiques**. La régression multiple n'en est qu'un cas particulier. De même, pour l'A.C.P., l'A.F.C., l'A.C.M. ou l'A.D.F.

J. D. Carroll a proposé une généralisation de l'analyse canonique à l'analyse de plus de deux groupes de variables en 1968[^3]. Le principe de la généralisation est simple. On dispose de $m$ ensembles de caractères numériques centrés représentés par les tableaux $X_1, X_2, \ldots{}, X_j, \ldots{}, X_m$, soit $W_i$ le potentiel de prévision associé à $X_i$. On recherche un nouveau caractère $z \in {\mathbb{R}}^n$ maximisant la somme des corrélations :

$\sum_{i = 1}^{m} {\mathrm{cor }}^2 \left( z, {\xi}_i \right)$

avec ${\xi}_i \in W_i$.

> [!NOTE]
> $z$ est solution de $\left( \sum_{i = 1}^{m} A_i \right).z = {\mu}.z$.

> [!NOTE]
> Si $m = 2$, $z$ est colinéaire à la bissectrice de ${\xi}^1$ et ${\eta}^2$.

L'analyse canonique généralisée (ou analyse multicanonique) présente quatre particularités intéressantes :

1. l'analyse canonique simple dans le cas où $m = 2$ ;

2. l'A.C.P. dans le cas où il n'existe qu'un seul caractère par groupe. L'A.C.P. est une analyse canonique généralisée de groupes de variables réduits chacun à un élément. Les composantes principales sont les variables générales et les variables canoniques sont confondues avec les variables initiales ;

3. l'A.C.M. dans le cas où les tableaux $X_i$ sont des tableaux de variables indicatrices. L'A.C.M. est une analyse canonique généralisée dans laquelle les groupes de variables sont composés chacun par les indicatrices des classes d'une même variable qualitative ;

4. l'A.F.M. dans le cas où les tableaux sont pondérés.

## Liens

- [Topo en format P.D.F.](./PDF/Seance-10-Chapitre-26.pdf)

## Notes de bas de page

[^1]: Bouroche, Jean-Marie & Saporta, Gilbert, 2002, *L'analyse de données*, Paris, P.U.F., 128 p. [Que sais-je ?]

[^2]: Hotelling, Harold, 1936, "Relation Between Two Sets of Variates", *Biometrika*, vol. 28, n°3/4, p. 321-377

[^3]: Carroll, J. Douglas, 1968, "A Generalisation of Canonical Correlation Analysis to Three ou More Sets of Variables", *Proceedings of the 76th Convention American Psychological Analysis*, Washington D.C., p. 227-228

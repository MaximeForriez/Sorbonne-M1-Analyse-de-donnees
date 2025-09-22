# Méthodes factorielles

Les méthodes factorielles sont des **analyses en axes principaux**. Elles permettent de dépouiller une enquête. Elles opèrent une **réduction** des variables en produisant des **visualisations graphiques**, et ce, en suivant toujours la même méthode :

1. créer un tableau de données ;

2. opérer la décomposition en valeurs singulières[^1] (D.V.S.) ;

3. adapter la D.V.S. au cas d'espèce (variables quantitatives, variables qualitatives, variables mixtes, *etc*.).

> [!WARNING]
> L'approche nécessite une connaissance de l'[algèbre linéaire](../../Formulaire-mathematique/Seance-09/05-Algebre%20lineaire.md).

## Le tableau de données

Un **tableau de données** présente une masse d'information sous la forme d'une matrice rectangulaire. Il se base sur la distinction entre deux analyses :

1. celle des individus ;

2. celle des caractères.

En lignes, notées $i = \left\lbrace 1, 2, \ldots{}, n \right\rbrace$, les individus sont représentés. En colonne, notées $j = \left\lbrace 1, 2, \ldots{}, p \right\rbrace$, les caractères sont représentés. Le tableau est noté $\mathbf{X}$. Il se décompose en :

- vecteurs lignes représentant les individus dans l'espace ${\mathbb{R}}^p$. Ils représentent un point avec $p$ coordonnées.
- vecteurs colonnes représentant les individus dans l'espace ${\mathbb{R}}^n$. Ils représentent un point avec $n$ coordonnées.

Chacune des deux dimensions du tableau de données permet de définir des **distances** (ou des proximités) entre les éléments définissant l'autre dimensions.

1. L'ensemble des colonnes permet de définir des distances (ou des proximités) entre lignes.

2. L'ensemble des lignes permet de calculer des distances (ou des proximités) entre colonnes.

**Les proximités géométriques traduisent des associations statistiques** soit entre les individus, soit entre les caractères.

Les tableaux de distances (ou de proximités) associés à ces représentations géométriques peuvent être décrits par les deux grandes familles de méthodes :

1. les méthodes en axes principaux (ou méthodes factorielles) : A.C.P., A.F.C., A.C.M., *etc*. ;

2. les méthodes de classification : nuées dynamiques, C.A.H., A.F.D., *etc*.

La métrique permet de calculer les distances entre points-lignes ou entre points-colonnes.

Les types de tableau possibles sont :

- le tableau de type « caractères-individus » ;

    - Ce tableau s'emploie avec des **variables quantitatives continues**.

    - La proximité entre caractères s'établit avec le calcul d'une corrélation. La proximité entre individus se caractérise par des similitudes globales entre les valeurs observées.

    - C'est le tableau d'entrée, par exemple, d'une analyse en composantes principales (A.C.P.).

- le tableau de contingences (ou binaire) ;

    - Le tableau de contingences est un tableau de comptages obtenu par le croisement entre **deux caractères nominaux**.

    - Les lignes et les colonnes jouent un rôle identique. La proximité s'établit en utilisant une distance ${\chi}^2$.

    - C'est le tableau d'entrée, par exemple, d'une analyse factorielle des correspondances (A.F.C.).

- le tableau disjonctif complet (T.D.C.) (ou tableau disjonctif joint ou tableau logique).

    - Le T.D.C. est un grand tableau contenant des **caractères nominaux**. Il croise les individus avec les modalités des caractères.

    - C'est le tableau d'entrée, par exemple, d'une analyse des correspondances multiples (A.C.M.).

## L'analyse factorielle

« L'analyse factorielle traite des tableaux de nombres et elle remplace un tableau difficile à lire par un tableau plus simple à lire qui soit une bonne approximation de celui-ci »[^2] (p. 5).

Que signifie mettre en facteur ? Comment procéder ? Soit une matrice $\mathbf{A}$, une analyse factorielle recherche des vecteurs $\mathbf{u}_i$ proportionnels à des facteurs ${\lambda}_i$ (les valeurs propres), c'est-à-dire :
    $\left( \mathbf{A} - \mathbf{I} \right).{\mathbf{u}_i} = {{\lambda}_i}{\mathbf{u}_i}$

avec $\mathbf{I}$ la matrice identité.

### Écart à l'indépendance

« Le respect de la proportion moyenne pour toutes les lignes du tableau correspond à ce que l'on nomme la **situation d'indépendance** »[^2] (p. 7). La situation d'indépendance aboutit à la déduction d'un **effectif théorique**. À partir de là, il est possible d'étudier l'**écart** entre la situation observée et la situation indépendante. « L'écart à l'indépendance nous permet de repérer s'il y a **attraction** entre une ligne et une colonne (écart positif), s'il y a **indépendance** entre la ligne et la colonne (écart nul), ou si au contraire il y a **répulsion** entre la ligne et la colonne (écart négatif) »[^2] (p. 10-11) En projetant orthogonalement les données sur les axes factoriels ($\mathbf{u}_i$) avec un produit scalaire, on peut proposer une autre définition des trois termes en utilisant l'angle de projection formé entre la droite définie par l'origine et le point projeté, et la droite définie par l'origine et le projeté du point. Cet angle $\theta$ varie entre 0 et $\pi$.

1. Si $\theta \in \left[ 0, \frac{\pi}{2} \right[$, alors on se situe dans une situation de conjonction, c'est-à-dire d'attraction.

2. Si $\theta = \frac{\pi}{2}$, alors on se situe dans une situation de quadrature, c'est-à-dire d'indépendance.

3. Si $\theta \in \left] \frac{\pi}{2}, \pi \right]$, alors on se situe dans une situation de opposition, c'est-à-dire de répulsion.

### Écart à l'indépendance pondérée : la distance du ${\chi}^2$

« Le principe de base de la décomposition factorielle [consiste] à remplacer le tableau initial par une **approximation de rang un** donc facile à lire, mais qui soit la plus proche possible au nom d'un certain critère. Dans le cas de l'analyse des correspondances, ce critère est le ${\chi}^2$ »[^2] (p. 21) Il s'agit d'un écart à l'indépendance **pondéré**, appelé la **contribution au** ${\chi}^2$.

Soit $\mathbf{T}$ un tableau de données.

$\mathbf{T} = \left( \begin{array}{ccc} 13 & 2 & 5\\ 20 & 2 & 8\\ 10 & 5 & 5\\ 7 & 1 & 22\\ \end{array} \right)$

On calcule les marges lignes, composantes d'un vecteur ligne calculées en additionnant les effectifs des colonnes :

$\begin{array}{l} 13 + 20 + 10 + 7 = 50\\ 2 + 2 + 5 + 1 = 10\\ 5 + 8 + 5 + 22 = 40 \end{array}$

ce qui donne le vecteur $\left( \begin{array}{ccc} 50 & 10 & 40 \end{array} \right)$.

On calcule les marges colonnes, composantes d'un vecteur colonne calculées en additionnant les effectifs des lignes :

$\begin{array}{l} 13 + 2 + 5 = 20\\ 20 + 2 + 8 = 30\\ 10 + 5 + 5 = 20\\ 7 + 1 + 22 = 30 \end{array}$

ce qui donne le vecteur $\left( \begin{array}{c} 20\\ 30\\ 20\\ 30 \end{array} \right)$.

L'effectif total $n$ vaut : $n = 100$. Il permet de calculer les effectifs théoriques ${\mathbf{T}}_0$ à partir des marges lignes et des marges colonnes. On calcule les moyennes marginales des lignes :

$\left( \begin{array}{ccc} \frac{50}{100} & \frac{10}{100} & \frac{40}{100} \end{array} \right) = \left( \begin{array}{ccc} \frac{1}{2} & \frac{1}{10} & \frac{2}{5} \end{array} \right)$

On utilise la matrice du vecteur marginale colonne et la matrice diagonale des moyennes marginales des lignes pour calculer l'effectif théorique en fonction des marges lignes.

$\left( \begin{array}{ccc} 20 & 20 & 20\\ 30 & 30 & 30\\ 20 & 20 & 20\\ 30 & 30 & 30 \end{array} \right) . \left( \begin{array}{ccc} \frac{1}{2} & 0 & 0\\ 0 & \frac{1}{10} & 0\\ 0 & 0 & \frac{2}{5} \end{array} \right) = \left( \begin{array}{ccc} 10 & 2 & 8\\ 15 & 3 & 12\\ 10 & 2 & 8\\ 15 & 3 & 12 \end{array} \right)$

En calculant les effectifs théoriques à partir des moyennes marginales des colonnes :

$\left( \begin{array}{c} \frac{1}{5}\\ \frac{3}{10}\\ \frac{1}{5}\\ \frac{3}{10} \end{array} \right)$

On obtient un résultat identique.

$\left( \begin{array}{cccc} \frac{1}{5} & 0 & 0 & 0\\ 0 & \frac{3}{10} & 0 & 0\\ 0 & 0 & \frac{1}{5} & 0\\ 0 & 0 & 0 & \frac{3}{10} \end{array} \right) . \left( \begin{array}{ccc} 50 & 10 & 40\\ 50 & 10 & 40\\ 50 & 10 & 40\\ 50 & 10 & 40 \end{array} \right) = \left( \begin{array}{ccc} 10 & 2 & 8\\ 15 & 3 & 12\\ 10 & 2 & 8\\ 15 & 3 & 12 \end{array} \right)$

Pour utiliser le ${\chi}^2$, on procède en trois étapes.

1. $\mathbf{T} - {\mathbf{T}}_0 = \mathbf{R}$ permet d'obtenir l'écart entre les valeurs observées et les valeurs théoriques.

$\left( \begin{array}{ccc} 13 & 2 & 5\\ 20 & 2 & 8\\ 10 & 5 & 5\\ 7 & 1 & 22\\ \end{array} \right) - \left( \begin{array}{ccc} 10 & 2 & 8\\ 15 & 3 & 12\\ 10 & 2 & 8\\ 15 & 3 & 12 \end{array} \right) = \left( \begin{array}{ccc} 3 & 0 & -3\\ 5 & -1 & -4\\ 0 & 3 & -3\\ -8 & -2 & 10 \end{array} \right)$

2. On divise les éléments de $r_{ij}$ par les éléments de $t_{0_{ij}}$ :

${\mathbf{T}}_1 = \left( \begin{array}{ccc} \frac{3}{10} & 0 & -\frac{3}{8}\\ \frac{1}{3} & -\frac{1}{3} & -\frac{1}{3}\\ 0 & \frac{3}{2} & -\frac{3}{8}\\ -\frac{8}{15} & -\frac{2}{3} & \frac{5}{6} \end{array} \right)$

3. On calcule l'écart pondéré en multipliant les éléments $r_{ij}$ par les éléments de $t_{1_{ij}}$. C'est la contribution au ${\chi}^2$ de chaque valeur $\left( i, j \right)$ :

${\chi}^{2}_{ij} = \left( \begin{array}{ccc} \frac{9}{10} & 0 & \frac{9}{8}\\ \frac{5}{3} & \frac{1}{3} & \frac{4}{3}\\ 0 & \frac{9}{2} & \frac{9}{8}\\ \frac{64}{15} & \frac{4}{3} & \frac{25}{3} \end{array} \right)$

La contribution totale du ${\chi}^2$ vaut :

${\chi}^2 = \sum_{i = 1}^{n} \sum_{j = 1}^{=} {\chi}^2_{ij} = \frac{9}{10} + 0 + \frac{9}{8} + \frac{5}{3} + \frac{1}{3} + \frac{4}{3} + 0 + \frac{9}{2} + \frac{9}{8} + \frac{64}{15} + \frac{4}{3} + \frac{25}{3}$

donc ${\chi}^2 = \frac{299}{12} \approx 24,917$.

On peut calculer la part du ${\chi}^2$ de chaque ligne, de chaque colonne, de chaque élément. Idéalement, on convertit les valeurs brutes en pourcentage. 

« L'indice ${\chi}^2$ est une approximation de la quantité d'information (au sens de la théorie mathématique de l'information) »[^2] (p. 24).

- Si ${\chi}^2 = 0$, alors l'indépendance entre les lignes et les colonnes est validée.

- Si ${\chi}^2_{ij} = 0$, alors les valeurs du couple $\left( i, j \right)$ sont indépendantes entre elles.

La **contribution absolue** est notée ${\phi}^2$.

${\phi}^2 = \frac{{\chi}^2}{n} = \frac{299}{12000} \approx 0,249$

On peut calculer pour chaque couple un ${\phi}^2_{ij}$ à partir de chaque ${\chi}^2_{ij}$. Comme le ${\chi}^2$, il vaut mieux exprimer les valeurs en pourcentage.

La décomposition du ${\chi}^2$ est additive. Chaque facteur calculé peut être utilisé.

${\chi}^2 = {\lambda}_1 {\chi}^2 + {\lambda}_2 {\chi}^2 + \ldots{}$

De fait, ${\lambda}_1 {\chi}^2$ est la contribution au ${\chi}^2$ de l'axe 1, ${\lambda}_2 {\chi}^2$, la contribution au ${\chi}^2$ de l'axe 2, *etc*.

« Pour bien utiliser une méthode statistique comme l'analyse factorielle, comprendre son fonctionnement est nécessaire **mais non suffisant** : il faut aussi en acquérir une expérience, en quelque sorte **étalonner** la méthode pour son propre compte, voir ses réactions dans telle ou telle situation »[^2] (p. 68).

## La décomposition en valeurs singulières (D.V.S.)

Il s'agit ici de détailler le calcul général des facteurs $\lambda$. Soit $\mathbf{X}$ une matrice ayant $n$ lignes et $p$ colonnes. $n \times p$ est le nombre d'éléments.

### Recherche d'une droite de régression orthogonale dans le nuage des caractères

On recherche un vecteur $\mathbf{u}$ tel que $\mathbf{X}\mathbf{u}$ avec la contrainte ${{}^t}\mathbf{u}.\mathbf{u} = 1$. Cela permet de maximiser la distance entre le vecteur projeté et l'origine du vecteur $\mathbf{u}$ recherché. La répétition de la manipulation permet de définir tous les axes de projection.

Le vecteur unitaire ${\mathbf{u}}_1$ qui caractérise le sous-espace à une dimension ajustant au mieux le nuage des $n$ points individus dans ${\mathbb{R}}^p$, est le **vecteur propre** de la matrice diagonalisée ${{}^t}\mathbf{X}.\mathbf{X}$ d'ordre $\left( p, p \right)$ correspondant à la plus grande **valeur propre** ${\lambda}_1$. L'axe définit par ${\mathbf{u}}_1$ est le premier **axe factoriel** (ou principal).

L'analyse générale effectue une rotation du repère autour de l'origine $O$ et fournit un système de **vecteurs orthonormés** : ${\mathbf{u}}_1$, $\left(  {\mathbf{u}}_1,  {\mathbf{u}}_2 \right)$, $\ldots{}$, $\left(  {\mathbf{u}}_1, {\mathbf{u}}_2, \ldots{}, {\mathbf{u}}_p \right)$ passent au plus près du nuage étudié.

On note $\mathbf{u_{\alpha}}$ le vecteur propre de la matrice ${{}^t}\mathbf{X}.\mathbf{X}$ correspondant à la valeur propre $\mathbf{{\lambda}_{\alpha}}$.

### Ajustement du nuage des variables dans l'espace des individus

On recherche ici le vecteur unitaire $\mathbf{v}$ tel que ${{}^t}\mathbb{X}.\mathbf{v}$ avec la contrainte ${{}^t}\mathbf{v}.\mathbf{v} = 1$.

On utilise la matrice diagonalisée $\mathbf{X}.{{}^t}\mathbf{X}$ d'ordre $\left( n, n \right)$

On note $\mathbf{v_{\alpha}}$ le vecteur propre normé de la matrice $\mathbf{X}.{{}^t}\mathbf{X}$ correspondant à la valeur propre $\mathbf{{\mu}_{\alpha}}$.

### Relation entre les deux espaces

Dans ${\mathbb{R}}^p$, on a : ${{}^t}\mathbf{X}.\mathbf{X}.\mathbf{u_{\alpha}} = \mathbf{{\lambda}_{\alpha}}.\mathbf{u_{\alpha}}$, tandis que, dans ${\mathbb{R}}^n$, on a : $\mathbf{X}.{{}^t}\mathbf{X}.\mathbf{v_{\alpha}} = \mathbf{{\mu}_{\alpha}}.\mathbf{v_{\alpha}}$.

À partir de la première équation, on peut écrire : $\left( \mathbf{X}.{{}^t}\mathbf{X} \right).\mathbf{X}.\mathbf{u_{\alpha}} = \mathbf{{\lambda}_{\alpha}}.\mathbf{X}.\mathbf{u_{\alpha}}$.

À partir de la seconde équation, on peut écrire : $\mathbf{X}.{{}^t}\mathbf{X}.\mathbf{v_{\alpha}}.{{}^t}\mathbf{v_{\alpha}} = \mathbf{{\mu}_{\alpha}}.\mathbf{v_{\alpha}}.{{}^t}\mathbf{v_{\alpha}}$, or, on avait posé la contrainte $\mathbf{v_{\alpha}}.{{}^t}\mathbf{v_{\alpha}} = 1$, donc $\mathbf{X}.{{}^t}\mathbf{X} = \mathbf{{\mu}_{\alpha}}$.

En combinant les deux résultats précédents, on obtient : $\mathbf{{\mu}_{\alpha}}.\mathbf{X}.\mathbf{u_{\alpha}} = \mathbf{{\lambda}_{\alpha}}.\mathbf{X}.\mathbf{u_{\alpha}}$, d'où $\mathbf{{\mu}_{\alpha}} = \mathbf{{\lambda}_{\alpha}}$. **Ce résultat est fondamental, car il unit les deux nuages de points**, caractères et individus. Pour chaque nuage, les vecteurs propres seront différents, pas les valeurs propres.

Les valeurs propres étant égales d'un nuage à l'autre, on en déduit les **formules de transition** entre ${\mathbb{R}}^p$ et ${\mathbb{R}}^n$.

$\left\lbrace \begin{array}{l} \mathbf{v_{\alpha}} = \frac{1}{\sqrt{{\lambda}_{\alpha}}}.\mathbf{X}.\mathbf{u_{\alpha}} \mathbf{u_{\alpha}} = \frac{1}{\sqrt{{\lambda}_{\alpha}}}.{{}^t}\mathbf{X}.\mathbf{v_{\alpha}} \end{array} \right.$

Dans ${\mathbb{R}}^p$, $\mathbf{u_{\alpha}}$ est le $\alpha$-ième axe factoriel. On calcule le vecteur ${\psi}_{\alpha}$ des coordonnées sur cet axe par :

$\mathbf{{\psi}_{\alpha}} = \mathbf{X}.\mathbf{u_{\alpha}}$

Dans ${\mathbb{R}}^n$, $\mathbf{v_{\alpha}}$ est le $\alpha$-ième axe factoriel. On calcule le vecteur ${\psi}_{\alpha}$ des coordonnées sur cet axe par :

$\mathbf{{\varphi}_{\alpha}} = {{}^t}\mathbf{X}.\mathbf{v_{\alpha}}$

Les facteurs peuvent se calculer :

$\mathbf{{\psi}_{\alpha}} = \mathbf{v_{\alpha}}.\sqrt{\mathbf{{\lambda}_{\alpha}}}$

et

$\mathbf{{\varphi}_{\alpha}} = \mathbf{u_{\alpha}}.\sqrt{\mathbf{{\lambda}_{\alpha}}}$

> [!NOTE]
> L'orientation des axes est **arbitraire**. Les vecteurs propres sont définis au signe près.
> [!NOTE]
> Les vecteurs de coordonnées dans ${\mathbb{R}}^p$ et ${\mathbb{R}}^n$ ont pour norme :
> ${{}^t}\mathbf{{\psi}_{\alpha}}.\mathbf{{\psi}_{\alpha}} = \sum_{i = 1}^{n} {\psi}_{{\alpha}i} = \mathbf{{\lambda}_{\alpha}}$
> et
> ${{}^t}\mathbf{{\varphi}_{\alpha}}.\mathbf{{\varphi}_{\alpha}} = \sum_{j = 1}^{p} {\varphi}_{{\alpha}i} =$

## La diversification de l'analyse générale

La **métrique** est la formule de la distance. Le **critère d'ajustement** est la pondération des points. Les deux varient suivant la **nature des caractères**.

L'analyse générale présuppose deux éléments.

1.Les espaces sont munis de la métrique euclidienne usuelle dont la forme quadratique est associée à la matrice identité $\mathbf{I}$.

2. Tous les points du nuage ont la même importance.

**Constat.** Il arrive que l'on ait à travailler avec une métrique plus générale et avec des individus dont les masses sont différentes qui interviennent dans les calculs de moyennes et lors de l'ajustement des sous-espaces.

**Le principe d'analyse factorielle se généralise à des métriques et des critères quelconque**.

Dans l'espace ${\mathbb{R}}^p$, on considère le nuage de $n$ points lignes pesants. Soient la matrice $\mathbf{X}$ d'ordre $\left( n, p \right)$ représentent un tableau de données, $M$ la matrice symétrique définie positive d'ordre $\left( p, p \right)$ définissant la métrique dans ${\mathbb{R}}^p$, et $\mathbf{D}$ la matrice diagonale d'ordre $\left( n, n \right)$ dont les éléments diagonaux sont les masses $m_i$ des $n$ points.

Un vecteur unitaire $\mathbb{u}$ de ${\mathbb{R}}^p$ vérifie la **relation de normalisation** :

${{}^t}\mathbf{u}.\mathbf{M}.\mathbf{u} = 1$

Les coordonnées de la projection $H_i$ du point $i$ sur l'axe $\mathbf{u}$ vaut :

$OH_i = {x_i}.\mathbf{M}.\mathbf{u}$

L'ensemble $F$ des coordonnées des projections sur l'axe $\mathbf{u}$ des $n$-points lignes s'exprime par :

$\mathbf{F} = \mathbf{X}.\mathbf{M}.\mathbf{u}$	

Selon le critère d'ajustement, on recherche le vecteur $\mathbf{u}$ qui rend maximale la somme pondérée des carrés des projections, c'est-à-dire ${\max}_{\left( u \right)} \left\lbrace {{}^t}\mathbf{u}.\mathbf{M}.{{}^t}\mathbf{X}.\mathbf{D}.\mathbf{X}.\mathbf{M}.\mathbf{u} \right\rbrace$ sous la contrainte ${{}^t}\mathbf{u}.\mathbf{M}.\mathbf{u} = 1$.

$\mathbf{u}$ est le vecteur propre de la matrice $\mathbf{A} = {{}^t}\mathbf{X}.\mathbf{D}.\mathbf{X}.\mathbf{M}$ correspondant à la plus grande valeur propre $\lambda$.

L'équation de l'axe factoriel $\mathbf{u}$ dans ${\mathbb{R}}^p$ s'écrit :
${{}^t}\mathbf{X}.\mathbf{D}.\mathbf{X}.\mathbf{M}.\mathbf{u} = {\lambda}.\mathbf{u}$

et les coordonnées factorielles des $n$ points sont données par la relation :
$\mathbf{\psi} = \mathbf{X}.\mathbf{M}.\mathbf{u}$

> [!WARNING]
> Si les masses et les métriques dans ${\mathbb{R}}^p$ ($\mathbf{D}$ et $\mathbf{M}$) et dans ${\mathbb{R}}^n$ ($\mathbf{P}$ la matrice des masses des $p$ points colonnes et $\mathbf{Q}$ la métrique dans ${\mathbb{R}}^n$) n'ont **aucune relation privilégiée entre elles**. De fait, on perd les relations de transition et la formule de reconstitution.
> 1. En A.C.P. normée, on utilise la même métrique dans les deux espaces.
> 2. En A.F.C., la matrice des masses dans un espace est liée à la métrique de l'autre espace, ce qui permet de conserver les relations de transition.

Les **axes principaux** (ou axes d'inertie) s'expriment par la quantité :

${{}^t}\mathbf{u}.\mathbf{M}.{{}^t}\mathbf{X}.\mathbf{D}.\mathbf{X}.\mathbf{M}.\mathbf{u} = \mathbf{\psi}.\mathbf{D}.\mathbf{\psi} = \sum_{i = 1}^{n} m_i {\psi}_{i}^{2}$

représentant l'inertie du nuage de points pesants le long de l'axe d'allongement maximal, l'axe factoriel $\mathbf{u}$. Elle est égale à la valeur propre $\mathbf{\lambda}$ associée au vecteur propre $\mathbf{u}$. Les $p$ vecteurs propres définissent des axes d'inertie du nuage de points. On les obtient par odre d'inerties décroissantes. La somme de toutes les valeurs propres donne l'inertie totale du nuage. C'est la trace de la matrice diagonalisée, appelée **matrice d'inertie** $\mathbf{B} = {{}^t}\mathbf{X}.\mathbf{D}.\mathbf{X}.\mathbf{M}$

$\textrm{Tr} \left( B \right) = \sum_{\alpha = 1}^{p} {\lambda}_{\alpha}$

## La motivation d'effectuer une analyse factorielle

Pourquoi réaliser une analyse factorielle ?

Une méthode factorielle se résume en trois points.

1. Étudier l'inertie des facteurs
    - Elle permet de comprendre l'importance globale des liaisons entre caractères.
    
    -  L'outil d'analyse principal est le diagramme des valeurs propres.
    
    - On établit le pourcentage d'inertie pour chaque facteur.

2. Étudier la contribution des individus aux axes

3. Interpréter axe par axe chaque caractère

La démarche d'interprétation d'une analyse factorielle se résume en trois éléments.

1. « Interpréter, c'est d'abord rendre clair »[^3] (p. 279).

2. « Interpréter, c'est aussi donner un sens »[^3] (p. 280).

3. « Interpréter, c'est enfin jouer de façon personnelle »[^3] (p. 281).

Il faut vérifier les biais et interpréter les facteurs.

1. Vérifier si un facteur s'explique par quelques éléments aberrants

2. Vérifier s'il y a un facteur d'opposition

3. Vérifier si un facteur met en évidence un groupe

4. Vérifier si un facteur est associé à une partition

5. Vérifier s'il y a un facteur d'échelle

6. Vérifier s'il y a un effet taille, notamment pour une A.C.P.

7. Vérifier s'il y a un effet Guttman, notamment pour une A.F.C. ou une A.C.M.

8. Donner en toute prudence un nom aux facteurs. Cette démarche est risquée, car elle peut limiter l'interprétation aux noms données aux axes.

« Il est évident que l'analyse factorielle n'est qu'un instrument, un outil : elle permet de décrire les grandes lignes d'un tableau de nombres comme une moyenne décrit une valeur centrale d'une distribution ou un écart type sa variabilité. Ces outils peuvent-ils avoir statut de modèle ? Dans le cas de l'analyse factorielle le débat existe »[^2] (p. 118).

## Notes de bas de page

[^1]: En anglais : *Singular Value Decomposition* (D.V.S.)

[^2]: Cibois, Philippe, 2000, *L'analyse factorielle. Analyse en composantes principales et analyse factorielle des correspondances*, Paris, P.U.F., 128 p. [Que sais-je ?]

[^3]: Escofier, Brigitte & Pagès, Jérôme, 2016, *Analyses factorielles simples et multiples. Cours et études de cas*, Paris, Dunod, VIII-392 p. [Sciences sup]

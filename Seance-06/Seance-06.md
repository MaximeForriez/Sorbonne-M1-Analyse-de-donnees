# Statistiques univariées (4). Statistique d'ordre des variables qualitatives

Devant l'importance de cette statistique en géographie, il me semble intéressant de développer quelques idées pour éviter tout quiproquo sur la statistique d'ordre.

La statistique d'ordre est le cœur de la géographie humaine. De manière annuelle, mensuelle, voire hebdomadaire, un certain nombre de classements est opéré en utilisant des objets géographiques. Leur objectif commun est de montrer quelle entité a descendu, stagné ou monté dans le classement. Ainsi, un lien entre ordination et variable quantitative s'effectue spontanément dans toute étude géographique. Par exemple, les manuels du secondaire de géographie sont truffés de ce genre de tableaux qui, malgré leur apparence basique, peuvent subir des traitements statistiques relativement complexes.

## Références

- Fréchet, Maurice, 1941, [« Sur la loi de répartition de certaines grandeurs géographiques »](https://www.numdam.org/item/JSFS_1941__82__114_0.pdf), *Journal de la société statisitque de Paris*, t. 82, p. 114-122

## Les règles générales des statistiques d'ordre

L'ordre qui doit être privilégié est l'**ordre croissant** (ou l'ordre naturel). Il existe des exceptions en géographie telles que la loi dite rang-taille. L'ordination permet de rechercher les valeurs aberrantes, trop grandes ou trop petites, d'une série d'observations. De plus, elle offre la possibilité d'étudier la loi de la plus grande valeur d'une série d'observations.

Soit une suite finie d'observations indépendantes $\left( X_i \right)$, avec $i \in \left[ 1, n \right]$, classées par ordre croissant. On désigne par :

- $X_{\left( 1 \right)}$ la plus petite valeur observée, c'est-à-dire la plus petite des valeurs $X_i$ ;

- $X_{\left( k \right)}$ la valeur de rang $k$, et ainsi de suite jusqu'à la plus grande valeurs $\left( X_n \right)$.

On écrit cette suite d'observations sous la forme :

$X_{\left( 1 \right)} \leq \ldots{} \leq X_{\left( n \right)}$

La suite ordonnée des $X_{\left( i \right)}$ est appelée **statistique d'ordre associée à la série des observations $\left( X_i \right)$**.

> [!NOTE]
> On aurait dû écrire $X_{\left( i, n \right)}$, car le rang d'une observation dépend du nombre $n$ des observations.

> [!NOTE]
> Si la loi $X$ est une loi continue, on peut se limiter à des inégalités strictes :
> $X_{\left( 1 \right)} < \ldots{} < X_{\left( n \right)}$
> car l'événement $X = k$ est un événement de probabilité nulle $\Pr \left( X = k \right) = 0$.
> La quantité $X_{\left( n \right)} - X_{\left( 1 \right)}$ est l'étendue de l'échantillon.

Toute statistique d'ordre possède une fonction de répartition $F \left( x_i \right)$ dont les valeurs varient de 0 à 1 dont il faut calculer son approximation (Tab. 1).

| **Approximations de\ldots{}** | **Fonction de répartition empirique** |
| :-: | :-: |
| Haazen (1930) | $F \left( X \right) = \frac{i - 0,5}{n}$ |
| Weibull (1939) | $F \left( X \right) = \frac{i}{n + 1}$ |
| Chegodaev (1955) | $F \left( X \right) = \frac{i - 0,3}{n + 0,4}$  |
| Tukey (1962) | $F \left( X \right) = \frac{i - \frac{1}{3}}{n - \frac{1}{3}}$ |
 
**Tableau 1. Les approximations de la fonction de répartition $F$ d'un rang**

L'approximation de A. D. Chegodaev[^1] reste la meilleure formule d'approximation. L'erreur maximale demeure inférieure à 1 % quelle que soit la taille de l'échantillon $n$. La fonction de répartition étant la dérivée de la distribution, il est par la suite facile de déduire la distribution statistique en présence dans le cas étudié.

Soit $R_n \left( x \right)$ le nombre de répétitions de l'événement $\left( X < x \right)$ au cours de $n$ épreuves indépendantes. Par définition, la fonction de répartition est :

$F \left( x \right) = \Pr \left( X < x \right)$

Pour $x$ fixé, la probabilité est constante au cours des $n$ épreuves. La variable $R_n \left( x \right)$ suit alors la loi binomiale $\beta \left[ n, F \left( x \right) \right]$, d'où :

$\Pr \left( R_n \left( x \right) = h \right) = C_{n}^{h} \left[ F \left( x \right) \right]^h \left[ 1 - F \left( x \right) \right]^{n - h}$

La réalisation de l'événement $X_{\left( k \right)} < a$ implique que :

1. $k$ valeurs de la variable $X$, au moins, soient inférieurs à $x$ ;

2. on peut en avoir $k + 1, k + 2, \dots{}, n$.

On en déduit la fonction de répartition $H_{\left( k \right)} \left( x \right)$ de la variable aléatoire $X_{\left( k \right)}$ :

$H_{\left( k \right)} \left( x \right) = \Pr \left( X_{\left( k \right)} < x \right) = \sum_{h = k}^{n} C_{n}^{h} \left[ F \left( x \right) \right]^h \left[ 1 - F \left( x \right) \right]^{n - h}$

La densité de $X_{\left( k \right)}$ peut être obtenue à partir de la définition :

$h_{\left( k \right)} \mathrm{d} x = \Pr \left( x \leq X_{\left( k \right)} < x + \mathrm{d} x \right)$

La réalisation d'un événement implique que :

1. au moins une des valeurs $x_i$ appartienne à l'intervalle $\left[ x, x + \mathrm{d} x \right]$ ; la probabilité de réalisation de cet événement est $n f \left( x \right) \mathrm{d} x$, car il existe $n$ choix possibles pour la valeur $x_i$ ;

2. $\left( k - 1 \right)$ valeurs des $x_i$ soient inférieures à $x_i$ ; la probabilité de réalisation de cet événement est $\left[ F \left( x \right) \right]^{k - 1}$ ;

3. $\left( n - k \right)$ des valeurs $x_i$ soient supérieures à $x$ ; la probabilité de réalisation de cet événement est $\left[ 1 - F \left( x \right) \right]^{n - k}$ ; $k$ nombre de réalisations possibles de cet événement est $C_{n - 1}^{n - k} = C_{n - 1}^{k - 1}$.

La **densité de probabilité** de la variable aléatoire $X \left( k \right)$ est de fait égale à :

$h_{\left( k \right)} \left( x \right) = n C_{n - 1}^{k - 1} \left[ F \left( x \right) \right]^{k - 1} \left[ 1 - F \left( x \right) \right]^{n - k} f \left( x \right)$

> [!NOTE]
> La fonction de répartition $H_{\left( k \right)} \left( x \right)$ ne dépend que $F \left( x \right)$, fonction de répartition de la variable $X$, et non de la nature de cette variable.

> [!NOTE]
> Si $X$ est une variable continue, la densité de la loi de probabilité de la variable $X_{\left( k \right)}$ peut être obtenue en dérivant la fonction de répartition $H_{\left( k \right)} \left( x \right)$.

> [!NOTE]
> Si $X$ est une variable discrète, la densité de la loi de probabilité de $H_{\left( k \right)} \left( x \right)$ est égale à :
> $H_{\left( k \right)} \left( x \right) = H_{\left( k \right)} \left( x + 1 \right) - H_{\left( k \right)} \left( x \right)$

> [!NOTE]
> Il existe une relation mathématique simple entre $H_{\left( k \right)} \left( x \right)$ et la fonction bêta incomplète :
> $H_{\left( k \right)} \left( x \right) = I_{F \left( x \right)} \left( k, n - k +1 \right)$
> où la fonction bêta incomplète est définie par :
> $I_{u} \left( p, q \right) = \int_{0}^{u} t^{p - 1} \left( 1 - t \right)^{q - 1} \mathrm{d} t$
> La fonction de répartition $H_{\left( k \right)} \left( x \right)$ est égale à l'intégrale bêta incomplète, tronquée en $F \left( x \right)$.

Les lois d'ordre sont aussi fréquentes en géographie humaine qu'en géographie physique. En géographie physique, elles servent notamment à étudier la hauteur maximale des crues d'un cours d'eau, l'intensité du plus fort tremblement de terre dans une zone sismique donnée, *etc*. En géographie humaine, leur utilisation découle du fait de l'apparition plus ou moins spontanée de hiérarchies au sein des sociétés et des espaces étudiés.

## La corrélation des rangs

Tout classement dispose d'une part d'arbitraire due à celui qui l'élabore, et ce même en constituant des nomenclatures très détaillées. Il faut par conséquent être en mesure de proposer des analyses statistiques des différents classements possibles. Le problème se formule de manière relativement simple : « Les classements opérés sont-ils identiques ? ». Pour répondre à cette question, il existe deux tests : celui de C. Spearman[^2] et celui de M. G. Kendall[^3].

Soient $X$ et $Y$ deux variables ordinales prises dans un ensemble de $n$ individus (ou objets) qui ont été soumis à deux classements différents. Ainsi, on obtient deux classements, dont les rangs sont représentés par deux variables aléatoires $U$ et $V$.

| **Objet** | **Objet A** | **Objet B** | **...** | **Objet Z** |
| :-: | :-: | :-: | :-: | :-: |
| Classement n°1 | $u_1$ | $u_2$ | ... | $u_n$ |
| Classement n°2 | $v_1$ | $v_2$ | ... | $v_n$ |
 
**Tableau 2. Classements de $ n $ objets réalisés par deux individus**

Le problème posé consiste à comparer les deux classements, c'est-à-dire de répondre à la question suivante : « ces classements sont-ils identiques ou non ? ». Les tests de C. Spearman et de M. G. Kendall ont été conçus pour y répondre ce problème.

#### Le test de Spearman (1904)

Le psychologue C. Spearman proposa en 1904 un test sur les rangs *via* le coefficient de corrélation usuel rebaptisé Spearman $r_s$[^4].

$r_s = \frac{\mathrm{cov} \left( u , v \right)}{s_u s_v}$

$u$ et $v$ sont des nombres entiers et $s_u$ et $s_v$ sont les écarts types empiriques. Chacun des classements n'est qu'une permutation de ces nombres. Par conséquent, moyenne et variance de $U$ et $V$ sont identiques. Par ailleurs, il est possible d'identifier une distribution particulière applicable à ce cas d'espèce, la **loi uniforme discrète** qui est appliquée ici à un ensemble de nombres entiers allant de 1 à $n$. La moyenne et la variance de cette loi valent respectivement :

$\left\langle U \right\rangle = \frac{n + 1}{2} = \left\langle V \right\rangle$

et

$\mathbb{V} \left( U \right) = \frac{n^2 - 1}{12} = \mathbb{V} \left( V \right)$

Ce cas montre l'importance de bien connaître les distributions statistiques afin de ne pas se tromper dans le calcul des moyennes.

En utilisant ces formules dans l'expression de $r_s$, on obtient la formule plus pratique :

$r_s = 1 - \frac{6}{n \left( n^2 - 1 \right)} \sum_{i = 1}^{n} \left( u_i - v_i \right)^2$

Si le coefficient de corrélation de C. Spearman $r_s$ vaut 1, c'est-à-dire que la différence entre $u_i$ et $v_i$ est nulle, les classements sont identiques. Si le coefficient de corrélation de C. Spearman $r_s$ vaut $-1$, cela signifie que les classements sont strictement l'inverse l'un par rapport à l'autre. Si le coefficient de corrélation de C. Spearman $r_s$ est nul, les classements sont indépendants.

Ainsi, le test de C. Spearman est un test non paramétrique qui permet d'établir deux hypothèses. D'une part, le coefficient de corrélation des rangs n'est pas significativement différent de zéro $\left( H_0 \right)$. D'autre part, le coefficient de corrélation des rangs est significativement différent de zéro $\left( H_0 \right)$. L'unique condition est que l'on considère que les rangs ont des permutations équiprobables.

Pour le classement de C. Spearman, il ne doit pas y avoir de rang *ex aequo*. S'il y en a, alors on a besoin d'une correction $\xi$. Dans ce cas,

$r_s = \frac{\sum \left( r_1 \times r_2 \right) - \xi}{\sqrt{\left( \sum {r_1}^2 - \xi \right) \left( \sum {r_2}^2 - \xi\right)}}$

$r_1$ le rang 1, $r_2$ le rang 2, et $\xi$ la correction valant :

$\xi = \frac{1}{4} n \left( n + 1 \right)^2$

avec $n$ le nombre de rangs.

Pour $n > 30$, la distribution du coefficient de corrélation de C. Spearman $r_s$ peut être rapprochée d'une distribution normale qui possède une moyenne $\mathbb{E} \left( r_s \right) = 0$ et une variance $\mathbb{V} \left( r_s \right) = \frac{1}{n - 1}$. Il est par conséquent possible de construire un intervalle de confiance avec une probabilité critique.

En géographie urbaine, cela peut s'appliquer aux classements des villes par rapport à leur population. Les géographes sont en désaccord sur la définition des limites des villes, donc de la population contenue à l'intérieur. Ainsi, les classements peuvent être très différents, alors que le nom des agglomérations est identique. La méthode de C. Spearman peut permettre de rapprocher et de comparer les différents classements urbains.

Par ailleurs, le test de C. Spearman permet également de comparer plusieurs variables rattachées à un objet d'étude. Par exemple, toujours en géographie urbaine, les villes ont souvent des indicateurs de fécondité, d'activités, *etc*. Il est possible de faire un classement sur un échantillon de plusieurs villes de la fécondité et de l'activité, par exemple. Dans ce cas, le coefficient de C. Spearman donne un lien de dépendance entre le classement des villes en fonction de la fécondité et le classement des villes en fonction des activités.

Pour effectuer un test, on distingue deux cas.

- Si $n \leq 30$, la table $r$ de Bravais[^5]-Pearson[^6] est le plus souvent utilisée.

- Si $n > 30$, $r_s$ peut se calculer avec un $t$ de Student.


$t = \left( \sqrt{n - 2} \right) \frac{r_s}{\sqrt{1 - {r_s}^2}}$

$t$ est lu dans la table de Student avec un degré de liberté $ddl = n - 2$.

#### Le test de Kendall

M. G. Kendall inventa son test d'indépendance des rangs en 1938[^7] [^8].

Soient deux classements correspondant respectivement à deux séries de valeurs $x_i$ et de valeurs $y_i$ correspondant à des valeurs allant de 1 à $n$. Ainsi, il est possible de former des couples de rang $\left( x_i , y_i \right)$. Pour simplifier l'estimation du coefficient de M. G. Kendall, il est conseillé de classer par ordre naturel l'un des classements (Tab. 3).

| **Objet** | **D** | **C** | **...** | **B** |
| --- | :-: | :-: | :-: | :-: |
| Classement n°1 : Série ($x_{i}$)| 1 | 2 | ... | $n$ |
| Classement n°2 : Série ($y_{i}$)| $y_{i1}$ | $y_{i2}$ | ... | $y_{in}$ |
 
**Tableau 3. Classements des objets ordonnés selon l'ordre naturel du classement n°1**

À présent, il faut évaluer un score $S_c$ grâce au tableau 3. On regarde tous les couples $y_{i1}$ par rapport aux autres valeurs qui suivent $y_{i2} , \ldots{} , y_{in}$. Si l'ordre naturel est respecté, on note $+1$, sinon $-1$. Dans le premier cas, les classements sont **concordants** ; dans le second, **discordant**. On effectue la même manipulation avec $y_{i2}$, et ainsi de suite jusque la valeur $y_{i n \left( n - 1 \right)}$. Le score $S_c$ correspond à la somme des valeurs $+1$ et $-1$ observée. En sachant que la somme totale $S_T$, c'est-à-dire le cas de concordance parfaite, vaut :

$S_T = \frac{n \left( n - 1 \right)}{2}$

Le coefficient de M. G. Kendall $\tau$ correspond au rapport entre $S_c$ et $S_T$. Après quelques calculs, il s'estime plus simplement de la manière suivante :

$\tau = \frac{2 S_c}{n \left( n - 1 \right)}$

Si le coefficient de M. G. Kendall $\tau$ vaut $+1$, les classements sont identiques. Si le coefficient de M. G. Kendall $\tau$ vaut $-1$, les classements sont inverses. Si le coefficient de M. G. Kendall $\tau$ vaut $+1$, les classements sont identiques.

Pour $n \geq 8$, la distribution du coefficient de M. G. Kendall est une distribution normale qui possède une moyenne $\mathbb{E} \left( \tau \right) = 0$ et une variance $\mathbb{V} \left( \tau \right) = \sqrt{\frac{2 \left( 2 n + 5 \right)}{9 n \left( n - 1 \right)}}$. Il est par conséquent possible de construire un intervalle de confiance avec une probabilité critique.

L'avantage du coefficient de M. G. Kendall $\tau$ réside dans sa capacité à se généraliser à $k$ classements.

###### Exemple.

Soient quatre objets A, B, C et D qui peuvent être classés de deux manières (Tab. 4).

| Objet | A | B | C | D |
| --- | :-: | :-: | :-: | :-: |
 | Classement 1 | 3 | 4 | 2 | 1 |
 | Classement 2 | 3 | 1 | 4 | 2 |
 
**Tableau 4. Rangs obtenus pour chaque objet**

1. Réarranger par ordre naturel du classement 1 (Tab. 5)

| Objet | D | C | A | B |
| --- | :-: | :-: | :-: | :-: |
 | Classement 1 | 1 | 2 | 3 | 4 |
 | Classement 2 | 2 | 4 | 3 | 1 |
 
**Tableau 5. Rangs obtenus pour chaque objet par rapport au classement 1**

2. Étudier les cas possibles. Au rang n°1, la valeur 2 du classement 2 se combine avec les trois valeurs suivantes : $\left( 2, 4 \right), \left( 2, 3 \right), \left( 2, 1 \right)$. Les deux premiers ont un ordre concordant, tandis que le dernier a un ordre discordant. Au rang n°2, la valeur 4 du classement 2 se combine avec les deux valeurs suivantes : $\left( 4, 3 \right), \left( 4, 1 \right)$. Il y a deux valeurs discordantes. Au rang n°3, la valeur 3 du classement 2 se combine avec la valeur suivante : $\left( 3, 1 \right)$, soit une valeur discordante. Cela se traduit d'après le test en :

$+1 ; +1 ; -1 ; -1 ; -1 ; -1$ 

3. Calculer $S_C = 1 + 1 - 1 - 1 - 1 - 1 = -2$

    - On peut également poser que le nombre de concordances $N_a = 2$ et le nombre de discordances $N_d = 4$, ce qui fait que : $S_C = N_a - N_d = 2 - 4 = -2$.

4. Calculer $S_T = \frac{4 \times 3}{2} = 6$

	- En utilisant le nombre de concordances $N_a$ et le nombre de discordances $N_d$, on peut calculer : $S_T = N_a + N_d = 2 + 4 = 6$.

5. Calculer $\tau = \frac{S_C}{S_T} = \frac{-2}{6} = -\frac{1}{3}$

> [!NOTE]
> $\tau = \frac{S_C}{S_T} = \frac{S_C}{\frac{n \left( n - 1 \right)}{2}} = \frac{2 S_C}{n \left( n - 1 \right)}$

6. On utilise la loi normale si $n \geq 8$, ce qui n'est pas le cas ici.

$\begin{array}{l} \mathbb{E} \left( \tau \right) = 0 \\ \mathbb{V} \left( \tau \right) = \sqrt{\frac{2 \left( 2n + 5 \right)}{9n \left( n - 1 \right)}} = \sqrt{\frac{2 \left( 2 \times 4 + 5 \right)}{9 \times 4 \left( 4 - 1 \right)}} = \sqrt{\frac{26}{108}} \approx 0,4907 \\ \mathrm{SE} = \frac{0,4907}{\sqrt{4}} \approx \frac{0,4907}{2} \approx 0,2453 \end{array}$

Pour construire un intervalle de confiance, on pourrait utiliser :

- pour un risque $\alpha = 0,05$, $t_{0,95} = 3,182$

- pour un risque $\alpha = 0,01$, $t_{0,99} = 51,075$

Les coefficients de corrélation des rangs sont très utiles pour tester l'indépendance des deux variables non normales, car le test du coefficient de corrélation linéaire ne s'applique pas dans ce cas. De plus, ils sont invariants par toute transformation monotone croissante des variables.

###### Exercice type

On souhaite comparer deux classements de 12 objets (A, B, C, D, E, F, G, H, I, J, K, L) (Tab 6). La concordance ou la discordance s'évalue en comparant l'ordre du classement n°2 avec celui du classement n°1.

| **Objet** | **Classement 1** | **Classement 2** | **Concordant** | **Discordant** | **TOTAL** |
| :-: | --: | --: | --: | --: | --: |
| A | 1 | 1 | 11 | 0 | **11** |
| B | 2 | 2 | 10 | 0 | **10** |
| C | 3 | 4 | 8 | 1 | **9** |
| D | 4 | 3 | 8 | 0 | **8** |
| E | 5 | 6 | 6 | 1 | **7** |
| F | 6 | 5 | 6 | 0 | **6** |
| G | 7 | 8 | 4 | 1 | **5** |
| H | 8 | 7 | 4 | 0 | **4** |
| I | 9 | 10 | 2 | 1 | **3** |
| J | 10 | 9 | 2 | 0 | **2** |
| K | 11 | 12 | 0 | 1 | **1** |
| L | 12 | 11 | - | - | **-** |
|  |  | **TOTAL** | **61** | **5** | **66** |
 
**Tableau 6. Concordances et discordances entre le classement 2 et le classement 1**

Le classement n°2 présente un ordre alternatif. Pour chaque individu de ce classement, on compare si l'ordre est naturel, donc **concordant**, ou si l'ordre est **discordant**. En première ligne, $1 = 1$, l'ordre est concordant ; on place dans la colonne « Concordant » $12 - 1 = 11$, et dans la colonne « Discordant » $0$. En deuxième ligne, $2 = 2$, l'ordre est concordant ; on place dans la colonne « Concordant » $11 - 1 = 10$, et dans la colonne « Discordant » $0$. En troisième ligne, $4 > 3$, l'ordre est discordant ; on place dans la colonne « Concordant » $8$, et dans la colonne « Discordant » $1$, de sorte que $8 + 1 = 9$. En quatrième ligne, $3 < 4$, l'ordre est concordant ; on place dans la colonne « Concordant » $8$, et dans la colonne « Discordant » $0$. En cinquième ligne, $6 > 5$, l'ordre est discordant ; on place dans la colonne « Concordant » $6$, et dans la colonne « Discordant » $1$, de sorte que $6 + 1 = 7$, et ainsi de suite. Une fois l'algorithme appliqué, on dénombre les couples concordants et les couples discordants. Plus on avance dans les lignes, plus le nombre de couples testés diminue, comme l'illustre la colonne « TOTAL ».

On pose $N_a = 61$ et $N_d = 5$. Le coefficient $\tau$ vaut alors :

$\tau = \frac{N_a - N_d}{N_a + N_d} = \frac{S_C}{S_T} = \frac{56}{66} \approx 0,85$

La concordance $\tau = 1$ est **parfaite** s'il n'y a aucune paire discordante. Si $\tau = -1$, alors les classements sont parfaitement **inverses**.

Il est possible de mesurer la significativité de $\tau$ en calculant $z$.

$z = \frac{3 \tau \sqrt{n \left( n - 1 \right)}}{\sqrt{2 \left( 2n + 5 \right)}}$

ici $\tau \approx 0,85$ et $n = 12$ rangs, donc $z \approx 3,85$. $z$ est une variable $t$ de Student avec un degré de liberté $ddl = S_T - 2$. Il n'y a plus qu'à regarder la probabilité critique au risque voulu pour juger si $\tau$ est significatif. Le test d'hypothèse est :

- $H_0$ : la concordance entre les classements est due au hasard ;

- $H_1$ : la concordance entre les classements n'est pas due au hasard.

## La concordance de $p$ classements

La concordance de $p$ classements est la généralisation du coefficient de corrélation des rangs de M. G. Kendall. Dans ce cas, $n$ individus ont été classés selon $p$ critères (Tab. 7).

|  | **Individu 1** | **Individu 2** | **...** | **Individu $n$** |
| :-: | :-: | :-: | :-: | :-: |
| **Critère 1** | $r_{11}$ | $r_{21}$ | ... | $r_{n1}$ |
| **Critère 2** | $r_{12}$ | $r_{22}$ | ... | $r_{n2}$ |
| **...** | ... | ... | ... | ... |
| **Critère $p$** | $r_{1p}$ | $r_{2p}$ | ... | $r_{np}$ |
| **Total** | $r_{1.}$ | $r_{2.}$ | ... | $r_{n.}$ |
 
**Tableau 7. Classement de $ n $ individus selon $ p $ critères**

Chaque ligne est une permutation des entiers de 1 à $n$, la somme des termes de n'importe quelle ligne est égale à $\frac{n \left( n - 1 \right)}{2}$. La somme des termes du tableau $N$ est de fait égale à $N = \frac{np \left( n + 1 \right)}{2}$. Si les classements étaient rigoureusement identiques, une des colonnes aurait pour somme $p$, une autre $2p$, une autre $3p$, *etc*.

Pour étudier la concordance entre ces classements, on considère la statistique :

$S = \sum_{i = 1}^{n} \left( r_{i.} - \frac{N}{n} \right)^2$

Cette statistique est une mesure de la dispersion des sommes des colonnes par rapport à leur moyenne.

Si la concordance est parfaite, la statistique $S$ est alors maximale. Elle vaut :

$S_{\max} = \frac{np ^2 \left( n^2 - 1 \right)}{12}$

En partant de ce constat, afin d'étudier la concordance de $p$ classements, D. G. Kendall a proposé le coefficient $W$ :

$W = \frac{12S}{np^2 \left( n^2 - 1 \right)} = \frac{S}{S_{\max}}$

Ce coefficient est compris entre 0 et 1.

- **Propriété 1.** Pour $W = 0$, les sommes de toutes les colonnes sont égales.

- **Propriété 2.** Une faible valeur de $W$ indique l'indépendance entre les classements.

- **Propriété 3.** $H_0$ est rejetée si $W$ est trop grand. Des tables donnent les valeurs critiques de $W$ pour différentes valeurs de $n$ et de $p$.
\end{description}

> [!NOTE]
> Pour $n \geq 15$ et $p < 7$, la variable $\frac{\left( p - 1 \right)W}{1 - W}$ est une variable de Fisher $F \left[ n - 1 - \frac{2}{p}, \left( n - 1 \right) \left( n - 1 -\frac{2}{p} \right) \right]$.

> [!NOTE]
>  Pour $p \geq 7$, la variable $p \left( n - 1 \right) W$ suit une loi du ${\chi}^2$ à $\left( n - 1 \right)$ degrés de liberté.

## Le coefficient $\Gamma$ de Goodman-Krusdal

Le coefficient de Goodman[^9]-Krusdal[^10] est noté $\Gamma$ ou $g$. Il se base sur la différence entre les paires concordantes $\left( N_a \right)$ et les paires discordantes $\left( N_d \right)$ [^11] [^12] [^13] [^14].
	$\Gamma = \frac{N_a - N_d}{N_a + N_d} = \frac{S_C}{S_T}$

$\Gamma$ calcule le « surplus » de paires concordantes par rapport aux paires discordantes. Il s'agit d'une proportion.

$\Gamma$ varie entre $-1$ et $+1$. Si $\Gamma = 0$, les paires sont indépendantes.

> [!WARNING]
> $\Gamma$ peut être nul même s'il n'y a pas d'indépendance statistique dans le cas où $S_C = 0$ par exemple.

$\Gamma$ s'interprète comme $\rho$ et $\tau$.

On peut faire un test de Student

$t \approx \Gamma \sqrt{\frac{S_C}{n \left( 1 - {\Gamma}^2 \right)}}$

avec $n \neq S_C$

## Le coefficient $Q$ d'association de Yule

Le coefficient $Q$ d'association de G. U. Yule[^15] est un cas particulier du coefficient de Goodman-Krusdal. Il est appliqué dans le cas des matrices $2 \times 2$. Il faut construire la table de contingence qui évalue la fréquence des événements.

|  | **Oui** | **Non** | **TOTAL** |
| :-: | :-: | :-: | :-: |
| **Positif** | $a$ | $b$ | **$a + b$** |
| **Négatif** | $c$ | $d$ | **$c + d$** |
| **TOTAL** | **$a + c$** | **$b + d$** | **$n$** |
 
**Tableau 8. Tableau de contingence**

À partir du tableau 8, le coefficient $Q$ vaut :

$Q = \frac{ad - bc}{ad + bc}$

Le signe de $Q$ dépend de l'appariement que l'analyse effectuée considère être concordant, mais les couples restent symétriques. Le choix de l'appariement n'affecte pas l'ampleur de $Q$.

$Q$ varie entre $-1$ et $+1$.

- $Q = -1$ signifie que l'association est négative totale.

- $Q = 0$ signifie qu'il existe aucune association.

- $Q = +1$ signifie que l'association est positive parfaite.

En termes de rapport de cotes[^16] (ou de chances) $\mathrm{OU}$, $Q$ est donné par :

$Q = \frac{\mathrm{OU} - 1}{\mathrm{OU} + 1}$

avec $\mathrm{OU}$, le connecteur logique.

Le $Q$ de Yule et le $Y$ de Yule sont liés :

$Q = \frac{2Y}{1 + Y^2}$

et

$Y = \frac{1 - \sqrt{1 - Q^2}}{Q}$

## Liens

- [Topo en format P.D.F.](./PDF/Seance-06.pdf)

- [Exercice](./Exercice/Seance-6.pdf)

## Notes de bas de page

[^1]: Andrej Dmitrievich Chegodaev (1905-1994)

[^2]: Charles Spearman (1863-1945)

[^3]: Maurice G. Kendall (1907-1983)

[^4]: Spearman, Charles, 1904, "The Proof and Measurement of Association between Two Things", *The American Journal of Psychology*, vol. 15, n°1, p. 72-101

[^5]: Auguste Bravais (1811-1863)

[^6]: Karl Pearson (1857-1936)

[^7]: Kendall, Maurice G., 1938, "A New Measure of Rank Correlation", *Biometrika*, vol 30, n°1-2, p. 81-93

[^8]: Rateau, Patrick, 2001, *Méthode et statistiques expérimentales en sciences humaines*, Paris, Ellipses, 240 p. [Université] 

[^9]: Leo A. Goodman (1928-2020)

[^10]: William Henry Krusdal (1919-2005)

[^11]: Goodman, Leo A. & Kruskal, William H., 1954, "Measures of Association for Cross Classification", *Journal of the American Statistical Association*, vol. 49, n°268, p. 732-764

[^12]: Goodman, Leo A. & Kruskal, William H., 1959, "Measures of Association for Cross Classification II: Further Discussion and References", *Journal of the American Statistical Association*, vol. 54, n°285, p. 123-163

[^13]: Goodman, Leo A. & Kruskal, William H., 1963, "Measures of Association for Cross Classification III: Approximate Sampling Theory", *Journal of the American Statistical Association*, vol. 58, n°302, p. 310-364

[^14]: Goodman, Leo A. & Kruskal, William H., 1972, "Measures of Association for Cross Classification IV: Simplification of Asymptotic Variances", *Journal of the American Statistical Association*, vol. 67, n°338, p. 415-421

[^15]: George Udny Yule (1871-1851)

[^16]: En anglais : *odds ratio*

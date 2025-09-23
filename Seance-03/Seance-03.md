# Statistiques univariées (1). Paramètres statistiques élémentaires

Les paramètres statistiques concernent principalement les variables quantitatives, et ponctuellement qualitatives. Il existe trois sortes de paramètres : les paramètres de position, les paramètres de dispersion et les paramètres de forme.

## Tutoriels

- [Traitement, analyse et modélisation avec Pascal et Léa : la statistique descriptive](https://www.youtube.com/watch?v=99jDA-hN3P8&list=PLWwpP-YNkDjb7PefcxvLoOt0rsIcI3VWu)

## Première approche : espérance, variance et écart type

Pour comprendre les notions paramétriques, on peut les présenter sous la forme d'un exemple simple.

### Moyenne

On suppose deux élèves ayant eu les notes suivantes (Tab. 1).

| **Élève** | **Note 1** | **Note 2** | **Note 3** | **Note 4** | **Moyenne** |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 10 | 10 | 10 | 10 | 10 |
| 2 | 0 | 20 | 5 | 15 | 10 |
| Notation statistique | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $\mu$ |

**Tableau 1. Moyenne**

La moyenne ne permet pas de percevoir que l'élève n°1 a été plus régulier que l'élève n°2. Il faut proposer un autre indicateur pour le mesurer.

### Variance

Étape n°1. Calculer les écarts à la moyenne : $x_i - \mu$.

| **Élève** | $x_1 - \mu$ | $x_2 - \mu$ | $x_3 - \mu$ | $x_4 - \mu$ | **Moyenne des écarts** |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | -10 | 10 | -5 | 5 | 0 |


**Tableau 2. Écart à la moyenne**

Ce n'est pas suffisant. On arrive au même problème que pour la moyenne (Tab. 1). Il existe alors deux possibilités : soit prendre la valeur absolue (2a), soit prendre le carré de $x_i - \mu$ (2b)

Étape n°2a. Calculer la valeur absolue des écarts à la moyenne : $\left| x_i - \mu \right|$.

| **Élève** | **Note 1** | **Note 2** | **Note 3** | **Note 4** | **Total** |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 10 | 10 | 5 | 5 | 30 |

**Tableau 3. Valeur absolue des écarts à la moyenne**

Étape n°2b. Calculer le carré des écarts à la moyenne : $\left( x_i - \mu \right)^2$.

| **Élève** | **Note 1** | **Note 2** | **Note 3** | **Note 4** | **Total** |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 100 | 100 | 25 | 25 | 250 |

**Tableau 4. Carré des écarts à la moyenne**

(2b) est appelé la **variance $\mathbb{V}$**. On l'utilise car l'usage du carré offre des propriétés que ne possède pas la valeur absolue.

### Généralisation de la variance

Inconsciemment, la moyenne utilisée n'a pas été pondérée. On suppose que toutes les notes ont le même poids $p_i$

| **$x_i$** | **$x_1$** | **$x_2$** | **$x_3$** | **$x_4$** | **Total** |
| :-: | --: | --: | --: | --: | --: |
| $p_i$ | 0,25 | 0,25 | 0,25 | 0,25 | 1 |

**Tableau 5. Poids appliqués aux moyennes du tableau n°2**

On peut mettre d'autres $p_i$, mais leur somme doit **toujours** être égale à 1.

Si l'on introduit la notion de variable aléatoire $X$ dont $x_1$, $x_2$, $x_3$ et $x_4$ sont ses réalisations, le poids correspond à une **probabilité**. Dans le cas de la moyenne simple, on supposait que les notes étaient **équiprobables**.

| **$x_i$** | **$x_1$** | **$x_2$** | **$x_3$** | **$x_4$** |
| :-: | --: | --: | --: | --: |
| $\Pr \left( X = x_i \right)$ | $p_1$ | $p_2$ | $p_3$ | $p_4$ |

**Tableau 6. Notations probabilistes**

Étape n°1. Calculer l'espérance $\mathbb{E}$ de $X$, $\mathbb{E} \left( X \right)$ qui correspond à la moyenne pondérée.

$\mathbb{E} \left( X \right) = \sum_{i = 1}^{n} x_i p_i$

L'espérance mesure l'ordination de la variable aléatoire $X$ étudiée, c'est-à-dire la **position**. Elle sert de variable de référence.

Étape n°2. Calculer la  variance $\mathbb{V}$ de $X$, $\mathbb{V} \left( X \right)$ qui mesure la moyenne de l'écart à l'espérance au carré.

$\mathbb{V} \left( X \right) = \sum_{i = 1}^{n} p_i \left( x_i - \mathbb{E} \left( X \right) \right)^2$

La variance mesure la régularité de la variable aléatoire $X$ étudiée, c'est-à-dire la **dispersion**. Plus variance est grande, plus $X$ s'écarte de l'espérance, et *vice versa*.

### Écart type

L'écart type permet de faire revenir la variance à la même unité que la moyenne ou l'espérance.

$\sigma \left( X \right) = \sqrt{\mathbb{V} \left( X \right)}$

De fait, on écrit souvent la variance :

$\left( \sigma \left( X \right) \right)^2 = \mathbb{V} \left( X \right)$

> [!NOTE]
>  La racine carrée n'inverse pas l'ordre de la variance, donc son rapport avec la dispersion est le même que la variance. Néanmoins, écart type et variance ne doivent pas être confondus.

Espérance et variance sont des opérateurs. Il existe de fait une algèbre[^1] de l'espérance et une algèbre de la variance.

## Paramètres de position

Le premier paramètre de position est la moyenne, mais il en existe de nombreux autres : médiane, mode, médiale, *etc*.

### La moyenne

Soient $x_1, \ldots{}, x_p$ les modalités du caractère $n_1, \ldots{}, n_p$ les effectifs correspondants à $p$ modalités. $n = n_1 + \ldots{} + n_p$ représente l'effectif total.

Il existe plusieurs manières de calculer les moyennes en fonction de la nature de la variable (Tab. 7). On la note : $\bar{x}$ ou encore $\left\langle x \right\rangle$.

<table style="vertical-align:center;">
  <thead>
    <tr>
      <th style="text-align:center">Nom de la moyenne</th>
      <th style="text-align:center">Variables discrètes</th>
      <th style="text-align:center">Variables continues</th>
    </tr>
  <thead>
  <tbody>
    <tr>
      <td rowspan="2" style="text-align:center">Moyenne arithmétique</td>
      <td>$\left\langle x \right\rangle = \frac{1}{n} \sum_{i = 1}^{p} n_i x_i = \sum_{i = 1}^{p} f_i x_i$</td>
      <td>$\left\langle x \right\rangle = \int_{x_a}^{x_b} x \textrm{f} \left( x \right) \textrm{d} x$</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:left">La moyenne ayant été définie par la somme pour une variable discrète, devient une intégrale pour une variable continue.</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align:center">Moyenne quadratique</td>
      <td style="text-align:left">$q = \sqrt[m]{\frac{1}{n} \sum_{i = 1}^{n} {{x}_{i}}^{m}}$</td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:center">La moyenne quadratique est peu utilisée, car elle a peu d'intérêt. Exemple d'utilisation. Soit un carré de côté $a$ et soit un autre de côté $b$, la somme des aires des deux carrés est égale à : $q^2 = \frac{a^2 + b^2}{2} \Leftrightarrow q = \sqrt[2]{\frac{a^2 + b^2}{2}}$</td>
    </tr>
      <td rowspan="3" style="text-align:center">Moyenne harmonique</td>
      <td colspan="2" style="text-align:left">Une condition supplémentaire est nécessaire : $x_i > 0$.</td>
    </tr>
    <tr>
      <td style="text-align:center">$h = \frac{n}{\sum_{i = 1}^{p} \frac{n_i}{x_i}}$</td>
      <td style="text-align:center">$h = \int_{x_a}^{x_b} \frac{1}{x} \textrm{f} \left( x \right) \textrm{d} x$</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align:left">Exemple d'utilisation. Soit une distance parcourue $d$ dans un sens à la vitesse $v_1$ et dans l'autre à la vitesse $v_2$. La vitesse moyenne s'obtiendra en divisant la distance totale $2d$ par le temps mis à la parcourir : $ v_i = \frac{2d}{t} \Leftrightarrow t = \frac{2d}{v_i}$ $t = t_1 + t_2 = \frac{d}{v_1} + \frac{d}{v_2}$ $\frac{1}{v} = \frac{1}{2} \left( \frac{1}{v_1} + \frac{1}{v_2} \right)$</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align:center">Moyenne géométrique</td>
      <td colspan="2" style="text-align:center">Une condition supplémentaire est nécessaire : $x_i > 0$.</td>
    </tr>
    <tr>
      <td style="text-align:center">$g^n = {x_1}^{n_1} \times \ldots{} \times {x_p}^{n_p} = \prod_{i = 1}^{p} {x_i}^{n_i}$</td>
      <td style="text-align:center">$\ln g = \int_{x_a}^{x_b} \left( \ln x \right) \textrm{f} \left( x \right) \textrm{d} x$</td>
    </tr>
    <tr>
      <td style="text-align:center">Moyenne mobile (ou glissante)</td>
      <td style="text-align:center">${MM}_s = \frac{{M_1} + {M_2} + \ldots{} + {M_n}}{n}$</td>
      <td style="text-align:center"></td>
    </tr>
    <tr>
      <td style="text-align:center">Moyenne fonctionnelle</td>
      <td style="text-align:center"></td>
      <td style="text-align:center">$m = \frac{1}{b - a} \int_{a}^{b} \textrm{f} \left( x \right) \textrm{d} x$</td>
    </tr>
  </tbody>
</table>

**Tableau 7. Les différents types de moyenne**

La moyenne[^2] arithmétique [^3] est sensible aux valeurs extrêmes (ou « aberrantes »). Ainsi, il est parfois nécessaire de les supprimer.

> [!NOTE]
> La moyenne ne change pas si on remplace les effectifs par des effectifs proportionnels.

> [!NOTE]
> La moyenne ne change pas si on remplace $k$ valeurs $x_1, \ldots{}, x_k$ affectées des coefficients $n_1, \ldots{}, n_k$ par leur moyenne partielle affectée de la somme des coefficients $n_1, \ldots{}, n_k$. Il s'agit d'une **moyenne pondérée**[^4]. Soient trois sous-populations ayant pour moyennes partielles $\left\langle x_1 \right\rangle$, $\left\langle x_2 \right\rangle$ et $\left\langle x_3 \right\rangle$, et pour effectifs $N_1$, $N_2$ et $N_3$, alors la moyenne de la population totale est :
> $\left\langle x \right\rangle = \frac{N_1 \left\langle x_1 \right\rangle + N_2 \left\langle x_2 \right\rangle + N_3 \left\langle x_3 \right\rangle}{N_1 + N_2 + N_3}$

Il est à noter qu'il existe d'autres moyennes : la moyenne quadratique[^5], la moyenne harmonique [^6], la moyenne géométrique[^7], et la moyenne mobile[^8].

### La médiane

La **médiane**[^9] est la valeur, observée ou possible, dans la série des données classées par ordre croissant (ou décroissant) qui partage cette série en deux parties comprenant exactement le même nombre de données de part et d'autre de cette valeur, notée $m_e$. On l'appelle également « moyenne du milieu ».

##### Pour un caractère quantitatif discret

On classe les $n$ valeurs de la série statistique par **ordre croissant**.

Deux cas sont possibles.

1. Si $n$ est impair, alors la médiane est le rang de la valeur $\frac{n + 1}{2}$.

2. Si $n$ est pair, alors la médiane n'existe pas. On parle d'**intervalle médian** entre les rangs de valeurs $\frac{n}{2}$ et $\frac{n}{2} + 1$. La médiane pratique est souvent le milieu de cet intervalle.

##### Pour un caractère quantitatif continu

La médiane est le nombre $m_e$ tel que la fréquence cumulée jusqu'à ce que la valeur $m$ soit égale à $\frac{1}{2}$.

$\sum_{i = 1}^{m} f_i = \frac{1}{2}$

c'est-à-dire :

$\int_{x_a}^{m_e} \mathrm{f} \left( x \right) \mathrm{d} x = \int_{m_e}^{x_b} \mathrm{f} \left( x \right) \mathrm{d} x = \frac{1}{2}$

La médiane est la valeur qui divise la population en deux sous-populations de probabilité équiprobable. De fait, dans la pratique, il s'agit d'une valeur qui ne se calcule pas.

> [!NOTE]
> La médiane n'est pas influencée par les valeurs extrêmes (ou aberrantes), à la différence de la moyenne arithmétique.

> [!NOTE]
> Par contre, la médiane est influencée par le nombre des données. Elle ne peut ainsi être utilisée en théorie de l'estimation. La médiane est déterminée par le **classement** des valeurs, et non par les valeurs extrêmes, donc elle résume bien des distributions fortement dissymétriques.

> [!NOTE]
> La médiane ne peut exister pour une variable statistique discrète, puisqu'elle correspond à la seule valeur possible de cette variable.

> [!NOTE]
> La médiane est le point d'intersection des courbes cumulatives croissantes et décroissantes.

> [!NOTE]
> La médiane ne se prête pas aux combinaisons algébriques. La médiane d'une série globale ne peut pas être déduite des médianes des séries composantes.

### Le mode

Le **mode**[^10] (ou valeur dominante) $m_0$ d'une série statistique fait référence à toute modalité correspondant à l'effectif maximal (ou à la densité maximale). Il correspond à la valeur $x$ qui est la plus fréquente (variable discrète), ou qui a la plus forte densité de probabilité :

$\mathrm{f}' \left( m_0 \right) = 0 \textrm{ avec } x_a \leq m_0 \leq x_b$

Dit autrement, il s'agit d'une **moyenne de fréquence**.

> [!NOTE]
> Le mode n'existe pas toujours, et, lorsqu'il existe, il n'est pas toujours unique ; on parle alors de distribution bimodale (ou plurimodale).

> [!NOTE]
> Si, après le regroupement des données en classes, deux ou plusieurs modes différents sont trouvés. Il faut considérer que deux ou plusieurs populations distinctes ayant chacune leurs caractéristiques propres sont en présence. Dans ce cas, la moyenne arithmétique n'est pas une caractéristique de tendance centrale.
\end{description}

### La médiale

La **médiale** est la valeur centrale qui partage en deux parties égales la masse de la variable. Il s'agit d'une médiane calculée relativement aux **valeurs globales** $n_i x_i$.  Elle est noté $m_l$. Elle partage les valeurs globales en deux parties égales représentant chacune 50 % des valeurs globales. Le produit $n_i x_i$ ne représente plus seulement l'effectif, mais l'importance de la totalité du caractère possédé par les individus.

**Exemple.** La médiale partage un ensemble d'employés d'une entreprise en deux groupes, tels que la somme totale des salaires perçus par le premier groupe soit égale à la somme totale des salaires perçus par le second groupe.

Le calcul de la médiale suit trois étapes.

1. Détermination des valeurs globales relatives $q_i$

$q_i = \frac{n_i x_i}{\sum_{i = 1}^{n} n_i x_i}$

2. Détermination des valeurs globales relatives cumulées croissantes $Q_i$

3. Détermination de la médiale par interpolation linéaire, c'est-à-dire le calcul classique de la médiane.

La **concentration** $C$ compare la médiale à la médiane $m_e$.

$C = \frac{m_l - m_e}{\omega} = \frac{\Delta M}{\omega}$

avec $\omega$ l'intervalle de variation de la série statistique (ou étendue).

La médiale est toujours supérieure à la médiane. 50 % des effectifs cumulés croissants ne permettront jamais d'atteindre 50 % de la masse totale.

$m_l \geq m_e$

La comparaison des valeurs de la médiale et de la médiane constitue une **mesure de concentration**. En général, si $\Delta M$ est grand par rapport à l'intervalle de variation, la concentration est forte. Inversement, si $\Delta M$ est petit par rapport à l'étendue, la concentration est faible. Dit autrement, lorsque l'écart entre la médiale et la médiane est important par rapport à l'étendue de la distribution de la variable, la concentration est forte. Par contre, lorsque l'écart entre les deux est faible, la concentration est faible ; la distribution est égalitaire. La médiale est liée par l'**indice de C. Gini** [10bis].

La courbe de C. Gini a pour objectif de décrire les effets de la concentration d'une population statistique. Elle se construit sur un repère orthonormé à partir des fréquences cumulées relatives. Les valeurs de la fréquence cumulée globale relative de la série $Q \left( x \right)$ sont portées en ordonnée. Elles varient entre 0 et 1. La courbe se construit point par point. On porte sur l'axe des abscisses les valeurs $F \left( x \right)$ et sur l'axe des ordonnées les valeurs $Q \left( x \right)$. On obtient le **carré de M. O. Lorenz**[^12]. Un pourcentage $F_i$ de la population se partage un pourcentage $Q_i$ de la masse totale des valeurs globales. **Plus la courbe s'éloigne de la diagonale du carré, plus la concentration est importante**.

> [!NOTE]
> Les valeurs de la fréquence cumulée de la série $\left( n_i, x_i \right)$ sont portées en abscisse. Elles varient entre 0 et 1.

**Pour définir n'importe quelle caractéristique, à l'exception de la moyenne arithmétique, il faut que les données soient classées en ordre croissant (ou décroissant)**. Par exemple, pour le calcul de la médiane, un résultat différent peut être établi selon que les données sont classées par ordre croissant ou décroissant.

## Paramètres de dispersion

Le premier paramètre de dispersion est la variance (ou l'écart type), mais il en existe d'autres : le coefficient de variation, l'étendue, l'écart interquantile, l'écart moyen, la boîte à moustache, *etc*. Les **paramètres de dispersion** correspondent souvent à des paramètres d'échelle concernant les données étudiées. Ils donnent un sens aux paramètres de position.

### La variance et l'écart type

Comme vu précédemment, la variance est l'indicateur de dispersion par excellence, mais, exprimé dans la même unité que la moyenne, il est souvent plus pratique d'utiliser l'écart type.

##### La variance

La variance[^13] peut être également appelée **écart quadratique moyen** (E.Q.M.) ou {variance estimée}.

La **variance $\mathbb{V}$** est la moyenne de la somme des carrés des écarts par rapport à la moyenne arithmétique (ou à la moyenne des carrés moins le carré de la moyenne). Elle correspond au nombre :

$\mathbb{V} \left( X \right) = \frac{1}{n} \sum_{i = 1}^{p} \left[ n_i \left( x_i - \left\langle x \right\rangle \right)^2 \right] = \frac{1}{n} \sum_{i = 1}^{p} \left( n_i {x_i}^2 \right) - \left\langle x \right\rangle^2$

La variance tient compte de toutes les données ; il s'agit de la **meilleure caractéristique de dispersion**. 

##### L'écart type

L'écart type[^14] s'appelle aussi **dispersion** ou **déviation standard**.

On note l'écart type $\sigma \left( X \right)$ et correspond à la racine carrée de la variance.

$\sigma \left( X \right) = \sqrt{\mathbb{V} \left( X \right)}$

- **Propriété 1.** L'écart type caractérise la dispersion d'une série de valeurs. Plus l'écart type est petit, plus les données sont regroupées autour de la moyenne arithmétique, et plus la population est homogène. Cependant, avant de conclure, il faut faire attention à l'ordre de grandeur des données.

- **Propriété 2.** L'écart type permet de trouver le pourcentage de la population appartenant à un intervalle centré sur l'espérance mathématique.

### Le coefficient de variation

Le **coefficient de variation**[^15] d'une série statistique est le rapport $CV$ :

$CV = \frac{\sigma}{\left\langle x \right\rangle}$

Il s'agit d'un nombre sans dimension permettant de comparer la dispersion de séries statistiques dont les moyennes sont différentes. Ce paramètre est très usité.

> [!NOTE]
> Le coefficient de variation ne dépend pas des unités choisies.

> [!NOTE]
> Il permet d'apprécier la représentativité de la moyenne arithmétique par rapport à l'ensemble des données.

> [!NOTE]
> Il permet d'apprécier l'homogénéité de la distribution. Une valeur du coefficient de variation inférieure à 15 % traduit une bonne homogénéité de la distribution.

> [!NOTE]
> Il permet de comparer deux distributions, même si les données ne sont pas exprimées avec la même unité, ou si les moyennes arithmétiques des deux séries sont différentes.

### L'étendue

L'**étendue**[^16] $E$ d'une série statistique associée à un caractère quantitatif est la différence entre la plus grande valeur observée et la plus petite.

$E = x_{\max} - x_{\min}$


> [!NOTE]
> L'étendue est facile à calculer.
 
> [!NOTE]
> L'étendue ne contient que des valeurs extrêmes de la série. Elle ne dépend ni du nombre, ni des valeurs intermédiaires. Elle est très peu utilisée dès que le nombre de données dépasse 10.

### L'écart interquantile

Les **quantiles**[^17] sont des caractéristiques de position partageant la série statistique ordonnée en $k$ parties égales.

En partageant la série ordonnée des résultats en quatre parties de même effectif $\left( k = 4 \right)$, on obtient les quartiles $Q_1$, $Q_2$ et $Q_3$. Le deuxième quartile $Q_2$ est la médiane. L'écart interquartile est le nombre $Q_3 - Q_1$ ; il contient 50 % des valeurs de la série.

L'intervalle interquartile peut également se définir de manière continue :

$\int_{x_a}^{Q_1} \mathrm{f} \left( x \right) \mathrm{d} x = \int_{Q_1}^{x_b} \mathrm{f} \left( x \right) \mathrm{d} x = 0,25$

L'intervalle interquartiles $\left( Q_2 - Q_1 \right)$ contient 50 % de la population.

L'**étendue interquartile**[^18] (E.I.Q.) est la différence entre deux quartiles. Elle mesure la dispersion de la moitié centrale des observations.

> [!NOTE]
> On peut définir également les quatre quintiles $\left( k = 5 \right)$, les neuf déciles $\left( k = 10 \right)$, les quatre-vingt dix-neuf centiles $\left( k = 100 \right)$, *etc*.

### L'écart moyen

L'**écart moyen**[^19] d'un ensemble $X = \left\lbrace x_1, x_2, \ldots{}, x_n \right\rbrace$ est défini par :

$EM = \frac{1}{n} \sum_{i = 1}^{n} \left| x_i - \left\langle x \right\rangle \right|$

où $\left\langle x \right\rangle$ est la moyenne arithmétique des nombres, et $\left| x_i - \left\langle x \right\rangle \right|$ est la valeur absolue de la différence entre $x_i$ et $\left\langle x \right\rangle$.

Si $x_1, x_2, \ldots{}, x_k$ ont les fréquences respectives $f_1, f_2, \ldots{}, f_k$ d'apparition, l'écart moyen s'écrit :

$EM = \frac{1}{n} \sum_{i = 1}^{k} n_i \left| x_i - \left\langle x \right\rangle \right|$

avec $\frac{n_i}{n} = f_i$.

On peut définir aussi l'écart moyen en fonction des écarts absolus à la médiane, ou à tout autre indicateur de tendance centrale. Une propriété importante de la somme $\sum_{i = 1}^{k} \left| x_i - a \right|$ est qu'elle est minimale pour la médiane. Cela signifie que l'écart moyen par rapport à la médiane est inférieur à tout autre indicateur.

La terminologie d'**écart moyen absolu** serait mieux appropriée que celle d'écart moyen.

L'**écart moyen $e_a$** peut également s'écrire de manière continue. Il correspond à la moyenne des valeurs absolues des déviations $\left( x - \left\langle x \right\rangle \right)$.

$e_a = \int_{x_a}^{x_b} \left| x - \left\langle x \right\rangle \right| \mathrm{f} \left( x \right) \mathrm{d} x$

### La boîte de dispersion

J. W. Tukey[^20] baptisa la boîte de dispersion[^21]. La boîte à moustache permet de représenter schématiquement les principales caractéristiques d'une distribution en utilisant les quartiles, par exemple.

Elle correspond à une représentation graphique d'un **caractère quantitatif**. Elle sert à comparer visuellement plusieurs séries statistiques.

Pour une série donnée, on trace un rectangle qui s'étend de $Q_1$ à $Q_3$, et on marque la médiane par un trait. On ajoute les « moustaches » qui sont les segments qui vont de la valeur minimale à $Q_1$, et de $Q_3$ à la valeur maximale, puis on fait de même avec les déciles $D_1$ et $D_9$ (Fig 1).

![fig1](./IMG/Boite-a-moustache.png "La boîte à moustache")

**Figure 1. La boîte à moustache**

## Propriétés de l'espérance, de la variance et de l'écart type

Les propriétés suivantes sont universelles. Elles s'appliquent à n'importe quelle distribution. Ces formules permettent d'en établir les paramètres de position et de dispersion. Elles fixent leur algèbre.

### Espérance

L'espérance se calcule de façon discrète :

$\mathbb{E} \left( X \right) = \sum_{i = 1}^{n} {p_i} {x_i}$

ou, en version continue :

$\mathbb{E} \left( X \right) = \int_{-\infty}^{+\infty} x f \left( x \right) \mathrm{d} x$

Soient $X$ et $Y$ deux variables aléatoires, soient $a$ et $b$ deux constantes réelles,

- **Propriété 1.** $\mathbb{E} \left( a X \right) = a \mathbb{E} \left( X \right)$

- **Propriété 2.** $\mathbb{E} \left( X + b \right) = \mathbb{E} \left( X \right) + b$

- **Propriété 3.** $\mathbb{E} \left( X \pm Y \right) = \mathbb{E} \left( X \right) \pm \mathbb{E} \left( Y \right)$

- **Propriété 4.** $\mathbb{E} \left( aX + bY \right) = a \mathbb{E} \left( X \right) + b \mathbb{E} \left( Y \right)$

- **Propriété 5.** $\mathbb{E} \left( aX + b \right) = a \mathbb{E} \left( X \right) + b$

### Variance

La variance se calcule de façon discrète :

$\mathbb{V} \left( X \right) = \sum_{i = 1}^{n} {p_i} \left( {x_i} - \mathbb{E} \left( X \right) \right)^2$

ou, en version continue :

$\mathbb{V} \left( X \right) = \int_{-\infty}^{+\infty} \left( x - \mathbb{E} \left( X \right) \right)^2 f \left( x \right) \mathrm{d} x$

La variance peut être vue comme l'espérance du carré des écarts à l'espérance $\mathbb{E} \left( X \right)$.

$\mathbb{V} \left( X \right) = \mathbb{E} \left[ {\left( X - \mathbb{E} \left( X \right) \right)}^2 \right]$

Soient $X$ et $Y$ deux variables aléatoires, soient $a$ et $b$ deux constantes réelles,

- **Propriété 1.** $\mathbb{V} \left( X \right) = \mathbb{E} \left( X^2 \right) - {\left[ \mathbb{E} \left( X \right) \right]}^2$

- **Propriété 2.** $\mathbb{V} \left( a X \right) = a^2 \mathbb{V} \left( X \right)$ (fonction scalante)

- **Propriété 3.** $\mathbb{V} \left( X + a \right) = \mathbb{V} \left( X \right)$

- **Propriété 4.** $\mathbb{V} \left( a X + b \right) = \mathbb{V} \left( a X \right) = a^2 \mathbb{V} \left( X \right)$

- **Propriété 5.** Pour $\mathbb{V} \left( a X \right) = 0$, si $\mathbb{V} \left( X \right) = 0$ alors $X = \mathbb{E} \left( X \right)$

### Propriétés conditionnées par la nature de la variable aléatoire

Soient $X$ et $Y$ deux variables aléatoires indépendantes, soient $a$ et $b$ deux constantes réelles :

- **Propriété 1.** $\mathbb{E} \left( XY \right) = \mathbb{E} \left( X \right) \mathbb{E} \left( Y \right)$

- **Propriété 2.** $\mathbb{V} \left( aX + bY \right) = a^2 \mathbb{V} \left( X \right) + b^2 \mathbb{V} \left( Y \right)$

- **Propriété 3.** $\mathbb{V} \left( X \pm Y \right) = \mathbb{V} \left( X \right) + \mathbb{V} \left( Y \right)$

> [!WARNING]
> La réciproque est fausse.

Soient $X$ et $Y$ deux variables aléatoires dépendantes, soient $a$ et $b$ deux constantes réelles :

- **Propriété 1.** $\mathbb{V} \left( X \pm Y \right) = \mathbb{V} \left( X \right) + \mathbb{V} \left( Y \right) \pm 2 \mathrm{cov} \left( X, Y \right)$ avec $\mathrm{cov} \left( X, Y \right) = \mathbb{E} \left( XY \right) - \mathbb{E} \left( X \right) \mathbb{E} \left( Y \right)$

- **Propriété 2.** $\mathbb{V} \left( aX + bY \right) = a^2 \mathbb{V} \left( X \right) + b^2 \mathbb{V} \left( Y \right) + 2ab\mathrm{cov} \left( X, Y \right)$

### Écart type

Soit $X$ une variable aléatoire et $a$ et $b$ deux variables réelles :

- **Propriété 1.** $\sigma \left( X \right) = \sqrt{\mathbb{V} \left( X \right)}$

- **Propriété 2.** $\sigma \left( X + b \right) = \sigma \left( X \right)$

- **Propriété 3.** $\sigma \left( a X \right) = \left| a \right| \sigma \left( X \right)$

- **Propriété 4.** $\sigma \left( a X + b \right) = \sigma \left( a X \right) = \left| a \right| \sigma \left( X \right)$

### Remarque importante

Tout cela se généralise sans problème avec $n$ variables.

## Les paramètres de forme

Les **paramètres de forme** caractérisent l'aplatissement, la symétrie, *etc*. de la loi de distribution statistique de la variable aléatoire étudiée. Avant de définir les paramètres de forme, il faut expliquer rapidement la notion de moments.

### Les moments

Pour $r \in \mathbb{N} \textrm{ ou } \mathbb{Z}$ et sous réserve de convergence absolue, le **moment**[^22] **d'ordre $r$** est défini par :

$m_r = \frac{1}{n} \sum_{i = 1}^{p} n_i {x_i}^r$

ou encore,

$m_r = \int_{x_a}^{x_b} x^r \mathrm{f} \left( x \right) \mathrm{d} x$

Le **moment 1** est l'espérance. La formule du moment généralise la notion de moyenne. La variance est la différence entre le moment d'ordre 2 et le carré du moment d'ordre 1.

Pour tout $r\acute{} < r$, si $m_r$ existe alors $m_{r\acute{}}$ existe. 

Le **moment centré**[^23] **d'ordre $r$** est :

${\mu}_r = \frac{1}{n} \sum_{i = 1}^{p} n_i \left( x_i - \left\langle x \right\rangle \right)^r$

ou encore,

${\mu}_r = \frac{1}{n} \sum_{i = 1}^{p} \left( x - \left\langle x \right\rangle \right)^r$

ou encore,

${\mu}_r = \int_{x_a}^{x_b} \left( x_i - \left\langle x \right\rangle \right)^r \mathrm{f} \left( x \right) \mathrm{d} x$

Le **moment absolu d'ordre $k$** (ou moment centré d'ordre $k$) par rapport à un point $a$, est égal à, sous réserve de l'existence de l'intégrale :

$\mathbb{E} \left(\left| X - a \right|^k \right) = \int \left| x - a \right|^k \mathrm{f} \left( x \right) \mathrm{d} x$

La propriété essentielle est la **formule de Königs**[^24]**-Huyghens**[^25]  :

$\mathbb{E} \left[ \left( X - a \right)^2 \right] = \mathbb{V} \left( X \right) + \left[ \mathbb{E} \left( X \right) - a \right]^2$
 
Il peut également s'écrire :

$x_k = \sum_{i = 1}^{p} f_i \left( x_i - a \right)^k$

ou

$x_k = \frac{1}{n} \sum_{i = 1}^{p} n_i \left( x_i - a \right)^k$

Les moments permettent de caractériser une distribution.

| **Ordre** | **Moment** | **Moment centré** |
| :-: | :-: | :-: |
| $r=1$ | $m_1 = \int_{x_a}^{x_b} x \textrm{f} \left( x \right) \textrm{d} x$ Il correspond à la moyenne. | ${\mu}_1 = 0$ |
| $r=2$ | $m_2 = \int_{x_a}^{x_b} x^2 \textrm{f} \left( x \right) \textrm{d} x$ | ${\mu}_2 = \int_{x_a}^{x_b} \left( x - \left\langle x \right\rangle \right)^2 \textrm{f} \left( x \right) \textrm{d} x$ Il correspond à la variance. L'écart type correspond à : $\sigma = \sqrt{{\mu}_2}$. |
 
**Tableau 8. Les moments d'ordre 1 et 2**

###### Démonstration du moment centré d'ordre 1

${\mu}_1 = \int_{x_a}^{x_b} \left( x - \left\langle x\right\rangle \right) \mathrm{f} \left( x \right) \mathrm{d} x = \int_{x_a}^{x_b}  x \mathrm{f} \left( x \right) \mathrm{d} x - \int_{x_a}^{x_b} \left\langle x \right\rangle \mathrm{f} \left( x \right) \mathrm{d} x = m_1 - m_1 \int_{x_a}^{x_b} \mathrm{f} \left( x \right) \mathrm{d} x = 0$

car $\int_{x_a}^{x_b} \mathrm{f} \left( x \right) \mathrm{d} x$ est la loi de probabilité c'est-à-dire que l'intégrale vaut 1.

Les premiers moments centrés sont liés aux moments non centrés (Tab. 9).

| **Moment centré** | **Moment non centré** |
| :-: | :-: |
| ${\mu}_2 = m_2 - {m_1}^2$ | $m_2 = {\mu}_2 + {m_1}^2$ |
| ${\mu}_3 = m_3 - 3 {m_1} {m_2} + 2 {m_1}^3$ | $m_3 = {\mu}_3 - 3 {m_1} {\mu}_2 + {m_1}^3$ |
| ${\mu}_4 = m_4 - 4 {m_1} {m_3}^2 + 6 {m_1}^2 {m_2} - 3 {m_1}^4$ | $m_4 = {\mu}_4 - 4 {m_1} {\mu}_3 + 6 {m_1}^2 {\mu}_2 + {m_1}^4$ |
 
**Tableau 9. Lien entre les moments centrés et les moments non centrés**

###### Exemple du moment centré d'ordre 3

${\mu}_3 = \frac{1}{n} \sum_{i = 1}^{p} n_i \left( x_i - \left\langle x \right\rangle \right)^3 = \frac{1}{n} \sum_{i = 1}^{p} n_i \left( {x_i}^3 - 2 {x_i}^2 \left\langle x \right\rangle + x_i \left\langle x \right\rangle^2 - {x_i}^2 \left\langle x \right\rangle + 2 x_i \left\langle x \right\rangle^2 - \left\langle x \right\rangle^3 \right)$

${\mu}_3 = m_3 - 2 m_1 m_2 + {m_1}^3 - m_1 m_2 + 2 {m_1}^3 - \frac{1}{n} \sum_{i = 1}^{p} n_i \left\langle x \right\rangle^3 \textrm{ où } \frac{1}{n} \sum_{i = 1}^{p} n_i = 1$

${\mu}_3 = m_3 - 3 m_1 m_2 + {m_1}^3 + 2 {m_2}^3 - {m_1}^3$

${\mu}_3 = m_3 - 3 m_1 m_2 + 2 {m_1}^3$

### Les coefficients ${\beta}_1$ et ${\beta}_2$ de Pearson[^26] et de Fisher[^27]

Pour une **distribution symétrique**, le mode, la moyenne arithmétique et la médiane sont égaux.

##### La mesure de la dissymétrie ${\beta}_1$

La mesure de la dissymétrie[^28] ${\beta}_1$ (ou de l'asymétrie) vaut :

${\beta}_1 = \frac{{\mu}_3}{{{\mu}_2}^{\frac{3}{2}}} = \frac{{\mu}_3}{{\sigma}^3}$

Si ${\beta}_1 > 0$ alors la distribution est étalée sur la droite. La dissymétrie est dite **positive**.

Si ${\beta}_1 < 0$ alors la distribution est étalée sur la gauche. La dissymétrie est dite **négative**.

Si ${\beta}_1 = 0$ alors la distribution est **symétrique**.

##### La mesure d'aplatissement ${\beta}_2$

La mesure d'aplatissement[^29] ${\beta}_2$ vaut :

${\beta}_2 = \frac{{\mu}_4}{{{\mu}_2}^4} - 3$

Si ${\beta}_2 > 0$ alors la distribution est dite **platicurtique**.

Si ${\beta}_2 < 0$ alors la distribution est dite **leptocurtique**.

Si ${\beta}_2 = 0$ alors la distribution est dite **mésocurtique**. On peut citer la **loi normale** qui entre dans cette catégorie.

> [!NOTE]
> Si les coefficients d'asymétrie et d'aplatissement sont proches de zéro, alors la distribution est symétrique.

> [!WARNING]
> Si les coefficients d'asymétrie et d'aplatissement sont des estimateurs biaisés. Il faut utiliser les définitions de la moyenne et de l'écart type non biaisés pour les calculer dans le cadre d'un échantillon.

## Liens

- [Topo en format P.D.F.](./PDF/Seance-03.pdf)

- [Exercice](./Exercice/Seance-3.pdf)

## Notes de bas de page

[^1]: Une algèbre est un ensemble de règles de calcul.

[^2]: En anglais, on emploie soit *mean* qui est un nom, soit *average* qui est un nom et un adjectif.

[^3]: En anglais : *arithmetic mean*, *arithmetic average*

[^4]: En anglais : *weighted average*

[^5]: En anglais : *root mean square*, *quadratic mean*

[^6]: En anglais : *harmonic mean*

[^7]: En anglais : *geometric mean*, *geometric average*

[^8]: En anglais : *moving average*

[^9]: En anglais : *median value*

[^10]: En anglais : *mode*

[^11]: Corrado Gini (1884-1965)

[^12]: Max Otto Lorenz (1876-1959)

[^13]: En anglais : *variance*

[^14]: En anglais : *standard deviation*

[^15]: En anglais : *coefficient of variation*

[^16]: En anglais : *extent*

[^17]: En anglais : *quantile*

[^18]: En anglais : *interquartile ranges* (I.Q.R.)

[^19]: En anglais : *mean spread*, *average spread*

[^20]: En anglais : John Wilder Tukey (1915-2000)

[^21]: En anglais : *box-plot*

[^22]: En anglais : *moment*

[^23]: En anglais : *central moment*

[^24]: Johann Samuel König (1712-1757)

[^25]: Christian Huygens (1629-1695)

[^26]: Karl Pearson (1857-1936)

[^27]: Ronald Aymer Fisher (1890-1962)

[^28]: En anglais : *shewness*

[^29]: En anglais : *kurtosis*

# Séries temporelles

Une **série chronologique** (ou une chronique) est constituée par une suite ordonnée d'observations d'une grandeur au cours du temps. Il s'agit de décrire, expliquer, contrôler, prévoir des phénomènes évoluant au cours du temps.

## Éléments constitutifs d'une série chronologique

L'étude d'une série chronologique $\left\lbrace x_p : t = 1, \ldots{}, T \right\rbrace$ consiste à dissocier les différents mouvements qui la composent et à les analyser. Cette décomposition est une **construction de l'esprit** puisque les séries composantes sont des concepts abstraits et ne peuvent pas être directement observées.

En début d'analyse, **une représentation graphique s'impose**. Il s'agit de faire apparaître les éléments fondamentaux.

Les intervalles entre deux observations successives sont supposés de même longueur.

> [!NOTE]
> En pratique, c'est rarement le cas. De nombreuses données sont censurées.

- L'intervalle peut être

	- l'année ;

	- le mois ;

	- le jour ;

	- l'heure ;

	- la minute ;

	- la seconde ;

	- *etc*.

### La tendance à long terme

La **tendance à long terme**[^1], notée $f_t$, est le facteur représentant l'évolution à long terme de la grandeur. Elle traduit l'aspect général de la série chronologique étudiée.

Un **mouvement cyclique** peut se superposer à la tendance à long terme. La composante cyclique est liée à la succession des phases d'un cycle.

### Le mouvement saisonnier

Le **facteur saisonnier**, noté $s_t$, se répète à **intervalles de temps égaux** avec une forme à peu près constante. On peut ainsi déterminer des **périodes** $T$ au sens mathématique :

- $T = 12$ pour les séries mensuelles ;

- $T = 4$ pour les séries trimestrielles ;

- *etc*.

On a ainsi :

$s_t = s_{t + T} = s_{t + 2T} = \ldots{}$

Le facteur saisonnier est **totalement** déterminé par $T$ coefficients saisonniers :

$s_1, \ldots{}, s_j, \ldots{}, s_T$

### Les irrégularités

Les **irrégularités** sont appelées **mouvement résiduel**. Elles sont notées $e_t$. Elles regroupent tout ce qui n'a pas été pris en compte par la tendance et le facteur saisonnier. Elles sont la résultante de fluctuations irrégulières et imprévisibles dues à des facteurs perturbateurs non permanents. Ces fluctuations sont supposées de **faible amplitude** et de **moyenne nulle** sur un petit nombre d'observations consécutives.

### Les perturbations

Les **perturbations** sont des fluctuations ponctuelles de forte amplitude. Il convient de les **éliminer** avant tout traitement de la série. Les méthodes pour y parvenir sont simples :

1. l'interpolation ;

2. la règle de trois.

On traite généralement des séries :

- à deux composantes : tendance et mouvement résiduel ;

- à trois composantes : tendance, mouvement saisonnier et mouvement résiduel.

Les observations d'une chronique possédant une composante saisonnière peuvent être disposées dans un tableau selon deux dimensions de temps : annuelle et mensuelle (ou trimestrielle). Ce type de présentation fut inventé par C. Buys-Ballot[^2] en 1847.

## Les modèles de composition d'une série chronologique

La décomposition d'une série chronologique possédant un **mouvement saisonnier** peut s'effectuer selon trois types de modèles :

1. le modèle additif : $x_t = f_t + s_t + e_t$ avec $t = 1, \ldots{}, T$ ;

2. le modèle multiplicatif : $x_t = f_t \left( 1 - s_t \right)\left( 1 + e_t\right)$ avec $t = 1, \ldots{}, T$ ;

3. le modèle mixte : $x_t = f_t \left( 1 + s_t \right) + e_t$ avec $t = 1, \ldots{}, T$ ;

#### Le modèle multiplicatif

On choisit un modèle multiplicatif ou mixte si le mouvement saisonnier présente des amplitudes proportionnelles à la tendance.

> [!NOTE]
> Une transformation logarithmique permet de linéaiser le modèle multiplicatif :
> $\ln \left( x_t \right) = \ln \left( f_t \left( 1 - s_t \right)\left( 1 + e_t\right) \right) = \ln \left( f_t \right) \ln \left( 1 - s_t \right) \ln \left( 1 + e_t\right)$

Souvent, on pose $\ln \left( 1 + e_t\right) \approx e_t$.

Pour le mouvement saisonnier de période $T$, on fait l'hypothèse d'une compensation exacte sur une période entre les variations saisonnières positives et les variations saisonnières négatives, afin de lever l'indétermination sur le partage entre le facteur saisonnier et la tendance générale :

$\sum_{j = 1}^{T} s_j = 0$

**La série présente-t-elle des variations saisonnières ? Si oui, quel est le schéma de composition le mieux adapté ?**

1. On repère les points maximaux et les points minimaux, les *extrema*. Ils doivent être saisonniers, c'est-à-dire séparés par une période $T$.

2. Pour établir le modèle de décomposition, on relie les *extrema*. On obtient deux courbes.

- Si ces deux courbes sont à peu près parallèles, alors le facteur saisonnier a des amplitudes à peu près constantes. Dit autrement, il affecte la tendance indépendamment de son niveau. Le **modèle additif** est le plus adapté.

- Si ces deux courbes sont à peu près parallèles dans le repère bi-logarithmique, alors le facteur saisonnier a des amplitudes à peu près proportionnelles à la tendance. Dit autrement, les effets des variations saisonnières sont proportionnels au niveau atteint par la tendance. Le **modèle multiplicatif** est adapté.

#### Le modèle additif

Le modèle additif, si la somme des coefficients saisonniers n'est pas nulle sur une période, doit être corrigé. Les coefficients saisonniers doivent être obtenus avec une somme non nulle :

$s_t \rightarrow s_t^{*} = s_t - \bar{s}$

avec $\bar{s} = \frac{1}{p} \sum_{t = 1}^{p} s_t$

On appelle **série corrigée des variations saisonnières** (C.V.S.) la série des différences : $x_t^{*} = x_t - s_t^{*}$ :

$e_t = x_t - s_t^{*} = x_t^{*} - y_t$

## Analyse de la tendance

### Ajustement de la tendance par une fonction analytique

Il existe plusieurs modèles :

- le modèle linéaire : $y \left( t \right) = a + bt$ ;

- le modèle quadratique : $y \left( t \right) = a + bt + ct^2$ ;

- le modèle exponentiel : $y \left( t \right) = e^{a + bt}$ ;

- le modèle logarithmique : $y \left( t \right) = a + b \ln \left( t \right)$ ;

- le modèle en S (avec un courbe sigmoïde) : $y \left( t \right) = e^{a + \frac{b}{t}}$ ;

Il existe deux principaux filtres linéaires :

1. la moyenne mobile ;

2. le lissage exponentiel simple.

Le choix du filtre linéaire approprié à certains objectifs s'effectue par l'intermédiaire du choix des coefficients ${\alpha}_k$.

$y \left( t \right) = \sum_{k \in K}^{} {\alpha}_{k^x t +k}$

avec $K \subset \mathbb{Z}$, et

$\sum_{k \in K}^{} {\alpha}_{k} = 1$

### Moyenne mobile

On appelle **moyennes mobiles centrées** de longueur $p$ avec $p < T$ de la série chronologie $\left\lbrace x_t : t = 1, \ldots{}, T \right\rbrace$ les moyennes successives calculées en fonction de la parité de $p$.

- Si $p$ est impair, $p = 2m + 1, M_p \left( t \right) = \frac{1}{p} \sum_{k = m}^{m} x_{t + k}$, il existe $T - p + 1$ moyennes mobiles centrées de longueur impaire $p$

- Si $p$ est pair, $p = 2m, M_p \left( t \right) = \frac{1}{p} \left( \frac{x_{t - m}}{2} + \sum_{k = -m + 1}^{m - 1} x_{t + k} + \frac{x_{t + k}}{2} \right)$.

La moyenne centrée mobile $M_{2m} \left( t \right)$ est une **moyenne pondérée** de valeurs de la série encadrant la date $t$ avec les coefficients de pondération égaux à $\frac{1}{2p}$ pour les valeurs extrêmes $x_{t - m}$ et $x_{t + m}$, et égaux à $\frac{1}{p}$ pour les $p - 2$ valeurs intermédiaires $x_{t - m + 1}$ à $x_{t + m + 1}$. Il existe $T - p$ moyennes mobiles centrées de longueur paire $p$. La série comporte $p + 1$ termes.

La moyenne mobile centrée de longueur $p$ rend **constantes** les séries périodiques de période $p$. Dit autrement, deux chroniques ont la même suite de moyennes mobiles centrées de longueur $p$ si leur différence est une série périodique de période $p$ dont la somme des termes sur une période est nulle.

La moyenne mobile centrée transforme une série alignée en elle-même. Plus généralement, une série monotone à faible courbure en une série peu différente.

Les irrégularités sont supposées être indépendantes, de moyenne nulle sur un petit nombre de dates successives. et de même variance. La moyenne mobile transforme des écarts dus à des irrégularités en écarts de variance plus faibles. C'est un **effet de rabot**. Elle liste la chronologie, en ce sens que la série $Y$ est moins dispersée que la série initiale $X$.

> [!NOTE]
> Les nouvelles irrégularités qui sont corrélées entre elles, peuvent faire apparaître des oscillations parasites, non présentes dans la série initiale. C'est un **effet Slutsky-Yule**[^3] [^4] [^5] (traduit en anglais dans [^6]).

Si la période du mouvement saisonnier est égale à $T$, alors la moyenne mobile centrée de longueur $T$ est un filtre linéaire éliminant le mouvement saisonnier tout en réduisant l'amplitude du mouvement résiduel.

La technique de la moyenne mobile présente deux inconvénients.

1. Un changement de niveau ou de pente de la tendance à une date $t$ entraîne une mauvaise approximation de cette composante pendant toute une période précédant et suivant cette date.

2. Si $T = np$ observations avec $n$ le nombre d'années (par exemple) et $p$ la période du mouvement saisonnier, alors on ne peut calculer que $T - p$ moyennes mobiles de longueur $p$. De fait, pour la tendance des $\frac{p}{2}$ dernières dates, on ne disposera pas de valeurs pour une prévision.

### Lissage exponentiel

Les **méthodes de lissage exponentiel** furent inventées par R. G. Brown[^7] en 1962. Elles constituent des méthodes d'extrapolation qui fournissent un poids prépondérant aux valeurs récentes. Elles se caractérisent par :

1. la simplicité des calculs ;

2. le petit nombre des données à garder en mémoire.

Il existe deux types de lissage exponentiel :

- le lissage exponentiel simple (L.E.S.) ;

- le lissage exponentiel double (L.E.D.).

#### Le lissage exponentiel simple (L.E.S.)

La méthode de prévision s'applique à des **chroniques sans variations saisonnières et à tendance localement constante**. On suppose que la grandeur observée caractérisée par des variations irrégulières autour de la moyenne :
	$X_t = a + e_t$

avec $t = 1, \ldots{}, T$.

La prévision ${\hat{x}}_T \left( h \right)$ réalisée par la méthode de lissage exponentiel simple à la date $T$ pour l'horizon $h$, c'est-à-dire $T + h$ est :

${\hat{x}}_T \left( h \right) = \alpha \sum_{i = 0}^{T - 1} \left( 1 - \alpha \right)^i.x_{T - i}$

$0 < \alpha < 1$.

Le paramètre $\alpha$ est la constante de lissage. Si $T$ est élevé, la somme des pondérations est peu différente de $1$ :

$\alpha \sum_{i = 0}^{T - 1} \left( 1 - \alpha \right)^i = \alpha \frac{1 - \left( 1 - \alpha \right)^T}{\alpha} = 1 - \left( 1 - \alpha \right)^T \approx 1$

et la prévision ${\hat{x}}_T \left( h \right)$ apparaît comme la moyenne pondérée des valeurs $x_1, \ldots{}, x_T$. Cette prévision ne dépend pas de l'horizon $h$.

Les propriétés du lissage exponentiel sont au nombre de trois.

1. La chronique lissée $\left\lbrace {\hat{x}}_T : t = 1, \ldots{}, T \right\rbrace$ a une variance inférieure à celle de la chronique initiale $\left\lbrace x_T : t = 1, \ldots{}, T \right\rbrace$.

2. Le lissage exponentiel simple est un filtre linéaire.

3. Le lissage exponentiel simple s'adapte avec retard à un changement de niveau de la chronique. C'est de la valeur de la constante de lissage $\alpha$ que dépendent la stabilité et le taux de réponse de la série lissée.

#### Le lissage exponentiel double (L.E.D.)

Le lissage exponentiel double est utilisé pour une **chronique à tendance localement linéaire**. On suppose que la série peut être ajustée par une droite au voisinage de $T$ :

$x_1 = a_1 \left( T \right) + a_2 \left( T \right) \left( t - T \right)$

Les coefficients $a_1 \left( T \right)$ et $a_2 \left( T \right)$ sont choisis de façon à minimiser la quantité :

$\sum_{i = 0}^{T - 1} \left( 1 - \alpha \right)^i \left( x_{T - i} - \left( a_1 \left( T \right) + a_2 \left( T \right) \left( -i \right) \right) \right)^2$

On obtient la solution suivante :

$\left\lbrace \begin{array}{l} {\hat{a}}_1 \left( T \right) = 2 S_1 \left( T \right) - S_2 \left( T \right)\\ {\hat{a}}_2 \left( T \right) = \frac{\alpha}{1 - \alpha} \left( S_1 \left( T \right) - S_2 \left( T \right) \right) \end{array} \right.$

$\left\lbrace \begin{array}{l} S_1 \left( T \right) = \alpha \sum_{i = 0}^{T - 1} \left( 1 - \alpha \right)î x_{T - i}\\ S_2 \left( T \right) = \alpha \sum_{i = 0}^{T - 1} \left( 1 - \alpha \right)î S_1 \left( T - i \right) \end{array} \right.$, ce qui conduit à la prévision :

${\hat{x}}_T \left( h \right) = {\hat{a}}_1 \left( T \right) + {\hat{a}}_2 \left( T \right) h$

La quantité $S_1 \left( T \right)$ résulte du lissage exponentiel de la série $\left\lbrace x_t : t = 1, \ldots{}, T \right\rbrace$. La quantité $S_2 \left( T \right)$ résulte du lissage exponentiel simple de la série $\left\lbrace S_1 \left( t \right) : t = 1, \ldots{}, T \right\rbrace$.

$\left\lbrace \begin{array}{l} S_1 \left( T \right) = \alpha x_T + \left( 1 - \alpha \right) S_1 \left( T - 1 \right)\\ S_2 \left( T \right) = \alpha S_1 \left( T \right) + \left( 1 - \alpha \right) S_2 \left( T - 1 \right) \end{array} \right.$

L'initialisation de ces formules de mise à jour peut être :

$\left\lbrace \begin{array}{l} S_1 \left( T \right) = x_1\\ S_2 \left( T \right) = S_1 \left( 2 \right) \end{array} \right.$

ce qui permet de mettre à jour ${\hat{a}}_1 \left( T \right)$ et ${\hat{a}}_2 \left( T \right)$.

$\left\lbrace \begin{array}{l} {\hat{a}}_1 \left( T \right) = x_T - \left( 1 - \alpha \right)^2 \left( x_T - {\hat{x}}_{T - 1 \left( 1 \right)}\right)\\ {\hat{a}}_2 \left( T \right) = {\hat{a}}_2 \left( T - 1 \right) + {\alpha}^2 \left( x_T - {\hat{x}}_{T - 1} \left( 1 \right) \right) \end{array} \right.$

L'initialisation de ces formules peut être :

$\left\lbrace \begin{array}{l} {\hat{a}}_1 \left( T \right) = x_2\\ {\hat{a}}_2 \left( T \right) = x_2 - x_1 \end{array} \right.$

Le choix de la constante de lissage $\alpha$ peut s'effectuer par la minimisation d'un critère choisi.

#### Le lissage exponentiel des séries saisonnières

On utilise la **méthode de Holt**[^8] [^9]**-Winters**[^10] [^11].

## Liens

- [Topo en format P.D.F.](./PDF/Series-temporelles.pdf)

## Notes de bas de page

[^1]: En anglais : *trend*

[^2]: Christoph Buys-Ballot (1817-1890)

[^3]: Evgenii Evgenievich Slutsky (1880-1948)

[^4]: Yule, George Udny, 1926, "Why Do We Sometimes Get Nonsense-Correlations Between Time-Series? A Study un Sampling and the Nature of Time-Series", *Journal of the Royal Statistical Society*, vol. 89, n°1, p. 1-63

[^5]: Slutsky, Evgenii Evgenievich, 1927, "Slozhenie slucjaunykh prichin, kak istochnik tsiklicheskikh protsessov", *Voprosy kon yunktury*, vol. 3, n°1, p. 34-64

[^6]: Slutsky, Evgenii Evgenievich, 1937, "The Summation of Random Causes as the Source of Cyclic Processes", *Econometrica*, vol. 5, n°2, p. 105-146

[^7]: Brown, Robert Goodell, 1962, *Smoothing forecasting and prediction of discrete time series*, London, Prentice-Hall, X-468 p. [Quantitative Methods Series]

[^8]: Charles C. Holt (1921-2010)

[^9]: Holt, Charles C., 1957, "Forecasting Trends ans Seasonals by Exponentially Weighted Averages", *Carnegie Institute of Technology, Pittburgh Office of Naval Research Memorandum*, 52

[^10]: Peter R. Winters (?-?)

[^11]: Winters, Peter R., 1960, "Forecasting Sales by Exponentially Weighted Moving Averages", *Management Science*, vol. 6, n°3, p. 324-342

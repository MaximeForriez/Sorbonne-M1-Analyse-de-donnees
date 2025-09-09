# Séance 1. Présentation du contenu du cours et mise en route

## Objectifs de la séance

## Présentation des objectifs pédagogiques

## Analyse de données

« L'analyse des données [...] reçoit du calcul des probabilités son inspiration mais non ses méthodes »[^1].

En statistique classique, l'analyse de données correspond à l'étude d'un nombre restreint de caractères mesurés sur un petit ensemble d'individus. On effectue des échantillons, des estimations, des tests statistiques, *etc*. Le problème est que « Dans la pratique, les individus observés sont fréquemment décrits par un grand nombre de caractères »[^2] (p. 3). De plus, « les méthodes d'analyse des données permettent une étude globale des individus et des variables en utilisant généralement des représentations graphiques suggestives »[^2] (p. 3). Cela consiste en :

1. la recherche des vraisemblances ou des différences entre individus ;

2. la recherche d'une classification ;

3. la recherche d'une corrélation ;

4. la recherche d'une indépendance ;

5. l'échantillonnage d'individus tirés aléatoirement dans une population.

En statistique multidimensionnelle, on utilise des méthodes factorielles.

### Références

- [Pour bien commencer...](./PDF/Data-Science-For-Beginners-Sketch-Notes.pdf)

- Pereboom, Victor & van Weerdenburg, Sascha, [Comment créer et gérer un projet nécessitant l'apport de données ?](./PDF/Pereboom-van%20Weerdenburg-Manuel%20for%20Data%20Science%20Projects.pdf)

- Kumar, Lovee, [Synthèse sur les statistiques élémentaires](./PDF/Kumar-Lovee-Statistics.pdf)

- Lin, Maverick, 2018, [Essentiels des statistiques pour l'analyse des données](./PDF/Lin-Maverick-Data-Science-Cheatsheet.pdf)

- Soulmachine, 2017, [*Machine Learning Cheet Sheet*](./PDF/Soulmachine-2007-Machine%20Learning%20Cheat%20Sheet-Classical%20Equations%20Diagrams%20and%20Tricks%20in%20Machine%20Learning.pdf) [Hors programme, mais utile pour ceux qui manipuleront des intelligences artificielles]

### Vocabulaire de base

**Population :** ensemble (mathématique) des individus étudiés

**Tableau de données :** tableau regroupant les individus et les caractères

- **Individu :** « entité de base sur laquelle l'observateur réalise un certain nombre de mesures »[^2] (p. 6). Le terme a pour synonyme : observation, unité statistique, *etc*. L'analyse s'opère soit sur un échantillonnage dans une population, soit sur la population tout entière.

- **Caractère :** élément caractérisant un individu. Le terme a pour synonyme : variables, *etc*. Il peut être soit qualitatif, soit quantitatif.

    - « Un **caractère** est **quantitatif** lorsqu'il prend ses valeurs sur une échelle numérique. [... Il] est quantitatif lorsque l'ensemble des valeurs qu'il prend sur les individus est inclus dans l'ensemble des nombres réels (noté $\mathbb{R}$) et que l'on peut effectuer sur le caractère les opérations algébriques habituelles »[^2] (p. 6-7). Dans ce cadre, le terme « mesure » est synonyme de caractère.

    - « Un **caractère** est **qualitatif** lorsqu'il prend des modalités non numériques »[^2] (p. 7). Le terme « attribut » est dans ce cadre synonyme de caractère. « Sur un caractère qualitatif représenté par ses modalités les opérations algébriques n'ont plus aucun sens »[^2] (p. 7). Toutefois, il ne faut pas croire qu'une modalité non numérique se caractérise par une absence de chiffres. En général, le caractère qualitatif subit un dénombrement rigoureux à partir duquel va découler toutes les analyses de données. Il existe deux types principaux de modalités qualitatives :

        1. les **caractères qualitatifs ordinaux** comme les niveaux hiérarchiques, les niveaux de satisfaction, *etc*. ;

        2. les **caractères qualitatifs nominaux** comme la taille, la couleur des yeux, le nom d'un territoire, *etc*.

- Si on revient au tableau de données, les différents dépendent, entre autres, de la nature des variables étudiées. Il faut insister sur un point fondamental sur lequel il existe beaucoup de confusion, y compris dans les manuels de statistique. Les caractères qualitatifs sont beaucoup plus généraux que les caractères quantitatifs. S'il est possible de transformer n'importe quel caractère quantatitatif en caractère qualitatif (en utilisant des intervalles par exemple), l'inverse n'est pas vrai. Par exemple, si vous recueillez l'âge précis des individus d'une population statistique lors d'une enquête, rien ne vous interdit de catégoriser ce caractère quantitatif en dénombrant les données sont la forme d'un intervalle : « Entre 0 et 18 ans : $n_1$ individus », « Entre 18 et 30 ans : $n_2$ individus », *etc*. Il est à retenir que **tout caractère quantitatif peut être transformé en caractère qualitatif**. Néanmoins, travailler avec des variables quantitatives du fait de leur facilité à être utilisables directement, est toujours plus agréable et préférable pour un apprenti statisticien. Toutefois, ce cours a pour objectif de vous former professionnellement, et un équilibre entre les deux types de variable sera proposé dans ce cours. Au niveau des tableaux de données, il en existe trois grands types :

1. le tableau individus en ligne et caractères en colonne. Chaque cellule contient soit une valeur numérique si le caractère est quantitatif, soit un codage binaire d'absence (0) ou de présence (1) si le caractère est qualitatif ;

> [!NOTE]
> Le codage binaire permet de faire des calculs algébriques avec des caractères qualitatifs.

2. le tableau de contingence. « Le tableau de contingence contient les fréquences d'association entre les modalités de deux caractères qualitatifs »[^2] (p. 9)

3. le tableau de proximité. Avec lui, « étant donné un ensemble d'objets, on dispose d'une mesure de ressemblance ou de dissemblance entre tous les objets pris deux à deux »[^2] (p. 10). En général, ce tableau de proximité contient des distances. Ce peut être des distances au sens géographique, comme une distance à vol d'oiseau entre deux villes, ou des distances au sens de l'algèbre linéaire. Dans chaque méthode statistique, il faut bien faire attention à la définition de la distance utilisée (distance du ${\chi}^2$, distance de Manhattan, *etc*.). La distance est une matrice symétrique dont les valeurs sont positives.

### Objectifs des analyses de données

« En analyse de données on s'intéresse à la **structure** de l'ensemble des individus observés sans chercher nécessairement à en déduire des lois valables pour les populations dont ils sont issus : en ceci, l'analyse de données se rapproche davantage de la statistique descriptive que de la statistique inférentielle »[^2] (p. 6).

En analyse de données, on poursuit deux objectifs non simultanés.

- La **réduction des données** est un ensemble d'opérations consistant à synthétiser les données :

    - par des valeurs de position :

        - moyenne ;
        
        - médiane ;

        - *etc*.
    
    - par des valeurs de dispersion :

        - variance ;

        - écart type ;

        - moments ;

        - *etc*

    - par un centrage (sur la moyenne) et une réduction (par la variance) des données quantitatives.

$z = \frac{x \bar{x}}{{\sigma}^2}$

avec $x$ la valeur initiale, $\bar{x}$ la moyenne de l'ensemble des valeurs, ${\sigma}^2$ la variance de l'ensemble des valeurs, et $z$ la variable $x$ centrée réduite.

    - par une analyse factorielle :

        - A.C.P. ;

        - A.F.C. ou A.C.M. ;

        - classifications ;

        - A.F.D.

        - *etc*.

- La **liaison entre deux ou plusieurs caractères** traduit une dépendance d'un caractère par rapport à un ou plusieurs autres. Il existe trois cas :

    1. la liaison entre caractères quantitatifs. Elle s'opère avec un **coefficient de corrélation $\rho$**, dont la valeur se situe entre -1 et 1 ;

    2. la liaison entre caractères qualitatifs. Elle s'opère avec une mesure de la **correspondance** (distance du ${\chi}^2$, test d'indépendance, *etc*.) ;

    3. la liaison entre un caractère qualitatif et un caractère quantitatif. Elle s'opère avec un **rapport de corrélation** ${\eta}^2$ dont la valeur se situe entre 0 et 1. 0 traduit une absence de corrélation, et 1, une dépendance fonctionnelle.

### Différence entre distance et dissimilarité

Dans son sens mathématique, une **distance** vérife trois conditions :

1. $d \left( a, b \right) = 0 \Leftrightarrow a = b$, ce qui signifie que la distance entre les points $a$ et $b$ est nulle si et seulement si $a$ et $b$ sont confondus ;

2. $d \left( a, b \right) = d \left( b, a \right)$, ce qui signifie que la valeur de la distance est identique si on la mesure entre $a$ et $b$, ou entre $b$ et $a$. C'est une relation symétrique ;

3. $d \left( a, b \right) \leq d \left( a, c \right) + d \left( b, c \right)$, ce qui signifie qu'une distance doit vérifier la propriété de l'inégalité triangulaire. Si on place un point $c$ à l'extérieur du segment formé entre $a$ et $b$, alors la distance $d \left( a, b \right)$ est plus petite que la somme des distance entre $a$ et $c$ et entre $b$ et $c$. C'est la règle basique pour justifier l'existence des triangles.

Si les conditions 1 et 2 sont vérifiées, mais pas la condition 3, alors $d$ est une **dissimilarité**.

Ces notions sont loin d'être simples. Elles feront l'objet de précision, si nécessaire, tout au long du cours.

### Les méthodes statistiques

Le choix de la méthode statistique dépend de la nature des variables.

1. Pour une régression, on utilise entre deux et $n$ variables quantitatives.

2. Pour une A.C.P., on utilise $n$ variables quantitatives.

3. Pour une A.F.C. ou une A.C.M., on utilise entre deux et $n$ variables qualitatives.

4. Pour faire une classification ou une analyse discriminante, on utilise $n$ variables quantitatives ou qualitatives.

5. *etc*.

### Les données en géographie

En géographie, tous les cas statistiques sont possibles.

1. La statistique univariée étudie un seul caractère (niveau débutant).

2. La statistique bivariée étudie deux caractères (niveau intermédiaire).

3. La statistique multivariée étudie plus de deux caractères (niveau confirmé - GEOINT).

### La géographie à l'ère des humanités numériques

### La géographie et les mathématiques, entre rapprochement et éloignement

## Prise en main des outils

### `GitHub`

### `Docker`

### Établissement d'une architecture propre

### `Python` avec `Docker`

### Découverte du `Python`

## Bibliographie

- Abiteboul, Serge & Florence Hachez-Leroy, 2015, [« Humanités numériques »](https://1024.socinfo.fr/2015/07/1024_6_2015_41.pdf), *Bulletin de la société informatique de France*, n°6, p. 41-57

- Berry, David, 2011, ["The Computational Turn: Thinking About the Digital Humanities"](https://culturemachine.net/wp-content/uploads/2019/01/10-Computational-Turn-440-893-1-PB.pdf), *Culture Machine*, vol. 12, 22 p.

- Dacos, Marin, [« Manifeste des* Digital Humanities *»](https://tcp.hypotheses.org/318), Paris, THATCamp

- Dacos, Marin & Mounier, Pierre, 2012, [*Humanités numériques. État des lieux et positionnement de la recherche française dans le contexte international*](https://www.enssib.fr/bibliotheque-numerique/documents/65357-humanites-numeriques-etat-des-lieux-et-positionnement-de-la-recherche-francaise-dans-le-contexte-international.pdf), Paris, Institut français, 90 p.

- Debray, Régis, 1991, *Cours de médiologie générale*, Paris, Gallimard, 396 p. [Bibliothèque des idées]

- Debray, Régis, 2000, *Introduction à la médiologie*, Paris, P.U.F., VIII-222 p.

- Flichy, Patrick, 2001, *L'imaginaire d'Internet*, Paris, La Découverte, 276 p.

- Gold, Matthew (s.d.), 2012, [*Debates in the Digital Humanities*](https://www.jstor.org/stable/10.5749/j.ctttv8hq), Minneapolis, University of Minnesota Press, 532 p.

- Guillaud, Hubert, 2010, [« Qu'apportent les *Digital Humanities* ? »](https://www.researchgate.net/publication/346935835_Qu%27apportent_les_digital_humanities), *La Feuille*, 

- McCarty, Willard, 2002, ["Humanities Computing: Essential Problems, Experimental Practice"](https://www.researchgate.net/publication/250900076_Humanities_Computing_Essential_Problems_Experimental_Practice), *Literacy and Linguistic Computing*, vol. 17, n°1, p. 103-125

- McCarty, Willard, 2005, *Humanities Computing*, London, Palgrave Macmillan, 326 p.

- Paquienséguy, Françoise & Pélissier, Nicolas (s.d.), 2021, (*Questionner les humanités numériques*)[https://www.sfsic.org/wp-inside/uploads/2021/06/questionner-humanites-numeriques.pdf], Neuilly-sur-Seine, Société française des sciences de l'information et de la communication, 298 p.

- Stiegler, Bernard, 2014, Digital Studies *: organologie des savoirs et technologies  de la connaissance*, Limoges, FYP, 190 p.

- Svensson, Patrik, 2012, ["Envisioning the Digital Humanities"](https://dhq.digitalhumanities.org/vol/6/1/000112/000112.html), *Digital Humanities Quarterly*, vol. 6, n°1, 32 p.

- Terras, Melissa, 2011, ["Peering Inside the Big Tent: Digital Humanites and the Crisis of Inclusion"](http://melissaterras.blogspot.com/2011/07/peering-inside-big-tent-digital.html), *Melissa Terras' Blog*

- Turner, Fred, 2012, *Aux sources de l'utopie numérique de la contre-culture à la cyberculture : Steward Brand, un homme d'influence*, Caean, C. & F., 428 p.

- Van Hooland, Seth, Gillet, Florence, Hengchen, Simon & De Wilde, Max, 2016, *Introduction aux humanités numériques : méthodes et pratiques. Sciences humaines et sociales*, Louvain-la-Neuve, De Boeck supérieur, 208 p. [Méthodes en sciences humaines]

## Notes de bas de page

[^1]: Benzécri, Jean-Paul, 1976, « Histoire et préhistoire de l'analyse des données. Partie I. La préhistoire », *Les cahiers de l'analyse des données*, vol. 1, n°1, p. 9-32

[^2]: Bouroche, Jean-Marie & Saporta, Gilbert, 2002, *L'analyse de données*, Paris, P.U.F., 128p. [Que sais-je ?]

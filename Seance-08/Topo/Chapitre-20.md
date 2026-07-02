# L'analyse discriminante

L'**analyse discriminante** est une technique statistique ayant pour objectif de décrire, expliquer et prédire l'appartenance à des groupes prédéfinis (classes, modalités de la variable à prédire, *etc*.) d'un ensemble d'observations (individus, exemples, *etc*.) à partir d'une série des variables prédictives (descripteurs, variables exogènes, *etc*.). La construction d'outils discriminants répond à des **objectifs opérationnels**.

Le champ d'application de l'analyse discriminante est large :

- la médecine ;

- le marketing ;

- l'analyse financière des entreprises ;

- l'agronomie ;

- la reconnaissance de formes ;

- la reconnaissance de la parole ;

- l'archéologie ;

- la météorologie ;

- *etc*.

La discrimination est un terme neutre utilisé pour distinguer des groupes (des ensembles) ayant des caractéristiques propres suffisamment fortes pour constituer des groupes.

La perception humaine est souvent plus efficace que les techniques mathématiques pour définir des groupes. Qu'en est-il si le nombre de variables se multiplie ? Le développement informatique permet à l'analyse discriminante de traiter les cas complexes.

L'analyse discriminante débute par la **description des oppositions entre les groupes *a priori*** à partir de variables caractérisant les individus, appelées **descripteurs**.

À partir des variables, on peut construire un **indicateur synthétique** dont les valeurs permettent d'opposer les groupes. Cela permet d'établir une **règle d'affectation** à un des groupes pour tout nouvel individu à examiner et dont l'appartenance à un des groupes est inconnue.

L'analyse discriminante vise à construire un **outil d'aide à la décision** qui permet d'assigner à une des catégories toute observation nouvelle caractérisée par ses descripteurs, mais dont on ignore le groupe d'appartenance.

L'analyse discriminante utilise la **méthode expérimentale** dans la mesure où elle confronte constamment la réalité et les résultats du modèle mis en place. Elle fournit la possibilité d'évaluer la performance de la règle d'assignation de l'objet, par le calcul de **taux de bons classements**. La règle d'assignation à un groupe, fournie par l'outil discriminant, s'accompagne généralement d'un certain pourcentage d'erreurs. Cela permet d'estimer une probabilité *a posteriori* d'appartenir à un groupe une fois sa caractérisation connue par l'outil discriminant. De fait, la discrimination est une **classification supervisée**.

Soit une population d'individus $E$. Chaque individu peut être placé dans différentes situations appelées **état de la nature**. Ces états sont **exclusifs** les uns des autres. Ils permettent de définir une **partition** de la population en nombre fini $k$ de groupes : $E_1, \ldots{}, E_k$. L'ensemble des états de la nature est noté : $\Theta = \left\lbrace {\theta}_1, {\theta}_2, \ldots{}, {\theta}_k \right\rbrace$. Il existe $k$ états de la nature correspondant aux $k$ groupes définis. Chaque individu est caractérisé par des variables appelés descripteurs. Elles peuvent être de différentes natures : qualitatives, quantitatives ou mixtes.

Les analyses discriminantes possibles sont très nombreuses :

- l'analyse discriminante de E. M. Fisher[^1] ;

- la discrimination logistique (avec une régression logistique) ;

- l'analyse discrimante décisionnelle (ou l'analyse discrimante prédictive), qui effectue une prévision avec une technique de *scoring*. Il s'agit de construire une **fonction de classement** (ou des règles d'affectation) qui permet de prédire le groupe d'appartenance d'un individu à partir des valeurs prises par les variables prédictives. Elle entre dans un **cadre probabiliste**, comme la **technique de la régression logistique**[^2], fondée sur un modèle de régression binomiale et inventée par Joseph Berkson[^3] en 1944 et en 1951. Elle constitue un cas particulier de modèle linéaire généralisé. Elle se base sur un choix binaire (0 et 1).

$\ln \left( \frac{\Pr \left( X \left| 1 \right. \right)}{\Pr \left( X \left| 0 \right. \right)} \right) = a_0 + a_1 x_1 + \ldots{} + a_j x_j$

ou

$\ln \left( \frac{\Pr \left( 1 \left| X \right. \right) }{1 - \Pr \left( 1 \left| X \right. \right)} \right) = b_0 + b_1 x_1 + \ldots{} + b_j x_j$

$\Pr \left( 1 \left| X \right. \right) = \frac{e^{b_0 + b_1 x_1 + \ldots{} + b_j x_j}}{1 + e^{b_0 + b_1 x_1 + \ldots{} + b_j x_j}}$

- l'analyse discriminante descriptive (ou analyse factorielle discriminante) ;

- la méthode DISQUAL inventé par Gilbert Saporta[^4] [^5] ;

- les réseaux de neurones ;

- la méthode d'Emmanuel Parzen[^6] [^7] ;

- la méthode des $k$ plus proches voisins ;

- les arbres de discrimination.

L'analyse discriminante est utilisée pour :

- de la statistique exploratoire[^8] ;

- de l'analyse de données[^9] ;

- de la reconnaissance de formes[^10] ;

    - **Exemple.** La reconnaissance optique des caractères[^11] (R.O.C.) ou l'océrisation

- de l'apprentissage automatique[^12] ;

- de la fouille de données[^13] ;

- *etc*.

Les traitements de variables se distinguent :

- pour les valeurs manquantes (ou censurées) ;

- pour les valeurs aberrantes ;

- pour les valeurs extrêmes.

## Liens

- [Topo en format P.D.F.](./PDF/Seance-09-Chapitre-20.pdf)

## Notes de bas de page

[^1]: Fisher, E. M., 1936, "Linear Discriminant Analysis", *Statistics & Discrete Methods of Data Sciences*, 392., p. 1-5

[^2]: ou modèle logit

[^3]: Joseph Berkson (1899-1982)

[^4]: Gilbert Saporta (né en 1946)

[^5]: Saporta, Gilbert, 1975, *Liaisons entre plusieurs ensembles de variables et codage de données qualitatives*, Paris, Université Pierre et Marie Curie - Paris VI, IV-110 p.

[^6]: Emmanuel Parzen (1929-2016)

[^7]: Parzen, Emmanuel, 1962, "On Estimation of a Probability Density Function and Mode", *Annals of Mathematical Statistics*, vol. 33, n°3, p. 1066-1075

[^8]: En anglais : *Exploratory Data Analysis*

[^9]: En anglais : *Data Analysis*

[^10]: En anglais : *Pattern Recognition*

[^11]: En anglais : *Optical Character Recognition* (O.C.R.)

[^12]: En anglais : *Machine Learning*

[^13]: En anglais : *Data Mining*

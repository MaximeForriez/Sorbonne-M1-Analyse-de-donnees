# Séance 9. Statistiques multivariées (1). Les méthodes descriptives

Exposer la richesse des statistiques multivariées en une séance est une gageure. L'usage de `Python` va simplifier la tâche, mais ce n'est qu'une vision globale qu'il vous faudra approfondir par et pour le traitement de vos données dans vos mémoires. L'objectif est de vous donner l'ensemble des possibilités qui s'offre à vous, et surtout contrôler un minimum les calculs que vous lancez, afin d'éviter d'analyser n'importe quoi.

J'ai peu insisté sur le caractère progressif à l'intérieur de chaque séance, mais ici, il faut bien suivre l'ordre des analyses. **Le niveau de complexité et de puissance d'analyse est progressif**. Suivez bien l'ordre établi par la leçon.

## Tutoriels

>[!WARNING]
> L'objectif de ces tutoriels n'est pas de les visualiser en totalité, mais de fournir une base de cours alternatif si :
> - mes explications vous paraissent peu claires ;
> - vous voulez compléter et approfondir ce que vous avez compris ;
> - vous voulez révisez ;
> - *etc*.
> Bref, vous devez en faire un usage personnalisé, donc ciblé, afin d'éviter de regarder toutes les vidéos. Ce n'est qu'une aide complémentaire.
> En analyse multivariée, les informations que vous trouverez seront soit très vulgarisées (ce qui est idéal si vous ne voulez qu'interpréter les résultats), soit très, voire trop, mathématisées, donc inaccessibles.

- [Pour commencer et avoir une vision d'ensemble](https://www.youtube.com/watch?v=RmFUTYFsFbE) (chaîne `YouTube`)

- [Le Coin Stat](https://www.youtube.com/@LeCoinStat/playlists) (chaîne `YouTube`)

- [MathAgrocampus](https://www.youtube.com/@mathAgrocampus/playlists) (chaîne `YouTube`)

- [Rémi Bachelet](https://www.youtube.com/@BacheletRemi/playlists) (chaîne `YouTube`)

- [François Husson](https://www.youtube.com/@HussonFrancois/playlists) (chaîne `YouTube`)

- [François Husson](https://husson.github.io/index.html) (Cours et ressources)

## Bagage mathématique nécessaire

- Avoir mathématiquement compris l'ensemble des analyses univariées et bivariées

- Connaître l'algèbre linéraire : matrices, systèmes linéaires, espaces vectoriels

    - [Comprendre les matrices](https://www.youtube.com/watch?v=Dr9J1BIcVBw)

## Documentation mathématique

- [Cours de Jean-Marc Lasgouttes](https://who.rocq.inria.fr/Jean-Marc.Lasgouttes/ana-donnees/) : l'approche est extrêmement synthétique et mathématique, mais c'est la plus accessible pour faire des mathématiques appliquées.

    - Jean-Marc Lasgouttes, 2023-2024, [Cours d'analyse de données : A.C.P. - Synthèse du calcul matriciel](https://who.rocq.inria.fr/Jean-Marc.Lasgouttes/ana-donnees/cours-acp.pdf)

    - Jean-Marc Lasgouttes, 2023-2024, [Cours d'analyse de données : A.F.C. et A.C.M. - Synthèse du calcul matriciel](https://who.rocq.inria.fr/Jean-Marc.Lasgouttes/ana-donnees/cours-afc-acm.pdf)

## Tests statistiques

- [Table du Khi<sup>2</sup>](https://who.rocq.inria.fr/Jean-Marc.Lasgouttes/ana-donnees/chi-deux.pdf)

- [Table de la loi normale centrée et réduite](https://www.math.u-bordeaux.fr/~mchabano/Tab0.pdf)

## Calculer des matrices

[Calculer des matrices](https://matrixcalc.org/fr/)

## L'analyse factorielle en composantes principales (A.C.P.)

- Escofier, Brigitte & Pagès, Jérôme, 2016, [*Analyses factorielles simples et multiples. Cours et études de cas*](https://cdn-cms.f-static.com/uploads/1460418/normal_5b9ba5dc15394.pdf), Paris, Dunod, VIII-392 p. [Sciences sup]

- Lebart, Ludovic, Piron, Marie & Morineau, Alain, 2006, [*Statistique exploratoire multidimensionnelle. Visualisations et inférences en fouille de données*](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/2022-03/010029478.pdf), Paris, Dunod, XVI-464 p. [Science sup] [3<sup>e</sup> édition] [Référence complète et simple d'accès pour les statistiques multivariées]

- [Explication détaillée de l'ensemble des calculs](https://www.youtube.com/watch?v=QZMQMYQ_g_8)

- [Explication du calcul d'une A.C.P. avec `Python`](https://www.youtube.com/watch?v=RHMyN1z4eHM)

- [Explication du calcul d'une A.C.P. avec `NumPy`](https://www.youtube.com/watch?v=DIaFh15mSbE)

- Philippeau, Gérard, (1992). *Comment interpréter les résultats d'une analyse en composantes principales*, Paris, Institut technique des céréales et des fourrages (I.T.C.F.), 64 p. [STAT-ICTF]

## L'analyse factorielle des correspondances (A.F.C.)

- Escofier, Brigitte & Pagès, Jérôme, 2016, [*Analyses factorielles simples et multiples. Cours et études de cas*](https://cdn-cms.f-static.com/uploads/1460418/normal_5b9ba5dc15394.pdf), Paris, Dunod, VIII-392 p. [Sciences sup]

- Lebart, Ludovic, Piron, Marie & Morineau, Alain, 2006, [*Statistique exploratoire multidimensionnelle. Visualisations et inférences en fouille de données*](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/2022-03/010029478.pdf), Paris, Dunod, XVI-464 p. [Science sup] [3<sup>e</sup> édition] [Référence complète et simple d'accès pour les statistiques multivariées]

- [Explication détaillée de l'ensemble des calculs](https://www.youtube.com/watch?v=NPYihsWv8bA&list=PLzjg2z2kYUrg6XvYVYMxdZQnouBEwavfQ&index=1) (17 vidéos)

- [Explication de l'A.F.C.](https://www.youtube.com/watch?v=69_2dvLroho)

- Dervin, Catherine, 1992, *Comment interpréter les résultats d'une analyse factorielle des correspondances ?*, Paris, Institut technique des céréales et des fourrages (I.T.C.F.), 72 p. [STAT-ICTF]

- Moreau, Jean, Doudin, Pierre-André & Cazes, Pierre, 2000, *L'analyse des correspondances et les techniques connexes. Approches nouvelles pour l'analyse statistique des données*, Berlin, Springer, XVI-266 p. [Mathématiques & Applications 32]

## L'analyse factorielle des correspondances multiples (A.C.M.)

- Escofier, Brigitte & Pagès, Jérôme, 2016, [*Analyses factorielles simples et multiples. Cours et études de cas*](https://cdn-cms.f-static.com/uploads/1460418/normal_5b9ba5dc15394.pdf), Paris, Dunod, VIII-392 p. [Sciences sup]

- Lebart, Ludovic, Piron, Marie & Morineau, Alain, 2006, [*Statistique exploratoire multidimensionnelle. Visualisations et inférences en fouille de données*](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/2022-03/010029478.pdf), Paris, Dunod, XVI-464 p. [Science sup] [3<sup>e</sup> édition] [Référence complète et simple d'accès pour les statistiques multivariées]

## Les classifications non supervisées

- Lebart, Ludovic, Piron, Marie & Morineau, Alain, 2006, [*Statistique exploratoire multidimensionnelle. Visualisations et inférences en fouille de données*](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/2022-03/010029478.pdf), Paris, Dunod, XVI-464 p. [Science sup] [3<sup>e</sup> édition] [Référence complète et simple d'accès pour les statistiques multivariées]

- Nakache, Jean-Pierre & Confais, Josiane, 2000, *Méthodes de classification avec illustrations SPAD® et SAS®*, Montreuil, Centre international de statististique et d'informatique appliquées (C.I.S.I.A.), X-186 p.

## L'analyse factorielle discriminante (A.F.D.)

- Bardos, Mireille, 2001, *Analyse discriminante. Application au risque et scoring financier*, Paris, Dunod, VIII-224 p. [Manuel]

- Celeux, Gilles & Nakache, Jean-Pierre, 1994, *Analyse discriminante sur variables qualitatives*, Paris, Polytechnica, X-270 p.

- Lebart, Ludovic, Piron, Marie & Morineau, Alain, 2006, [*Statistique exploratoire multidimensionnelle. Visualisations et inférences en fouille de données*](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/2022-03/010029478.pdf), Paris, Dunod, XVI-464 p. [Science sup] [3<sup>e</sup> édition] [Référence complète et simple d'accès pour les statistiques multivariées]

## L'analyse factorielle multiple (A.F.M.)

Si vous avez survécu à l'A.C.P., à l'A.C.M., aux classifications non supervisées et à l'A.F.D., il se peut que l'A.F.M. soit la goutte d'eau qui fait déborder le vase. Cette technique est en réalité la plus proche des modèles que l'on peut déployer en sciences humaines et sociales, donc en géographie, mais c'est la plus difficile à comprendre. Pour l'instant, la vulgarisation est inexistante. Il faut vous contenter de la description de l'A.F.M. proposée par ses inventeurs, Brigitte Escofier et Jérôme Pagès, mais surtout d'articles scientifiques bruts lorsque l'on souhaite affiner la technique en fonction des données.

Maîtriser toutes les subtilités de l'A.F.M. n'est pas votre priorité, mais il faut tout de même essayer de comprendre l'intérêt des méthodes pour pouvoir reconnaître les occasions de les appliquer. Comme avec les autres techniques, il suffit juste de télécharger le module et d'appliquer les méthodes afin de réaliser votre A.F.M.

- Escofier, Brigitte & Pagès, Jérôme, 2016, [*Analyses factorielles simples et multiples. Cours et études de cas*](https://cdn-cms.f-static.com/uploads/1460418/normal_5b9ba5dc15394.pdf), Paris, Dunod, VIII-392 p. [Sciences sup]

### L'analyse factorielle multiple suivant le modèle INDSCAL

- Husson, François & Pagès, Jérôme, 2006 [« Aspects méthodologiques du modèle INDSCAL »](https://www.numdam.org/item/RSA_2006__54_2_83_0.pdf), *Revue de Statistique Appliquée*, vol. 54, n°2, p. 83-100

### L'analyse factorielle multiple suivant l'approche P.L.S.

- Pagès, Jérôme & Tenenhaus, Michel, 2002, [« Analyse factorielle multiple et approche PLS »](https://www.numdam.org/item/RSA_2002__50_1_5_0.pdf), *Revue de Statistique Appliquée*, vol. 50, n°1, p. 5-33

### L'analyse factorielle multiple hiérarchique

- Le Dien, Sébastien & Pagès, Jérôme, 2003, [« Analyse factorielle multiple hiérarchique »](https://www.numdam.org/item/RSA_2003__51_2_47_0.pdf), *Revue de Statistique Appliquée*, vol. 51, n°2, p. 47-73

### L'analyse factorielle multiple procustéenne

- Morand, Elisabeth & Pagès, Jérôme, 2007, [« Analyse factorielle multiple procustéenne »](https://www.numdam.org/item/JSFS_2007__148_2_65_0.pdf), *Journal de la Société française de statistique & Revue de statistique appliquée*, vol. 148, n°2, p. 65-97

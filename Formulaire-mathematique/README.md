# Cours express de mathématiques

- [Lettres spéciales](./Lettres-speciales-utilisees.md)

- [Statisticiens - Mathématiciens](./Statisticiens.md)

- [Formulaires de statistique](./Girschig-M-1969-Analyse%20statistique.pdf)

- [Outils statistiques en géographie](./Dumolard-Allignol-Paul-Quesseveur--L%20outil%20informatique%20en%20geographie.pdf)

## Séance 1. Ensembles finis, dénombrement, probabilités et statistique

Il faut prendre conscience que toutes les données que vous aurez à traiter, sont des ensembles finis. Il faut bien comprendre cette notion afin de pouvoir dénombrer efficacement les éléments de vos données, d'où l'impératif de savoir bien compter vos éléments. Une fois que vous maîtriser les ensembles finis et le dénombrement, vous pourrez vous attaquer à la notion clé de probabilités. Les probabilités en statistique servent souvent de **modèles théoriques**. Tout l'art des statistiques est de comparer une distribution observée de fréquences avec une distribution théorique de probabilités. Ainsi, cette leçon s'achève par les notions de clés de statistiques, et surtout leur comparaison avec les notions vues en probaibilités.

### Ensembles finis

#### Cours

- [Ensembles et applications](https://www.youtube.com/watch?v=bPT6-g3B5wQ&list=PL6690366268FBF2C0)

#### Liens

- [Topo en format P.D.F.](./PDF/01-Ensembles-finis.pdf)

#### Exercices

- [Exercices sur les ensembles finis](./PDF/01-Ensembles-finis-Exercices.pdf)

- [Corrections des exercices sur les ensembles finis](./PDF/01-Ensembles-finis-Corrections.pdf)

### Dénombrement

L'art du dénombrement est essentiel dans l'analyse de données. Si, la plupart du temps, les logiciels ou les codes permettent d'éviter de se poser la question, il est tout de même utile de savoir compter correctement l'ensemble des possibilités d'une situation.

Apprendre à compter est de fait la **base** des probabilités et des statistiques. Toutes ces formules vont être utilisées par la suite dans des situations d'analyse de données précises. Elles doivent être maîtrisées.

Même si ces formules peuvent paraître abscons, en réalité, il n'existe que deux cas possibles :
1. soit on sélectionne **tous** les élements ;
2. soit on sélectionne **quelques** éléments par d'autres, constituant la totalité des cas possibles.

Concrètement, à chaque situation pratique, vous devez poser la question de la situation statistique dans laquelle vous vous trouvez. De fait, si vous ne maîtrisez pas le dénombrement, faites des exercices. En général, ils sont à base de boules dans une urne ou de tirage de cartes. Les situations statistiques en géographie sont différentes. Par exemple, on étudiera les réponses d'un questionnaire :
- une question avec un ensemble de réponses pour laquelle le sondé ne doit faire qu'un choix. Dans quelle situation mathématique est-on ? Dans le cas d'une sélection dans le cadre d'un tirage successif sans remise. Assez naturellement, on répond qu'il y a 5 choix possibles ;
- une question avec un ensemble de réponses pour laquelle le sondé dispose de cinq réponses et peut en choisir autant qu'il veut parmi elles. Dans quelle situation mathématique est-on ? Dans le cas d'une sélection dans le cadre d'un tirage successif sans remise. La réponse est moins simple, mais ici il y a 120 choix possibles ;
- *etc*.

La bonne méthode est d'éliminer les cas.
- Est-ce un dénombrement nécessitant une sélection d'éléments ?
    - Si non, il s'agit d'une **permutation**. On utilise toutes les possibilités. Les éléments sont-ils utilisés sans ou avec répétition (ou remise) ?
        - Sans répétition, il s'agit d'une **permutation simple**. Si on a 5 éléments, tous les 5 éléments doivent présents dans la combinaison.
        - Avec répétition, il s'agit d'une **permutation avec répétitions**. Si on a 5 éléments, quelques éléments parmi les 5 peuvent présents dans la combinaison. Le jeu type est le mastermind. Vous avez le choix entre 5 éléments par exemple, mais vous pouvez choisir de créer une combinaison avec seulement 4 éléments pris parmi 5. Dans ce cas, un élément sera répété pour obtenir une combinaison avec 5 éléments.
    - Si oui, la sélection des élements est-elle successive ou simultanée ? On utilise quelques possibilités parmi un ensemble de possibilités bien défini.
        - Si elle est **successive**, c'est un **arrangement**. L'arrangement présuppose un ordre. Les élements sélectionnés sont-ils écartés du tirage suivant ou sont-ils remis dans la liste des choix possibles ?
            - Sans remise, il s'agit d'un **arrangement simple**.
            - Avec remise, il s'agit d'un **arrangement avec répétitions**.
        - Si elle est **simultanée**, c'est une **combinaison**. La combinaison présuppose l'absence d'ordre. Les élements sélectionnés sont-ils écartés du tirage suivant ou sont-ils remis dans la liste des choix possibles ?
            - Sans remise, il s'agit d'une **combinaison simple**.
            - Avec remise, il s'agit d'une **combinaison avec répétitions**.

Il faut se poser les questions sans *a priori* sur la situation géographique qu'on analyse. Suis-je **mathématiquement** dans ce cas plutôt que dans tel autre ? Il n'existe que **six possibilités**. Il faut s'entraîner pour bien les reconnaître au sein des cas pratiques. L'erreur que l'on commet le plus souvent au début consiste à identifier les cas avec ou sans remise, or c'est la dernière question à se poser. C'est comme si on raisonnait spontanément à l'envers. Raisonner en termes de dénombrement est le plus dur à acquérir et à maîtriser. Une fois que cela est fait, tout deviendra plus simple au niveau des probabilités et des statistiques, car, dans les deux cas, tout part du dénombrement.

#### Les formules préalables à connaître

- Savoir calculer une factorielle

- Savoir calculer le binôme de Newton

La base des probabilités, et, par extension, des statistiques, est de savoir compter. Si vous avez des difficultés, travaillez ce cours jusqu'à sa maîtrise totale.

#### Cours

- [Topo en format P.D.F.](./PDF/02-Denombrement.pdf)

#### Exercices

- [Exercices sur le dénombrement](./PDF/02-Denombrement-Exercices.pdf)

- [Corrections des exercices sur le dénombrement](./PDF/01-Ensembles-finis-Corrections.pdf)

#### Tutoriels

- [Le dénombrement - Vision d'ensemble](https://www.youtube.com/watch?v=fO3T4njqyAs)

- [Les arrangements](https://www.youtube.com/watch?v=4UFSi4bD4xw)

- [Les combinaisons 1](https://www.youtube.com/watch?v=56QOmkALKjg)

- [Les combinaisons 2](https://www.youtube.com/watch?v=YPSJnwkiZ04)

#### Ressources

- [Ensembles et dénombrement](https://math.univ-lyon1.fr/~perrut/mass/cours1-4.pdf)

- [Le dénombrement](https://www.maths-et-tiques.fr/telech/20Combi.pdf)

- [Le dénombrement](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/PROBA1.PDF) (Cours de Didier Müller)

    - [Corrections des exercices](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/CORRIGE.PDF)

    - [Quiz sur le dénombrement](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/quiz1.php)

### Probabilités

Vous savez [dénombrer](./PDF/02-Denombrement.pdf). Désormais, il est possible d'envisager de comprendre les probabilités. En statistiques, les probabilités sont souvent ramener à des fréquences, qui correspondent à des « probabilités pratiques ». De fait, les statistiques ne peuvent être comprises qu'à deux conditions :

1. savoir dénombrer ;

2. savoir établir des probabilités.

Dans le cadre des statistiques, il est difficile de ne pas évoquer la notion de probabilité. Toutefois, il est fondamental, pour bien comprendre ce chapitre, qu'il ne s'agit que de récapituler les notions utiles dans le cadre des statistiques des variables quantitatives. Dit autrement, ce chapitre n'est qu'une vaste introduction à la notion mathématique de probabilité.

Mathématiquement, les probabilités peuvent être très complexes. En cas pratique, il faut savoir reconnaître des situations plutôt simples, mais parfois contre-intuitives. Il n'y a pas de secret, il faut pratiquer pour comprendre.

À partir des lois de probabilités, il devient possible d'établir les **distributions statistiques**.

## Ressources

- [Probabilité](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/PROBA2.PDF) (Cours de Didier Müller)

    - [Corrections des exercices](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/CORRIGE.PDF)

    - [Quiz sur les probabilités](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/quiz2.php)

    - [Approfondissement et programmes en `Python`](https://www.apprendre-en-ligne.net/hearthstone/index.html)

## Cours

- [Topo en format P.D.F.](./PDF/03-Probabilites.pdf)

## Exercices

- [Exercices sur les probabilités](./PDF/02-Probabilites-Exercices.pdf)

- [Corrections des exercices sur les probabilités](./PDF/02-Probabilites-Corrections.pdf)

### Statistique

Certains paramètres de position correspondent clairement à des probabilités. La **médiane** est la valeur dont la probabilité d'être dépassée est $\frac{1}{2}$. Les **quartiles** sont les valeurs dont la probabilité d'être dépassées sont $\frac{1}{4}$, $\frac{1}{2}$ et $\frac{3}{4}$.

La statistique est une application des probabilités. Elle effectue des tests statistiques pour vérifier si les données sont **indépendantes**, **équiprobables**, *etc*. La notion d'indépendance est particulièrement importante si l'on souhaite lier plusieurs variables entre elles. Si les variables sont dépendantes, un test utilisera les probabilités conditionnelles, et le principe des probabilités totales. Elle propose également des **tests de distribution** afin de vérifier la pertinence des paramètres statistiques. Bref, la statistique utilise le vocabulaire probabiliste. Elle établit l'opérationnabilité d'un modèle probabiliste par rapport au jeu de données. Encore une fois, ce chapitre ne fait que présenter les notions clés qui seront présentes dans les autres chapitres. Il faut par conséquent bien avoir assimilé ces notions abstraites afin de poursuivre sereinement la lecture de ce texte.

## Cours

- [Topo en format P.D.F.](./PDF/04-Introduction-aux-statistiques.pdf)

## Ressources

- [Variables aléatoires](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/PROBA3.PDF) (Cours de Didier Müller)

    - [Corrections des exercices](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/CORRIGE.PDF)

    - [Quiz sur les variables aléatoires](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/quiz3.php)

## Séance 2. Algèbre et géométrie élémentaire (ou pas)

### Les applications dans le plan

#### Cours

- [Topo en format P.D.F.](./PDF/05-Les-applications-dans-le%20plan.pdf)

#### Exercices

En construction

### Les règles de calcul élémentaire (ou l'algèbre des nombres réels)

#### Cours

- [Topo en format P.D.F.](./PDF/06-Les-regles-de-calcul-elementaire-ou-l-algebre-des-nombres-reels.pdf)

#### Exercices

En construction

### La géométrie descriptive

#### Cours

- [Topo en format P.D.F.](./PDF/07-La-geometrie-descriptive.pdf)

#### Exercices

En construction

### Trigonométrie

#### Cours

- [Topo en format P.D.F.](./PDF/08-Trigonometrie.pdf)

#### Exercices

En construction

### Les vecteurs

#### Cours

- [Topo en format P.D.F.](./PDF/09-Les-vecteurs.pdf)

#### Exercices

En construction

### Équations cartésiennes

#### Cours

- [Topo en format P.D.F.](./PDF/10-Equations-cartesiennes.pdf)

#### Exercices

En construction

### Calcul vectoriel dans le plan

#### Cours

- [Topo en format P.D.F.](./PDF/11-Calcul-vectoriel-dans-le-plan.pdf)

#### Exercices

En construction

### Calcul vectoriel dans l'espace

#### Cours

- [Topo en format P.D.F.](./PDF/12-Calcul-vectoriel-dans-un-espace-a-trois-dimensions.pdf)

#### Exercices

En construction

### Courbes paramétrées

#### Cours

- [Topo en format P.D.F.](./PDF/13-Courbes-parametrees.pdf)

#### Exercices

En construction

### Barycentre dans le plan et dans l'espace à trois dimensions

#### Cours

- [Topo en format P.D.F.](./PDF/14-Barycentre-dans-le-plan-et-dans-l-espace-a-trois-dimensions.pdf)

#### Exercices

En construction

## Séance 3. Les fonctions mathématiques

### Les fonctions en mathématiques

#### Cours

- [Topo en format P.D.F.](./PDF/15-Les-fonctions-mathematiques.pdf)

#### Exercices

En construction

### Les fonctions numériques d'une variable réelle

#### Cours

- [Topo en format P.D.F.](./PDF/16-Les-fonctions-numeriques-d-une-variable-reelle.pdf)

#### Exercices

En construction

### Les fonctions numériques de deux variables réelles

#### Cours

- [Topo en format P.D.F.](./PDF/17-Les-fonctions-numeriques-de-deux-variables-reelles.pdf)

#### Exercices

En construction

### Les fonctions numériques de plusieurs variables réelles

#### Cours

- [Topo en format P.D.F.](./PDF/18-Les-fonctions-numeriques-de-plusieurs-variables-reelles.pdf)

#### Exercices

En construction

### Les approximations de fonctions

#### Cours

- [Topo en format P.D.F.](./PDF/19-Les-approximations-de-fonctions.pdf)

#### Exercices

En construction

### Courbe et tracé

#### Cours

- [Topo en format P.D.F.](./PDF/20-Courbe-et-trace.pdf)

#### Exercices

En construction

## Séance 4. Notation indicielle, suites numériques et séries numériques

### Notation indicielle

#### Cours

- [Topo en format P.D.F.](./PDF/21-Notation-indicielle.pdf)

#### Exercices

En construction

### Les suites numériques

#### Cours

- [Topo en format P.D.F.](./PDF/22-Les-suites-numeriques.pdf)

#### Exercices

En construction

### Les séries numériques

#### Cours

- [Topo en format P.D.F.](./PDF/23-Les-series-numeriques.pdf)

#### Exercices

En construction

## Séance 5. Les nombres complexes

### Les nombres complexes

#### Cours

- [Topo en format P.D.F.](./PDF/24-Les-nombres-complexes.pdf)

#### Exercices

En construction

## Séance 6. Les équations différentielles

### Les équations différentielles

#### Cours

- [Topo en format P.D.F.](./PDF/25-Les-equations-differentielles.pdf)

#### Exercices

En construction

## Séance 7. Vecteurs, matrices et algèbre linéaire

### Les vecteurs dans le plan (ou espace à deux dimensions)

#### Cours

- [Topo en format P.D.F.](./PDF/11-Calcul-vectoriel-dans-le-plan.pdf)

#### Exercices

En construction

### Les vecteurs dans l'espace à trois dimensions

#### Cours

- [Topo en format P.D.F.](./PDF/12-Calcul-vectoriel-dans-un-espace-a-trois-dimensions.pdf)

#### Exercices

En construction

### Les vecteurs dans un hyperplan

#### Cours

- [Topo en format P.D.F.](./PDF/26-Generalisation-de-la-notion-de-vecteurs.pdf)

#### Exercices

En construction

### Le calcul matriciel

#### Cours

- [Topo en format P.D.F.](./PDF/27-Calcul-matriciel.pdf)

#### Exercices

- [Exercices sur le calcul matriciel](./PDF/27-Matrices-Exercices.pdf)

- [Corrections des exercices sur le calcul matriciel](./PDF/27-Matrices-Corrections.pdf)

### L'algèbre linéaire

#### Cours

- [Topo en format P.D.F.](./PDF/28-Algebre-lineaire.pdf)

#### Exercices

- [Exercices sur le calcul matriciel](./PDF/28-Applications-lineaires-Exercices.pdf)

- [Corrections des exercices sur le calcul matriciel](./PDF/28-Applications-lineaires-Corrections.pdf)

## Bibliographie

La collection qui explique le mieux les notions mathématiques à mon sens est la série Schaum de l'éditeur McGraw-Hill.

- Ayres, Frank, 1962, *Algèbre moderne*, trad. Michel Lobenberg, Paris, McGraw-Hill Book Company, VI-248 p. [Série Schaum]

- Ayres, Frank, 1972, *Théorie et applications des équations différentielles*, trad. fr., Paris, McGraw-Hill, 296 p. [Série Schaum]

- Ayres, Frank, 1979, *Trigonométrie*, trad. Michel Lobenberg, Paris, McGraw-Hill, VI-208 p. [Série Schaum]

- Ayres, Frank, 1986, *Les matrices*, trad. fr., Paris, McGraw-Hill, 214 p. [Série Schaum]

- Ayres, Frank, 1989, *Théorie et applications du calcul différentiel et intégral*, trad. fr., Paris, McGraw-Hill Book Company, VIII-480 p. [Série Schaum]

- Ayres, Frank & Mendelson, Elliott, 1993, *Calcul différentiel et intégral*, trad. Abdellatif Abouhmzi, Paris, McGraw-Hill, VIII-480 p. [Série Schaum]

- Ayres, Frank & Mendelson, Elliott, 2002, *Analyse*, trad. Christos Grammatikas, Paris, Dunod, VI-130 p. [Mini Schaum's - EdiScience]

- Ayres, Frank & Moyer, Robert E., 1999, *Theory and Problems of Trigonometry*, New York, McGraw-Hill Book Company, VIII-216 p. [Schaum's Outline Series]

- Ayres, Frank & Schmidt, Philip A., 1992, *Mathématiques de base*, Paris, McGraw-Hill, VIII-456 p. [Série Schaum]

- Bronson, Richard, 1994, *Équations différentielles. Méthodes et applications*, trad. Hervé Mignot, Paris, McGraw-Hill, XII-352 p. [Série Schaum]

- Dameron, Jean-Claude, 1994, *Analyse mathématique schématisée*, t. 1, *Les bases*, Paris, Économica, XII-374 p.

- Dameron, Jean-Claude, 1995, *Analyse mathématique schématisée*, t. 2, *Les fonctions*, Paris, Économica, XII-330 p.

- Dameron, Jean-Claude, 1997, *Analyse mathématique schématisée*, t. 3, *Les développements*, Paris, Économica, XII-270 p.

- Dameron, Jean-Claude, 1997, *Analyse mathématique schématisée*, t. 4, *L’intégration*, Paris, Économica, XIV-358 p.

- Fleurant, Sandrine, Fleurant, Cyril, 2015, *Bases de mathématiques pour la géologie et la géographie*, Paris, Dunod, XII-290 p. [Cours]

- Kindle, Joseph H., 1979, *Géométrique analytique*, trad. fr., Paris, McGraw-Hill, VI-148 p. [Série Schaum]

- Lipschutz, Seymour, 1965, *Topologie*, trad. fr., Paris, McGraw-Hill, X-262 p. [Série Schaum]

- Lipschutz, Seymour, 1984, *Algèbre linéaire*, Paris, McGraw-Hill, VIII-330 p. [Série Schaum]

- Lipschutz, Seymour, 1986, *Les structures de données*, trad. Romain Jacoud, Paris, McGraw-Hill, VIII-342 p. [Série Schaum]

- Lipschutz, Seymour, 1987, *Probabilités*, trad. fr., Paris, McGraw-Hill, VI-154 p. [Série Schaum]

- Lipschutz, Seymour, 1990, *Mathématiques discrètes*, trad. Bernard Geoffrion, Paris, McGraw-Hill, X-248 p. [Série Schaum]

- Scheid, Francis, 1986, *Analyse numérique*, trad. Romain Jacoud, Paris, McGraw-Hill, IV-424 p. [Série Schaum]

- Spiegel, Murray R., 1973, *Analyse vectorielle*, trad. fr., Paris, McGraw-Hill, VI-224 p. [Série Schaum]

- Spiegel, Murray R., 1974, *Formules et tables de mathématiques*, trad. Michel Lobenberg, Paris, McGraw-Hill, 1-272 p. [Série Schaum]

- Spiegel, Murray R., 1980, *Analyse de Fourier et application aux problèmes de valeurs aux limites*, trad. Romain Jacoud, Paris, McGraw-Hill, VIII-200 p. [Série Schaum]

- Spiegel, Murray R., 1981, *Probabilités et statistique*, trad. Romain Jacoud, Paris, McGraw-Hill, X-386 p. [Série Schaum]

- Spiegel, Murray R., 1984, *Théorie et applications de la statistique*, trad. Alain Ergas & Jean-François Marcotorchino, Paris, McGraw-Hill, X-358 p. [Série Schaum] [réédition de 1972]

- Spiegel, Murray R., 1986, *Transformée de Laplace*, trad. Romain Jacoud, Paris, Série Schaum, VIII-272 p. [Série Schaum]

- Spiegel, Murray R., 1987, *Théorie et applications de l'analyse*, Paris, McGraw-Hill, VIII-382, [Série Schaum]

- Spiegel, Murray R., 1992, *Variables complexes*, trad. fr., Paris, Série Schaum, VIII-314 p. [Série Schaum]

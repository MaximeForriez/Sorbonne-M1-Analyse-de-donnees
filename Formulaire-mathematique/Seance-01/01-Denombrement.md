# Dénombrement

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

## Les formules préalables à connaître

- Savoir calculer une factorielle

- Savoir calculer le binôme de Newton

## Les principes du dénombrement

### Le principe des tiroirs

### Le principe de décomposition

## Les situations sans sélection

### Permutation simple

### Permutation avec répétitions

## Les situations avec sélection

### Les situations successives

#### Les tirages sans remise : l'arrangement simple

#### Les tirages avec remise : l'arrangement avec répétitions

### Les situations simultanées

#### Les tirages sans remise : la combinaison simple

#### Les tirages avec remise : la combinaison avec répétitions

## Tutoriels

- [Le dénombrement - Vision d'ensemble](https://www.youtube.com/watch?v=fO3T4njqyAs)

- [Les arrangements](https://www.youtube.com/watch?v=4UFSi4bD4xw)

- [Les combinaisons 1](https://www.youtube.com/watch?v=56QOmkALKjg)

- [Les combinaisons 2](https://www.youtube.com/watch?v=YPSJnwkiZ04)

## Ressources

- [Ensembles et dénombrement](https://math.univ-lyon1.fr/~perrut/mass/cours1-4.pdf)

- [Le dénombrement](https://www.maths-et-tiques.fr/telech/20Combi.pdf)

- [Le dénombrement](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/PROBA1.PDF) (Cours de Didier Müller)

    - [Corrections des exercices](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/CORRIGE.PDF)

    - [Quiz sur le dénombrement](https://www.apprendre-en-ligne.net/MADIMU2/PROBA/quiz1.php)

## Exercices

- [Exercices sur le dénombrement](./Exercices/01-Denombrement.pdf)

- [Corrections](./Solutions/01-Denombrement-Corrections.pdf)

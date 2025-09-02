# Statistiques multivariées avec `Python`

## Les analyses factorielles

Les analyses factorielles fonctionnent de toutes avec la même logique informatique. Seule l'A.C.P. sera développée. Pour les autres, il faut vous reporter à la documentation officielle de `Python`.

### Analyse en composantes principales (A.C.P.)

Pour faire des A.C.P., on a besoin de la bibliothèque `Scikit-learn`.

> [!WARNING]
> Avant de l'utiliser, il faut centrer-réduire les données, les normaliser. L'objectif est de pouvoir comparer les colonnes entre elles.

```

```

```

```

```

```

### Analyse factorielle des correspondances (A.F.C.)

```

```

### Analyse des correspondances multiples (A.C.M.)

```

```

## Les modèles de régression

### La régression linéaire

```

```

### La régression logistique

```

```

## Les classifications

L'objectif est d'étudier des groupes (ou *clusters*) comme :

- les aires géographiques avec des propriétés similaires ;

- les proximités de mots dans des textes ;

- la détermination des individus aux propriétés sociales proches

Peu importe la classification retenue, on applique toujours la même méthode :

1. sélectionner les informations ;

2. définir la méthode de regroupement (qui dépend d'une métrique) ;

3. définir les règles d'association ou de séparation des individus (deux à deux).

### Partitionnement en $k$-moyennes (ou nuées dynamiques)

On caractérise l'algorithme~:

1. en définissant un nombre $k$ de groupes à rechercher ;

2. en découpant par un algorithme de l'ensemble des données en $k$ groupes avec comme objectif de réduire la distance entre les éléments contenus au sein de chaque groupe.

On utilise la bibliothèque `Scikit-learn`.

```

```

### Classification ascendante hiérarchique (C.A.H.)

L'algorithme définit ce qu'est « être proche ».

1. Les deux éléments les plus proches sont regroupés et deviennent un nouvel élément caractérisé par la moyenne des valeurs.

2. Recommencer l'algorithme jusqu'à ce que tous les éléments soient regroupés.

On obtient ainsi un arbre inversé, le **dendrogramme**.

```

```






```

```

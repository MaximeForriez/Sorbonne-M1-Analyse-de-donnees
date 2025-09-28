# Statistique descriptive en `Python`

## Analyse univariée des données avec `Pandas`

### Dénombrer

Il est possible de compter le nombre d'occurrences de chaque élément de la colonne et de l'aficher dans une nouvelle série. Par exemple, on peut calculer les effectifs d'une variable qualitative.

```
    donnees["nom de la colonne"].value_counts(normalize=True)
```

> [!NOTE]
> `normalize=True` est une option.

### Utiliser les indicateurs de tendance centrale

La moyenne :

```
    donnees["nom de la colonne"].mean()
```

La médiane :

```
    donnees["nom de la colonne"].median()
```

Le mode :

```
    donnees["nom de la colonne"].mode()
```

### Utiliser les indicateurs de dispersion

L'écart type :

```
    donnees["nom de la colonne"].std()
```

Un quantile avec des intervalles définissant, par exemple, un quartile :

```
    donnees["nom de la colonne"].quantile([0, 0.25, 0.5, 0.75, 1])
```

> [!NOTE]
> Les intervalles sont : $\left[ 0, 0.25 \right[$, $\left[ 0.25, 0.5 \right[$, $\left[ 0.5, 0.75 \right[$ et $\left[ 0.75, 1 \right]$.

On peut définir un seul intervalle afin de calculer la **distance interquantile**.

```
    Q = donnees["nom de la colonne"].quantile([0.25, 0.75])
    distance = Q[0.75] - Q[0.25]
```

> [!NOTE]
> On peut coder un tableau avec les variables interquantiles et la méthode `qcut(` données`,` quantiles`,` nom des quantiles `)`.

### Identifier les valeurs extrêmes

- Identifier le nombre minimal d'une liste

```
    donnees["nom de la colonne"].min()
```

- Identifier le nombre maximal d'une liste

```
    donnees["nom de la colonne"].max()
```

## Calculer l'effectif total d'une colonne

```
    donnees["nom de la colonne"].sum()
```

## Analyse bivariée des données avec `Pandas`

### Croisement entre deux variables

La méthode `crosstab(colonne1, colonne2)` permet de croiser des variables.

```
   pd.crosstab(donnees["..."], donnees["..."]) 
```

La méthode a plusieurs options :

- `margins=True` qui donne les totaux des lignes et des colonnes ;

- `normalize='columns'` qui permet de calculer les pourcentages par colonnes ;

- `normalize='index'` qui permet de calculer les pourcentages par lignes.

### Régression linéaire par la méthode des moindres carrées entre deux variables

Tutoriel : [https://tube-sciences-technologies.apps.education.fr/w/dJg6Vq7ByfvxgW36YUap68](https://tube-sciences-technologies.apps.education.fr/w/dJg6Vq7ByfvxgW36YUap68)

La bibliothèque permettant de calculer une régression linéaire par la méthode des moindres carrées entre deux variables est `scipy.stats` en utilisant la méthode `linregress(x, y)` prenant en paramètres : `x`, la variable à expliquer et `y`, la variable explicative. Le résultat est une liste comprenant :

- le coefficient directeur de la droite de régression ;

- l'ordonnée à l'origine de la droite de régression ;

- le coefficient de corrélation de K. Pearson ;

- la probabilité critique ;

- la déviation standard.

Pour utiliser la méthode, on suppose que `x` et `y` sont deux listes de même dimension, et on utilise une liste appelée `params` :

```
    params = scipy.stats.linregress(x, y)
    pente = params[0]
    ordonnee = params[1]
    correlation = params[2]
    pvalue = params[3]
    deviationstandard = params[4]
```

Pour visualiser le résultat, il faut :

1. Calculer la droite de régression :

```
    y_modele = []
    for i in range(0,len(x)):
        y_modele.append(a * x[i] + b)
```

2. Tracer le nuage de points et la droite de régression

```
    fig, plot = plt.subplots()
    plot.scatter(x, y, c = "blue")
    plot.plot(x, y_modele, "-r", color = "red")
    plot.set_title("Régression linéaire entre x et y")
    plot.set_xlabel("x (unité de x)")
    plot.set_ylabel("y (unité de y)")
    plt.show()
    plt.savefig("./regression.png")
```

> [!WARNING]
> Il faut bien écrire tous les arguments dans `plot.plot(x, y_modele, "-r", color = "red")` pour tracer une droite de régression en rouge.

### Corrélation entre deux variables

```
    from scipy.stats import pearsonr
    variable1 = list(donnees["nom1"].dropna())
    variable2 = list(donnees["nom2"].dropna())
    round(pearsonr(variable1, variable2)[0], 2)
```

La fonction `pearsonr()` calcule le coefficient de corrélation.

Avec `Pandas`, l'écriture est un peu plus simple avec la méthode `.corr()`.

```
    donnees[["nom de la colonne 1", "nom de la colonne 2"]].corr()
```

`Pandas` permet de grouper des catégories avec la méthode `.groupby()`

```
    donnees.groupby("colonne pour le regroupement")["nom de la colonne servant de référence au calcul"].mean()
```

> [!NOTE]
> On peut appliquer plusieurs méthodes de calcul avec la méthode `.agg()` :
> - avec une liste : `donnees.agg(["median", "mean"])` ;
> - avec un dictionnaire : `donnees.agg({"Médiane": "median", "Moyenne": "mean"})`.

### Test du ${\chi}^2$

[https://sites.google.com/view/aide-python/statistiques/test-du-%CF%87-khi2](https://sites.google.com/view/aide-python/statistiques/test-du-%CF%87-khi2)

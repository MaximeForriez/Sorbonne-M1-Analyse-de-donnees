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

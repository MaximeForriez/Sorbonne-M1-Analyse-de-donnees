# Statistiques multivariées avec `Python`

## Les analyses factorielles

Les analyses factorielles fonctionnent de toutes avec la même logique informatique. Seule l'A.C.P. sera développée. Pour les autres, il faut vous reporter à la documentation officielle de `Python`.

### Analyse en composantes principales (A.C.P.)

1. Pour faire des A.C.P., on a besoin de la bibliothèque `Scikit-learn`.

> [!WARNING]
> Avant de l'utiliser, il faut centrer-réduire les données, les normaliser. L'objectif est de pouvoir comparer les colonnes entre elles.

```
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    import pandas as pd
    tableau = données_quantitatives
    #Centrer-réduire
    tab_norm = StandardScaler().fit_transform(tableau)
    #ACP
    pca = PCA(n_components = 3)
    decomposition = pd.DataFrame(data = decomposition, columns = ['Facteur 1', 'Facteur 2', 'Facteur 3'])
```

- `PCA` signifie *Principal Components Analysis*. Il faut retenir que, en général, l'abréviation anglaise des méthodes statistiques premd de retrouver les fonctions sur `Python`.

- `n_components` détermine le nombre d'axes factoriels choisi, ici `3`.

2. On peut obtenir les valeurs propres $\lambda$.

```
    decomposition.head()
```

3. On peut obtenir les valeurs singulières $\sqrt{\lambda}$.

```
    print([round(i, 2) for i in pca.explained_singular_values_])
```

4. On peut obtenir la proportion de variance expliquée.

```
    print([round(i, 2) for i in pca.explained_variance_ratio_])
```

5. On peut visualiser les résultats

```
    plot = decomposition.plot(
        kind = "scatter",
        color = "gray",
        alpha = 0.5,
        x = "Facteur 1",
        y = "Facteur 2",
        marker = "v"
    )
```

6. On peut calculer la qualité de la projection des données. Cela permet d'avoir une information sur la définition produite par la projection sur quelques axes. La mesure correspond aux cosinus carrés.

```
    d2 = (tab_norm ** 2).sum(axis = 1)
    cos2 = decomposition ** 2
    cos2["d2"] = d2
    cos2 = cos2.apply(lambda x : x/x["d2"], axis = 1)
    cos2 = cos2.drop("d2", axis = 1)
    cos2 = head()
```

7. On peut calculer la contribution des individus aux facteurs (CTR)

```
    valeurs_propres = pca.singular_values_ ** 2
    n = len(decomposition)
    ctr = decomposition ** 2
    for col, val in zip(ctr.columns, valeurs_propres):
        ctr.loc[:,col] = ctr.loc[:, col] / (n * val)
    ctr.columns = ["CTR Facteur 1", "CTR Facteur 2", "CTR Facteur 3"]
    ctr.head()
```

8. La bibliothèque `Prince` a une fonction `pca` qui calcule directement la contribution des individus.

```
    import prince
    pca = prince.PCA(
        n_components = 3,
        rescale_with_mean = True,
        rescale_with_std = True
    )
    pca = pca.fit(tableau.values)
    decomposition = pca.transform(tableau.values)
    print([round(i, 2) for i in pca.explained_inertia_])
```

- `pca.explained_inertia_` calcule la variance expliquée par chaque axe.

- `pca_eigenvalues_` calcule les valeurs propres.

- `columns.correlations(...)` calcule le coefficient de corrélation.

- `row_contributions(...)` calcule la contribution de chaque individu.

### Analyse factorielle des correspondances (A.F.C.)

Le tableau d'entrée est un tableau croisant deux variables qualitatives.

```
    import prince
    X = données
    afc = prince.CA(n_components = 2)
    afc = afc.fit(X)
```

On peut visualiser les résultats.

```
    afc = afc.plot_coordinates(
        X = X,
        figsize = (5, 5),
        show_row_labels = False,
        x_component = 0,
        y_component = 1
    )
```

On peut calculer les valeurs propres avec `afc.eigenvalues_`.

On peut calculer l'inertie expliquée avec `afc.explained_inertia_`.

### Analyse des correspondances multiples (A.C.M.)

L'A.C.M. s'utilise avec plusieurs variables catégorielles. Les lignes correspondent aux individus et les colonnes, aux variables qualitatives.

1. Construction le tableau disjonctif complet (T.D.C.) sur lequel l'A.C.M. sera réalisée. On note `X` le tableau catégoriel.

```
    import pandas as pd
    X = pd.read_vcs(./fichier.csv)
    pd.get_dummies(X)
```

2. Calculer l'A.C.M. sur deux facteurs

```
    acm = prince.MCA(n_components = 2)
    print([round(i, 3) for i in acm.explained_inertia_])
```

- Les valeurs propres se calculent avec `acm.eigenvalues_`.

- Les coordonnées des lignes s'obtiennent avec `mca.row_coordinates(X)`.

- Les coordonnées des lignes s'obtiennent avec `mca.columns_coordinates(Y)`.

3. Visualiser les deux premiers facteurs

```
    X.columns = [i.replace("_", "") for i in X.columns]
    plot = acm.plot_coordinates(
        X = X,
        figsize = (4, 4),
        row_points_size = 10,
        show_row_labels = False,
        column_points_size = 30,
        show_column_labels = False
    )
    plot.get_figure().savefig('mca.png')
```
4. Calculer la contribution de l'A.C.M. avec `Prince`

```
    mca_prince = prince.MCA(n_components = 12)
    mca_prince.fit(X)
    T = mca_prince.row_coordinates(X)
    d2 = (T ** 2).sum(axis = 1)
    intermediaire = (T ** 2)
    intermediaire["d2"] = d2
    cos2 = intermediaire.apply(lambda x : x/x["d2"], axis = 1)
    cos2 = cos2.drop("d2", axis = 1)
```

## Les modèles de régression

### La régression linéaire

On peut l'hypothèse qu'il existe une variable dépendante `Y`, reliée à des variables indépendantes `X` par une relation linéaire[^1].

```
    import statsmodels.api as sm
    donnees = ...
    X = donnees[[ ..., ..., ...]]
    Y = donnees[]
    modele = sm.OLS(Y, X)
    regression = modele.fit()
```

1. Afficher les paramètres de la régression

```
    print('Paramètres : ', regression.params)
```

2. Afficher le coefficient de détermination

```
    print('R2 : ', round(regression.rsquared, 2))
```

3. Présenter l'ensemble des éléments du modèle de régression

```
    print(regression.summary())
```

4. Opérer un test d'hypothèse et déterminer les barres d'erreur

```
    regression.pvalues()
```

### La régression logistique

La régression logistique se calcule soit sur des variables qualitatives, soit sur des variables quantitatives. La régression s'effectue sur la probabilité d'avvoir l'une ou l'autre des valeurs de la variable dépendante par rapport aux variables indépendantes.

On utilise la bibliothèque `Patsy`, notamment la fonction `dmatrice(...)` pour faire un T.D.C.

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

On caractérise l'algorithme :

1. en définissant un nombre $k$ de groupes à rechercher ;

2. en découpant par un algorithme de l'ensemble des données en $k$ groupes avec comme objectif de réduire la distance entre les éléments contenus au sein de chaque groupe.

On utilise la bibliothèque `Scikit-learn`.

```
    from sklearn.cluster import KMeans
    import pandas as pd
    tableau_cluster = tableau[[..., ...]].dropna()
    kmeans = KMeans(n_clusters = 3)
    kmeans.fit(tableau_cluster)
    moyennes_groupes = pd.DataFrame(kmeans.cluster_centers_)
    moyennes_groupes.columns = tableau_cluster.columns
```

On peut calculer le nombre dans chaque groupe avec `pd.Series(kmeans.labels_).value_counts()`

`Scikit-learn` peut calculer l{'}indice de Rand et l{'}information mutuelle normalisée.

### Classification ascendante hiérarchique (C.A.H.)

L'algorithme définit ce qu'est « être proche ».

1. Les deux éléments les plus proches sont regroupés et deviennent un nouvel élément caractérisé par la moyenne des valeurs.

2. Recommencer l'algorithme jusqu'à ce que tous les éléments soient regroupés.

On obtient ainsi un arbre inversé, le **dendrogramme**.

```
    from scipy.cluster.hierarchy import dendrogram
    import matplotlib.pyplots as plt
    fig, ax = plt.subplots()
    dendrogram(
        arbre_associations,
        distance_sort = 'ascending',
        truncate_mode = 'lastp',
        p = 100,
        color_threshold = 50000,
        leaf_rotation = 90.,
        leaf_font_size = 8.,
        ax = ax
    )
    fig.set_figwidth(12)
    fig.set_figheight(8)
```

Pour « couper » l'arbre, on tape :

```
    from scipy.cluster.hierarchy import fcluster
    import pandas as pd
    distance = 50000
    clusters = fcluster(arbre_associations, distance, criterion = 'distance')
    pd.Series(clusters).value_counts()
```

- Il existe également `criterion = 'maxclust'`.

- Il existe les méthodes `groupby()` et `agg()`.

# Notes de bas de page

[^1]: En anglais : *Ordinary Least Square* (O.L.S.)

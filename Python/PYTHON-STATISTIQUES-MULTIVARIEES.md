# Statistiques multivariées avec `Python`

## Les analyses factorielles

Les analyses factorielles fonctionnent de toutes avec la même logique informatique. Seule l'A.C.P. sera développée. Pour les autres, il faut vous reporter à la documentation officielle de `Python`.

### Analyse en composantes principales (A.C.P.)

En complément : [https://fxjollois.github.io/cours-2019-2020/lp-iot--python-ds/seance2-ACP-classif.html](https://fxjollois.github.io/cours-2019-2020/lp-iot--python-ds/seance2-ACP-classif.html)

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
    pca = PCA(n_components = 3).fit(tab_norm)
    #Affichage des composantes principales
    decomposition = pd.DataFrame(data = pca.components_, columns = ['Facteur 1', 'Facteur 2', 'Facteur 3'])
    print(decomposition)
```

- `PCA` signifie *Principal Components Analysis*. Il faut retenir que, en général, l'abréviation anglaise des méthodes statistiques premd de retrouver les fonctions sur `Python`.

- `n_components` détermine le nombre d'axes factoriels choisi, ici `3`.

2. On peut obtenir les valeurs propres $\lambda$.

```
    nbindividus = tab_norm.shape[0]
    valeurpropre = (nbindividus - 1)/nbindividus * pca.explained_variance_
```

3. On peut obtenir les valeurs singulières $\sqrt{\lambda}$.

```
    varianceexpliquee = pca.explained_singular_values_
```

4. On peut obtenir la proportion de variance expliquée.

```
    pourcentagevarianceexpliquee = pca.explained_variance_ratio_
```

5. On peut visualiser les résultats à partir de la décomposition calculée précédemment. Elle visualise le nuage de points des variables.

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

Néanmoins, pour représenter les individus correctement, il faut passer par `Matplotlib` :

```
    #Coordonnées des individus
    individu = pca.transform(tab_norm)
    decompositionindividu = pd.DataFrame(data = individu, columns = ['Facteur 1', 'Facteur 2', 'Facteur 3'])
    print(decompositionindividu)
    #Visualisation des individus
    x = decompositionindividu["Facteur 1"]
    y = decompositionindividu["Facteur 2"]
    nom = #Mettre le nom des individus
    cm = 1/2.54  # centimeters in inches
    fig, plot = plt.subplots(figsize=(50*cm, 50*cm))
    plot.scatter(x, y, c = 'blue')
    for i in range(0,len(nom)):
        plot.annotate(nom[i], (x[i], y[i]))
    plot.set_title("Projection des facteurs 1 et 2 des lignes")
    plot.set_xlabel("Facteur 1")
    plot.set_ylabel("Facteur 2")
    plt.savefig("./acp.png")
```

6. Calculer la qualité de la projection des données. Cela permet d'avoir une information sur la définition produite par la projection sur quelques axes. La mesure correspond aux cosinus carrés.

```
    d2 = (tab_norm ** 2).sum(axis = 0)
    cos2 = decomposition ** 2
    cos2["d2"] = d2
    cos2 = cos2.apply(lambda x : x/x["d2"], axis = 1)
    cos2 = cos2.drop("d2", axis = 1)
    cos2.columns = ["COS2 Facteur 1", "COS2 Facteur 2", "COS2 Facteur 3"]
    print(cos2)
```

7. Calculer la contribution des individus aux facteurs (CTR)

```
    valeurs_propres = pca.singular_values_ ** 2
    ctr = decomposition ** 2
    for col, val in zip(ctr.columns, valeurs_propres):
        ctr.loc[:,col] = ctr.loc[:, col] / (len(decomposition) * val)
    ctr.columns = ["CTR Facteur 1", "CTR Facteur 2", "CTR Facteur 3"]
    ctr.head()
```

8. Calculer les coordonnées des variables et tracer le cercle de corrélation

```
    #Coordonnées des variables : cercle de corrélation
    nbvariables = tab_norm.shape[1]
    #Racine carrée des valeurs propres
    sqrt_eigval = np.sqrt(valeurpropre)
    #Matrice vide pour avoir les coordonnées
    correlationvariable = np.zeros((nbvariables, nbvariables)) 
    for k in range(nbvariables):
        correlationvariable[:,k] = pca.components_[k,:] * sqrt_eigval[k]
    #Création d'un Dataframe contenant les coordonnées de la corrélation des variables : 'id' appelle une liste contenant des noms des variables qu'il faut récupérer ; 'COR_1', ... 'COR_n' listent autant de corrélation qu'il y a de variables.
    coordonneesvariable = pd.DataFrame({
        'id': nomdesvariables,
        'CORRELATION FACTEUR 1': correlationvariable[:,0],
        'CORRELATION FACTEUR 2': correlationvariable[:,1], 
        'CORRELATION FACTEUR 3': correlationvariable[:,2]
    })
    print(coordonneesvariable)
    #Visualisation du cercle de corrélation entre la COR_1 (facteur 1) et la COR_2 (facteur 2)
    x = coordonneesvariable["CORRELATION FACTEUR 1"]
    y = coordonneesvariable["CORRELATION FACTEUR 2"]
    nomligne = nomdesvariables
    # Astuce : Pour agrandir correctement l'image qui, par défaut, est exprimée en inches. On utilise la conversion suivante :
    cm = 1/2.54
    fig, plot = plt.subplots(figsize=(50*cm, 50*cm))
    fig.suptitle("Cercle des corrélations")
    plot.set_xlim(-1, 1)
    plot.set_ylim(-1, 1)
    # Ajout des axes
    plot.axvline(x = 0, color = 'lightgray', linestyle = '--', linewidth = 1)
    plot.axhline(y = 0, color = 'lightgray', linestyle = '--', linewidth = 1)
    # Ajout des noms des variables
    for i in range(0,len(nomligne)):
        plot.annotate(nomligne[i], (x[i], y[i]))
    # Ajout du cercle
    plt.gca().add_artist(plt.Circle((0,0), 1, color='blue', fill=False))
    plt.savefig("./acp-cercle-de-correlation.png")
```

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

L'A.C.M. s'utilise avec plusieurs variables catégorielles. Les lignes correspondent aux individus et les colonnes, aux variables qualitatives. En plus de `Pandas`, on utilise la bibliothèque `Prince`.

1. Construire le tableau disjonctif complet (T.D.C.) sur lequel l'A.C.M. sera réalisée avec `Pandas`. On note `X` le tableau catégoriel.

```
    import pandas as pd
    import prince
    import matplotlib.pyplot as plt
    X = pd.read_csv(./fichier.csv)
    tdc = pd.get_dummies(X)
```

2. Calculer l'A.C.M. sur deux facteurs avec `Prince`

```
    acm = prince.MCA(n_components = 2).fit(X)
```

ou

```
    acm = prince.MCA(n_components = 2).fit(tdc)
```

- L'attribut `n_components` fixe le nombre d'axes. Il est possible de faire l'A.C.M. avec les données brutes, ici `X`, ou le T.D.C., ici `tdc`.

- Les valeurs propres se calculent avec `acm.eigenvalues_`.

- Les coordonnées des lignes s'obtiennent avec `acm.row_coordinates(X)` ou `acm.row_coordinates(tdc)`.

- Les coordonnées des colonnes s'obtiennent avec `acm.column_coordinates(X)` ou `acm.column_coordinates(tdc)`.

3. Visualiser les deux premiers facteurs avec `Prince`

```
    plot = acm.plot_coordinates(
        X = X,
        figsize = (4, 4),
        row_points_size = 10,
        show_row_labels = False,
        column_points_size = 30,
        show_column_labels = False
    )
    plot.get_figure().savefig('acm.png')
```

Malheureusement, la solution `Prince` peut poser problème. On utilise alors `Matplotlib` pour s'en sortir.

```
    #1 - On récupère les coordonnées des lignes et des colonnes
    coordX = acm.row_coordinates(tdc)
    coordY = acm.column_coordinates(tdc)
    #2 - On récupère le nom des lignes et des colonnes
    nomligne = coordX.index
    nomcolonne = coordY.index
    #3 - On visualise les deux premiers facteurs
    xligne = coordX[0]
    yligne = coordX[1]
    xcolonne = coordY[0]
    ycolonne = coordY[1]
    # Astuce : Pour agrandir correctement l'image qui, par défaut, est exprimée en inches. On utilise la conversion suivante :
    cm = 1/2.54
    fig, plot = plt.subplots(figsize=(50*cm, 50*cm))
    # On crée un nuage de points pour les lignes (individus) et un nuage de points pour les colonnes (modalités)
    plot.scatter(xligne, yligne, c = 'blue')
    plot.scatter(xcolonne, ycolonne, c = 'red')
    # Astuce : On visualise le nom des lignes et des colonnes avec ces deux boucles :
    for i in range(0,len(nomligne)):
        plot.annotate(nomligne[i], (xligne[i], yligne[i]))
    for i in range(0,len(nomcolonne)):
        plot.annotate(nomcolonne[i], (xcolonne[i], ycolonne[i]))
    plot.set_title("Projection des facteurs 1 et 2 des lignes")
    plot.set_xlabel("Facteur 1")
    plot.set_ylabel("Facteur 2")
    plt.savefig("./acm.png")
```

4. Calculer la qualité des axes de l'A.C.M. (les cosinus carrés) avec `Prince` des lignes (avec `X` et `tdc`) :

```
    T = acm.row_coordinates(X)
    d2 = (T ** 2).sum(axis = 1)
    intermediaire = (T ** 2)
    intermediaire["d2"] = d2
    cos2 = intermediaire.apply(lambda x : x/x["d2"], axis = 1)
    cos2 = cos2.drop("d2", axis = 1)
    print(cos2)
```

5. Calculer la qualité des axes de l'A.C.M. (les cosinus carrés) avec `Prince` des colonnes (avec `X` et `tdc`) :

```
    T = acm.column_coordinates(X)
    d2 = (T ** 2).sum(axis = 1)
    intermediaire = (T ** 2)
    intermediaire["d2"] = d2
    cos2 = intermediaire.apply(lambda x : x/x["d2"], axis = 1)
    cos2 = cos2.drop("d2", axis = 1)
    print(cos2)
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

`Scikit-learn` peut calculer l'[indice de Rand](../Formulaire-mathematique/Seance-09/09-Indice-de-Rand.md) et l{'}information mutuelle normalisée.

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

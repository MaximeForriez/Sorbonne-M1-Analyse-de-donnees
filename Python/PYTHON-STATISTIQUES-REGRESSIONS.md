# Régressions linéaires avec `Python`

## La régression linéaire simple

On peut l'hypothèse qu'il existe une variable dépendante `Y`, reliée à une variable indépendante `X` par une relation linéaire[^1].

1. Calculer la régression linéaire avec `SciPy`

```
    import scipy
    import scipy.stats
    X = [...]
    Y = [...]
    params = scipy.stats.linregress(X, Y)
    print(params)
    a = params[0]
    b = params[1]
```

Il faut remplacer `[...]` par la liste de données.

2. Calculer la droite de régression

```
    y_modele = []
    for i in range(0,len(Y)):
        y_modele.append(a * Y[i] + b)
```

3. Sortir l'image de la régression obtenue

```
    x = X
    y = Y
    fig, plot = plt.subplots()
    plot.scatter(x, y, c="blue")
    plot.plot(x, y_modele, "-r", color="red")
    plot.set_title("Régression linéaire entre X et Y")
    plt.savefig("./img/nom_de_l_image.png")
```

4. Calculer le coefficient de corrélation

```
    my_cor, pval = scipy.stats.pearsonr(X,Y)
    #Coefficient de corrélation 
    print(my_cor)
    #p value
    print(pval)
```

## La régression linéaire multiple

Avec `Scikit-Learn`, on peut calculer une régression linéaire multiple.

```
    from sklearn.linear_model import LinearRegression
    donnees = ...
    X = donnees[[ ..., ..., ...]]
    Y = donnees[]
    modele = LinearRegression().fit(X, Y)
    print(modele.intercept_)
    print(modele.coef_)
```

1. `modele.intercept_` calcule la constante de la régression linéaire multiple.

2. `modele.coef_` calcule les coefficients des paramètres explicatifs de la régression linéaire multiple.

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
    regression.pvalues
```

## La régression logistique

La régression logistique se calcule soit sur des variables qualitatives, soit sur des variables quantitatives. La régression s'effectue sur la probabilité d'avvoir l'une ou l'autre des valeurs de la variable dépendante par rapport aux variables indépendantes.

On utilise la bibliothèque `Patsy`, notamment la fonction `dmatrice(...)` pour faire un T.D.C.



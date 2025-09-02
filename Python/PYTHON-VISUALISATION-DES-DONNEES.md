# Visualisation des données avec `Python`

Il existe trois bibliothèques pour faire des visualisations de données :

- `Pandas` ;

- `Matplotlib` ;

- `Seaborn`.

## Documentation

### `Pandas`

- - [Documentation officielle](https://pandas.pydata.org/)

### `Matplotlib`

- [Documentation officielle](https://matplotlib.org/)

- [Documentation non officielle](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)

- Khan, Tajamul, [`matplotlib` *Cheat Sheet*](./PDF/Matplotlib/Khan-Tajamul-MatPlotLib.pdf)

- [`matplotlib` *Cheat Sheet*](./PDF/Matplotlib/MatPlotLib-Cheat-Sheet.pdf)

- [Comment utiliser `matplotlib` ?](./PDF/Matplotlib/MatPlotLib-for-Python.pdf)

- [Comment utiliser `matplotlib` ?](./PDF/Matplotlib/MatPlotLib.pdf)

`import matplotlib.pyplot`

### `Seaborn`

- [Documentation officielle](https://seaborn.pydata.org/)

- Khan, Tajamul, [`Seaborn` *Cheat Sheet*](./PDF/Seaborn/Khan-Tajamul-Seaborn.pdf)

- Mishra, Abhishek, [Comment utiliser `Seaborn` ?](./PDF/Seaborn/Mishra-Abhishek-Seaborn.pdf)

- Vardhan, Prudhvi, [Comment utiliser `Seaborn` ?](./PDF/Seaborn/Vardhan-Prudhvi-Seaborn.pdf)

### `GeoPandas`

- [Documentation officielle](https://geopandas.org/en/stable/)

## Démarche générale pour construire un graphique avec les différents outils

1. Préparer les données dans le bon format

2. Choisir le type de représentation souhaité

3. Définir une nouvelle figure dans `Python`

4. Afficher les données avec la fonction de représentation souhaitée

5. Ajouter des informations de contexte

6. Afficher et sauvegarder la figure

## Construire un graphique avec `Pandas`

```
    donnees = liste_des_données
    plot = donnees.plot(
        kind = "barlh",
        color = "lightgray",
        figsize = (x, y),
        title = "Titre du graphique",
        s = 0.1,
        c = "couleur",
        alpha = 0.5,
        edgecolor = "couleur"
    )
    plot.set_xlabel("titre des abscisses")
    plot.set_ylabel("titre des ordonnées")
```

- Le paramètre `kind` définit le type de graphique.

    - `kind = "barlh"` affiche des barres horizontales.

    - `kind = "bar"` affiche des barres verticales.

    - `kind = "pie"` affiche un diagramme circulaire.

    - `kind = "hist"` affiche un histogramme.

    - `kind = "scatter"` affiche un nuage de points.

- Le paramètre  `color` définit la couleur de fond.

- Le paramètre  `figsize` définit la taille de l'image sous la forme d'un tuple.

- Le paramètre  `title` définit un titre à l'image.

- Le paramètre  `s` définit la taille des points.

- Le paramètre  `c` définit la couleur des éléments.

- Le paramètre  `alpha` définit la transparence de l'image.

- Le paramètre  `edgecolor` définit la couleur des lignes.


## Construire un graphique avec `Matplotlib`

`Matplotlib` est une bibliothèque créée par John Hunter en 2002. Elle est spécialisée dans les représentations graphiques à deux dimensions.

```
    import matplotlib.pyplot as plt
    x = liste_contenant_les_abscisses
    y = liste_contenant_les_ordonnées
    fig, plot = plt.subplots()
    plot.bar(x, y)
    plot.set_title("titre du graphique")
    plot.set_xlabel("titre de l'axe des abscisses")
    plot.set_ylabel("titre de l'axe des ordonnées")
    plot.show()
```

- `plt` est un alias de `pyplot`.

- `fig` est la variable qui définit la figure. `plot` est la variable qui définit les axes.

- `.bar(x, y)` est la méthode qui affiche un diagramme en barres. Il existe d'autres représentations :

    - `.hist(donnees, bins = 20)` définit un histogramme. Le paramètre `bins` définit le nombre d'intervalles de l'histogramme.

    - `pie.(x, labels = donnees.index)` définit un diagramme circulaire

    - `plot.plot(x, y, "o-", label = "titre de la courbe de la légende")` définit une coube avec deux listes. `o-` définit la forme de la courbe. Il est à noter que, pour que le paramètre `label` fonctionne, il faut ajouter `plt.legends()` avant l'instruction `plot.show()`.

    - `.scatter(x, y, s=1, alpha = 0.3)` définit un nuage de points. Le paramètre `s` définit la taille des points. Le paramètre `alpha` définit la transparence.

    - `.boxplot(donnees, labels = "...", notch = True)` crée une boîte à moustaches.

> [!NOTE]
> On peut faire un diagramme en bulles (ou *bubble chart*).

> [!NOTE]
> On peut créer une figure avec plusieurs graphiques.

> [!NOTE]
> On peut mettre des couleurs dans les options avec :
> - `b =` : bleu (*blue*)
> - `g =` : vert (*green*)
> - `r =` : rouge (*red*)
> - `c =` : cyan (*cyan*)
> - `m =` : magenta (*magenta*)
> - `y =` : jaune (*yellow*)
> - `k =` : noir (*black*)
> - `w =` : blanc (*white*)

- Il est possible de contrôler la graduation :

    - `.get_xticks()`

    - `.xticklabels()`

    - `.xtickslabels(...)`

    - `.get_yticks()`

    - `.yticklabels()`

    - `.ytickslabels(...)`

- Il est possible de limiter la visualisation des axes :

    - `plot.set_xlim(...)`

    - `plot.set_ylim(...)`

- Il est possible de sauvegarder la figure créée avec : `plt.savefig("adresse", dpi = 400)`. Le paramètre `dpi` est très important. Il définit la résolution des pixels. Pour obtenir une image imprimable, il faut impérativement qu'il soit supérieur à 300. Si l'image ne sert qu'à être affichée sur un écran, 72 dpi suffit. Les formats de sortie possibles sont : `*.png`, `*.jpg`, `*.eps`, `*.pdf`.

## Construire un graphique avec `Seaborn`

```
    import seaborn as sns
    sns.countplot(x = "colonne", data = donnees)
```

La méthode `.countplot()` permet de :

- faire le comptage de chaque catégorie ;

- afficher le diagramme avec un choix automatique de couleur.

L'avantage de la méthode `.countplot()` est que l'on a plus besoin de calculer un tableau de données. Néanmoins, elle cumule trois inconvénients.

1. La taille de la figure est inappropriée.

2. La légende est souvent illisible.

3. Elle ne permet pas d'ajouter un titre.

Pour combler ces défauts, on utilise `Matplotlib`.

`Seaborn` permet de réaliser des **visualisations complexes**.

- `sns.catplot(...)` permet d'afficher une boîte à moustache.

- `sns.histplot(...)` permet d'afficher un histogramme. La méthode doit être couplée avec `displot(...)`.

- `sns.joinplot(...)` permet de joindre plusieurs graphiques.

- `sns.lmplot(...)` permet de calculer une droite de régression.

- `sns.heatmap(...)` permet de visualiser un tableau croisé.

- *etc*.

`Seaborn` permet de styliser les thèmes.

- `sns.set_style("whitegrid")` doit être placé en début de graphique pour fixer un thème. Il existe également : `darkgrid`, `dark`, `white` et `ticks`.

- `sns.set_context("paper", font_scale = 1)` définit le contexte de publication de la figure. Il existe également `notebook`, `talk` et `poster`.

## Construire une carte avec `GeoPandas`

Il est possible constuire directement une carte avec `Python` à partir de vos données statistiques. La bibliothèque `GeoPandas` peut lire des *shapefile* (`*.shp`). Elle manipule :

- des points ;

- des lignes, des polylignes ;

- des polygones.

```
    import geopandas as gpd
    fichier = "./france.shp"
    france = gpd.readfile(fichier)
```

La variable `france` est un objet `GeoDataFrame`.

Pour obtenir la liste des champs, on tape :

```
    list(france.columns)
```

Pour visualiser la carte (la couche dessin), on tape

```
    france.plot()
```

On peut zoomer sur un élément de la carte à partir de données attributaires.

```
    corse = france[france["attribut"] == "valeur"]
    plot = corse.plot()
    print(type(corse.loc[1, "geometry"]))
```

On peut créer des formes avec la bibliothèque `shapely.geometry`

```
    from shapely.geometry import Point, LineString, Polygon
```

On peut construire une couche en utilisant le format `GeoJSON`

```
    gpd.GeoDataFrame({
        'geometry': [Point(..., ...)]
        'donnees': [données 1, ...]
    })
```

Il existe de nombreux attributs et méthodes :

- `centroid` pour afficher un centroïde ;

- `dissolve(...)` pour défaire une union de formes ;

- `distance(...)` pour calculer une distance ;

- `geometry` ;

- `crs` pour définir un système de projection ;

- *etc*.

## Constuire des figures interatives

Il existe trois bibliothèques :

- [`Plotly`](https://plotly.com/) ;

- [`Bokeh`](https://bokeh.org/) ;

- [`Bqplot`](https://bqplot.readthedocs.io/en/stable/introduction.html).

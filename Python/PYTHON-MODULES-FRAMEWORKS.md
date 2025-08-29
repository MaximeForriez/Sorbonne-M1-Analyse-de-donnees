# Les modules de `Python`

## Modules utiles pour manipuler les données

### Le module `PyPDF`

La documentation est :

- [La documentation officielle du paquet](https://pypi.org/project/pypdf/) ;

- [la documentation officielle](https://pypdf.readthedocs.io/en/stable/) ;

- [la documentation non officielle en français](https://products.documentprocessing.com/fr/merger/python/pypdf/).

`import pypdf`

Les fonctions et les méthodes principales sont :

- `reader = pypdf.PdfReader("example.pdf")` pour instancier un objet P.D.F. L'objet contient le fichier si on est dans le même dossier, ou le chemin absolu ou relatif du fichier ;

- `number_of_pages = len(reader.pages)` pour avoir le nombre de pages du document.;

- `page = reader.pages[0]` pour lire la première page du P.D.F. ;

- `text = page.extract_text()` pour extraire les éléments textuels de la page P.D.F. ;

- `meta = reader.metadata` pour lire les métadonnées de la page P.D.F. :

	+ `meta.author` ;

	+ `meta.producer` ;

	+ `meta.subject` ;

	+ `meta.title`.

- `writer = pypdf.PdfWriter()` pour écrire des éléments dans le P.D.F. ;

- `writer.write("` nom du fichier `")` pour enregistrer les éléments écrits ;

- `writer.close()` pour fermer les modifications. Cette commande doit être mise chaque fois qu'un `pypdf.PdfWriter()` est créé ;

- `writer.add_page(` nouvellePage `)` pour ajouter une page ;

- `writer.add_metadata(` données en format J.S.O.N. `)` pour ajouter des métadonnées ; 

- `page2 = new_elements.add_blank_page(` largeur`,` hauteur`)` pour ajouter une page blanche ;

- `page2.merge_transformed_page(reader.pages[` numéro de page` ], pypdf.Transformation().translate(` nombre `),` nombre de pages `)` pour ajuster le contenu de la page.

### L'objet `PIL.Image`

-[Documentation officielle](https://pillow.readthedocs.io/en/stable/)

-[Documentation non officielle](https://he-arc.github.io/livre-python/pillow/index.html)

`import PIL.Image`

### L'objet `openpyxl`

- [Documentation officielle du paquet](https://pypi.org/project/openpyxl/)

- [Documentation officielle](https://readthedocs.org/projects/openpyxl/)

- [Documentation officielle](https://openpyxl.readthedocs.io/en/stable/)

- [Documentation non officielle en français](https://www.python-simple.com/python-autres-modules-non-standards/openpyxl.php)

`import openpyxl`

## Traitement des données avec des *framework*

### Documentation

- [Comment explorer et analyser les données avec les paquets `Python` ?](./PDF/Exploratory-Data-Analysis.pdf)

- [Comment visualiser les données avec les paquets `Python` ?](./PDF/Data%20Visualization-The%2017%20Mots%20Common%20Graph%20Types.pdf)

- [Comment visualiser les données avec les paquets `Python` ?](./PDF/Data-Visualization-Cheat-Sheet.pdf)

- Mester, Tomi, [Comment visualiser les données avec les paquets `Python` ?](./PDF/Mester-Tomi-Python-for-Data-Science-Cheat-Sheet.pdf)

- Mishra, Abhishek, [Comment visualiser les données avec les paquets `Python` ?](./PDF/Mishra-Abhishek-Plotly%20Python-Data%20Visualization.pdf)

- [Comment visualiser les données avec les paquets `Python` ?](./PDF/Plotly.pdf)

### Liste des *framework*

| *Framework* | Utilité | Documentation | Natif |
| :-: | :-: | :-: | :-:  |
| `SciPy` | Calcul scientifique | [`SciPy`](https://www.scipy.org) | non |
| `NumPy` | Stockage et calcul des données (fonctions et nombres aléatoires) | [`NumPy`](https://numpy.org/) | non |
| `Pandas` | Données de tableurs | [`Pandas`](https://pandas.pydata.org/) | non |
| `Matplolib` | Visualisation des données | [`Matplotlib`*: Visualization with* `Python`](https://matplotlib.org/) | non |
| `Nltk` | Analyse textuelle | [*Natural Language Toolkit*](https://www.nltk.org/) | non |
| `Networkx` | Analyse de réseaux | [*Network Analysis in* `Python`](https://networkx.org/) | non |
| `Scikit-learn` | *Machine Learning* | [*Machine Learning in *`Python`](https://scikit-learn.org/stable/) | non |
| `Dask` | Analyse de données massives[^1] | [*Parallel *`Python` *Fast and Easy*](https://www.dask.org/) | non |
| `Seaborn` | Visualisation de données statistiques | [`Seaborn`*: Statistical Data Visualisation*](https://seaborn.pydata.org/) | non |
| `BeautifulSoup` | Manipulation des pages internet | [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/) | oui |
| `Scrapy` | Collecte des données sur internet | [`Scrapy`](https://www.scrapy.org/) | non |
| `Tweepy` | interface avec `Twitter`/`X` | [`Tweepy`](https://www.tweepy.org/) | non |
| `GeoPandas` | Construction d'une carte à partir de données géoréférencées | [`GeoPandas`](https://geopandas.org/en/stable/) | non |
| `smtplit` | Envoi de courriel avec le protocole S.M.T.P.[^2] | [`smtplit`](https://docs.python.org/3/library/smtplib.html) | oui |
| `requests` | Requête sur internet | [`requests`](https://pypi.org/project/requests/) | oui |
| `random` | Générateur de nombres aléatoires | [`random`](https://docs.python.org/3/library/random.html) | oui |
| `glob` | Recherche de chemin de style `Unix`[^3] | [`glob`](https://docs.python.org/3/library/glob.html#module-glob) | oui |

## Notes de bas de page

[^1]: En anglais : *Big Data*

[^2]: *Simple Mail Transfer Protocol*

[^3]: `Unix` est le noyau des systèmes d'exploitation `MacOS` et `Linux`.
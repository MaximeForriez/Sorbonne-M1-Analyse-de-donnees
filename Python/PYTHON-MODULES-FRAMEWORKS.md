# Les modules de `Python`

- [Top 18 des paquets `Python` pour explorer, analyser et visualiser des données](./PDF/Top%2018%20Python%20Libraires%20for%20Data%20Scientists.pdf)

## Le module `PyPDF`

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

## L'objet `turtle`

[Documentation officielle de turtle](https://docs.python.org/3/library/turtle.html)

`import turtle`

## L'objet `PIL.Image`

-[Documentation officielle](https://pillow.readthedocs.io/en/stable/)

-[Documentation non officielle](https://he-arc.github.io/livre-python/pillow/index.html)

`import PIL.Image`

## L'objet `openpyxl`

- [Documentation officielle du paquet](https://pypi.org/project/openpyxl/)

- [Documentation officielle](https://readthedocs.org/projects/openpyxl/)

- [Documentation officielle](https://openpyxl.readthedocs.io/en/stable/)

- [Documentation non officielle en français](https://www.python-simple.com/python-autres-modules-non-standards/openpyxl.php)

`import openpyxl`

## Traitement des données

- [Comment explorer et analyser les données avec les paquets `Python` ?](./PDF/Exploratory-Data-Analysis.pdf)

- [Comment visualiser les données avec les paquets `Python` ?](./PDF/Data%20Visualization-The%2017%20Mots%20Common%20Graph%20Types.pdf)

- [Comment visualiser les données avec les paquets `Python` ?](./PDF/Data-Visualization-Cheat-Sheet.pdf)

- Mester, Tomi, [Comment visualiser les données avec les paquets `Python` ?](./PDF/Mester-Tomi-Python-for-Data-Science-Cheat-Sheet.pdf)

- Mishra, Abhishek, [Comment visualiser les données avec les paquets `Python` ?](./PDF/Mishra-Abhishek-Plotly%20Python-Data%20Visualization.pdf)

- [Comment visualiser les données avec les paquets `Python` ?](./PDF/Plotly.pdf)

- [`Python` *Cheat Sheets*](./PDF/Universite-de-Compiegne-Python-for-Data-Science-Cheat-Sheet-v1.pdf)

- [`Python` *Cheat Sheets*](./PDF/Universite-de-Compiegne-Python-for-Data-Science-Cheat-Sheet-v2.pdf)

### `pandas`

- Wadeed, Madni, [Comment utiliser `Pandas` ?](./PDF/Pandas/Madni-Wadeed-Pandas-Cheat-Sheet.pdf)

- [Comment utiliser `Pandas` ?](./PDF/Pandas/Pandas-Cheatsheet-A%20Beginners%20Guide.pdf)

- [Comment utiliser `Pandas` ?](./PDF/Pandas/Exploratory-Data-Analysis-with-Pandas.pdf)

- [Apprendre `Pandas` ?](./PDF/Pandas/Learning-Pandas.pdf)

- [Apprendre `Pandas` ?](./PDF/Pandas/Ali-Syed%20Afroz-Python%20Master%20Data%20Manipulation%20and%20Visualization.pdf)

### `matplotlib`

- [Documentation non officielle](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)

- Khan, Tajamul, [`matplotlib` *Cheat Sheet*](./PDF/Matplotlib/Khan-Tajamul-MatPlotLib.pdf)

- [`matplotlib` *Cheat Sheet*](./PDF/Matplotlib/MatPlotLib-Cheat-Sheet.pdf)

- [Comment utiliser `matplotlib` ?](./PDF/Matplotlib/MatPlotLib-for-Python.pdf)

- [Comment utiliser `matplotlib` ?](./PDF/Matplotlib/MatPlotLib.pdf)

`import matplotlib.pyplot`

### `Seaborn`

- Khan, Tajamul, [`Seaborn` *Cheat Sheet*](./PDF/Seaborn/Khan-Tajamul-Seaborn.pdf)

- Mishra, Abhishek, [Comment utiliser `Seaborn` ?](./PDF/Seaborn/Mishra-Abhishek-Seaborn.pdf)

- Vardhan, Prudhvi, [Comment utiliser `Seaborn` ?](./PDF/Seaborn/Vardhan-Prudhvi-Seaborn.pdf)

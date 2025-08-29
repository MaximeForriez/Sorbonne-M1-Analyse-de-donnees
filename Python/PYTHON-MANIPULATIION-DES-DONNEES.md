# Manipulation des données

## Documentation

- [Top 18 des paquets `Python` pour explorer, analyser et visualiser des données](./PDF/Top%2018%20Python%20Libraires%20for%20Data%20Scientists.pdf)

- [`Python` *Cheat Sheets*](./PDF/Universite-de-Compiegne-Python-for-Data-Science-Cheat-Sheet-v1.pdf)

- [`Python` *Cheat Sheets*](./PDF/Universite-de-Compiegne-Python-for-Data-Science-Cheat-Sheet-v2.pdf)

## Types de données

Il existe plusieurs manières de classer les types de données. La classification dépend du contexte. Est-ce un contexte d'analyse ou un contexte informatique ?

### Données brutes et données raffinées

En analyse, on distingue classique les **données brutes** des **données raffinées**. Les données brutes sont des informations récoltées sur internet, sur le terrain, *etc*. Elles n'ont subi aucun traitement. Par opposition, les données raffinées sont des données qui ont été nettoyées. Elles ne contiennent plus de données aberrantes, extrêmes, *etc*. Les doublons ont été supprimés. En résumé, ce sont les données utilisées pour faire des analyses de données.

### Format textuel ou format binaire

En informatique, on distingue les données en fonction de leur format. Cela se résume en deux types : le **format textuel** et le **format binaire**. Le format textuel est un fichier dont le contenu est écrit en langage lisible par un être humain. En général, il est possible de les ouvrir sur un éditeur de type `Bloc-Notes` sur `Windows`. Parmi tous les formats textuels existants, les plus courants sont : `*.txt`, `*.csv`, `*.json`, `*.html`, `*.svg`, *etc*. Le format binaire est un fichier dont le contenu n'est pas lisible par un être humain sur un éditeur. Parmi tous les formats binaires existants, les plus courants sont : `*.jpg`, `*.bmp`, `*.png`, `*.docx`, `*.xlsx`, `*.shp`, `*.pdf`, `*.ai`, *etc*.

## Ouvrir, lire, écrire un fichier

### Lire un fichier textuel - méthode 1

```
    fichier = open("./fichier.csv", "r")
    contenu = fichier.read()
    fichier.close()
    print(contenu[:])
```

- `"./fichier.csv"` est à compléter. Cela indique le répertoire. ``./` indique le répertoire courant (dossier racine). Pour indiquer un répertoire à partir d'un dossier racine, on tape `./src/fichier.csv`. On peut également mettre l'adresse absolue.

- `"r"` indique le type de permission sur les données ouvertes. Ici, cela signifie *read*, lecture.

- `[:]` permet de lire tout le fichier. Il s'agit d'un intervalle tel qu'il a été défini dans les [commandes de base](./PYTHON-COMMANDES-DE-BASE.md). Il est par conséquent possible de placer par des nombres entiers, comme `[1:2]`, qui lit entre les lignes 2 et 3.

### Lire un fichier textuel - méthode 2

```
    with open("./fichier.csv", "r") as fichier:
        contenu = fichier.read()
    print(contenu[:])
```

### Écrire un fichier textuel

```
    with open("./fichier.csv", "w") as fichier:
        contenu = fichier.write("cle": valeur)
```

- `"r"` indique le type de permission sur les données ouvertes. Ici, cela signifie  *write*, écriture. Il est à noter qu'il existe également `"x"` pour *execution*, exécution d'un script.

- Dans la méthode `write(...)`, on indique un dictionnaire.

### Lire ou écrire un fichier binaire

> [!WARNING]
> Les fichiers `*.pdf` ou `*.xlsx` sont binaires. Ils nécessitent des permissions différentes.

Pour lire un fichier binaire, on utilise `"rb"` au lieu de `"r"`.

Pour écire un fichier binaire, on utilise `"wb"` au lieu de `"w"`.

## Gérer un dossier

On gère un dossier avec les modules `os` ou `glob`.

```
    import glob
    fichier_excel = glob.glob('*.xls')
```

La commande permet de lister les fichiers ayant un format `Excel`.

```
    import requests as req
    info = req.get("https://lemonde.fr")
    with open("sauvegarde-Monde.txt","w") as fichier:
        fichier.write(info.text)
```

- Il faut noter que, dans `info.text`, `.text` est  un attribut.

## Manipuler les données lues

Les données lues forment souvent des [listes](./PYTHON-COMMANDES-DE-BASE.md). Pour parcourir les listes, on utilise une ou des [boucles](./PYTHON-COMMANDES-DE-BASE.md).

> [!TIP]
> Il sera toujours plus simple de lire un fichier textuel que binaire. Il est vivement conseillé de convertir vos données `Excel` en format `*.csv`.

Dans le cas d'un fichier textuel, il est possible de lire les données ligne par ligne.

```
    with open("./data/csv","r") as fichier:
        contenu = fichier.readlines()
    print(contenu[0][:])
    donnees = []
    for ligne in contenu:
        ligne_decoupe = ligne.split(",")
        donnees.append(ligne_decoupe)
    print(donnees[0][:])
```

- `donnees` définit une **ligne emboîtée**. `donnees[0][:]` se lit « ligne 1, toutes les colonnes ». Il est possible de définir un intervalle sur les lignes, comme les colonnes.

Le code peut s'écrire de manière plus abrégée.

```
    donnees = [ligne.split(",") for ligne in contenu]
```

> [!WARNING]
> Il faut bien faire attention à l'encodage des données textuelles.

> [!TIP]
> Il faut utiliser les [expressions régulières](https://docs.python.org/fr/3/howto/regex.html) (ou rationnelles).

## Utiliser la bibliothèque `Pandas`

La bibliothèque `Pandas` permet de :

- manipuler et de produire des données, organisées sous la forme de tableaux ;

- faciliter le nettoyage des données ;

- traiter des statistiques.

`Pandas` sert souvent de référence. Des bibliothèques spécifiques vont utiliser un vocabulaire et des conventinos de nommage similaire.

`Pandas` a été développé par Wes McKinney à partir de 2008 pour répondre à ses besions d'analyse financière d'évolutions temporelles.

### Documentation

- Wadeed, Madni, [Comment utiliser `Pandas` ?](./PDF/Pandas/Madni-Wadeed-Pandas-Cheat-Sheet.pdf)

- [Comment utiliser `Pandas` ?](./PDF/Pandas/Pandas-Cheatsheet-A%20Beginners%20Guide.pdf)

- [Comment utiliser `Pandas` ?](./PDF/Pandas/Exploratory-Data-Analysis-with-Pandas.pdf)

- [Apprendre `Pandas` ?](./PDF/Pandas/Learning-Pandas.pdf)

- [Apprendre `Pandas` ?](./PDF/Pandas/Ali-Syed%20Afroz-Python%20Master%20Data%20Manipulation%20and%20Visualization.pdf)

> [!NOTE]
> `Pandas` est plus puissant qu'`Excel`.

### Charger la bibliothèque

```
    import pandas as pd
```

> [!NOTE]
> `pd` est un alias conventionnel. Toutefois, il est possible d'utiliser `pandas` si on souhaite de ne pas mettre d'alias.

### Paramétrer `Pandas`

- `pd.set_option('display.with', 80)` permet de limiter le nombre de caractères, ici 80.

- `pd.set_option('display.max_columns', 5)` permet de définir un nombre de colonnes maximal, ici 6.

- `pd.set_option('display.precision', 1)` permet de définir le nombre de chiffres après la virgule, ici un seul.

- `pd.set_option('display.max_colwidth', 12)` permet de définir le nombre de caractères maximal dans une colonne.

Il en existe beaucoup d'autres : [https://pandas.pydata.org/docs/user_guide/options.html](https://pandas.pydata.org/docs/user_guide/options.html).

> [!NOTE]
> Il existe des attributs pour appeler les éléments définis par les méthodes précédentes.

### Charger des données à partir d'un fichier `Excel`

```
    tableau = pd.read_excel("./fichier.xlsx")
```

La commande permet d'ouvrir et de renvoyer du contenu d'un fichier `Excel`.

### Charger des données à partir d'un fichier C.S.V.

```
    tableau = pd.read_csv("./fichier.csv")
```

La commande permet d'ouvrir et de renvoyer du contenu d'un fichier C.S.V..

### Formater les données `Pandas`

Il existe deux objets :

- `DataFrame` ;

- `Series`.

Avec `DataFrame`, chaque colonne est un objet `Series`. Chaque ligne est une rangée (ou *row*). Un index est créé. Il commence par 0.

#### Visualiser les données

- `tableau.head()` permet de lire le début du tableau.

- `tableau.tail()` permet de lire la fin du tableau.

#### Obtenir la forme générale du tableau

Il s'agit d'obtenir le nombre de lignes et de colonnes.

```
    tableau.shape
```

#### Obtenir le nom des lignes et des colonnes


```
    list(tableau.index)[:]
    list(tableau.columns)[:]
    tableau.loc[index,colonne]
```

- Il est possible de définir tous les intervalles possibles.

- L'attribut `.loc` prend en paramètre obligatoire l'index de la ligne, et en paramètre facultatif le nom de la colonne.

#### Afficher la dernière ligne du tableau

```
    total = len(tableau)
    tableau.loc[total - 1]
```

> [!NOTE]
> La variable intermédiaire `total` est facultative. Elle n'est utilisée que de manière pédagogique. On peut directement écrire : `tableau.loc[len(tableau) - 1]`.

#### Afficher une colonne

```
    colonne_a_afficher = tableau.columns[0]
    tableau[colonne_a_afficher].head()
```

### Modifier un tableau  `Pandas`

#### Sélection des colonnes

Pour sélectionner des colonnes, on crée une liste `colonnes` avec les noms des colonnes, puis on tape :

```
    tableau = tableau[colonnes]
```

#### Manipuler l'index

Il existe une méthode dédiée `set_index()` permettant de définir qu'une des colonnes du tableau soit son index. L'intérêt est de pouvoir sélectionner les lignes en fonction des valeurs de cette colonne.

```
    tableau = tableau.set_index(colonne)
```

La méthode `set_index(...)` prend en paramètre le nom de la colonne.

> [!WARNING]
> La méthode `set_index(...)` ne modifie pas l'objet original, mais elle renvoie une copie modifiée. Il faut stocker ces informations dans une nouvelle variable.

#### Renommer les colonnes

```
    tableau.columns = ["nom de la colonne 1", "nom de la colonne 2", ...]
```

#### Créer une nouvelle colonne

```
    tableau = ["nom de la colonne"] = None
```

La commande crée une colonne vide, mais il est possible de créer une colonne ne contenant que des zéros.

```
    tableau = ["nom de la colonne"] = 0
```

#### Modifier une case du tableau

```
    tableau = ["nom de la ligne", "nom de la colonne"] = nouvelle valeur
```

#### Supprimer des lignes ou des colonnes

```
    tableau = tableau.drop("nom de la ligne", axis = 0)
```

ou

```
    tableau = tableau.drop("nom de la colonne", axis = 1)
```

#### Répéter une opération sur un tableau

On peut utiliser `apply`.

```
    recodage = tableau["nom de la colonne"].apply(recodage_population)
    tableau["nom de la colonne"] = recodage
```

On peut utiliser dans `apply` :

- `axis = 0`

- `axis = 1`

On peut utiliser des fonctions anonymes dans `apply`.

#### Parcourir un tableau ligne par ligne

```
    for i in tableau.head().iterrows():
        ...
```

#### Gérer les valeurs manquantes

Il existe deux méthodes :

- `dropna()` qui permet de supprimer des lignes avec des valeurs absentes ;

- `fillna(...)` qui permet de traiter les données absentes.

La méthode `replace(dictionnaire)` utilise un dictionnaire.

```
    {"valeur à remplacer": "valeur nouvelle"}
    tableau.replace(dictionnaire)
```

### Filtrer des informations

```
    filtre = tableau["nom de la colonne"] > 10000
    echantillon = tableau[filtre]
```

Voici quelques méthodes filtrantes :

- `isin()` ;

- `str.contains()`;

- `isnull()` ;

- `where()` ;

- `mask()`.


### Relier des informations de tableaux différents

Il est possible de passer par un dictionnaire en utilisant la fonction ``dict(...)`.

Il est possible de joindre des tableaux en utilisant la fonction `join(...)`.

### Créer un tableau `Pandas`

Pour créer un tableau dans `Pandas`, on utilise `Series`.

```
    valeur = pd.Series([..., ...], [..., ...], ..., columns = ["titre1", "titre2"])    
```

### Sauvegarder ses données

Les méthodes possibles sont :

- `to_excel(...)` pour convertir en `*.xls` ;

- `to_csv(...)` pour convertir en `*.csv`.

Par exemple

```
    valeur.to_excel("./fichier.xls")    
```

Il est possible de créer un fichier par ligne de données.

```
    for i, ligne in tableau.head().iterrows():
        with open("./fichier.csv" + i, "w") as file
            file.write(str(dict(ligne)))    
```

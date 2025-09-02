# Analyse de corpus textuel avec `Python`

## Traiter des textes pour en dégager de l'information

Le traitement des textes permet de répondre à quatre questions.

1. Les textes sont-ils similaires ou différents ?

2. De quoi parlent les textes ?

3. Quels sont les thèmes présents dans les textes ?

4. Quelles sont les entités nommées ?

Il existe quatre étapes pour réaliser ce traitement :

1. constituer un corpus ;

2. mettre en forme le texte en unités de base ;

3. sélectionner les éléments pertinents ;

4. appliquer un traitement statistique.

### Constituer un corpus

On utilise la bibliothèque `Wikipedia`.  faire des recherches sur Wikipédia, ici sur le mot « cancer ».

```
    import wikipedia as wp
    wp.set_lang("fr")
    pages = wp.search("cancer", results = 100)
    pages[0:8]
    corpus = []
    for i in pages[0:8]:
        p = wp.page(i)
        corpus.append([i, p.content])
    corpus = pd.DataFrame(corpus, columns = ["page", "contenu"])
    corpus.to_csv("./corpus_cancer_wiki.csv")
```

- La méthode `page()` permet de récupérer une page Wikipédia.

### Décomposer les textes en mots

[Analyse des textes](http://www.iramuteq.org)

```
    import nltk
    texte = corpus.loc[0, "contenu"]
    texte_tokenise = nlth.word_tokenize(texte)
    print(texte_tokenise[0:10])
```

1. Lemmatiser les mots décomposés, c'est-à-dire réduire les mots à leur racine

```
    from nltk.stem.snowball import FrenchStemmer
    stemmer = FrenchStemmer()
    texte_lemmatise = [stemmer.stem(m) for m in texte_tokenise]
    print(texte_lemmatise[0:10])
```

2. Repérer les éléments de ponctuation

```
    import pandas as pd
    from nltk.corpus import stopwords
    from string import punctuation
    stop_words = stopwords.word('french') + list(punctuation)
    texte_lemmatise_filtre = [i for i in texte_lemmatise if i not in stop_words]
    print(texte_lemmatise_filtre[0:5])
    pd.Series(texte_lemmatise_filtre).value_counts()[0:10]
```

3. Appliquer le modèle *Term Frequency-Inverse Document Frequency* (`td-idf`)

- soit en utilisant la bibliothèque `gemsim` avec ses objets `TfidModel`, `Dictionray` et `Phrases` ;

- soit en utilisant la bibliothèque `Spacy`.

### Créer un nuage de mots

Pour créer un nuage de mots, on utilise la bibliothèque `WordCloud`.

```
    from wordcloud import WordCloud
    texte = [" ".join(i) for i in corpus['contenu_lem'].values]
    texte = " ".join(texte)
    wordcloud = WordCloud(background_color = "white", max_words = 5000, contour_width = 3)
    wordcloud.generate(texte)
    wordcloud.to_image()
    wordcloud.to_file("nuage.png")
```

### Analyser les thèmes d'un corpus

Le modèle *Latent Dirichlet Allocation* (L.D.A.) cherche à identifier des thématiques dans un texte sur la base d'associations statistiques, identifiées sur la base de la proximité des mots.

Une fois le modèle obtenu sur un corpus, il est possible de calculer à quelles thématiques appartient un texte donné.

Un thème est un ensemble de mots-clés caractéristiques.

La qualité de l'analyse va dépendre de :

1. la nature et la taille du corpus ;

2. le travail en amont de nettoyage du corpus ;

3. le type de modèle ;

4. les paramètres de ce modèle.

```
    from gensim.corpora import Dictionary
    from gensim.models.phrases import Phrases, Phraser
    from gensim.models.ldamodel import LdaModel
    #Générer les bigrams
    phrases = Phrases(list(corpus["contenu_lem"]), min_count = 1, threshold = 1)
    phraser = Phraser(phrases)
    corpus["contenu_lem_bi"] = corpus["contenu_lem"] \ .apply(lambda x:  phraser[x])
    #Création du corpus
    dictionary = Dictionary(corpus["contenu_lem_bi"])
    corpus_convert = [dictionary.doc2bow(line) for line in list(corpus["contenu_lem_bi"])]
    #Modélisation
    lda_model = LdaModel(corpus = corpus_convert, id2word = dictionary, num_topics = 5, random_state = 100, update_every = 1, chunksize = 100, passes = 10, alpha = 'auto', per_word_topics = True)
    #Affichage
    categories = lda_model.print_topics()
    print(categories[0])
```

La bibliothèque `pyLDAvis` est un outil de visualisation graphique des thèmes L.D.A.

## [Analyser un réseau de mots](./PYTHON-ANALYSE-DE-RESEAUX.md)

# L'information relationnelle dans les réseaux

Les types de réseaux possibles sont très variés :

- les réseaux sociaux ;

- les réseaux de mots ;

- les réseaux de transports.

## Voir et mesurer les relations

Les traitements possibles sont :

1. l'identification des entités centrales et des entités plus marginales ;

2. le calcul des distances sur le réseau ;

3. la détermination des communautés ;

4. la visualisation des relations et des proximités.

## Construire un réseau

On utilise la bibliothèque `Networkx`. Pour la tester, on utilise les données Wikipédia sur le mot « cancer » (cf. [Analyse de corpus textuel](./PYTHON-ANALYSE-DE-CORPUS-TEXTUEL.md)).

```
    corpus = []
    for i in pages[0:8]:
        p = wp.page(i)
        corpus.append([i, p.links])
    print("Nombre de pages : {}".format(len(corpus)))
    for i in corpus:
        print("La page {} a {} liens.".format(i[0], len(i[1])))
    
    import networkx as nx
    #Définition d'un réseau
    G = nx.Graph()
    #Boucle sur nos données
    for p in corpus:
        p_ini = p[0]
        #Ajouter la page ou augmenter son poids
        if not p_ni in G:
            G.add_node(p_ini, size = 1)
        else:
            G.nodes[p_ini]["size"] += 1
        #Faire une boucle sur les liens
        for p_ext in p[1]:
            #Ajouter la page du lien ou augmenter son poids
            if not p_ext in G:
                G.add_node(p_ext, size = 1)
            else:
                G.nodes[p_ext]["size"] += 1
            #Ajouter le lien ou augmenter son poids
            if G.has_edge(p_ini, p_ext):
                G[p_ini][p_ext]["weight"] += 1
            else:
                G.add_edge(p_ini, p_ext, weight = 1)
    print("{} nœuds et {} liens".format(G.number_of_nodes(), G.nuumber_of_edges()))
```

- L'attribut `p.links` récupère le lien des pages.

## Établir des statistiques pour les réseaux

Les mesures possibles sont :

- le degré des nœuds ;

- la densité ;

- le diamètre.

```
    import networkx as nx
    densite = nx.density(G)
    diametre = nx.diameter(G)
    hist = nx.degree_historgram(G)
```

On peut afficher le résultat.

```
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (10, 5))
    ax.bar(range(0, len(hist[0:10])), hist[0:10])
    plt.title("Distribution des degrés d'un réseau : ")
    plt.subplots_adjust(left = 0.3, right = 0.7, top = 0.7, bottom = 0.3)
```

## Visualiser un réseau

La bibliothèque `Networkx` possède un ensemble de fonctions pour produire les visualisations, mais elles ne sont adaptées que pour les petits réseaux.

```
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (5, 5))
    nx.draw(G_filtre, pos = nx.spring_layout(G_filtre), node_size = 15, width = 0.1, alpha = 0.5)
```

> [!NOTE]
> On peut appeler plus loin dans l'analyse avec le logiciel `Gephi` qui est dédié à l'analyse des réseaux en sortant le résultat obtenu dans le format de logiciel :
> `nx.write_graphml(G_filtre, "mon_reseau.graphml")`

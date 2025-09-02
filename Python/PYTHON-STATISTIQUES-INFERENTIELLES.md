# Statistiques inférentielles avec `Python`

Les statistiques inférentielles cherchent à établir la **significativité statistique**.

## Générer des données aléatoires

```
    import random
    random.randint(min, max)
    random.random()
    random.choice(liste)
    random.normalvariate(moyenne, écart type)    
```

- `random.randint(min, max)` génère un nombre entier aléatoire entre la valeur minimale `min` et la valeur maximale `max`.

- `random.random()` génère un nombre réel aléatoire entre 0 et 1.

- `random.choice(liste)` choisit un élément de la liste tiré aléatoirement.

- `random.normalvariate(moyenne, écart type)` génère un nombre aléatoire en suivant une distribution normale avec la moyenne et l'écart type indiqués.

## Calculer un intervalle de confiance

1. Calculer la moyenne et l'écart type avec d'une liste afin de fixer un intervalle de confiance de type : moyenne $\pm$ écart type :

```
   moyenne =  donnees["nom"].mean()
   ecartype =  donnees["nom"].std()
```

2. Calculer un intervalle de confiance avec la distribution normale

```
   from scipy.stats import normaltest
   test = normaltest(donnees["nom"].dropna()) 
```

Le calcul de la $p$-valeur du test est : `test[1]`.

3. Sélectionner aléatoirement un échantillon d'un tableau `Pandas` en indiquant la proportion par rapport à la taille totale

```
    echantillon = donnees["nom"].sample(frac=0.01)
    moyenne = echantillon.mean()
    ecarttype = echantillon.std()
```

4. Calculer un intervalle de confiance avec l'ereur standard `sem`

```
    from scipy.stats import sem, norm
    moyenne = echantillon.mean()
    erreur = sem(echantillon)
    intervalle = norm.interval(0.95, loc = moyenne, scale = erreur)
```

- `0.95` signifique que l'on opère à tester à 95 %.

- `intervalle[0]` correspond à l'intervalle minimal.

- `intervalle[1]` correspond à l'intervalle maximal.

## Calculer la significativité d'un tableau croisé avec le ${\chi}^2$

```
    from scipy.stats import chi2_contingency
    tableau_croise = pd.crosstab(donnees["nom 1"]), donnees["nom2"])
    chi2 = chi2_contingency(tableau_croise)
```

- `chi2[0]` correspond à la valeur minimale du ${\chi}^2$

- `chi2[1]` correspond à la valeur maximale du ${\chi}^2$

## Calculer le $V$ de Cramér entre deux variables qualitatives

Cette méthode ne fonctionne que pour les tableaux croisés ayant des valeurs comprises entre 0 et 1.

```
    import researchpy
    tableau = researchpy.crosstab(donnees["nom 1"], donnees["nom 2"], test = "chi_square")
```

`tableau[1]` correspond au calcul du $V$ de Cramér.

## Établir les différences entre deux groupes

### Le test de comparaison de moyenne (test de Student)

```
    from scipy.stats import ttest_ind
    mediane = donnees["nom"].median()
    pv = donnees[donnees["nom"] < mediane]["nom 2"].dropna()
    gv = donnees[donnees["nom"] >= mediane]["nom 2"].dropna()
    test = ttest_ind(pv, gv)
```

- `pv.mean()` est la moyenne du groupe 1.

- `gv.mean()` est la moyenne du groupe 2.

- `ttest_ind(pv, gv)` est la $p$-valeur du test de Student.

### Le test de Fisher et la méthode ANOVA

```
    from scipy.stats import f_oneway
    Q1 = échantillon 1
    Q2 = échantillon 2
    Q3 = échantillon 3
    Q4 = échantillon 4
    Q1.mean()
    Q2.mean()
    Q3.mean()
    Q4.mean()
    f_oneway(Q1, Q2, Q3, Q4)
```

`f_oneway(Q1, Q2, Q3, Q4)` fournit la $p$-valeur du test de Fisher.

### Le test de rang-somme de Wilcoxon

Le test de rang-somme de Wilcoxon vérifie si les deux échantillons de données provenant de la même distribution.

```
    from scip.stats import ranksums
    Q1 = échantillon 1
    Q2 = échantillon 2
    test = ranksums(Q1, Q2)
```

`test[1]` fournit la $p$-valeur du test de Wilcoxon.

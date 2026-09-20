#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def tableauDeContingence(nom, donnees):
    indexValeurs = {}
    for element in range(0,len(nom)):
        indexValeurs.update({element: nom[element]})
    return pd.DataFrame(donnees).rename(index = indexValeurs)

def sommeDesColonnes(tableau):
    colonne = list(tableau.head(0))
    sommeColonne = []
    for element in colonne:
        sommeColonne.append(tableau[element].sum())
    return sommeColonne

def sommeDesLignes(tableau):
    colonne = list(tableau.head(0))
    sommeLigne = []
    for element1 in range(0,len(tableau)):
        ligne = []
        for element2 in range(0,len(colonne)):
            ligne.append(tableau.iloc[element1, element2])
        sommeLigne.append(np.sum(list(ligne)))
    return sommeLigne

data = pd.DataFrame(ouvrirUnFichier("./data/France-Granulats-2006-2020-par-region.csv"))
# print(data)

# Création du tableau de contingence
# Contrairement à l'usage, vous ne devez pas créer de tableau croisé dynamique, puisque le fichier est déjà un tableau de contingence
tableauDeContingence = tableauDeContingence(data["Région"], {"2006": data["2006"], "2007": data["2007"], "2008": data["2008"], "2009": data["2009"], "2010": data["2010"], "2011": data["2011"], "2012": data["2012"], "2013": data["2013"], "2014": data["2014"], "2015": data["2015"], "2016": data["2016"], "2017": data["2017"], "2018": data["2018"], "2019": data["2019"], "2020": data["2020"]})
print(tableauDeContingence)

# Question 1
print("Question 1")
# Calculer les marges

# Question 2
print("Question 2")

# Question 3
print("Question 3")
# Faire le test du chi2 avec les outils Scipy.stats

# Question 4

# Question bonus
print("Question bonus")

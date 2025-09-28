#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
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

data = pd.DataFrame(ouvrirUnFichier("./data/Socioprofessionnelle-vs-sexe.csv"))
#print(data)

#Création du tableau de contingence
#Contrairement à l'usage, vous ne devez pas créer de tableau croisé dynamique, puisque le fichier est déjà un tableau de contingence
tableauDeContingence = tableauDeContingence(data["Catégorie"], {"Femmes": data["Femmes"], "Hommes": data["Hommes"]})
print(tableauDeContingence)

#Calculer les marges
print("Calcul des marges")


#Faire le test du chi2 avec les outils Scipy.stats
print("Test du chi2")


#Calculer l'intensité de liaison phi2 de Pearson
print("Intensité de liaison phi2")


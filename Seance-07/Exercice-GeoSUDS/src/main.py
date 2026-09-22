#coding:utf8
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

data = pd.DataFrame(ouvrirUnFichier("./data/Afrique-Scolarisation.csv"))
# print(data)

# "Country Name" : Nom du territoire
# "Country Code" : Code ISO du territoire
# "Continent" : Nom du continent
# "SE.PRM.ENRL" : Nombre d'enfants en primaire
# "SE.PRM.UNE" : Nombre d'enfants en secondaire
# "SE.SEC.ENRL" : Nombre d'enfants non scolarisés en primaire

# Nettoyage des données des valeurs NaN
nomdescolonnes = ["Country Name","SE.PRM.ENRL","SE.SEC.ENRL","SE.PRM.UNE"]
nomterritoire = list(data["Country Name"])
primaire = list(data["SE.PRM.ENRL"])
secondaire = list(data["SE.SEC.ENRL"])
nonscolarise = list(data["SE.PRM.UNE"])
nomterritoire2 = []
primaire2 = []
secondaire2 = []
nonscolarise2 = []
for element in range(0,len(nomterritoire)):
    if np.isnan(primaire[element]) == False and np.isnan(secondaire[element]) == False and np.isnan(nonscolarise[element]) == False:
        nomterritoire2.append(nomterritoire[element])
        primaire2.append(primaire[element])
        secondaire2.append(secondaire[element])
        nonscolarise2.append(nonscolarise[element])
tableau = [nomterritoire2,primaire2,secondaire2,nonscolarise2]

# Création du tableau de contingence
# Contrairement à l'usage, vous ne devez pas créer de tableau croisé dynamique, puisque le fichier est déjà un tableau de contingence
dictionnaire = {}
for element in range(1, len(nomdescolonnes)):
    dictionnaire[nomdescolonnes[element]] = tableau[element]
tableauDeContingence = tableauDeContingence(data[nomdescolonnes[0]], dictionnaire)
# print(tableauDeContingence)

# Question 1
print("Question 1")
# Calculer les marges

# Question 2
print("Question 2")

# Question 3
print("Question 3")
# Faire le test du chi2 avec les outils Scipy.stats

# Question 4
print("Question 4")
# Calculer l'intensité de liaison phi2 de Pearson

# Question bonus
print("Question bonus")

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

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
data = pd.DataFrame(ouvrirUnFichier("./data/resultats-elections-presidentielles-2022-1er-tour.csv"))
# print(data)

# "Code_du_département"
# "Libellé_du_département"
# "Inscrits"
# "Abstentions"
# "Votants"
# "Blancs"
# "Nuls"
# "Exprimés"
# "Nathalie_ARTHAUD"
# "Fabien_ROUSSEL"
# "Emmanuel_MACRON"
# "Jean_LASSALLE"
# "Marine_LE_PEN"
# "Éric_ZEMMOUR"
# "Jean_Luc_MÉLENCHON"
# "Anne_HIDALGO"
# "Yannick_JADOT"
# "Valérie_PÉCRESSE"
# "Philippe_POUTOU"
# "Nicolas_DUPONT_AIGNAN"

# Création du tableau de contingence
# Contrairement à l'usage, vous ne devez pas créer de tableau croisé dynamique, puisque le fichier est déjà un tableau de contingence
nomdescolonnes = ["Libellé_du_département", "Nathalie_ARTHAUD", "Fabien_ROUSSEL", "Emmanuel_MACRON", "Jean_LASSALLE", "Marine_LE_PEN", "Éric_ZEMMOUR", "Jean_Luc_MÉLENCHON", "Anne_HIDALGO", "Yannick_JADOT", "Valérie_PÉCRESSE", "Philippe_POUTOU", "Nicolas_DUPONT_AIGNAN"]
# print(nomdescolonnes)
dictionnaire = {}
for element in range(1, len(nomdescolonnes)):
    dictionnaire[nomdescolonnes[element]] = data[nomdescolonnes[element]]
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

# Question bonus
print("Question bonus")

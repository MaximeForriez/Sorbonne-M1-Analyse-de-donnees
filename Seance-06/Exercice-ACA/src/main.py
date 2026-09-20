#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1
print("Question 1")

# "Année" : Année, ici 2024
# "Code-ISO" : code ISO du territoire
# "Total-export-alimentaire-USD" : total des exportations concernant les produits alimentaires
# "Total-import-alimentaire-USD" : total des importations concernant les produits alimentaires
# "Total-export-autres-USD" : total des exportations concernant les produits non alimentaires
# "Total-import-autres-USD" : total des importations concernant les produits non alimentaires
# "Total-export-USD" : total des exportations
# "Total-import-USD" : total des importations

# Question 2
print("Question 2")
# Calcul de la régression linéaire pour la méthode des moindres carrées 1
# Calcul de la droite de régression 1
# Calcul de la régression linéaire pour la méthode des moindres carrées 2
# Calcul de la droite de régression 2
# Calcul de la régression linéaire pour la méthode des moindres carrées 3
# Calcul de la droite de régression 3

# Question 3
print("Question 3")
# Calcul du coefficient de corrélation 1
# Calcul du coefficient de corrélation 2
# Calcul du coefficient de corrélation 3

# Question 4
print("Question 4")
# Calcul du graphique 1
# Calcul du graphique 2
# Calcul du graphique 3

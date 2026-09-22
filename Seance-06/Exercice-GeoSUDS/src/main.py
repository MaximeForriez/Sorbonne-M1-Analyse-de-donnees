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

# "year" : année
# "origin_id" : code ISO du territoire d'origine
# "export_val" : exportations en USD
# "import_val" : importations en USD
# "export_ton" : exportations en tonnes
# "import_ton" : importations en tonnes

# Question 2
print("Question 2")
# Calcul de la régression linéaire pour la méthode des moindres carrées 1

# Calcul de la droite de régression 1

# Calcul de la régression linéaire pour la méthode des moindres carrées 2

# Calcul de la droite de régression 2

# Question 3
print("Question 3")
# Calcul du coefficient de corrélation 1

# Calcul du coefficient de corrélation 2

# Question 4
print("Question 4")
# Calcul du graphique 1

# Calcul du graphique 2

# Question bonus
print("Question Bonus")

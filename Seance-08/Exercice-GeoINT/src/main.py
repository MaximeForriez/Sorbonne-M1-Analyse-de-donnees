#coding:utf8

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import scipy
import scipy.stats
import prince
import matplotlib.pyplot as plt

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1
print("Question 1 : Analyse en composantes principales")
# Analyse en composantes principales
# Question 1b
print("Question 1b")

# "Code ISO" : code ISO du territoire
# "Country" : territory name
# "État" : nom du territoire
# "Continent" : Continent
# "1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025" : 77 colonnes des différentes années

# Centrer-réduire
# Question 1c
print("Question 1c")
# Remplacement des NaN par 0
# ACP
# Question 1d
print("Question 1d")
# Affichage de l'A.C.P.
# Variance expliquée
# Question 1e
print("Question 1e")
# print(pca.explained_variance_)
# Variance expliquée en pourcentage
# Calcul des valeurs propres

# Question 1f
print("Question 1f")
# Coordonnées des individus
# Question 1g
print("Question 1g")

# Visualisation des individus

# Contribution des individus
# Question 1h
print("Question 1h")

# Qualité de représentation (cosinus carré) des individus

# Coordonnées des variables : cercle de corrélation
# Question 1i
print("Question 1i")
# Racine carrée des valeurs propres
# Matrice vide pour avoir les coordonnées
# Création d'un DataFrame
# Visualisation du cercle de corrélation

# Question 2
print("Question 2 : Analyse factorielle de correspondances multiples")
# Analyse factorielle de correspondances multiples
# Question 2a

# Question 2b

# Question 2c
print("Question 2c")
# Calcul du tableau disjonctif complet

# Question 2d
print("Question 2d")

# Question 2e
print("Question 2e")
# Calcul des valeurs propres

# Question 2f
print("Question 2f")
# Coordonnées des lignes et des colonnes

# Question 2g
print("Question 2g")
# Visualiser les deux premiers facteurs

# Question 2h
print("Question 2h")
# Calculer la contribution de l'A.C.M. avec `Prince` des lignes

# Calculer la contribution de l'A.C.M. avec `Prince` des colonnes

# Question bonus
print("Question bonus")

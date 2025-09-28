#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

data = pd.DataFrame(ouvrirUnFichier("./data/pib-vs-energie.csv"))
#print(data)

#Visualisation des données
print("Visualisation des données")
#Pour résoudre le problème posé dans la question 1, il faut utiliser l'opérateur NaN avec la méthode qui le teste issue de la bibliothèque Numpy dans une boucle.



#Calcul de la régression linéaire pour la méthode des moindres carrées
print("Calcul de la régression linéaire pour la méthode des moindres carrées")



#Calcul du coefficient de corrélation simple de Pearson
print("Calcul du coefficient de corrélation simple de Pearson")



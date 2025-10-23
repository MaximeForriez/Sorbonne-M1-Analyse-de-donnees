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
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Analyse en composantes principales
temperature =ouvrirUnFichier("./data/france-temperatures.csv")



#Analyse factorielle de correspondances multiples
chien = ouvrirUnFichier("./data/chiens.csv")



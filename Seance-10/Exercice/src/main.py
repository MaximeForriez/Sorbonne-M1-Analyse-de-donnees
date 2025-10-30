#coding:utf8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
import scipy
import scipy.stats
import math

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Partie sur les températures
temperature = ouvrirUnFichier("./data/temperature.csv")

#Partie sur le géomarketing
geomarketing = ouvrirUnFichier("./data/geomarketing.csv")

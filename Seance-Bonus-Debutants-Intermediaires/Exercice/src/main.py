#coding:utf8

import pandas as pd
import requests

#Consulter : https://rtavenar.github.io/poly_python/content/api.html
#Autres A.P.I. : https://www.data.gouv.fr/dataservices/search

def geturl(method, format, stations, start, end, token):
    stationstexte = ""
    for element in stations:
        stationstexte = stationstexte + "&stations[]={}".format(element)
    return "https://www.infoclimat.fr/opendata/?version=2&method={}&format={}{}&start={}&end={}&token={}".format(method, format, stationstexte, start, end, token)

def testConnexion(reponse):
    if str(reponse) == "<Response [200]>":
        data = str(reponse.text)
        data = data.split("\n")#La fonction crée une liste des lignes à partir des sauts de ligne.
        data2 = []
        for element in data:
            data2.append(element.split(";"))#La fonction crée les colonnes lorsqu'elles existent pour chacune des lignes identifiées.
        return data2
    else:
        return "Erreur de connexion : {}".format(str(reponse))
    
method = "get"#méthode de l'A.P.I. Rest
format = ""#format des données
stations = [""]#codes des données
start = ""#format : année-mois-jour
end = ""#format : année-mois-jour
token = ""#votre token

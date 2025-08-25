#coding:utf8

#Exemple d'affichage (sortie)
print("Bonjour tout le monde !")

#Syntaxe de base
#-Chaîne de caractères : '', "", """, '''
#-Commentaires #

#Variable
#-Déclaration et affectation
nom = "Forriez"
print(nom)
#-Déclaration et affectation d'une constante
PI = 3.1416
print(PI)
#-Réaffectation
nom = "Toto"
print(nom)
#-Réaffectation avec la même variable
nb = 1
nb = nb + 1
print(nb)

#Entrée-Sortie + Exemple de concaténation
age = input("Quel est votre âge ? ")
age = int(age)
print("Tu as {} ans.".format(age))

#Opérateurs
#-Opérateur d'affectation  =
#-Opérateurs arithmétiques
print(1 + 1)
print(4 - 6)
print(3 * 5)
print(3 / 5)
print(5 % 2)

print(3 ** 2)
#-Opérateurs d'affectation
var = 1
var += 1
print(var)
var = 4
var -= 6
print(var)
var = 3 
var *= 5
print(var)
var = 3 
var /= 5
print(var)
var = 5
var %= 2
print(var)
#-Opérateurs de comparaison
# == != < > <= >=

#-Opérateurs logiques
# and / or / in / not in / 

#Condition
age = 15
AGE_LEGAL = 18
if age < AGE_LEGAL:
#if 0 < age < AGE_LEGAL:
#if age >= 0 and age < AGE_LEGAL:
	print("Accès refusé")
#elif :
else:
	print("Accès autorisé")

AGE_MAXIMUM = 130
if age <= 0:
	print("Votre âge ne peut pas être négatif. Vous avez écrit n'importe quoi !")
elif age >= AGE_MAXIMUM:
	print("Soit vous êtes un vénérable ancien ! Soit vous avez écrit n'importe !")
elif 0 < age < AGE_LEGAL:
	print("Accès refusé")
else:
	print("Accès autorisé")	

#Boucles
compteur = 0
while compteur < 5:
	print(compteur)
	compteur += 1


for element in "A", "B", "C":
	print(element)

for element in range(1, 10, 1):
	if element == 5:
		continue;
#		break;
	print(element)

#Fonctions
#-Fonctions natives comme print(), input(), int(), float(), str(), bool(), etc.
#-Fonctions créées -> une fonction = une tâche
def direBonjour(nom):
	print("Bonjour {}".format(nom))

prenom = input("Quel est votre prénom ? ")
prenom = str(prenom)

#Appel de la fonction
direBonjour(prenom)

def direBonjour2(nom = "Maxime"):
	print("Bonjour {}".format(nom))

prenom = input("Quel est votre prénom ? ")
direBonjour2()

def direBonjour3(nom = "Maxime"):
	return "Bonjour {}".format(nom)

prenom = input("Quel est votre prénom ? ")
print(direBonjour3(str(prenom)))

def calculerSomme(nombre1, nombre2):
	return nombre1 + nombre2

print(calculerSomme(1, 2))

#Modularité dans Python
#-Module Python = une bibliothèque (library)

import math
print(math.sqrt(2))

#-Un module est un fichier *.py
#1 Créer et écrire dans un fichier toto.py
def test():
	print("Bonjour ! Test réussi !")

#2 Dans main.py, taper :
from toto import test
test()

#Chaîne de caractères
nom = "forriez"
print(len(nom))
print(nom[1])
print(nom.upper())
print(nom.lower())
print(nom.capitalize())
print("Maxime " + nom)
#...

#Listes
#-Création d'une liste
liste1 = list
liste2 =[]
liste3 = [1, 3, 15]
liste4 = [0]*10
liste5 = range(20)
print(liste1)
print(liste2)
print(liste3)
print(liste4)
print(liste5)

#-Afficher un élément 
print(liste5[0])
print(liste5[15])
print(liste5[-1])
print(liste5[:2])
print(liste5[3:])
print(liste5[9:12])

#-Parcourir une liste
i = 0
while i < len(liste5):
	print(liste5[i])
	i += 1

for element in liste3:
	print(element)

#-Modifier un élément
print(liste3[1])
liste3[1] = 100000
print(liste3[1])
liste3[1] = 3

#-Les listes sont des objets qui disposent de plein de méthodes
liste3.append(100)
for element in liste3:
    print(element)

# insert, pop, remove, index, sort, reverse, count, clear, extend, etc.
	
#-Copier une liste
#--L'erreur courante
liste6 = liste3
print(liste6)
liste3.append(9)
print(liste6)
print(liste3)

#--La solution
import copy
liste6 = copy.deepcopy(liste3)
print(liste6)
liste6.append(7)
print(liste6)
print(liste3)

for objet in enumerate(liste6):
	print(objet)

#Test du module créé et de la condition de fin de fichier
# Ce test nécessite le fichier module.py
import module
	
module.module()
module.module2()

#Les tuples
#-Tuple = séquence immuable

#-Création
tuple = ()
tuple = (45,0)
tuple = 45,
tuple = (4,6)

#-Lire les données
print(tuple[0])

#Les dictionnaires
#-Liste avec des clés

#-Création
dictionnaire = {}
dictionnaire = {1:145, "prenom":"Maxime"}

#1 et "prenom" sont des clés, tandis que 145 et "Maxime" sont des valeurs associées aux clés.

#-Lire un élement
print(dictionnaire[1])
print(dictionnaire)
print(dictionnaire["prenom"])
print(dictionnaire)

#-Parcourir un dictionnaire
for cle in dictionnaire.keys():
	print(cle)

for valeur in dictionnaire.values():
	print(valeur)
	
for cle, valeur in dictionnaire.items():
	print(cle, " ", valeur)

#-Modifier une valeur
dictionnaire["prenom"]="Sophie"
print(dictionnaire["prenom"])

#-Les dictionnaires sont des objets possédant plein de méthodes : pop, 

#-Copier un dictionnaire
dictionnaire2 = dictionnaire.copy()
dictionnaire2["prenom"]="Maxime"
print(dictionnaire2)

#-Astuce pour les tuples et les dictionnaires
def fonction(*tuple):
  return tuple

print(fonction(1, 2, 3))

def fonction2(**dictionnaire):
  return dictionnaire

print(fonction2(prenom="Max" , nom="Forriez"))

# Introduction au langage de programmation `Python`

Pourquoi apprendre `Python` ? Pour beaucoup, `Python` sera l'`Excel` de demain, c'est-à-dire il sera plus judicieux d'opérer des traitements avec `Python` qu'`Excel`. C'est normal, la société évolue, et `Excel` est inapproprié pour opérer un traitement automatique performant, surtout lorsque la masse et les sources de données sont très importantes, or nous  sommes dans un monde de données massives. Le tableur n'est plus le meilleur outil pour tenir un tableau de bord par exemple.

## Documentation

Cette série de T.D. ne peut que vous donner un bref aperçu du langage de programmation `Python`. Vous allez apprendre les rudiments de la version 3[^1]. L'objectif est d'en acquérir les bases. Tout au long des séances, vous serez confrontés à des problèmes. Typiquement, un code qui ne marche pas, il faudra apprendre à résoudre par vous-mêmes les problèmes. Pour ce, la [documentation officielle](https://docs.python.org/3/) du langage doit devenir votre meilleure amie. De nombreuses documentations sont en français, mais, pour toutes les nouvelles technologies, il faut savoir lire l'anglais technique.

- [`Python` *Cheat Sheets*](https://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf) (Universite de Compiègne)

- [Association francophone du `Python`](https://www.afpy.org/)

Par ailleurs, les tutoriels sur `Youtube` sont très nombreux en français.

- [Formation vidéo - Cours](https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC)

- [Formation vidéo - Tutoriels](https://www.youtube.com/watch?v=a5HGF_ELI1E&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8)

- [Formation vidéo - Exercices](https://www.youtube.com/watch?v=HVN4qv6Dxdk&list=PLrSOXFDHBtfEiSgOG1FM4oq-yS24iV4s1)

- *etc*.

> [!TIP]
> Une version comprend trois nombres séparés par un point : $x$.$y$.$z$.
> - $x$ est le numéro de la version majeure.
> - $y$ est le numéro de la version mineure.
> - $z$ est le numéro de la version micro.

## Vocabulaire de base

- **Programme** : ensemble structuré réalisant des tâches beaucoup plus ciblées qu'un script

- **Programmer** : écrire une série d'instructions à un ordinateur dans le but qu'il exécute une tâche

- **Script** : ensemble de commandes organisant une action de l'ordinateur

## Position du cours par rapport au langage `Python`

« Un préjugé récurrent voudrait que les S.H.S. se montrent méfiantes à l'égard de nouveautés technologiques et, à ce titre, se tiennent à distance des évolutions informatiques. Non seulement ce préjugé est faux, en témoignant les traditions poussées d'analyse statistique en sciences sociales ou l'usage des historiens et des archéologues des bases de données, mais a pour conséquence de limiter l'appropriation de ces outils » (Schutz & Bussonnier, 2020, p. III). Avec ce cours d'analyse de données, c'est l'occasion pour vous, si vous vous reconnaissez dans cette citation, de pouvoir découvrir et apprendre les outils informatiques indispensables de nos jours. L'objectif de ce cours n'est pas d'être exhaustif. Il s'agit de vous donner les bases dans un contexte précis, ici l'analyse de données géographiques, afin que vous puissez effectuer vos analyses de données sereinement.

Vous allez apprendre à programmer pour produire des analyses géographiques. Quelles sont les conséquences de cette apprentissage dans la manière d'étudier ou de faire de la géographie.

1. Développer votre pensée abstraite

2. Apprendre à décomposer des problèmes

3. Encourager votre créativité pour résoudre des problèmes

4. Acquérir une compétence professsionnelle utile tout au long de votre vie

5. Renforcer votre confiance en vous

6. Favoriser la rencontre entre technologie et votre esprit critique

7. Vous amuser

Pourquoi le `Python` ?

1. C'est le langage le plus demandée par les organisations (avec le `Java`)

	- Source : [Tiobe](https://www.tiobe.com/tiobe-index)

2. C'est un langage intuitif, donc facile  à apprendre.

	- Cela étant, le langage donne de mauvaises habitudes de programmation, car elles ne sont pas universelles. Il faut sans arrêter se documenter.

Le cours de `Python`, comme celui de statistiques, est **progressif**. Avant de consulter les modules et les *framework*, il faut maîtriser les bases du langage, c'est ce que propose cette page.

Le but d'associer géographie, `Python` et statistiques est de vous faire acquérir des réflexes :

1. pour traiter vos données ;

2. dans l'analyse statistique de vos données ;

3. dans le choix de vos routines d'analyse statistique ;

4. dans l'analyse critique de vos données et de vos résultats.

> [!WARNING]
> Le langage `Python` évolue très vite. Il est possible que certains modules ou *framework* deviennent rapidement obsolètes.

Pourquoi un géographe doit-il consacrer du temps à l'apprentissage de la programmation ?

1. Réaliser automatiquement des traitements courants

	- Exemple : recoder des données

2. Réaliser des tâches avec une nouvelle stratégie

	- Exemple : collecter des données en ligne (*scrapping* ou autres téléchargements automatiques)

Quelles sont les raisons poussant les géographes à programmer ?

1. L'inadaptation à vos besoins des solutions existantes

2. L'inexistence du bon format (celui dont vous avez besoin) dans les données disponibles

3. L'inexistence des données, sauf si on les reconstitue avec d'autres données

4. L'inexistence de logiciels économiquement abordables (chéreté des licences)

5. La nécessité d'utiliser plusieurs logiciels pour un même jeu de données (ce qui est pénible)

6. L'envie d'automatiser certaines tâches, notamment sans valeur ajoutée

7. Le travail en équipe avec des programmeurs amateurs ou professionnels

Quelles sont concrètement les tâches pouvant être automatisées avec `Python` ?

1. Chercher de l'information présente dans plusieurs fichiers en local ou en ligne

2. Faire et automatiser des traitements statistiques

3. Extraire de l'information de fichiers de formats différents

4. Faire des visualisations (graphiques, cartes, *etc*.)

5. Mettre en forme un fichier

6. Faire une veille sur des sites ou des réseaux sociaux

7. Produire des documents mis en forme

8. Modifier automatiquement des fichiers

	- Exemple : En cas de mise à jour

9. Faire une interface avec une base de données spécifique

10. Résumer des informations présentes dans un grand ensemble de textes

11. Automatiser et vérifier des opérations de collecte

12. Faire de l'apprentissage automatique

13. Développer des logiciels adaptés à vos besoins

## Syntaxe de base

Tout programme informatique offre la possibilité à l'utilisateur de commenter son code. Au cours de votre apprentissage, n'hésitez pas à utiliser cette fonctionnalité pour ajouter **vos** éléments de compréhension.

	# Ceci est un commentaire en Python

On commence tout programme `Python` par la déclaration de l'encodage des caractères utilisés :

	#coding:utf8

> [!WARNING]
> Le `#` contenu dans `#coding:utf8` n'est pas un commentaire, mais une déclaration. Ce sera l'unique exception de toutes les séances.

## Algorithmique

Le mot « algorithmie » vient du nom du mathématicien persan, Muhammad ibn Musa al-Khuwarizmi dit Al Khuwarizmi (IX<sup>e</sup> siècle), latinisé en Algoritmi.

Un algorithme est une **recette**. Il s'agit d'une suite d'instructions qui, lorsqu'elles sont exécutées correctement, aboutissent au résultat attendu. C'est un énoncé en langage clair, bien défini et ordonné.

Plus précisément, un algorithme décrit une **méthode de résolution** de problèmes courants, le plus souvent par le calcul.

L'algorithmique[^2] est l'ensemble des éléments informatiques permettant d'écrire un programme. Apprendre l'algorithmique, c'est apprendre à programmer dans les règles de l'art. L'algorithmique doit permettre le développement de mécanisme de pensée par l'apprentissage permettant d'optimiser les traitements que le développeur doit programmer au niveau :

- de la vitesse de calcul ;

- de l'occupation de la mémoire ;

- de la quantité de lignes de programmation ;

- *etc*.

Il est possible d'apprendre le code informatique sans aucun langage de programmation. On parle alors de **langage de description d'algorithmes** (L.D.A.). Dans ce cadre, un **pseudo-code** fait référence à une syntaxe ressemblant à un code. Voici les éléments **presque** universels que l'on retrouve dans tout langage de programmation :

- les variables ;

- les opérateurs ;

- les instructions ;

- les conditions ;

- les boucles ;

- les boucles conditionnelles ;

- les fonctions et les procédures ;

- les objets[^3].

## Premier programme

Le plus simple pour commencer est de créer une sortie.

	print("Bonjour tout le monde !")

`print(...)` est la fonction permettant d'écrire un retour sur la console d'exécution. Les `"` permettent de créer une zone de texte (`String`, chaîne de caractères en informatique).

Tester le code pour voir si vous avez compris.

> [!TIP]
> Les chaînes de caractères peuvent s'écrire de quatre manières différentes : `''`, `""`, `'''`, et `"""`. Les guillemets simples ou doubles permettent d'écrire un texte sur une seule ligne, tandis que les guillements triples simples ou doubles permettent d'écrire du texte sur plusieurs lignes.

## Les variables

Une **variable** est une valeur qui est enregistrée temporairement dans la mémoire vive de votre ordinateur (ou R.A.M.). Toute variable possède un type. En `Python`, il existe quatre types de base :

- `int` pour les entiers ;

- `float` pour les nombres réels. Dans ce cas, un entier possède une virgule, par exemple, `1.0` pour 1 ;

- `str` pour les chaînes de caractères ;

- `bool` pour les variables booléennes (`True` ou `False`).

Le typage en `Python` est dit **faible** et **dynamique**. Il est **faible** parce que le langage déduit le type de variables. Toute variable possède une **étiquette**, c'est-à-dire un nom, lui permettant d'être retrouvée en mémoire, et une **valeur** qui lui est affectée par l'opérateur `=`. Par exemple,

	nom = "Forriez"

	print(nom)

Dans le cadre d'un typage faible, le programme sait que la variable `nom` est une chaîne de caractères `str`. De même,

	test = True

	print(test)

Le programme sait que la variable `test` est une variable booléenne, *etc*. Toutefois, il est possible d'utiliser des fonctions `int(...)`, `float(...)`, `str(...)` et `bool(...)` pour forcer le castage des variables, et ainsi avoir le bon type. Un prochain exemple l'illustrera.

Le typage est **dynamique**, car il est possible de changer le type d'une variable avec une simple nouvelle affectation, une **réaffectation**.

	nom = "Forriez"

	print(nom)

	nom = True

	print(nom)

Le premier `print(...)` affiche `Forriez`, le second `True`.

Il est possible de réaffecter une variable par elle-même. 

	nb = 1	

	nb = nb + 1

	print(nb)

Ici, à la première ligne, `nb` vaut 1. À la seconde ligne, on effectue toujours le calcul du membre de droite, ici `nb + 1`, valant 2, en avant d'opérer à sa réaffectation à l'étiquette `nb`. De fait, il s'affichera `2` sur la console.

> [!NOTE]
> En informatique, les valeurs constantes sont des variables particulières. Normalement, une constante est une variable qui n'est lisible qu'en lecture seule, c'est-à-dire qu'il est impossible de réaffecter sa valeur. En `Python`, ce type n'existe pas, mais, par convention, toute **constante** doit être écrite en majuscule.

	PI = 3.1416

	print(PI)

Il est possible de libérer de l'espace mémoire en supprimant une variable avec la fonction `del(...)`. On peut ainsi supprimer toutes  les variables créées précédemment.

	del(nom)

	del(test)

	del(nb)

	del(PI)

## Entrée-Sortie. Exemple de concaténation

En premier programme, nous avions vu ce qu'était une sortie. Voyons rapidement ce qu'est une entrée.

	age = input("Quel est votre âge ? ")

	age = int(age)

	print("Vous avez {} ans.".format(age))

On déclare l'entrée avec `input(...)`, la fonction contenant la requête demandée par la machine. On affecte une variable à la réponse de l'utilisateur, ici `age`. Le problème est que la fonction `input` ne renvoie que des chaînes de caractères, même si l'entrée est un nombre ou un booléen. C'est là que l'on utilise les fonctions de castage. Ici, on réaffecte `age` en transformant l'entrée en nombre entier.

La fonction `print(...)` contient une **concaténation**. Lorsque vous avez un texte type dans lequel va juste changer un élément, il n'est pas judicieux d'opérer des copier-coller de votre code. En utilisant la méthode `format(...)` et `{}` pour annoncer la position de la variable dans la chaîne de caractères, vous pouvez résoudre ce problème. L'outil est intéressant, car il évite de recaster `age`. La méthode `format(...)` s'occupe de tout. Nous reviendrons dans une autre séance sur les outils utilisables sur les chaînes de caractères.

## Les opérateurs

Nous avons déjà croisé l'**opérateur d'affectation** : `=`.

Il existe les **opérateurs arithmétiques** :

- l'addition `print(1 + 1)` (sortie: `2`) ;

- la soustraction `print(4 - 6)` (sortie: `-2`) ;

- la multiplication `print(3 * 5)` (sortie: `15`) ;

- la division `print(3 / 5)` (sortie: `0.6`) ;

- le modulo `print(5 % 2)` (sortie: `1`) ;

- la division entière `print(5 / 2)` (sortie: `4`) ;

- l'exponentiation `print(3 ** 2)` (sortie: `9`) ;

À partir des opérateurs arithmétiques `+`, `-`, `*`, `/` et `%`, il est possible de compléter la liste des **opérateurs d'affectation**. Le plus simple est de les tester avec ce code qui reprend les cinq premières opérations précédentes.

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

Les **opérateurs de comparaison** dans les instructions sont :

- `==` pour vérifier une identité. Il est à noter que le symbole prend un double égal afin de le différencier de l'opérateur d'affectation ;

- `!=` pour vérifier une différence ;

- `<` pour vérifier une inégalité inférieure stricte ;

- `>` pour vérifier une inégalité supérieure stricte ;

- `<=` pour vérifier une inégalité inférieure ou égale ;

- `>=` pour vérifier une inégalité supérieure ou égale.

Pour finir, il existe des **opérateurs logiques** :

- `and` pour « et » ;

- `or` pour « ou » strict[^4] ;

- `in` pour « dans un ensemble de » ;

- `not in` pour « en dehors d'un ensemble de » ;

- `not` pour « ne pas ».

## Les conditions

Les conditions permettent de mettre en œuvre les variables et les opérateurs. Elles correspondent à une implication mathématique : « si... alors... ». Par exemple, fixons un âge légal en dessous duquel il n'est pas possible d'accéder à l'information.

1. On crée une constante `AGE_LEGAL` et une variable `age`.

2. On teste si l'âge entré est strictement inférieur à l'âge légal. Si c'est vrai, on affiche que l'accès est refusé. Si c'est faux, on affiche que l'accès est autorisé.

		age = 15

		AGE_LEGAL = 18

		if age < AGE_LEGAL:

			print("Accès refusé")

		else:

			print("Accès autorisé")

Cette proposition conditionnelle n'est pas acceptable, car elle ne permet pas de visualiser toutes les erreurs possibles. Par exemple, si vous mettez un âge négatif, la condition traitera l'information comme correcte, alors qu'un âge négatif est impossible. On peut corriger la condition en créant un intervalle. Il est possible de l'écrire de deux manières :

	age = 15

	AGE_LEGAL = 18

	if 0 < age < AGE_LEGAL:

		print("Accès refusé")

	else:

		print("Accès autorisé")

ou

	age = 15

	AGE_LEGAL = 18

	if age >= 0 and age < AGE_LEGAL:

		print("Accès refusé")

	else:

		print("Accès autorisé")

Il faut faire deux remarques si vous testez cette solution.

1. Vous avez vu comment utiliser l'opérateur logique `and`, mais, entre la première et la seconde solution, il faut privilégier la première, car son écriture comporte moins de caractères.

2. La solution n'est toujours pas bonne, car, si `age = -15`, alors `Accès autorisé` s'affiche.

Pour solutionner le problème, il faut construire une solution plus complexe en introduisant la commande `elif`.

	age = 15

	AGE_LEGAL = 18

	AGE_MAXIMUM = 130

	if age <= 0:

		print("Votre âge ne peut pas être négatif. Vous avez écrit n'importe quoi !")

	elif age >= AGE_MAXIMUM:

		print("Soit vous êtes un vénérable ancien ! Soit vous avez écrit n'importe quoi !")

	elif 0 < age < AGE_LEGAL:

		print("Accès refusé")

	else:

		print("Accès autorisé")

On commence d'abord par vérifier si l'âge est négatif, car la valeur l'est, il est inutile de poursuivre l'instruction. Puis, on poursuit par vérifier que l'âge ne soit pas trop grand en créant au préalable une constante matérialisant un âge indépassable `AGE_MAXIMUM`. Ensuite, on vérifie si l'âge est compris entre 0 et l'âge légal, auquel cas l'accès est refusé. Enfin, si toutes les propositions précédentes sont fausses, avec `else`, on autorise l'accès.

> [!TIP]
> Si vous voulez tester votre compréhension, vous pouvez essayer avec l'aide de la documentation d'ajouter une condition qui vérifie si la valeur saisie est bien un nombre entier.

## Les boucles conditionnelles

L'informatique a pour objectif principal de gérer les tâches répétitives. Dans cet optique, les boucles ont été inventées. Il en existe deux en `Python` :

- les **boucles conditionnelles** ;

- les **boucles de parcours de séquence**.

Une boucle conditionnelles `while` a besoin d'une variable permettant de l'arrêter. Pour bien comprendre, demandons d'afficher les valeurs entières entre 0 et 4. Pour ce, on initialise la boucle avec la variable `compteur`. On lui affecte la valeur 0.

	compteur = 0

	while compteur < 5:

		print(compteur)

		compteur += 1

La boucle conditionnelle affiche `0`, réaffecte la variable `compteur` en ajoutant 1, puis on retourne en début de la boucle et on revérifie la condition. `compteur = 1`, il s'affiche alors `1`, puis la variable `compteur` en ajoutant 1, et ainsi de suite. La boucle s'arrête lorsque `compteur = 5` la condition n'est plus respectée, la boucle s'arrête. La console a affiché successivement `1 2 3 4`.

> [!WARNING]
> Il faut éviter les boucles infinies. Non pas qu'elles soient inutiles, votre ordinateur démarre avec une boucle infinie afin que vous puissiez l'utiliser, mais il est **toujours** prévu un point d'arrêt, l'extinction de votre ordinateur.

	arret = False

	while arret == False:

		if instruction arrêtant la boucle:

			arret = True

## Les boucles de parcours de séquence

Dans la suite des séances, nous verrons beaucoup de séquences. Pour l'heure, il s'agit juste de comprendre la syntaxe.

Exemple 1. Parcourir une liste de caractères `A B C`

	for element in "A", "B", "C":

		print(element)

La variable `element` est une variable temporaire qui se voit successivement affecter `A`, `B` et `C`.

Exemple 2. Parcourir une liste de nombres. Une fonction existe pour créer une suite de nombre, `range(...)`. Elle prend en paramètres le début de la liste de nombres voulue, la dernière valeur, celle-ci étant exclue de la liste, et le pas de l'itération générée. Par exemple, `range(1, 10, 1)` crée la séquence `1 2 3 4 5 6 7 8 9`, mais `range(1, 10, 2)` crée la séquence `2 4 6 8`. Il est à noter que le pas n'est pas obligatoirement un nombre entier et qu'il est possible de ne pas en mettre, dans ce cas, la valeur est par défaut 1.

	for element in range(1, 10, 1):

		print(element)

## Les points d'arrêt des boucles

Les boucles, quel que soit son type, peuvent utiliser deux points d'arrêt :

- `continue` ;

- `break`.

Pour bien comprendre le résultat, je vous conseille de tester les lignes suivantes :

	for element in range(1, 10, 1):

		if element == 5:

			continue;

		print(element)

	for element in range(1, 10, 1):

		if element == 5:

			break;

		print(element)

`continue` réinitialise la boucle. Dans l'exemple, la valeur `5` arrête la boucle et la réinitialise, ce qui affiche `1 2 3 4 6 7 8 9`.

`break` arrête la boucle. Dans l'exemple, la valeur `5` arrête la boucle, ce qui affiche `1 2 3 4`.

> [!NOTE]
> Les boucles de parcours seront pleinement comprises lors de l'utilisation des listes, des tuples, et des dictionnaires.

## Les fonctions

En `Python`, il existe deux types de fonction :

- les **fonctions natives** ;

- les **fonctions créées**.

Les fonctions natives ont déjà été rencontrées précédemment avec : `print()`, `input()`, `int()`, `float()`, `str()`, `bool()`, *etc*. Pour en apprendre d'autres, il faut lire la documentation. Il n'est pas rare que, lorsque vous voulez créer une fonction, elle existe déjà.

Les fonctions créées par le développeur sont celles que nous allons voir dans cette partie.

Peu importe la fonction, il faut partir du principe qu'**une fonction n'accomplit qu'une tâche**.

Créons une fonction pour afficher `Bonjour ` + le nom demandé. Testons ce code.

	def direBonjour(nom):

		print("Bonjour {}".format(nom))

	prenom = input("Quel est votre prénom ? ")

	prenom = str(prenom)

	#Appel de la fonction

	direBonjour(prenom)

Vous avez vu que la fonction n'affiche rien à l'écran, alors que le programme se lit ligne par ligne. Il pose directement la question d'entrée. Lorsque vous répondez, la valeur est placée en paramètre de la fonction `direBonjour()` pour appeler la fonction, et seulement afficher `Bonjour `...` !`

Il est possible de créer un paramètre par défaut dans la fonction.

	def direBonjour2(nom = "Maxime"):

		print("Bonjour {}".format(nom))

	prenom = input("Quel est votre prénom ? ")

	direBonjour2()
	
L'absence de réponse étant considéré comme un caractère vide, ici la fonction est appelée sans arguments. Peu importe votre réponse, la valeur par défaut prise et il s'affichera toujours `Bonjour Maxime !`

Il est également possible d'effectuer un retour. *Stricto sensu*, il s'agira d'une vraie fonction au sens informatique, les deux cas précédents étant des procédures.

	def direBonjour3(nom = "Maxime"):

		return "Bonjour {}".format(nom)

	prenom = input("Quel est votre prénom ? ")

	print(direBonjour3(str(prenom)))

Ici, la fonction prend en considération le paramètre saisi, mais retourne la réponse sans l'afficher. Pour afficher la réponse, il faut utiliser la fonction `print()` en l'appliquant à la fonction appelée.

Pour finir, traitons un cas numérique. Définissons la somme de deux nombres.

	def calculerSomme(nombre1, nombre2):

		return nombre1 + nombre2

	print(calculerSomme(1, 2))

Les fonctions peuvent retourner de nombreux types : les types principaux et les types composites qui seront vus dans les prochaines séances.

## La modularité

La modularité dans `Python` permet d'accéder aux bibliothèques natives (ou *libraries*[^5]) de `Python` et à d'autres programmes `Python`, ce qui permet d'éviter d'écrire la totalité du code dans un même fichier.

> [!IMPORTANT]
> Dans l'intégralité des T.D., au maximum deux fichiers seront utilisés, mais, dans des projets plus importants, il est fondamental de trier son code en créant des fichiers « thématiques » qui traiteront d'un problème particulier. C'est de cette façon que la puissance d'un outil comme `Python` apparaît.

Pour appeler une bibliothèque, par exemple, les fonctions mathématiques, on écrit :

	import math

puis, on peut appeler la méthode racine carrée `sqrt` :

	print(math.sqrt(2))

ici on demande la racine carrée de 2.

> [!IMPORTANT]
> Il existe des paquets à télécharger pour compléter les bibliothèques natives de base, mais leur emploi est hors programme.

Pour importer une fonction d'un autre fichier `Python`, on peut :

1. créer un onglet-fichier `toto.py` ;

2. y taper

		def test():

			print("Bonjour ! Test réussi !")

3. taper dans `main.py`

		from toto import test

		test()

Il s'affiche bien en lançant le `Run` : `Bonjour ! Test réussi !`

Il est important de noter que l'on appelle la fonction (ou l'objet) avec `from` dans le fichier `toto` (sans son extension).

> [!IMPORTANT]
> Le module n'effectue pas grand-chose. Il se charge et son programme se termine aussitôt. Il sert essentiellement à organiser efficacement son code.

## Le concept d'objet

Un objet traite un type de données particulier. Tout objet possède :

- des attributs ou des propriétés ;

- des méthodes.

Les propriétés désignent les variables propres à l'objet. Les méthodes renvoient aux fonctions propres de cet objet. Dans le cours précédent, on avait vu l'objet `math`. Il permet de comprendre simplement ce qu'est un objet.

L'objet `math` possède des constantes `pi` et `e` par exemple. On les appelle en tapant :

	math.pi

	math.e

c'est-à-dire le nom de l'objet et l'attribut appelé.

L'objet `math` possède des fonctions mathématiques :

- `math.pow(` nombre`,` puissance `)` : nombre à la puissance demandée ;

- `math.sqrt(` nombre `)` : racine carrée du nombre ;

- `math.cbrt(` nombre `)` : racine cubique du nombre ;

- `math.log(` nombre`,` base `)` : logarithme du nombre de base demandée ;

- `math.log2(` nombre `)` : logarithme de base 2 du nombre ;

- `math.log10(` nombre `)` : logarithme de base 10 du nombre ;

- `math.exp(` nombre `)` : exponentielle du nombre ;

- `math.cos(` nombre `)` : cosinus du nombre ;

- `math.sin(` nombre `)` : sinus du nombre ;

- `math.tan(` nombre `)` : tangente du nombre ;

- `math.acos(` nombre `)` : arc cosinus du nombre ;

- `math.asin(` nombre `)` : arc sinus du nombre ;

- `math.atan(` nombre `)` : arc tangente du nombre ;

- `math.floor(` nombre `)` : arrondir à l'entier inférieur ;

- `math.ceil(` nombre `)` : arrondir à l'entier supérieur ; 

- `math.factorial(` nombre `)` : factorielle du nombre ;

- *etc*.

> [!WARNING]
> Les nombres complexes ont leur propre module `cmath`.

La particularité de l'objet `math` est qu'il n'est pas nécessaire d'instancier un objet pour l'utiliser, à la différence de l'objet `string`.

## L'aide sur Python

Pour avoir de l'aide sur un objet connu, on tape

	help( nom de l'objet )

## Les chaînes de caractères

La chaîne de caractères en `Python` est un objet. L'objet est instancié en affectant une variable.

	nom = "forriez"

Vous venez de créer un objet `string`. On utilise par conséquent des méthodes pour transformer cet objet.

- `nom.upper()` met en tous les caractères en majuscule.

- `nom.lower()` met en tous les caractères en minuscule.

- `nom.capitalize()` met la première lettre de chaque mot en majuscule.

- `nom.strip()` efface les espaces blancs avant le premier mot et après le dernier mot.

- `nom.replace(` ancien(s) caractère(s)`,` nouveau(x) caractère(s)`,` occurrences `)`

- `nom.swapcase()` transforme toutes les majuscules en minuscules, et *vice versa*.

- `nom.split("` séparateur `")` transforme la chaîne en liste grâce au séparateur.

- `nom.isdigit()` teste si la chaîne est un entier.

- `nom.isalpha()` teste si la chaîne ne contient que des lettres.

- `nom[` indice `]` affiche le caractère de l'indice avec une valeur allant de 0 à l'infini.

- *etc*.

On peut obtenir la longueur d' une chaîne de caractères avec :

	len(nom)

On peut concaténer les chaînes de caractères de deux façons :

1. "J'ai {} ans.".format(41)

2. "J'ai " + str(41) + " ans."

La concaténation avec `+` n'a que des variables de type `str`, à la différence de la méthode `.format(...)`.

## Les listes en Python

Il n'existe pas de tableau en `Python`.

### Création d'une liste

	liste1 = list

ou

	liste2 =[]

ou

	liste3 = [1, 3, 15]

ou

	liste4 = [0]*10

ou

	liste5 = range(20)

	print(liste1)

	print(liste2)

	print(liste3)

	print(liste4)

	print(liste5)

### Afficher un élément 

> [!IMPORTANT]
> Les indices commencent à zéro, et pas un.

	print(liste5[0])

	print(liste5[15])

	print(liste5[-1])

	print(liste5[:2])

	print(liste5[3:])

	print(liste5[9:12])

### Parcourir une liste

	i = 0

	while i < len(liste5):

		print(liste5[i])

		i += 1

	for element in liste3:

		print(element)

### Modifier un élément

	print(liste3[1])

	liste3[1] = 100000

	print(liste3[1])

	liste3[1] = 3

### Les méthodes des listes

Les listes sont des objets qui disposent de plein de méthodes. Par exemple,

	liste3.append(100)

	for element in liste3:

		print(element)

mais encore `insert`, `pop`, `remove`, `index`, `sort`, `reverse`, `count`, `clear`, `extend`, *etc*.
	
### Copier une liste

Si vous effectuez les commandes suivantes :

	liste6 = liste3

	print(liste6)

	liste3.append(9)

	print(liste6)

	print(liste3)

vous voyez qu'elle ne marche pas. Vous avez créé une référence entre les variables `liste3` et `liste6`.

Pour copier une liste, il ne faut pas créer une nouvelle liste, mais un **clone**.

	import copy

	liste6 = copy.deepcopy(liste3)

	print(liste6)

	liste6.append(7)

	print(liste6)

	print(liste3)

	for objet in enumerate(liste6):

		print(objet)

Avec cette technique, vous avez copié la liste.

## La condition `if __name__ == "__main__":`

Cette condition permet de tester un module. Elle doit être obligatoirement à la fin d'un fichier `Python`. L'objectif est de vérifier si les fonctions fonctionnent en dehors du fichier principal.

Pour le tester simplement, il faut utiliser créer deux fichiers : `main.py` et `module.py`.

Dans `module.py`, il faut écrire pour tester la commande :

	def module():
		print("Je suis le module !")

	if __name__ == "__module__":

		print("Mon script est exécuté directement.")

	else:

		print("Mon script est importé par un autre module.")

avec `"__ __"` contenant le nom de la fonction à exporter, ici `module()`.

Dans `main.py`, il faut d'abord importer le module, ici `import module.py`.

## Les tuples

Un **tuple** est une séquence immuable, c'est-à-dire une liste en lecture seule.

### Création

	tuple = ()

ou

	tuple = (45,0)

ou

	tuple = 45,

ou

	tuple = (4,6)

### Lire les données

On lit les données grâce aux indices du tuple.

	print(tuple[0])

## Les dictionnaires

Un **dictionnaire** est une liste avec des clés.

### Créer un dictionnaire

	dictionnaire = {}

ou

	dictionnaire = {1:145, "prenom":"Maxime"}

Ici `1` et `"prenom"` sont des clés, tandis que `145` et `"Maxime"` sont des valeurs associées aux clés.

### Lire un élement

On peut appeler l'élément par sa clé.

	print(dictionnaire[1])

ou

	print(dictionnaire)

ou

	print(dictionnaire["prenom"])

ou

	print(dictionnaire)

### Parcourir un dictionnaire

Parcourir par les clés :

	for cle in dictionnaire.keys():

		print(cle)

Parcourir par les valeurs :

	for valeur in dictionnaire.values():

		print(valeur)

Parcourir par les clés et les valeurs :
	
	for cle, valeur in dictionnaire.items():

		print(cle, " ", valeur)

### Modifier une valeur

Il suffit d'utiliser la clé comme si c'était un indice.

	dictionnaire["prenom"]="Sophie"

	print(dictionnaire["prenom"])

### Copier un dictionnaire

Tout comme les listes, on ne peut pas copier directement par une simple affectation un dictionnaire.

	import copy

	dictionnaire2 = dictionnaire.copy()

	dictionnaire2["prenom"]="Maxime"

	print(dictionnaire2)

> [!IMPORTANT]
> Les dictionnaires possèdant plein de méthodes : `pop`, *etc*.

## Astuce pour les tuples et les dictionnaires

On peut créer un tuple avec les paramètres d'une fonction en appelant. Il suffit de placer `*` devant l'argument de la fonction.

	def fonction(*tuple):

		return tuple

	print(fonction(1, 2, 3))

On peut créer un dictionnaire avec les paramètres d'une fonction en appelant. Il suffit de placer `**` devant l'argument de la fonction.

	def fonction2(**dictionnaire):

		return dictionnaire

	print(fonction2(prenom="Max" , nom="Forriez"))

## L'objet `os`

[Documentation officielle](https://docs.python.org/3/library/os.html)

`import os`

`os` possède plusieurs méthodes importantes.

- `os.getcwd()` renvoie le répertoire courant.

- `os.chdir("` chemin du répertoire `")` change le répertoire courant.

- `os.listdir()` liste les dossiers et les fichiers du répertoire courant.

- `os.walk('.')` renvoie le contenu du répertoire courant.

- `os.mkdir('.', mode=0o755)` permet de créer un répertoire. L'option `mode=0o755` ne peut être utilisée qu'avec les systèmes d'exploitation `MAC/OS` et `Linux`.

- `os.makedirs("` chemin du répertoire `")` crée un répertoire et sa hiérarchie.

- `os.rename("` ancien nom `","` nouveau nom `)` renomme un fichier dans le répertoire courant.

- `os.removedirs('` chemin du répertoire `')` renomme les dossiers.

- `os.path.exists('` chemin du répertoire `')` vérifie l'existence d'un chemin.

- `os.path.realpath('` chemin du répertoire `')`  vérifie si le chemin est canonique.

- `os.path.join('` répertoire `, ` fichier.py `')` adapte le séparateur des chemins en fonction du système d'exploitation.

		base = 'c:\\Users\\Max'

		filename = 'test.py'

		os.path.join(base, filename)

- `os.path.split('` chemin `')` extrait le chemin du nom du fichier avec pour résultat un tuple. L'indice `0` renvoie l'adresse du répertoire et l'indice `1` renvoie le nom du fichier.

- `os.path.samefile('` chemin 1 `', '` chemin 2 `')` vérifie si deux chemins sont identiques. La méthode renvoie est booléen.

- `os.path.isdir('` chemin `')` vérifie s'il s'agit d'un dossier.

- `os.path.isfile('` fichier `')` vérifie s'il s'agit d'un fichier

- `os.path.islink('` lien `')` vérifie s'il s'agit d'un lien symbolique (ou raccourci).

- `os.path.stat('` fichier `')` renvoie les statistiques d'un fichier.

## L'objet `shutil`

- [Documentation officielle](https://docs.python.org/3/library/shutil.html)

- [Documentation officielle](https://python-simple.com/python-modules-fichiers/shutil.php)

- [Documentation non officielle en français](https://python-simple.com/python-modules-fichiers/shutil.php)

`import shutil`

## Les bibliothèques standard

- [Bibliothèques officielles du `Python en français`](https://docs.python.org/fr/3.13/library/index.html)

- [*Framework*](./PYTHON-MODULES-FRAMEWORKS.md)

## Notes de bas de page

[^1]: Les versions 2 et 3 sont incompatibles, même dans la syntaxe de base. Dit autrement, si la [version 4](https://answerpython.com/why-python-4-may-never-arrive/) annoncée venait à être publiée, il faudra s'attendre à la même incompatibilité.

[^2]: On peut également dire algorithmie. Les deux existent en français.

[^3]: Bien que `Python` soit un langage orienté objet, ce concept informatique ne sera pas abordé pleinement dans ces séances.

[^4]: « ou » strict signifie « soit l'un, soit l'autre, mais pas les deux ».

[^5]: Par abus de la langage, on francise souvent le terme anglais *library* en « librairie ».

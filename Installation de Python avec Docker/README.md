# `Python` avec `Docker`

Installer `Python` dans certains systèmes peut être une galère sans nom. Pour que vous ayez une version stable qui fonctionne sans souci, je vous propose d'utiliser un conteneur `Docker` contenant `Python`.

Il ne s'agit pas de déplacer le problème en vous proposant une installation encore plus compliquée. Normalement, `Docker` ne pose aucun problème d'installation. L'outil est conçu pour `Linux`. De fait, il nécessite une installation particulière sous `MAC/OS` et `Windows`.

Si vous voulez vous documenter sur `Docker`, libre à vous, et je ne saurais que trop vous le conseillez, mais, si vous voulez juste tester `Python`, suivez bien les instructions pour y parvenir.

## Installation de `Python` avec `Docker`

1. Pour `MAC/OS` et `Windows`, télécharger `Docker Engine`

2. Ouvrir un compte sur la plateforme `Docker`

3. Ouvrir le `Docker Desktop` et se connecter à son compte dans l'onglet `Hub`

4. Aller dans le dossier racine de vos fichiers `Python`, y placer l'architecture de ce GitHub (/src/main.py, docker-compose.yml, Dockerfile, requirements.txt), la conserver telle quelle, et y ouvrir un terminal

>[!TIP]
> Sous `Windows`, aller dans la barre d'adresse, y taper `cmd` et faire `Entrée` pour ouvrir un terminal.

5. Dans le terminal ouvert, taper `docker-compose up -d`

>[!WARNING]
> La première installation dure quelques minutes.

6. Dans le dossier `src`, il y a un fichier `main.py`. C'est dans ce fichier que vous taperez votre code

7. Pour tester pour code, taper `docker-compose run python`

## Démarrer votre console `Python`

>[!TIP]
> Je vous conseille à chaque exercice d'ouvrir un nouveau dossier racine.

1. Ouvrir le `Docker Desktop`

2. Aller dans le dossier racine de vos fichiers `Python` et y ouvrir un terminal

3. Dans le terminal ouvert, taper `docker-compose up -d`

>[!WARNING]
> Si vous avez déjà lancé une image `Docker`, il faudra taper : `docker-compose up -d --build`

4. Dans le dossier `src`, il y a un fichier `main.py`. C'est dans ce fichier que vous taperez votre code. Pour chaque séance, il vous suffira de copier les fichiers du T.D. dans ce dossier.

5. Pour tester votre code, taper `docker-compose run python` (juste cette commande à chaque modification)

>[!WARNING]
> Le point d'entrée de votre programme sera toujours `main.py`.

## Arrêter `Python` et `Docker`

1. Taper dans la console : `docker-compose down`

2. Éteindre `Docker Desktop`. Dans la fenêtre du logiciel en bas à gauche, il y a une zone verte avec un bouton `Quit Docker Desktop`.

>[!WARNING]
> Si vous n'effectuez pas cette commande, `Docker` restera ouvert tout le temps. À chaque ouverture de votre ordinateur, il ouvrira le conteneur `Python` que vous avez créé, même si vous ne l'utilisez pas. Dit autrement, des ressources seront consommées inutilement.

## Installer les paquets

Dans ce cours, on utilise de nombreux paquets. Il suffit de taper leurs noms dans le fichier `requirements.txt` **avant** de lancer la commande `docker-compose up -d --build`.

Par défaut, j'ai placé tous les paquets nécessaires pour les T.D.

## Désinstaller `Docker Desktop`

À la fin de ce cours, vous souhaiterez peut-être faire de la place sur votre P.C. Avant de supprimer `Docker`, il faut supprimer tout ce qu'il a créé. Pour cela, aller dans les onglets, en respectant l'ordre suivant :

1. `Containers` :

	- Stopper tous les conteneurs encore en activité
	
	- Supprimer les conteneurs
	
2. `Volumes` :

	- Supprimer tous les volumes

3. `Images`

	- Supprimer les images

>[!WARNING]
> Aucune image ne peut être supprimée si un conteneur associé est toujours en activité.

4. `Builds`

	- Supprimer tous les éléments qui s'y trouvent

## Installation alternative si `Docker` n'est pas installé

- [`Python` officiel en ligne et en console](https://www.python.org/shell/) (les données externes ne sont pas accessibles)

- [`Python` en `Google`](https://colab.research.google.com/) (nécessite un compte `Google`)

- [`Python` online](https://www.online-python.com/) (les bibliothèques externes ne peuvent pas être installées)

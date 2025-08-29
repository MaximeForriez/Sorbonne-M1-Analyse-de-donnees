# `Git`

Votre rendu final doit être déposé sur votre `GitHub` personnel sous la forme d'un portfolio. Vous devez juste m'envoyer son lien pour être évalué. Voici quelques éléments pour vous apprendre à utiliser efficacement `GitHub`. Pourquoi utiliser `Git` plutôt que `Moodle` ? La réponse est simple. Vous devez me transmettre des fichiers `Python`, or `Moodle` va les considérer comme des attaques au niveau de son serveur. Vous n'avez pas le choix. Vous devez maîtriser très rapidement `Git` afin de me rendre votre travail.

Le deuxièmme intérêt de `Git` est que le moteur tend à être utilisé de plus en plus dans les organisations professionnelles. C'est un atout important à mettre dans votre C.V. si vous allez au-delà de ce qui vous est demandé pour effectuer le dépôt de votre portfolio.

Le troisième intérêt de `Git` est le dépôt en lui-même des travaux que vous avez effectués en université. Vous pouvez envoyer un lien à l'entreprise dans laquelle vous voulez avoir un stage ou être recruté avec vos réalisations démontrant ainsi votre savoir faire. Au-delà du cde, vous pouvez par exemple l'utiliser pour gérer les versions de votre mémoire, vos rapports, *etc*. Il vous faudra être stratégique dans vos choix afin de prouver vos savoir-faire. Par ailleurs, vous montrez également votre maîtrise de la plateforme.

> [!NOTE]
> Il est possible de créer dans la version gratuite de `GitHub` trois dossiers (`repository`) confidentiels. Si votre mémoire est confidentiel, il est parfaitement possible de déposer sans aucune vue publique. Tout comme, il vous sera possible de le rendre public quand bon vous semble.

## Objectifs

- Créer votre compte `GitHub`

- Comprendre la différence entre `Git` et `GitHub`

- Comprendre la philosophie et l'intérêt de `Git`

- Savoir cloner un dépôt sur son compte `Git`

- Savoir lier son ordinateur local avec son dépôt `Git` distant avec `git init`, `git remote add` et `git branch`

- Savoir alimenter son dépôt avec `git add`, `git commit` et `git push`

- Savoir gérer son dépôt sur la plateforme et en lignes de commande, notamment les commandes permettant de revenir en arrière

> [!NOTE]
> `Git` est un outil `Linux`. Il fonctionne de manière optimale avec ce système d'exploitation. Si vous installez `Git` sur un P.C. tournant sur `Windows`, l'installateur de `Git` va installer un noyau `Linux` afin de faire fonctionner un terminal de type `bash`. Dans n'importe quel dossier de `Windows`, vous pourrez y accéder simplement en faisant un clic droit de votre souris et de cliquer sur `Open Git Bash here`.

> [!NOTE]
> Avec W.S.L., il vous est possible d'installer un terminal `Linux` en tant que sous-noyau de votre système d'exploitation `Windows`.
> - [Installer un terminal `Linux` sur `Windows` avec WSL en quelques clics](https://www.youtube.com/watch?v=VuXpOXhn2Hk)
> - [Maîtrisez le terminal `Linux` : commandes essentielles pour débutants](https://www.youtube.com/watch?v=GHPxJ7kPCcI)
> - [Cours sur W.S.L.](https://www.youtube.com/watch?v=uLbyhmpnbnE&list=PLSuzYIVSEUT4LyB66TpKeCUmbTteLYrXz) (Approfondissement sur W.S.L.)

## Tutoriels

Tous les tutoriels ne sont pas à visualiser. Idéalement, à partir des vidéos d'introduction des cours, vous choisissez le cours qui vous convient le mieux. Si ces ressources ne vous conviennent pas, pour vous aider à juger le sérieux d'un cours `YouTube`, sachez que un cours `Git` dure entre 1h30 et 2h00 pour que vous deveniez autonome sur la plateforme et dans votre apprentissage régulier de nouvelles commandes.

- [`Git` expliqué simplement : tutoriel complet pour débutants](https://www.youtube.com/watch?v=anP0LBVhUzA)

- [`Git` et `GitHub` pour le *data science* : le guide complet pour débutants](https://www.youtube.com/watch?v=xwFj6WCJW0I)

- [Cours sur `Git` et `GitHub`](https://www.youtube.com/watch?v=rcsqG0ZXXNk&list=PLLBWkn1N0gl7AO56vpDPWsKeDfYjEaZWT)

- [Formation `Git`](https://www.youtube.com/watch?v=rP3T0Ee6pLU&list=PLjwdMgw5TTLXuY5i7RW0QqGdW0NZntqiP)

- [Apprendre `Git`](https://www.youtube.com/watch?v=PjTilX5DeyM&list=PLtAnN3kwIVucWlr1pyfnmw8qCNaq0tusi)

- [Apprendre à utiliser `Git`](https://www.youtube.com/watch?v=A5_kJps4qjc&list=PLsm134NGfeYP67pmUoKSWb53lqVqA7oTg)

- [`Git`](https://www.youtube.com/watch?v=0sGQgfUdCAY&list=PLn6POgpklwWpUfM8BaIU1deH6peqHdmWL) (Approfondissement des notions de base)

- [`Git` et `GitLab`](https://www.youtube.com/watch?v=q5E-scBPYFA&list=PLn6POgpklwWrRoZZXv0xf71mvT4E0QDOF) (Approfondissement des notions de base)

## Ressources

- [Site officiel](https://git-scm.com/)

- [Guide simplifié de `Git`](./PDF/Pardo-Julen-2016-Git-Tutorial.pdf)

- [`Git` *Cheat Sheet*](./PDF/Git-Cheat-Sheet.pdf)







## `Git` et vos travaux en analyse de données

Dès la première semaine de cours, vous devez commencer à déposer des éléments sur la plateforme. Ce n'est pas forcément votre travail final, j'espère que vous l'avez compris après avoir vu quelques vidéos et lu quelques guides. Il faut vous entraîner régulièrement de sorte que le dépôt final se passe bien. Lors de votre évaluation, seule la dernière version de vos fichiers sera prise en compte pour votre évaluation.

Cela étant, l'horodatage pris en compte sera celui de la date limite. Si vous m'avez déposé de nouveaux éléments après la date du dépôt final, même de quelques secondes, ce sera l'ancienne version qui sera évaluée, d'où la nécessité de déposer régulièrement même des bouts de code qui ne sont pas terminés. Vous devez acquérir le réflexe suivant : "Je viens de changer une dizaine de lignes de code. Je dépose." Comme dit dans la plupart des tutoriels, il ne faut pas faire des dépôts avec des milliers de lignes transformées ou nouvelles. N'oubliez jamais que, en plus d'être la plateforme sur laquelle je vais vous évaluer, elle vous permet de revenir à une ancienne version de projet si la nouvelle ne fonctionne pas par exemple.


**TEST TECHNIQUE WAYCOM**
-----------

# Table des matières
1. [Présentation](#Présentation)
2. [Context](#Context)
3. [Arborescence](#Arborescence)
4. [Installation](#Installation)
5. [Utilisation](#Utilisation)

# Présentation
Ce projet a été mené pour répondre à un test technique proposé par la [société Waycom](https://www.waycom.net/) de Bordeaux. 

Il se décompose en 2 exercices : 
> **Objectif 1** : Écrire un programme permettant de classer par nombre d’occurrences les mots d’un texte capturé sur l’entrée standard.

> **Objectif 2** : Ecrire un programme qui lit une liste d'appels sur l’entrée standard. Cette liste d'appels est une succession de lignes présentées sous la forme suivante : **start:end** start" et "end" sont tous deux des integers, il s'agit de la date de début et de la date de fin d'un appel, au format timestamp. "end" est strictement supérieur à " start ". Les lignes sont triées sur le champ " start " par ordre croissant.

Reformulation du problème : 
> **Reformulation 1** : Compter le nombre de mots proposés sur l'entrée standard, j'entends par mot un ensemble de lettre. "123", "e123e", "e-e" ou encore "http/123" ne seront pas pris en compte. Exception faite pour "#".

> **Reformulation 2** : Sur un interval allant du début d'appel le plus tôt à la fin d'appel le plus tard, chercher le nombre maximal d'appels concourrents proprosé en entrée standard.

# Context

Vous vous attacherez à livrer cette réalisation comme vous le feriez dans une situation classique de projet.
> Cela implique pour moi de justifier la logique, la représenter schématiquement et de fournir une batterie de tests. 

# Arborescence 

Waycom 
>	- appel
		+ comptage_mots.py		| réponds aux problèmes en utilisant le module worker.py
		+ test.py 				| tests pour le class Worker
		+ worker.py 			| modules pour traiter les données

>	-comptage
		+ pic_appel.py 			| réponds aux problèmes en utilisant le module worker.py
		+ test.py 				| tests pour le class Worker
		+ worker.py 			| modules pour traiter les données

# Installation 

> $ git init 

> $ git remote add origin [lien vers le projet.git]

> $ git pull origin master

# Utilisation 

> $ cd comptage

> $ echo "foo bar baz foo" | ./comptage_mot.py

> $ cat /etc/services | ./comptage_mot.py

> $ cd ../appel

> $ cat calls.txt | ./pic_appel.py



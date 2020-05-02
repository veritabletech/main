#  Veritable.tech

Voici différents scripts qui implémentent le protocole de veritable.tech.  
L'objectif étant de permettre à chacun de rapidement implémenter sa solution sur notre protocole.

Si vous voulez un site simplifié qui implémente notre protocole il faut aller sur https://github.com/veritabletech/veritabletech.github.io

### Création de la base de données

Le fichier **database.py** parcourt toute la blockchain et récupère tous les certificats d'authenticité qui y sont présents. Le script affiche tous les certificats, mais pour un usage réel il suffit d'ajouter tous les certificats à votre base de données.

### Pour émettre un certificat

Le fichier **paiement.py** créer un certificat sur la blockchain.

A la première exécution le script va vous demander une clé privée lui permettant de poster les certificats sur la blockchain.  
En faisant cela il modifie son code pour inscrire la clé privée à la toute première ligne du script.

Ensuite il faut l'exécuter avec 4 arguments:
+ L'identifiant de votre certificat
+ L'artiste/La marque du produit de votre certificat
+ L'oeuvre/Le produit a certifier
+ Le type de tirage

Ainsi en exécutant `python3 script.py identifiant artiste oeuvre tirage` cela créer un certificat qui a les propriétés voulues.

#  Veritable.tech

#### Exemple de site implémentant notre protocole

Le fichier **verification_certificat.html** vérifie un certificat hebergé sur la blockchain. Un hash d'un certificat est demandé. Voici un exemple de hash pour tester : **15d9f8bb3a5ed8408fbe019ce590bc303250a5263c8b9a6cd12356db543e2202**.

Le fichier **database.py** parcourt toute la blockchain et récupère tous les certificats d'authenticité qui y sont présents. Le script affiche tous les certificats, mais pour un usage réel il suffit d'ajouter tous les certificats à votre base de données.

Le fichier **paiement.py** créer un certificat sur la blockchain.

private_key = None

#Import préliminaires
import sys
import os
import random

#Si l'utilisateur veut repartir de zéro on mets premier_lancement à True
if len(sys.argv) > 1 and sys.argv[1] == "reset":
    premier_lancement = True

#On demande la clé privée puis on quitte si l'utilisateur voulait la changer
if not private_key:
    print("Ce script a besoin d'une clé privée pour fonctionner")
    clef = input("Votre clé > ")
    nom = os.path.basename(__file__)
    nom_tmp = str(random.random())
    os.system("echo 'private_key = \"" + clef + "\"' > " + nom_tmp)
    os.system("tail --lines=+2 " + nom + " >> " + nom_tmp)
    os.system("mv " + nom_tmp + " " + nom)
    print("Votre fichier a bien été configuré avec votre clé privée")
    exit()

#On vérifie que l'utilisateur a compris comment marchait le script
if len(sys.argv) < 5:
    print("Utilisation: python3 script.py identifiant artiste oeuvre tirage")
    exit()

# Execution du script
import bitsv
my_key = bitsv.Key(private_key)

import urllib3
http = urllib3.PoolManager()

import hashlib, binascii
import string
import secrets

#On parse l'entrée
identifiant = sys.argv[1]
artiste = sys.argv[2]
oeuvre = sys.argv[3]
tirage = sys.argv[4]

#On génère le mot de passe
alphabet = string.ascii_uppercase.replace("O", "") + string.digits
mot_de_passe = ''.join(secrets.choice(alphabet) for i in range(20))

#On affiche par exemple le mot de passe
print(mot_de_passe, end="")

#On renvoit ce qui permets d'accéder au certificat
def chiffrement(mdp, identifiant):
    dk = hashlib.pbkdf2_hmac('sha256', mdp.encode(), identifiant.encode(), 1000000)
    return binascii.hexlify(dk).decode()

#Envoyer une tx à la blockchain
def send(data):
    list_of_pushdata = (["veritable.tech".encode("utf-8"), str(data).encode('utf-8')])
    return my_key.send_op_return(list_of_pushdata)

data = {'identifiant': identifiant, 'artiste': artiste, 'oeuvre': oeuvre, 'tirage': tirage, 'mdp': chiffrement(mot_de_passe, identifiant)}
h = send(data)
print(h)

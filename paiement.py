import bitsv
import sys
import random
import os
import urllib3
import hashlib, binascii
import string
import secrets

http = urllib3.PoolManager()

public_key = "18sRMTTFXJ1MK13D8LVN8poFCEn1nBbuAS"
private_key = ""
my_key = bitsv.Key(private_key)

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

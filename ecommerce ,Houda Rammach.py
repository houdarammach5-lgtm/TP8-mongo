
from pymongo import MongoClient
Client = MongoClient("mongodb://localhost:27017")
db = Client["ecommerceDB"]
produits = db.produits
clients = db.clients
commandes = db.commandes
#1
from datetime import datetime
def creer_commande(nom_cli,produit,date,statu,montant):
    commande={
        "client":nom_cli,
        "Produit":produit,
        "date":datetime.now(),
        "statu":statu,
        "montant":montant
    }
    commandes.insert_one(commande)
    print("Commande est ajouter ")
#2
def afficher_produit():
    for p in produits.find():
        print(p)
#3

def rechercher_commandes():
    nom_cli=input ("Entrez votre nom")
    for c in commandes.find({"client":nom_cli})  : 
        print(c)
#4
def rechercher_commandes_livree():
    for c in commandes.find({"statu":"livree"})  : 
        print(c)
#5
def choisir_produit(nom, nouveau_pro):
    produits.update_one(
        {"nom": nom},
        {"$set": nouveau_pro}
    )
    print("Le produit a faire la mise a jour")
#6
def ajouter_champ(nom,disponble=True):
    produits.update_one(
        {"nom":nom},
        {"$set":{"disponible":disponble}}
    )
    print("disponible")
#7
def supprimer_commande(nom_cli,nom_prod):
 
    commandes.delete_one({"client": nom_cli,"nom_prod":nom_prod})
    print("il a supprimer")
#8
def supprimer_tout(nom_cli):
    commandes.delete_many({"client": nom_cli})
    print("tous supprimer")
#9
def trier():
    for c in commandes.find().sort("date",-1):
        print(c)
#10
def afficher_disponible():
    for p in produit.find({"disponible":True}):
        print(p)
#11
def menu():
    while True:
        print(
"""1. Ajouter une commande 
2. Afficher tous les produits 
3. recherche tous les produits disponibles 
4. Rechercher une commande par client 
5. Mettre à jour un produit 
6. Supprimer une commande 
7. Supprimer les commandes d’un client donné 
8. Afficher les produits disponibles 
9. Trier les commandes par date de la commande 
10. Quitte"""
        )
        choix=input("Entrer votre choix ")
        if choix=="1":
            nom_cli=input("Nom de client")
            produit=input("Le nom de produit")
            date=input("Date(YYYY-MM-DD)")
            statu=input("statu:")
            montant=float(input("Mantant total est :"))
            creer_commande(nom_cli,produit,date,statu,montant)
        elif choix=="2":
           afficher_produit() 
        elif choix=="3":
           rechercher_commandes() 
        elif choix=="4":
            rechercher_commandes_livree()
        elif choix=="5":
            nom = input("Nom du produit: ").strip()
            champ = input("Entrer le champ à modifier: ").strip()
            n_champ = input("Nouvelle valeur: ").strip()
            choisir_produit(nom, {champ: n_champ})
        elif choix=="6":
            nom =input("Nom client:")
            nom_produit =input("Nom Produit:")
            supprimer_commande(nom,nom_produit)
        elif choix=="7":
            nom =input("Nom client:").strip()
            supprimer_tout(nom)
        elif choix=="8":
            trier()
        elif choix=="9":
            print("le programme fini")
            break
        else:
            print("choix invalide")

menu()
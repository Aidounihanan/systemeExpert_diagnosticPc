import json
from tkinter import messagebox, Toplevel, Label, Entry, Button
from tkinter import Tk
from admin_page import admin_page
from diagnostic_pc import diagnose_pc


def sauvegarder_utilisateurs(utilisateurs):
    with open("utilisateurs.json", "w") as f:
        json.dump(utilisateurs, f)

def charger_utilisateurs():
    try:
        with open("utilisateurs.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Dictionnaire des utilisateurs
utilisateurs = charger_utilisateurs()

# Dictionnaire des admins
admins = {
    "admin": "123456",
}

def login(E1, E2):
    nom_utilisateur = E1.get()
    mot_de_passe = E2.get()

    # Chargement des données actuelles depuis le fichier JSON
    with open('utilisateurs.json', 'r') as fichier:
        data = json.load(fichier)

    if nom_utilisateur in admins and admins[nom_utilisateur] == mot_de_passe:
        admin_page()
    elif nom_utilisateur in data['utilisateurs'] and data['utilisateurs'][nom_utilisateur] == mot_de_passe:
        diagnose_pc()
    elif messagebox.askyesno("Créer un compte", "Ce nom d'utilisateur n'existe pas. Voulez-vous créer un compte ?"):
        creer_compte(nom_utilisateur, mot_de_passe)
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
      


def creer_compte(nouvel_utilisateur, nouvel_mot_de_passe, fenetre):
    # Chargement des données actuelles depuis le fichier JSON
    with open('utilisateurs.json', 'r') as fichier:
        data = json.load(fichier)

    # Vérifier si le nouvel utilisateur existe déjà
    if nouvel_utilisateur not in data['utilisateurs']:
        # Ajouter le nouvel utilisateur au dictionnaire des utilisateurs
        data['utilisateurs'][nouvel_utilisateur] = nouvel_mot_de_passe

        # Écriture des nouvelles données dans le fichier JSON
        with open('utilisateurs.json', 'w') as fichier:
            json.dump(data, fichier, indent=4)

        # Afficher un message de succès
        messagebox.showinfo("Succès", "Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.")
    else:
        # Afficher une erreur si le nom d'utilisateur existe déjà
        messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")

    # Fermer la fenêtre de création de compte
    fenetre.destroy()
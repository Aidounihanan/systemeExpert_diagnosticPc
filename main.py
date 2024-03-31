from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel
from login import login, creer_compte  # Importez la fonction creer_compte

def ouvrir_fenetre_creer_compte():
    fenetre_creer_compte = Toplevel()  # Utilisez Toplevel() au lieu de Tk()
    fenetre_creer_compte.title("Créer un compte")
    fenetre_creer_compte.geometry("300x150")

    Label(fenetre_creer_compte, text="Nom d'utilisateur :").grid(row=0, column=0, padx=5, pady=5)
    E1 = Entry(fenetre_creer_compte)
    E1.grid(row=0, column=1, padx=5, pady=5)

    Label(fenetre_creer_compte, text="Mot de passe :").grid(row=1, column=0, padx=5, pady=5)
    E2 = Entry(fenetre_creer_compte, show="*")
    E2.grid(row=1, column=1, padx=5, pady=5)

    bouton_creer = Button(fenetre_creer_compte, text="Créer", command=lambda: creer_compte(E1.get(), E2.get(), fenetre_creer_compte))
    bouton_creer.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def fermer_fenetre(fenetre):
    fenetre.destroy()

# Créez la fenêtre principale
APL = Tk()
APL.geometry('500x500')
APL.title("Système expert d’aide au diagnostic de pannes d’un PC")

# Label et Entry pour l'identifiant
Label(APL, text="Veuillez renseigner votre identifiant:", font=('Arial', 10, 'bold')).pack()
E1 = Entry(APL, justify='center')
E1.pack()
E1.place(x=200, y=100)

# Label et Entry pour le mot de passe
Label(APL, text="Entrez votre mot de passe:", font=('Arial', 10, 'bold')).pack()
E2 = Entry(APL, justify='center', show='*')
E2.pack()
E2.place(x=200, y=150)

# Bouton de validation pour la connexion
btn_connexion = Button(APL, text="Se connecter", bg='black', fg='white', font=('Arial', 10, 'bold'), command=lambda: login(E1, E2))
btn_connexion.pack()
btn_connexion.place(x=230, y=200)

# Bouton pour ouvrir la fenêtre de création de compte
btn_creer_compte = Button(APL, text="Créer un compte", bg='black', fg='white', font=('Arial', 10, 'bold'), command=ouvrir_fenetre_creer_compte)
btn_creer_compte.pack()
btn_creer_compte.place(x=220, y=250)

APL.mainloop()

from tkinter import Button, Tk, messagebox, Entry, Toplevel, Label
from Systeme_Expert import SystemeExpert

# Instanciation du système expert
systeme_expert = SystemeExpert()


def admin_page():
    # Code for admin page goes here
    # Create a new window for the admin page
    admin_window = Tk()
    admin_window.geometry('500x500')
    admin_window.title("Admin Page")

    def afficher_regles():
        # Fonction pour afficher les règles dans une nouvelle fenêtre
        fenetre_regles = Toplevel(admin_window)
        fenetre_regles.title("Règles du Système Expert")
        message = ""

        for idx, regle in enumerate(systeme_expert.regles, start=1):
            conditions = ", ".join(regle["conditions"])
            action = regle["action"]
            message += f"Index de la règle: {idx}\nConditions de la règle: {conditions}\nAction de la règle: {action}\n\n"

        regles_label = Label(fenetre_regles, text=message)
        regles_label.pack()

    def ajouter_regle():
        # Fonction pour ajouter une nouvelle règle à l'ensemble de règles
        def valider_regle():
            conditions = conditions_entry.get().split(";")
            action = action_entry.get()
            new_rule = {"conditions": conditions, "action": action}  # Convertir l'ensemble en une liste
            systeme_expert.ajouter_regle(new_rule)
            messagebox.showinfo("Succès", "La règle a été ajoutée avec succès.")
            fenetre_regle.destroy()
        # Créer une nouvelle fenêtre enfant modale pour saisir les informations de la règle
        fenetre_regle = Toplevel(admin_window)
        fenetre_regle.title("Ajouter une règle")

        # Entrée pour les conditions de la règle
        conditions_label = Label(fenetre_regle, text="Entrez les conditions de la règle (séparées par ';'): ")
        conditions_label.pack()
        conditions_entry = Entry(fenetre_regle)
        conditions_entry.pack()

        # Entrée pour l'action de la règle
        action_label = Label(fenetre_regle, text="Entrez l'action de la règle: ")
        action_label.pack()
        action_entry = Entry(fenetre_regle)
        action_entry.pack()

        # Bouton pour valider la règle
        valider_button = Button(fenetre_regle, text="Valider", command=valider_regle)
        valider_button.pack()

    def modifier_regle():
        # Fonction pour modifier une règle existante dans l'ensemble de règles
        rule_index = int(index_entry.get()) - 1  # Index de la règle à modifier
        if 0 <= rule_index < len(systeme_expert.regles):
            modified_rule = systeme_expert.regles[rule_index]

            def valider_modification():
                conditions = conditions_entry.get().split(";")
                action = action_entry.get()
                modified_rule["conditions"] = set(conditions)
                modified_rule["action"] = action
                messagebox.showinfo("Succès", "La règle a été modifiée avec succès.")
                fenetre_modification.destroy()

            # Créer une nouvelle fenêtre pour modifier les informations de la règle
            fenetre_modification = Toplevel(admin_window)
            fenetre_modification.title("Modifier une règle")

            # Entrée pour les conditions de la règle
            conditions_label = Label(fenetre_modification, text="Modifiez les conditions de la règle (séparées par ';'): ")
            conditions_label.pack()
            conditions_entry = Entry(fenetre_modification)
            conditions_entry.insert(0, ";".join(modified_rule["conditions"]))  # Affiche les conditions actuelles
            conditions_entry.pack()

            # Entrée pour l'action de la règle
            action_label = Label(fenetre_modification, text="Modifiez l'action de la règle: ")
            action_label.pack()
            action_entry = Entry(fenetre_modification)
            action_entry.insert(0, modified_rule["action"])  # Affiche l'action actuelle
            action_entry.pack()

            # Bouton pour valider la modification
            valider_button = Button(fenetre_modification, text="Valider", command=valider_modification)
            valider_button.pack()
        else:
            messagebox.showerror("Erreur", "Index de règle invalide.")

    def supprimer_regle():
        # Fonction pour supprimer une règle de l'ensemble de règles
        rule_index = int(index_entry.get()) - 1  # Index de la règle à supprimer
        if 0 <= rule_index < len(systeme_expert.regles):
            systeme_expert.supprimer_regle(rule_index)
            messagebox.showinfo("Succès", "La règle a été supprimée avec succès.")
        else:
            messagebox.showerror("Erreur", "Index de règle invalide.")

    
    # Create button for viewing rules
    view_button = Button(admin_window, text="Afficher Règles", command=afficher_regles)
    view_button.pack()

    # Create button for adding a rule
    add_button = Button(admin_window, text="Ajouter Règle", command=ajouter_regle)
    add_button.pack()

    # Entry for rule index in modify/delete operations
    index_label = Label(admin_window, text="Indice de règle a modifier ou a supprimer: ")
    index_label.pack()
    index_entry = Entry(admin_window)
    index_entry.pack()

    # Create button for modifying a rule
    modify_button = Button(admin_window, text="Modifier Règle", command=modifier_regle)
    modify_button.pack()

    # Create button for deleting a rule
    delete_button = Button(admin_window, text="Supprimer Règle", command=supprimer_regle)
    delete_button.pack()

    # Create button to close the admin window
    close_button = Button(admin_window, text="OK", command=admin_window.destroy)
    close_button.pack()

    admin_window.mainloop()

if __name__ == "__main__":
    admin_page()

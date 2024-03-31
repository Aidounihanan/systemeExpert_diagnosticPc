from tkinter import Button, Entry, Label, Tk, messagebox
from Systeme_Expert import SystemeExpert

# Instanciation du système expert
systeme_expert = SystemeExpert()

def diagnose_pc():
    # Fonction pour soumettre les symptômes et diagnostiquer le PC
    def submit_symptoms():
        symptoms = symptoms_entry.get()
        diagnosis_result = systeme_expert.diagnostiquer_pc(symptoms)
        messagebox.showinfo("Résultat du diagnostic", diagnosis_result)

    # Créer une nouvelle fenêtre pour la page de diagnostic
    diagnose_window = Tk()
    diagnose_window.geometry('500x500')
    diagnose_window.title("Page de diagnostic")

    # Demander à l'utilisateur d'entrer les symptômes
    symptoms_label = Label(diagnose_window, text="Entrez les symptômes (séparés par une virgule): ")
    symptoms_label.pack()

    symptoms_entry = Entry(diagnose_window)
    symptoms_entry.pack()

    # Créer un bouton pour soumettre les symptômes et diagnostiquer le PC
    submit_button = Button(diagnose_window, text="Soumettre", command=submit_symptoms)
    submit_button.pack()

    # Exécuter la fenêtre de la page de diagnostic
    diagnose_window.mainloop()

# Exécuter la page de diagnostic
if __name__ == "__main__":   
    diagnose_pc()

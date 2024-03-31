import json
from tkinter import messagebox

class SystemeExpert:
    def __init__(self):
        self.faits = set()  # Utilisation d'un ensemble pour éviter les doublons
        self.charger_regles_depuis_fichier("Regles.json")

    def charger_regles_depuis_fichier(self, nom_fichier):
        try:
            with open(nom_fichier, 'r') as fichier:
                self.regles = json.load(fichier)
            
            # Convertir les ensembles de conditions en listes
            for regle in self.regles:
                regle["conditions"] = set(regle["conditions"])

        except FileNotFoundError:
            messagebox.showerror("Erreur", f"Le fichier {nom_fichier} n'a pas été trouvé.")
        except json.JSONDecodeError:
            messagebox.showerror("Erreur", f"Le fichier {nom_fichier} n'est pas au format JSON valide.")

    def sauvegarder_regles(self):
        with open('Regles.json', 'w') as f:
            json.dump(self.regles, f, indent=4)

    def ajouter_regle(self, nouvelle_regle):
        # Convertir les ensembles de conditions en listes
        for regle in self.regles:
            regle["conditions"] = list(regle["conditions"])
        self.regles.append(nouvelle_regle)
        self.sauvegarder_regles()

    def modifier_regle(self, indice_regle, nouvelle_regle):
        self.regles[indice_regle] = nouvelle_regle

    def supprimer_regle(self, indice_regle):
        del self.regles[indice_regle]

    def ajouter_fait(self, fait):
        self.faits.update(fait)

    def diagnostiquer_pc(self, symptomes):
        symptomes = set(symptomes)  # Convertir en ensemble pour faciliter la comparaison
        organes_defectueux = []
        for regle in self.regles:
            if set(regle["conditions"]).issubset(symptomes):
                organes_defectueux.append(regle["action"])
        return ", ".join(organes_defectueux) if organes_defectueux else "Aucun problème détecté."

    def afficher_regles_faits(self):
        message = "Règles du système expert :\n\n"
        for idx, regle in enumerate(self.regles, start=1):
            conditions = ", ".join(regle["conditions"])
            action = regle["action"]
            message += f"Règle {idx}: Si {conditions}, alors {action}.\n"
        
        message += "\nFaits enregistrés :\n\n"
        if self.faits:
            message += ", ".join(self.faits)
        else:
            message += "Aucun fait enregistré pour le moment."
        
        messagebox.showinfo("Règles et Faits du Système Expert", message)

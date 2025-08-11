import tkinter as tk

class PagePaiement(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Gestion de Paie", font=("Arial", 18)).pack(pady=10)
        tk.Button(self, text="Voir Historique des Paiements", command=self.voir_historique).pack(pady=5)
        tk.Button(self, text="Calculer un Paiement", command=self.calculer_paiement).pack(pady=5)
        tk.Button(self, text="Retour à l'accueil", command=lambda: controller.afficher_page("PageAccueil")).pack(pady=20)

    def voir_historique(self):
        print("Affichage de l'historique...")

    def calculer_paiement(self):
        print("Calcul du paiement...")
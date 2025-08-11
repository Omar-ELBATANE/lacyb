import tkinter as tk

class PageClient(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Gestion des Clients", font=("Arial", 18)).pack(pady=10)
        tk.Button(self, text="Ajouter un Client", command=self.ajouter_client).pack(pady=5)
        tk.Button(self, text="Supprimer un Client", command=self.supprimer_client).pack(pady=5)
        tk.Button(self, text="Rechercher un Client", command=self.rechercher_client).pack(pady=5)
        tk.Button(self, text="Retour à l'accueil", command=lambda: controller.afficher_page("PageAccueil")).pack(pady=20)

    def ajouter_client(self):
        print("Ajout d'un client...")

    def supprimer_client(self):
        print("Suppression d'un client...")

    def rechercher_client(self):
        print("Recherche d'un client...")
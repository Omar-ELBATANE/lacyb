import tkinter as tk
from gui.client import PageClient
from gui.paiement import PagePaiement

def lancer_interface():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logiciel de Paie Cyber")
        self.geometry("800x600")

        # Dictionnaire de pages
        self.pages = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        for Page in (PageAccueil, PageClient, PagePaiement):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.afficher_page("PageAccueil")

    def afficher_page(self, nom_page):
        page = self.pages[nom_page]
        page.tkraise()

class PageAccueil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Bienvenue au Logiciel de Paie Cyber", font=("Arial", 20)).pack(pady=20)
        tk.Button(self, text="Gérer les Clients", command=lambda: controller.afficher_page("PageClient")).pack(pady=10)
        tk.Button(self, text="Gestion de Paie", command=lambda: controller.afficher_page("PagePaiement")).pack(pady=10)

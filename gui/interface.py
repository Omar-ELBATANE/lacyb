import tkinter as tk

def lancer_interface():
    fenetre = tk.Tk()
    fenetre.title("Logiciel de Paie Cyber")
    fenetre.geometry("900x700")  # ← Taille personnalisée

    tk.Label(fenetre, text="Nom du client").pack()
    entry_nom = tk.Entry(fenetre)
    entry_nom.pack()

    tk.Label(fenetre, text="Durée (minutes)").pack()
    entry_duree = tk.Entry(fenetre)
    entry_duree.pack()

    def valider():
        nom = entry_nom.get()
        duree = entry_duree.get()
        print(f"Client: {nom}, Durée: {duree} minutes")

    tk.Button(fenetre, text="Valider", command=valider).pack()

    fenetre.mainloop()

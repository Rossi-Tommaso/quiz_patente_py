import tkinter as tk
from tkinter import font

class GridExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Esempio Grid")
        self.root.geometry("600x400")

        # Creazione di un font personalizzato
        self.text_font = font.Font(family="Arial", size=14)

        # Creazione dei widget con il metodo grid()
        tk.Label(root, text="Nome:", font=self.text_font).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_nome = tk.Entry(root, font=self.text_font)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        tk.Label(root, text="Cognome:", font=self.text_font).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_cognome = tk.Entry(root, font=self.text_font)
        self.entry_cognome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        tk.Button(root, text="Invia", font=self.text_font, command=self.stampa_dati).grid(row=2, column=0, columnspan=2, pady=20)

    def stampa_dati(self):
        nome = self.entry_nome.get()
        cognome = self.entry_cognome.get()
        print(f"Nome: {nome}, Cognome: {cognome}")

root = tk.Tk()
app = GridExample(root)
root.mainloop()

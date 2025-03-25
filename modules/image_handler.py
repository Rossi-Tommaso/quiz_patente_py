# modules/image_button.py
import tkinter as tk
from PIL import Image, ImageTk

def image_button(master, image_path, text, compound="top"):
    try:
        img = Image.open(image_path)
        tk_img = ImageTk.PhotoImage(img)
        button = tk.Button(master, image=tk_img, text=text, compound=compound)
        button.image = tk_img # Mantiene una referenza all'immagine
        return button

    except Exception as e:
        print(f"Errore nel caricamento dell'immagine (nella funzione image_button): {e}")


def image_label(master, image_path, w, h):
    try:
        image = Image.open(image_path)
        image = image.resize((350, 350), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)
        img_label = tk.Label(master, image=img)
        img_label.image = img # Mantiene una referenza all'immagine
        return img_label

    except Exception as e:
        print(f"Errore nel caricamento dell'immagine (nella funzione image_label): {e}")



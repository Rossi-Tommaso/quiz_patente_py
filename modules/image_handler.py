import tkinter as tk
from PIL import Image, ImageTk

def image_button(master, image_path, text, compound="top", w=None, h=None, tp=0):
    try:
        img = Image.open(image_path)
        
        if(w != None or h != None):
            img = img.resize((w, h), Image.Resampling.LANCZOS)
            
        tk_img = ImageTk.PhotoImage(img)

        button = None
        if tp == 1:
            button = tk.Checkbutton(master, image=tk_img, text=text, compound=compound)
        elif tp == 2:
            button = tk.Radiobutton(master, image=tk_img, text=text, compound=compound)
        else:
            button = tk.Button(master, image=tk_img, text=text, compound=compound)
        button.image = tk_img # Mantiene una referenza all'immagine
        return button

    except Exception as e:
        print(f"Errore nel caricamento dell'immagine (nella funzione image_button): {e}")


def image_label(master, image_path, w, h):
    try:
        image = Image.open(image_path)
        image = image.resize((w, h), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)
        img_label = tk.Label(master, image=img)
        img_label.image = img # Mantiene una referenza all'immagine
        return img_label

    except Exception as e:
        print(f"Errore nel caricamento dell'immagine (nella funzione image_label): {e}")



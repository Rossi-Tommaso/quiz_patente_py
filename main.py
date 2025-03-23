import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk


domande = [
        {
        "domanda": "È possibile guidare con la patente scaduta entro 30 giorni dalla data di scadenza",
        "risposta": False,
        "path": "/images/quiz/patente_scaduta.jpg"
}
]

class Page:
    def __init__(self, root):
        # Inizializzazione finestra principale
        self.root = root
        self.root.title('Quiz Patente')
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)

        # Fonts
        self.title = font.Font(family="Arial", size=70, weight='bold')
        self.subtitle = font.Font(family="Arial", size=30)
        self.text = font.Font(family="Arial", size=20)

        # Generazione oggetti pagina iniziale
        tk.Label(root, text="Quiz Patente", font=self.title).pack(pady=10)
        tk.Label(root, text='Inizia il quiz cliccando il pulsante', font=self.subtitle).pack(pady=20)
        tk.Button(root, text="Inizia", font=self.text, command=self.inizia_quiz).pack(pady=20)

    def inizia_quiz(self):
        # Nasconde la finestra principale
        self.root.withdraw()

        # Inizializzazione pagina quiz
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title('Quiz Patente')
        self.quiz_window.geometry('1024x768')
        self.quiz_window.configure(bg='#f0f0f0')  # Sfondo grigio chiaro

        # Frame per il contenuto
        content_frame = tk.Frame(self.quiz_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Intestazione
        header_frame = tk.Frame(content_frame, bg='#3498db')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        quiz_title = tk.Label(header_frame, text="QUIZ PATENTE", font=("Arial", 24, "bold"), bg='#3498db', fg='white')
        quiz_title.pack(pady=15)
        
        # Frame per l'immagine
        self.img_frame = tk.Frame(content_frame, bg='white', height=300)
        self.img_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Placeholder per l'immagine
        self.img_label = tk.Label(self.img_frame, bg='white')
        self.img_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Counter domande
        self.counter_frame = tk.Frame(content_frame, bg='#f0f0f0')
        self.counter_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.question_counter = tk.Label(
            self.counter_frame, 
            text="Domanda 1/50", 
            font=("Arial", 14), 
            bg='#f0f0f0'
        )
        self.question_counter.pack(side=tk.LEFT)
        
        self.score_label = tk.Label(self.counter_frame, text="Punteggio: 0/0", font=("Arial", 14), bg='#f0f0f0')
        self.score_label.pack(side=tk.RIGHT)
        
        # Domanda
        self.domanda_frame = tk.Frame(content_frame, bg='#e8e8e8', bd=1, relief=tk.SOLID)
        self.domanda_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.domanda = tk.Label(self.domanda_frame, text="", font=("Arial", 16), bg='#e8e8e8', justify=tk.LEFT, padx=15, pady=15)
        self.domanda.pack(fill=tk.X)
        
        # Frame per le risposte
        self.risposte_frame = tk.Frame(content_frame, bg='#f0f0f0')
        self.risposte_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Pulsanti per le risposte (Vero/Falso)
        self.btn_vero = tk.Button(
            self.risposte_frame,
            text="VERO",
            font=("Arial", 16, "bold"),
            bg='#27ae60',
            fg='white',
            activebackground='#2ecc71',
            activeforeground='white',
            padx=30,
            pady=15,
            command=lambda: self.verifica_risposta(True)
        )
        self.btn_vero.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill=tk.X)
        
        self.btn_falso = tk.Button(
            self.risposte_frame,
            text="FALSO",
            font=("Arial", 16, "bold"),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            activeforeground='white',
            padx=30,
            pady=15,
            command=lambda: self.verifica_risposta(False)
        )
        self.btn_falso.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill=tk.X)

root = tk.Tk()
app = Page(root)
root.mainloop() 
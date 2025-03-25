import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from modules.image_handler import image_button, image_label

class Page:
    #colors
    __primaryColor = '#2E3440'
    __secondaryColor = '#5E81AC'
    __tertiaryColor = '#88C0D0'
    __hoverColor = '#81A1C1'
    __textColor = '#D8DEE9'

    def __init__(self, root):
        self.root = root
        self.root.title('Quiz Patente')
        self.root.geometry("1920x1080")
        self.root.configure(bg=self.__primaryColor)
        self.root.resizable(False, False)

        #fonts
        fontTitle = font.Font(family="Arial", size=70, weight='bold')
        fontSubtitle = font.Font(family="Arial", size=30)
        fontTextBold = font.Font(family="Arial", size=20, weight='bold')
        fontInfo = font.Font(family="Arial", size=18, slant='italic')

        # Generazione oggetti pagina iniziale
        title = tk.Label(root, text="Quiz Patente B", font=fontTitle, bg=self.__primaryColor, fg=self.__tertiaryColor)
        title.place(rely=0.05, relx=0.5, anchor='center')
        
        # Testo introduttivo
        intro = tk.Label(root, text="Preparati al meglio per il tuo esame con domande aggiornate!", font=fontSubtitle, bg=self.__primaryColor, fg=self.__textColor)
        intro.place(rely=0.16, relx=0.5, anchor='center')

        # immagine decorativa
        image = image_label(self.root, './assets/icons/quiz_decorative_image.png', 400, 400)
        image.config(bg=self.__primaryColor)
        image.place(relx=0.5, rely=0.385, anchor='center')

        subtitle = tk.Label(root, text='Inizia il quiz cliccando il pulsante', font=fontSubtitle, bg=self.__primaryColor, fg=self.__textColor)
        subtitle.place(rely=0.60, relx=0.5, anchor='center')

        # Generazione pulsanti (allenamento e simulazione)
        simulationButton = image_button(root, './assets/icons/Simulazione.png', 'Inizia simulazione', 'left')
        simulationButton.config(
            bg=self.__tertiaryColor,
            fg=self.__textColor,
            font=fontTextBold,
            width=400, height=90,
            activebackground=self.__hoverColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.inizia_simulazione
        )
        simulationButton.place(relx=0.65, rely=0.75, anchor='center')

        praticleButton = image_button(root, './assets/icons/Esercitazione.png', 'Vai alla pratica', 'left')
        praticleButton.config(
            bg=self.__textColor,
            fg=self.__tertiaryColor,
            font=fontTextBold,
            width=400,
            height=90,
            activebackground=self.__hoverColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.inizia_pratica
        )
        praticleButton.place(relx=0.35, rely=0.75, anchor='center')

        # footer
        footer = tk.Label(root, text="Quiz aggiornato al 2025 - basato sull'attuale codice della strada", font=fontInfo, bg=self.__secondaryColor, fg=self.__textColor, padx=10, pady=5)
        footer.place(relx=0.5, rely=0.95, anchor='center')

    def inizia_simulazione(self):
        # Nasconde la finestra principale
        self.root.withdraw()

        # Inizializzazione pagina quiz
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title('Quiz Patente')
        self.quiz_window.geometry('1920x1080')
        self.quiz_window.configure(bg='#f0f0f0')  # Sfondo grigio chiaro
        self.quiz_window.resizable(False, False)
        self.risposte_frame = tk.Frame(self.quiz_window, bg='#f0f0f0')
        self.risposte_frame.pack(pady=20)

    def inizia_pratica(self):
        # Nasconde la finestra principale
        self.root.withdraw()

        # Inizializzazione pagina quiz
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title('Quiz Patente')
        self.quiz_window.geometry('1920x1080')
        self.quiz_window.configure(bg='#f0f0f0')  # Sfondo grigio chiaro
        self.quiz_window.resizable(False, False)
        self.risposte_frame = tk.Frame(self.quiz_window, bg='#f0f0f0')
        self.risposte_frame.pack(pady=20)

root = tk.Tk()
app = Page(root)
root.mainloop() 
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from modules.image_handler import image_button, image_label
from modules.carica_domande import randomize_30_questions

class Page:
    #colors
    __primaryColor = '#2E3440'
    __secondaryColor = '#5E81AC'
    __tertiaryColor = '#88C0D0'
    __hoverColor = '#81A1C1'
    __textColor = '#D8DEE9'
    __falseColor = '#c1121f'
    __trueColor = '#70e000'
    __simulationQuestionNumber = 0

    def __init__(self, root):
        self.root = root
        self.root.title('Quiz Patente')
        self.root.geometry("1920x1080")
        self.root.configure(bg=self.__primaryColor)
        self.root.resizable(False, False)

        #fonts
        self.fontTitle = font.Font(family="Arial", size=70, weight='bold')
        self.fontSubtitle = font.Font(family="Arial", size=30)
        self.fontTextBold = font.Font(family="Arial", size=20)
        self.fontText = font.Font(family="Arial", size=20, weight='bold')
        self.fontInfo = font.Font(family="Arial", size=18, slant='italic')

        # Generazione oggetti pagina iniziale
        title = tk.Label(root, text="Quiz Patente B", font=self.fontTitle, bg=self.__primaryColor, fg=self.__tertiaryColor)
        title.place(rely=0.05, relx=0.5, anchor='center')
        
        # Testo introduttivo
        intro = tk.Label(root, text="Preparati al meglio per il tuo esame con domande aggiornate!", font=self.fontSubtitle, bg=self.__primaryColor, fg=self.__textColor)
        intro.place(rely=0.16, relx=0.5, anchor='center')

        # immagine decorativa
        image = image_label(self.root, './assets/icons/quiz_decorative_image.png', 400, 400)
        image.config(bg=self.__primaryColor)
        image.place(relx=0.5, rely=0.385, anchor='center')

        subtitle = tk.Label(root, text='Inizia il quiz cliccando il pulsante', font=self.fontSubtitle, bg=self.__primaryColor, fg=self.__textColor)
        subtitle.place(rely=0.60, relx=0.5, anchor='center')

        # Generazione pulsanti (allenamento e simulazione)
        simulationButton = image_button(root, './assets/icons/Simulazione.png', 'Inizia simulazione', 'left')
        simulationButton.config(
            bg=self.__tertiaryColor,
            fg=self.__textColor,
            font=self.fontTextBold,
            width=400, height=90,
            activebackground=self.__hoverColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.startSimulation
        )
        simulationButton.place(relx=0.65, rely=0.75, anchor='center')

        praticleButton = image_button(root, './assets/icons/Esercitazione.png', 'Vai alla pratica', 'left')
        praticleButton.config(
            bg=self.__textColor,
            fg=self.__tertiaryColor,
            font=self.fontTextBold,
            width=400,
            height=90,
            activebackground=self.__hoverColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.startPraticle
        )
        praticleButton.place(relx=0.35, rely=0.75, anchor='center')

        # Generazione footer
        footer = tk.Label(root, text="Quiz aggiornato al 2025 - basato sull'attuale codice della strada", font=self.fontInfo, bg=self.__secondaryColor, fg=self.__textColor, padx=10, pady=5)
        footer.place(relx=0.5, rely=0.95, anchor='center')

    def startSimulation(self):
        # Nasconde la finestra principale
        self.root.withdraw()

        # Inizializzazione pagina quiz
        self.quizWindow = tk.Toplevel(self.root)
        self.quizWindow.geometry('1920x1080')
        self.quizWindow.configure(bg=self.__primaryColor) 
        self.quizWindow.resizable(False, False)
        
        # Carico le domande
        self.simulationQuestion = randomize_30_questions()

        # Generazione frame per domanda e immagine
        quizFrame = tk.Frame(self.quizWindow, bg=self.__hoverColor, width=1880, height=920)
        quizFrame.place(x=20, y=20)
        
        # Generazione oggetti per il quiz frame
        questionNumber = tk.Label(quizFrame, text=f'Domanda {self.__simulationQuestionNumber + 1}', font=self.fontTitle, fg=self.__primaryColor, bg=self.__hoverColor)
        questionNumber.place(rely=0.1, relx=0.5, anchor='center')

        image = image_label(quizFrame, 'assets/pericolo/curva_pericolosa_destra.png', 500, 500)
        image.place(relx=0.05, rely=0.55, anchor="w")

        questionLabel = tk.Label(quizFrame, font=self.fontText, bg=self.__hoverColor, wraplength=1000)
        questionLabel.place(relx=0.34, rely=0.5, anchor='w')
        self.setQuestion(self.simulationQuestion, questionLabel)
        
        vero = tk.Button(quizFrame, text="V", font=self.fontTextBold, bg=self.__trueColor, width=10, height=2)
        vero.place(relx=0.75, rely=0.9, anchor='center')

        falso = tk.Button(quizFrame, text="F", font=self.fontTextBold, bg=self.__falseColor, width=10, height=2)
        falso.place(relx=0.9, rely=0.9, anchor='center')
        
        # Generazione Home button
        homeButton = image_button(self.quizWindow, './assets/icons/home.png', '', 'center', 30,30)
        homeButton.config(
            bg=self.__textColor,
            fg=self.__tertiaryColor,
            font=self.fontTextBold,
            width=40,
            height=40,
            activebackground=self.__hoverColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.returnToRoot
        )
        homeButton.place(relx=0.97, rely=0.05, anchor='center')

    def setQuestion(self, questArr, widget):
        self.domanda = questArr[self.__simulationQuestionNumber]['domanda']
        
        widget.config(text=self.domanda)
    
    def startPraticle(self):
        # Nasconde la finestra principale
        self.root.withdraw()

        # Inizializzazione pagina quiz
        self.quizWindow = tk.Toplevel(self.root)
        self.quizWindow.title('Quiz Patente')
        self.quizWindow.geometry('1920x1080')
        self.quizWindow.configure(bg=self.__primaryColor)
        self.quizWindow.resizable(False, False)
        

    def returnToRoot(self):
        self.quizWindow.destroy()
        self.root.deiconify()

root = tk.Tk()
app = Page(root)
root.mainloop() 
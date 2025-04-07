import tkinter as tk
from tkinter import font, messagebox
from modules.image_handler import image_button, image_label
from modules.carica_domande import randomize_30_questions, extract_arguments, get_argument_question

class Page:
    #colors
    __primaryColor = '#0D0D0D'        # Nero profondo
    __secondaryColor = '#1A1A1A'      # Grigio molto scuro
    __tertiaryColor = '#FFD700'       # Oro
    __hoverColor = '#FFC300'          # Oro più chiaro per hover
    __textColor = '#FFFFFF'           # Testo bianco
    __falseColor = '#8B0000'          # Rosso scuro per "Falso"
    __trueColor = '#006400'           # Verde scuro per "Vero"
    __questionNumber = 0
    __question = None

    def __init__(self, root):
        self.root = root
        self.root.title('Quiz Patente')
        self.root.geometry("1920x1080")
        self.root.configure(bg=self.__primaryColor)
        self.root.resizable(False, False)

        #fonts
        self.fontTitle = font.Font(family="Arial", size=70, weight='bold')
        self.fontSubtitle = font.Font(family="Arial", size=30)
        self.fontTextBold = font.Font(family="Arial", size=20, weight='bold')
        self.fontText = font.Font(family="Arial", size=20)
        self.fontFooter = font.Font(family="Arial", size=18, slant='italic')
        self.fontInfo = font.Font(family="Courier", size=26, slant='italic')

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
            activebackground=self.__primaryColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.startSimulation
        )
        simulationButton.place(relx=0.65, rely=0.75, anchor='center')

        praticleButton = image_button(root, './assets/icons/Esercitazione.png', 'Vai alla pratica', 'left')
        praticleButton.config(
            bg=self.__secondaryColor,
            fg=self.__tertiaryColor,
            font=self.fontTextBold,
            width=400,
            height=90,
            activebackground=self.__primaryColor,
            activeforeground=self.__textColor,
            highlightthickness=3,
            highlightbackground=self.__secondaryColor,
            command=self.startPraticle
        )
        praticleButton.place(relx=0.35, rely=0.75, anchor='center')

        # Generazione footer
        footer = tk.Label(root, text="Quiz aggiornato al 2025 - basato sull'attuale codice della strada", font=self.fontFooter, bg=self.__secondaryColor, fg=self.__textColor, padx=10, pady=5)
        footer.place(relx=0.5, rely=0.95, anchor='center')

    def startSimulation(self):
        # Inizializzazione nuova pagina
        self.root.withdraw()
        self.quizWindow = tk.Toplevel(self.root)
        self.quizWindow.geometry('1920x1080')
        self.quizWindow.configure(bg=self.__primaryColor) 
        
        if self.__question == None:
            # Inizializzazione quiz
            self.remaining_time = 30 * 60
            self.__question = randomize_30_questions()
            
            # Generazione widget informativi
            self.questionNumber = tk.Label(self.quizWindow, text='Simulazione Esame', font=self.fontTitle, fg=self.__hoverColor, bg=self.__primaryColor)
            self.questionNumber.place(rely=0.05, relx=0.5, anchor='center')
            
            self.timerFrame = tk.Frame(self.quizWindow, bg=self.__secondaryColor, width=200, height=80, highlightthickness=2, highlightbackground=self.__tertiaryColor)
            self.timerFrame.place(relx=0.015, rely=0.03, anchor='w')

            self.timer_label = tk.Label(self.timerFrame, text="", font=self.fontInfo,fg=self.__textColor, bg=self.__secondaryColor)
            self.timer_label.pack(expand=True)            

            self.update_timer()
        
        self.questionInfoFrame = tk.Frame(self.quizWindow, bg=self.__secondaryColor, width=200, height=80, highlightthickness=2, highlightbackground=self.__tertiaryColor)
        self.questionInfoFrame.place(relx=0.015, rely=0.12, anchor='w')
    
        self.questionInfo = tk.Label(self.questionInfoFrame, text=f"Domanda {self.__questionNumber+1} di {len(self.__question)}", font=self.fontInfo,fg=self.__textColor, bg=self.__secondaryColor, relief='raised')
        self.questionInfo.pack(expand=True)

        self.homeButton = image_button(self.quizWindow, './assets/icons/home.png', '', 'center', 30, 30)
        self.homeButton.config(bg=self.__textColor, fg=self.__tertiaryColor, font=self.fontTextBold, width=40, height=40,
                          activebackground=self.__hoverColor, activeforeground=self.__textColor,
                          highlightthickness=3, highlightbackground=self.__secondaryColor,
                          command=self.returnToRoot)
        self.homeButton.place(relx=0.97, rely=0.05, anchor='center')

        # Generazione frame per immagini domande e risposte
        self.quizFrame = tk.Frame(self.quizWindow, bg=self.__secondaryColor, width=1690, height=790)
        self.quizFrame.place(relx=0.1, rely=0.53, anchor='w')

        self.setQuestionImage(self.quizFrame)
        
        # Generazione frame per i pulsanti di selezione 
        self.sidebar = tk.Frame(self.quizWindow, bg=self.__primaryColor, width=220, height=500)
        self.sidebar.place(relx=0.01, rely=0.53, anchor='w')

        # Pulstanti per la selezione delle domande
        self.questionButtons = []
        for i in range(len(self.__question)):
            btn = tk.Button(self.sidebar, text=str(i+1), font=self.fontTextBold,
                            bg=self.__secondaryColor, fg=self.__textColor,
                            width=2, height=1, relief='flat', bd=1,
                            activebackground=self.__hoverColor,
                            command=lambda i=i: self.goToQuestion(i))
            row = i // 2
            col = i % 2 
            btn.grid(row=row, column=col, padx=4, pady=4)
            self.questionButtons.append(btn)
            
        # Generazione frame per pulsanti di navigazione
        self.navigationFrame = tk.Frame(self.quizWindow, bg=self.__primaryColor, width=1690, height=80)
        self.navigationFrame.place(relx=0.1, rely=0.95, anchor='w')

        # Generazione widget del Navigation Frame
        prevBtn= image_button(
                self.navigationFrame,
                'assets/icons/arrow_left.png',
                '',
                'top',
                50,
                50
                )
        
        prevBtn.config(
                width=70,
                height=70,
                command=self.prevQuestion,
                font=self.fontTextBold,
                bg=self.__tertiaryColor,
                fg=self.__primaryColor,
                activebackground=self.__hoverColor,
                activeforeground=self.__primaryColor,
                bd=0,
                highlightthickness=2,
                highlightbackground=self.__tertiaryColor
            )
        prevBtn.place(relx=0.35, rely=0.5, anchor='center')
        
        # Pulsanti navigazione e Termina quiz
        self.endBtn = tk.Button(
                self.navigationFrame,
                text="\u2726 Termina quiz \u2726",
                width=20, height=2,
                command=self.confirmEndQuiz, 
                font=self.fontTextBold,
                bg=self.__tertiaryColor,
                fg=self.__primaryColor,
                activebackground=self.__hoverColor,
                activeforeground=self.__primaryColor,
                bd=0,
                highlightthickness=2,
                highlightbackground=self.__tertiaryColor
            )
        self.endBtn.place(relx=0.5, rely=0.5, anchor='center')

        nextBtn = image_button(
                self.navigationFrame,
                'assets/icons/arrow_right.png',
                '',
                'top',
                50,
                50
                )
        
        nextBtn.config(
                command=self.nextQuestion, 
                width=70,
                height=70,
                font=self.fontTextBold,
                bg=self.__tertiaryColor,
                fg=self.__primaryColor,
                activebackground=self.__hoverColor,
                activeforeground=self.__primaryColor,
                bd=0,
                highlightthickness=2,
                highlightbackground=self.__tertiaryColor
            )
        nextBtn.place(relx=0.65, rely=0.5, anchor='center')


    def setQuestionImage(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        self.domanda = self.__question[self.__questionNumber]['domanda']
        self.questionLabel = tk.Label(frame, text=self.domanda, font=self.fontText, bg=self.__secondaryColor,
                                      fg=self.__textColor, wraplength=800, justify='left')
        self.questionLabel.place(relx=0.4, rely=0.5, anchor='w')
        
        self.questionInfo.config(text=f'Domanda {self.__questionNumber+1} di {len(self.__question)}')

        img = self.__question[self.__questionNumber]['img']
        if img:
            self.image = image_label(frame, img, 500, 500)
            self.image.place(relx=0.05, rely=0.5, anchor="w")
        else:
            self.questionLabel.place(relx=0.5, rely=0.5, anchor='center')

        answer = self.__question[self.__questionNumber].get('ris_utente')

        self.veroBtn = tk.Button(frame, text="\u2714 Vero", font=self.fontTextBold,
                                 bg=self.__trueColor, fg=self.__primaryColor,
                                 activebackground=self.__hoverColor, activeforeground=self.__textColor,
                                 relief='raised', bd=3, width=12, height=2, command=self.true)
        self.veroBtn.place(relx=0.75, rely=0.9, anchor='center')

        self.falsoBtn = tk.Button(frame, text="\u2718 Falso", font=self.fontTextBold,
                                  bg=self.__falseColor, fg='white',
                                  activebackground=self.__hoverColor, activeforeground=self.__textColor,
                                  relief='raised', bd=3, width=12, height=2, command=self.false)
        self.falsoBtn.place(relx=0.9, rely=0.9, anchor='center')


        if answer is not None:
            if answer:
                self.veroBtn.config(bg=self.__hoverColor)
                self.falsoBtn.config(bg=self.__falseColor)
            else:
                self.veroBtn.config(bg=self.__trueColor)
                self.falsoBtn.config(bg=self.__hoverColor)
        else:
            self.veroBtn.config(bg=self.__trueColor)
            self.falsoBtn.config(bg=self.__falseColor)
            
    def true(self):
        self.__question[self.__questionNumber]['ris_utente'] = 'True'
        self.questionButtons[self.__questionNumber].config(bg=self.__trueColor)
        if self.__questionNumber < 30:
            self.__questionNumber += 1
        
        if self.__questionNumber < len(self.__question):
            self.setQuestionImage(self.quizFrame)

    def false(self):
        self.__question[self.__questionNumber]['ris_utente'] = 'False'
        self.questionButtons[self.__questionNumber].config(bg=self.__falseColor)
        self.__questionNumber += 1
        if self.__questionNumber < len(self.__question):
            self.setQuestionImage(self.quizFrame)

            
    def prevQuestion(self):
        if self.__questionNumber > 0:
            self.__questionNumber -= 1
            self.setQuestionImage(self.quizFrame)

    def nextQuestion(self):
        if self.__questionNumber < len(self.__question) - 1:
            self.__questionNumber += 1
            self.setQuestionImage(self.quizFrame)

    def confirmEndQuiz(self):
        unanswered = 0 
        
        for i, q in enumerate(self.__question):
            if q.get('ris_utente') is None:
                unanswered += 1

        msg = "Vuoi davvero terminare il quiz?"
        
        if unanswered:
            msg += f"\nAttenzione! Non hai risposto a {unanswered} domanda/e."
        
        confirm = tk.messagebox.askyesno("Conferma", msg)
        if confirm:
            self.quizFinished()
            
    def quizFinished(self):
        for widget in self.quizWindow.winfo_children():
            widget.destroy()
            
        corrette = 0
        for domanda in self.__question:
            if domanda.get('ris_utente') == domanda['risposta']:
                corrette += 1

        totali = len(self.__question)
        errori = totali - corrette
        
        esitoFrame = tk.Frame(self.quizWindow, bg=self.__secondaryColor, width=600, height=800, highlightthickness=2, highlightbackground=self.__tertiaryColor)
        esitoFrame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Titolo
        titleLabel = tk.Label(esitoFrame, text="ESITO", font=self.fontTitle, fg=self.__tertiaryColor, bg=self.__secondaryColor)
        titleLabel.place(relx=0.5, rely=0.15, anchor='center')
        
        
        if len(self.__question) == 30:
            esito = '\u2705 PROMOSSO' if errori <= totali // 3 else '\u274C BOCCIATO'
            coloreEsito = self.__trueColor if esito == '\u2705 PROMOSSO' else self.__falseColor
            
            # Esito (promosso/bocciato)
            esitoLabel = tk.Label(esitoFrame, text=esito, font=("Helvetica", 60, "bold"), fg=coloreEsito, bg=self.__secondaryColor)
            esitoLabel.place(relx=0.5, rely=0.35, anchor='center')
            
            # Commento
            frase = "Ottimo lavoro!" if esito == '\u2705 PROMOSSO' else "Puoi ancora migliorare!"
            fraseLabel = tk.Label(esitoFrame, text=frase, font=self.fontText, fg=self.__textColor, bg=self.__secondaryColor)
            fraseLabel.place(relx=0.5, rely=0.6, anchor='center')

        # Numero di errori
        errorLabel = tk.Label(esitoFrame, text=f"Errori: {errori}", font=self.fontSubtitle, fg=self.__textColor, bg=self.__secondaryColor)
        errorLabel.place(relx=0.5, rely=0.5, anchor='center')


        # Bottone per tornare alla Home
        homeBtn = tk.Button(esitoFrame, text="Torna alla Home", font=self.fontTextBold,
                            bg=self.__tertiaryColor, fg=self.__primaryColor, width=20, height=2,
                            activebackground=self.__hoverColor, activeforeground=self.__primaryColor,
                            command=self.returnToRoot)
        homeBtn.place(relx=0.5, rely=0.75, anchor='center')
        
        # Reset
        self.__question = None
        self.__questionNumber = 0
        
    def goToQuestion(self, index):
        self.__questionNumber = index
        self.setQuestionImage(self.quizFrame)

    def startPraticle(self):
        # Nasconde la finestra principale
        self.root.withdraw()

        # Inizializzazione pagina quiz
        self.selectionWindow = tk.Toplevel(self.root)
        self.selectionWindow.title('Quiz Patente')
        self.selectionWindow.geometry('1920x1080')
        self.selectionWindow.configure(bg=self.__primaryColor)
        self.selectionWindow.resizable(False, False)
        
        # Generazione widget informativi
        self.questionNumber = tk.Label(self.selectionWindow, text='Esercitazioni per Argomento', font=self.fontTitle, fg=self.__hoverColor, bg=self.__primaryColor)
        self.questionNumber.place(rely=0.05, relx=0.5, anchor='center')
        
        # Pulsante per tornare alla home
        self.homeButton = image_button(self.selectionWindow, './assets/icons/home.png', '', 'center', 30, 30)
        self.homeButton.config(bg=self.__textColor, fg=self.__tertiaryColor, font=self.fontTextBold, width=40, height=40,
                          activebackground=self.__hoverColor, activeforeground=self.__textColor,
                          highlightthickness=3, highlightbackground=self.__secondaryColor,
                          command=self.returnToRoot)
        self.homeButton.place(relx=0.97, rely=0.05, anchor='center')
        
        argomenti = extract_arguments()
        self.argumentsFrame = tk.Frame(self.selectionWindow, bg=self.__secondaryColor, width=1500, height=900)
        self.argumentsFrame.place(relx=0.5, rely=0.55, anchor='center')
        
        if argomenti:
            # Pulstanti per la selezione degli argomenti
            self.argumentsButtons = []
            for i,argomento in enumerate(argomenti):
                print(i,argomento)
                argumentBtn = tk.Button(self.argumentsFrame, text=argomento, font=self.fontInfo,
                                bg=self.__tertiaryColor, fg=self.__primaryColor,
                                width=18, height=3, bd=3,
                                activebackground=self.__hoverColor, wraplength=400,
                                command=lambda argomento=argomento, self=self: 
                                    self.startSimulationWArgument(argomento)
                                    )
                row = i // 4
                col = i % 4
                argumentBtn.grid(row=row, column=col, padx=15, pady=15)
                self.argumentsButtons.append(argumentBtn)
    
    def startSimulationWArgument(self, argument): 
        self.__questionNumber = 0
        self.__question = get_argument_question(argument)   
        self.selectionWindow.destroy()
        self.startSimulation()       
    
    def update_timer(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.timer_label.config(text=f"Tempo: {time_str}")

        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.quizWindow.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Tempo scaduto!")


    def returnToRoot(self):
        if hasattr(self, 'quizWindow'):
            self.quizWindow.destroy()
        elif hasattr(self, 'selectionWindow'):
            self.selectionWindow.destroy()
        
        # Reset
        self.__questionNumber = 0
        self.__question = None
        
        self.root.deiconify()

root = tk.Tk()
app = Page(root)
root.mainloop() 
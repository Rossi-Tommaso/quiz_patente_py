import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import os
import json
from PIL import Image, ImageTk

class QuizPatente:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Patente B")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#f5f5f5")
        self.root.resizable(True, True)
        
        # Variabili di controllo
        self.tempo_totale = 30 * 60  # 30 minuti in secondi
        self.tempo_rimasto = self.tempo_totale
        self.timer_attivo = False
        self.domanda_corrente_indice = 0
        self.risposte_utente = {}
        
        # Directory per le immagini
        self.immagini_dir = "immagini_quiz"
        if not os.path.exists(self.immagini_dir):
            os.makedirs(self.immagini_dir)
        
        # Preparazione delle domande
        self.carica_domande()
        
        # Creazione dell'interfaccia
        self.crea_interfaccia()
        
        # Mostra la prima domanda
        self.mostra_domanda(0)
    
    def carica_domande(self):
        # In un'applicazione reale, queste verrebbero caricate da un file JSON o database
        self.domande = [
            {
                "testo": "Il segnale di STOP obbliga a fermarsi e dare precedenza a tutti i veicoli.",
                "immagine": "stop.png",
                "risposta_corretta": True
            },
            {
                "testo": "Il limite di velocità massimo sulle autostrade in Italia è di 140 km/h in condizioni ottimali.",
                "immagine": "autostrada.png",
                "risposta_corretta": False  # È 130 km/h
            },
            {
                "testo": "La striscia continua di mezzeria può essere superata per effettuare un sorpasso se non ci sono veicoli in arrivo.",
                "immagine": "striscia_continua.png",
                "risposta_corretta": False
            },
            {
                "testo": "Questo segnale indica una strada con pavimentazione sdrucciolevole.",
                "immagine": "sdrucciolevole.png",
                "risposta_corretta": True
            },
            {
                "testo": "È consentito utilizzare il telefono cellulare durante la guida se si utilizza un auricolare.",
                "immagine": "cellulare.png",
                "risposta_corretta": True
            },
            {
                "testo": "La patente B consente di guidare motocicli di qualsiasi cilindrata.",
                "immagine": "patente.png",
                "risposta_corretta": False
            },
            {
                "testo": "Questo segnale indica l'obbligo di dare precedenza nei sensi unici alternati.",
                "immagine": "precedenza.png",
                "risposta_corretta": True
            },
            {
                "testo": "I bambini di altezza inferiore a 1,50 m devono essere assicurati con sistemi di ritenuta omologati.",
                "immagine": "bambini.png",
                "risposta_corretta": True
            },
            {
                "testo": "Il triangolo di emergenza deve essere posizionato ad almeno 50 metri dal veicolo in panne sulle strade extraurbane.",
                "immagine": "triangolo.png",
                "risposta_corretta": True
            },
            {
                "testo": "La cintura di sicurezza può non essere allacciata quando si viaggia a velocità inferiore a 30 km/h.",
                "immagine": "cintura.png",
                "risposta_corretta": False
            },
            {
                "testo": "Questo segnale indica un passaggio a livello con barriere.",
                "immagine": "passaggio_livello.png",
                "risposta_corretta": True
            },
            {
                "testo": "È consentito sostare in seconda fila in caso di sosta breve con conducente a bordo.",
                "immagine": "seconda_fila.png",
                "risposta_corretta": False
            },
            {
                "testo": "Questo segnale indica il divieto di transito per i veicoli di massa superiore a 3,5 tonnellate.",
                "immagine": "limite_peso.png",
                "risposta_corretta": True
            },
            {
                "testo": "È consentito sorpassare sulla destra in autostrada se il veicolo che precede ha segnalato l'intenzione di svoltare a sinistra.",
                "immagine": "sorpasso.png",
                "risposta_corretta": False
            },
            {
                "testo": "Il tasso alcolemico massimo consentito per i neopatentati è di 0,5 g/l.",
                "immagine": "alcol.png",
                "risposta_corretta": False  # È 0,0 g/l
            }
        ]
        
        # Creazione di immagini di esempio (in un'app reale, queste esisterebbero già)
        self.crea_immagini_esempio()

    def crea_immagini_esempio(self):
        # Questa funzione simula la creazione di immagini di esempio per il quiz
        # In un'applicazione reale, utilizzeresti immagini reali di segnali stradali
        
        segni = {
            "stop.png": ("rosso", "STOP"),
            "autostrada.png": ("blu", "AUTOSTRADA"),
            "striscia_continua.png": ("bianco", "LINEA CONTINUA"),
            "sdrucciolevole.png": ("giallo", "ATTENZIONE STRADA SDRUCCIOLEVOLE"),
            "cellulare.png": ("rosso", "VIETATO USO CELLULARE"),
            "patente.png": ("bianco", "PATENTE B"),
            "precedenza.png": ("blu", "PRECEDENZA"),
            "bambini.png": ("blu", "BAMBINI A BORDO"),
            "triangolo.png": ("rosso", "TRIANGOLO EMERGENZA"),
            "cintura.png": ("blu", "CINTURA OBBLIGATORIA"),
            "passaggio_livello.png": ("rosso", "PASSAGGIO A LIVELLO"),
            "seconda_fila.png": ("rosso", "DIVIETO DI SOSTA"),
            "limite_peso.png": ("rosso", "LIMITE 3.5t"),
            "sorpasso.png": ("rosso", "DIVIETO SORPASSO"),
            "alcol.png": ("rosso", "ALCOL 0.0")
        }
        
        for filename, (colore, testo) in segni.items():
            percorso = os.path.join(self.immagini_dir, filename)
            
            # Verifica se il file esiste già
            if not os.path.exists(percorso):
                # Crea un'immagine di segnaposto se non esiste
                img = Image.new('RGB', (300, 200), "#ffffff")
                try:
                    from PIL import ImageDraw
                    d = ImageDraw.Draw(img)
                    if colore == "rosso":
                        color_code = "#ff0000"
                    elif colore == "blu":
                        color_code = "#0000ff"
                    elif colore == "giallo":
                        color_code = "#ffcc00"
                    else:
                        color_code = "#000000"
                    
                    # Disegna un cerchio o triangolo per simulare un segnale
                    if "DIVIETO" in testo or colore == "rosso":
                        d.ellipse((50, 50, 250, 150), outline=color_code, width=5)
                    elif "ATTENZIONE" in testo or "giallo" == colore:
                        d.polygon([(150, 50), (50, 150), (250, 150)], outline=color_code, width=5)
                    else:
                        d.rectangle((50, 50, 250, 150), outline=color_code, width=5)
                    
                    # Aggiungi il testo
                    d.text((150, 100), testo, fill=color_code, anchor="mm")
                    
                    # Salva l'immagine
                    img.save(percorso)
                except Exception as e:
                    print(f"Errore nella creazione dell'immagine {filename}: {e}")
    
    def crea_interfaccia(self):
        # Frame principale diviso in 3 sezioni
        self.frame_superiore = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.frame_superiore.pack(fill=tk.X, padx=10, pady=10)
        
        self.frame_centrale = tk.Frame(self.root, bg="#ffffff", highlightbackground="#cccccc", highlightthickness=1)
        self.frame_centrale.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.frame_inferiore = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.frame_inferiore.pack(fill=tk.X, padx=10, pady=10)
        
        # === FRAME SUPERIORE ===
        # Titolo
        self.label_titolo = tk.Label(self.frame_superiore, text="QUIZ PATENTE B", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.label_titolo.pack(side=tk.LEFT, padx=10)
        
        # Frame per il timer e la progressbar
        self.frame_timer = tk.Frame(self.frame_superiore, bg="#f0f0f0")
        self.frame_timer.pack(side=tk.RIGHT, padx=10)
        
        # Timer Label
        self.label_timer = tk.Label(self.frame_timer, text="Tempo: 30:00", font=("Arial", 14), bg="#f0f0f0")
        self.label_timer.pack(anchor=tk.E, pady=(0, 5))
        
        # Progress bar per il tempo
        self.progress_tempo = ttk.Progressbar(self.frame_timer, orient=tk.HORIZONTAL, length=250, mode='determinate', maximum=self.tempo_totale)
        self.progress_tempo.pack(anchor=tk.E)
        
        # === FRAME CENTRALE ===
        # Frame per le domande e le risposte
        self.frame_domanda = tk.Frame(self.frame_centrale, bg="#ffffff", padx=20, pady=20)
        self.frame_domanda.pack(fill=tk.BOTH, expand=True)
        
        # Numero domanda e pulsanti navigazione
        self.frame_navigazione = tk.Frame(self.frame_domanda, bg="#ffffff")
        self.frame_navigazione.pack(fill=tk.X, pady=(0, 10))
        
        self.label_numero_domanda = tk.Label(self.frame_navigazione, text="Domanda 1/15", font=("Arial", 12, "bold"), bg="#ffffff")
        self.label_numero_domanda.pack(side=tk.LEFT)
        
        # Pulsanti navigazione tra domande
        self.frame_nav_buttons = tk.Frame(self.frame_navigazione, bg="#ffffff")
        self.frame_nav_buttons.pack(side=tk.RIGHT)
        
        self.btn_prev = ttk.Button(self.frame_nav_buttons, text="◀ Precedente", state=tk.DISABLED, command=self.domanda_precedente)
        self.btn_prev.pack(side=tk.LEFT, padx=5)
        
        self.btn_next = ttk.Button(self.frame_nav_buttons, text="Successiva ▶", command=self.domanda_successiva)
        self.btn_next.pack(side=tk.LEFT, padx=5)
        
        # Canvas per l'immagine
        self.canvas_immagine = tk.Canvas(self.frame_domanda, width=400, height=250, bg="#ffffff", highlightbackground="#cccccc", highlightthickness=1)
        self.canvas_immagine.pack(pady=10)
        
        # Testo della domanda
        self.label_domanda = tk.Label(self.frame_domanda, text="", font=("Arial", 14), wraplength=800, justify=tk.LEFT, bg="#ffffff", pady=20)
        self.label_domanda.pack(fill=tk.X)
        
        # Frame per le risposte
        self.frame_risposte = tk.Frame(self.frame_domanda, bg="#ffffff")
        self.frame_risposte.pack(fill=tk.X, pady=20)
        
        # Variabile per la risposta selezionata
        self.risposta_var = tk.StringVar(value="")
        
        # Radiobutton per VERO
        self.radio_vero = ttk.Radiobutton(self.frame_risposte, text="VERO", variable=self.risposta_var, value="VERO", 
                                         command=self.salva_risposta)
        self.radio_vero.pack(side=tk.LEFT, padx=(0, 20))
        
        # Radiobutton per FALSO
        self.radio_falso = ttk.Radiobutton(self.frame_risposte, text="FALSO", variable=self.risposta_var, value="FALSO", 
                                          command=self.salva_risposta)
        self.radio_falso.pack(side=tk.LEFT)
        
        # Visualizzazione piccole icone per tutte le domande (mappa navigazione)
        self.frame_mappa = tk.Frame(self.frame_domanda, bg="#f5f5f5", padx=10, pady=10)
        self.frame_mappa.pack(fill=tk.X, pady=10)
        
        self.pulsanti_mappa = []
        for i in range(len(self.domande)):
            btn = ttk.Button(self.frame_mappa, text=str(i+1), width=3, command=lambda idx=i: self.mostra_domanda(idx))
            btn.grid(row=i//10, column=i%10, padx=2, pady=2)
            self.pulsanti_mappa.append(btn)
        
        # === FRAME INFERIORE ===
        # Pulsanti azione
        self.btn_inizia = ttk.Button(self.frame_inferiore, text="INIZIA QUIZ", command=self.inizia_quiz)
        self.btn_inizia.pack(side=tk.LEFT, padx=10)
        
        self.btn_termina = ttk.Button(self.frame_inferiore, text="TERMINA E VALUTA", command=self.termina_quiz)
        self.btn_termina.pack(side=tk.RIGHT, padx=10)
        
        # Checkbox per segnare la domanda per revisione
        self.rivedi_var = tk.BooleanVar(value=False)
        self.check_rivedi = ttk.Checkbutton(self.frame_inferiore, text="Segna per revisione", variable=self.rivedi_var,
                                          command=self.segna_per_revisione)
        self.check_rivedi.pack(side=tk.LEFT, padx=20)
        
        # Etichetta info
        self.label_info = tk.Label(self.frame_inferiore, text="Clicca su INIZIA QUIZ per avviare il timer di 30 minuti", 
                                  bg="#f0f0f0", fg="#666666")
        self.label_info.pack(side=tk.RIGHT, padx=20)
    
    def inizia_quiz(self):
        """Inizia il quiz attivando il timer"""
        self.timer_attivo = True
        self.btn_inizia.config(state=tk.DISABLED)
        self.label_info.config(text="Quiz in corso...")
        
        # Avvia il timer
        self.aggiorna_timer()
    
    def aggiorna_timer(self):
        """Aggiorna il timer ogni secondo"""
        if self.timer_attivo and self.tempo_rimasto > 0:
            self.tempo_rimasto -= 1
            minuti = self.tempo_rimasto // 60
            secondi = self.tempo_rimasto % 60
            self.label_timer.config(text=f"Tempo: {minuti:02d}:{secondi:02d}")
            
            # Aggiorna la barra di progressione
            self.progress_tempo.config(value=self.tempo_rimasto)
            
            # Cambia colore quando mancano meno di 5 minuti
            if self.tempo_rimasto <= 300:
                self.label_timer.config(fg="#ff0000")
            
            # Programma il prossimo aggiornamento
            self.root.after(1000, self.aggiorna_timer)
        elif self.timer_attivo and self.tempo_rimasto <= 0:
            messagebox.showinfo("Tempo Scaduto", "Il tempo è scaduto! Il quiz verrà terminato.")
            self.termina_quiz()
    
    def mostra_domanda(self, indice):
        """Visualizza la domanda specificata"""
        # Aggiorna l'indice corrente
        self.domanda_corrente_indice = indice
        
        # Aggiorna lo stato dei pulsanti di navigazione
        self.btn_prev.config(state=tk.NORMAL if indice > 0 else tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL if indice < len(self.domande) - 1 else tk.DISABLED)
        
        # Aggiorna il numero della domanda
        self.label_numero_domanda.config(text=f"Domanda {indice + 1}/{len(self.domande)}")
        
        # Ottieni la domanda corrente
        domanda = self.domande[indice]
        
        # Aggiorna il testo della domanda
        self.label_domanda.config(text=domanda["testo"])
        
        # Carica e visualizza l'immagine
        self.mostra_immagine(domanda["immagine"])
        
        # Imposta lo stato del radiobutton in base alla risposta precedente
        risposta_salvata = self.risposte_utente.get(indice, None)
        if risposta_salvata is not None:
            self.risposta_var.set("VERO" if risposta_salvata else "FALSO")
        else:
            self.risposta_var.set("")
        
        # Aggiorna lo stato del checkbox per "segna per revisione"
        self.rivedi_var.set(self.pulsanti_mappa[indice].cget("style") == "Accent.TButton")
        
        # Aggiorna lo stile del pulsante nella mappa
        self.aggiorna_stile_pulsante_mappa()
    
    def mostra_immagine(self, nome_file):
        """Carica e visualizza l'immagine nel canvas"""
        percorso_immagine = os.path.join(self.immagini_dir, nome_file)
        
        try:
            # Cancella l'immagine precedente
            self.canvas_immagine.delete("all")
            
            # Carica la nuova immagine se esiste
            if os.path.exists(percorso_immagine):
                img = Image.open(percorso_immagine)
                img = img.resize((380, 230), Image.LANCZOS)
                self.img_tk = ImageTk.PhotoImage(img)
                self.canvas_immagine.create_image(200, 125, image=self.img_tk)
            else:
                # Se l'immagine non esiste, mostra un messaggio
                self.canvas_immagine.create_text(200, 125, text="Immagine non disponibile", fill="#999999")
        except Exception as e:
            print(f"Errore nel caricamento dell'immagine {nome_file}: {e}")
            self.canvas_immagine.create_text(200, 125, text="Errore nel caricamento dell'immagine", fill="#ff0000")
    
    def salva_risposta(self):
        """Salva la risposta dell'utente"""
        risposta = self.risposta_var.get() == "VERO"
        self.risposte_utente[self.domanda_corrente_indice] = risposta
        
        # Aggiorna lo stile del pulsante nella mappa
        self.aggiorna_stile_pulsante_mappa()
    
    def aggiorna_stile_pulsante_mappa(self):
        """Aggiorna lo stile dei pulsanti nella mappa di navigazione"""
        # Reimposta stile di tutti i pulsanti
        for i, btn in enumerate(self.pulsanti_mappa):
            # Verifica se è la domanda corrente
            if i == self.domanda_corrente_indice:
                btn.config(style="Accent.TButton")
            # Verifica se è segnata per revisione
            elif btn.cget("style") == "Accent.TButton" and i != self.domanda_corrente_indice:
                # Mantieni lo stile di revisione
                pass
            # Verifica se ha una risposta
            elif i in self.risposte_utente:
                btn.config(style="")  # Stile normale ma con bordo
            else:
                btn.config(style="")  # Stile normale
    
    def segna_per_revisione(self):
        """Segna o toglie segno per revisione alla domanda corrente"""
        if self.rivedi_var.get():
            self.pulsanti_mappa[self.domanda_corrente_indice].config(style="Accent.TButton")
        else:
            # Ripristina lo stile normale se non è la domanda corrente
            if self.domanda_corrente_indice in self.risposte_utente:
                self.pulsanti_mappa[self.domanda_corrente_indice].config(style="")
            else:
                self.pulsanti_mappa[self.domanda_corrente_indice].config(style="")
    
    def domanda_precedente(self):
        """Passa alla domanda precedente"""
        if self.domanda_corrente_indice > 0:
            self.mostra_domanda(self.domanda_corrente_indice - 1)
    
    def domanda_successiva(self):
        """Passa alla domanda successiva"""
        if self.domanda_corrente_indice < len(self.domande) - 1:
            self.mostra_domanda(self.domanda_corrente_indice + 1)
    
    def termina_quiz(self):
        """Termina il quiz e mostra i risultati"""
        # Ferma il timer
        self.timer_attivo = False
        
        # Conta le risposte corrette
        risposte_corrette = 0
        domande_senza_risposta = []
        
        for i, domanda in enumerate(self.domande):
            if i in self.risposte_utente:
                if self.risposte_utente[i] == domanda["risposta_corretta"]:
                    risposte_corrette += 1
            else:
                domande_senza_risposta.append(i + 1)
        
        # Verifica se ci sono domande senza risposta
        if domande_senza_risposta:
            msg = f"Ci sono {len(domande_senza_risposta)} domande senza risposta:\n"
            msg += ", ".join(map(str, domande_senza_risposta))
            msg += "\n\nVuoi comunque terminare il quiz?"
            
            if not messagebox.askyesno("Domande senza risposta", msg):
                return
        
        # Calcola il punteggio
        punteggio_percentuale = (risposte_corrette / len(self.domande)) * 100
        esito = "SUPERATO" if punteggio_percentuale >= 90 else "NON SUPERATO"
        
        # Mostra il risultato
        msg_risultato = f"Quiz terminato!\n\n"
        msg_risultato += f"Risposte corrette: {risposte_corrette}/{len(self.domande)}\n"
        msg_risultato += f"Punteggio: {punteggio_percentuale:.1f}%\n"
        msg_risultato += f"Esito: {esito}\n\n"
        
        # Tempo utilizzato
        tempo_utilizzato = self.tempo_totale - self.tempo_rimasto
        minuti = tempo_utilizzato // 60
        secondi = tempo_utilizzato % 60
        msg_risultato += f"Tempo utilizzato: {minuti:02d}:{secondi:02d}"
        
        messagebox.showinfo("Risultati Quiz", msg_risultato)
        
        # Chiedi se si vuole rivedere le risposte
        if messagebox.askyesno("Revisione", "Vuoi rivedere le risposte date?"):
            self.mostra_revisione()
        else:
            # Chiudi l'applicazione o reinizializza per un nuovo quiz
            if messagebox.askyesno("Nuovo Quiz", "Vuoi iniziare un nuovo quiz?"):
                self.reset_quiz()
            else:
                self.root.destroy()
    
    def mostra_revisione(self):
        """Mostra la revisione delle risposte"""
        # Crea una nuova finestra
        revisione_window = tk.Toplevel(self.root)
        revisione_window.title("Revisione Quiz")
        revisione_window.geometry("800x600")
        
        # Frame principale
        frame_main = tk.Frame(revisione_window, padx=20, pady=20)
        frame_main.pack(fill=tk.BOTH, expand=True)
        
        # Titolo
        tk.Label(frame_main, text="REVISIONE RISPOSTE", font=("Arial", 16, "bold")).pack(pady=(0, 20))
        
        # Crea un canvas con scrollbar
        canvas = tk.Canvas(frame_main)
        scrollbar = ttk.Scrollbar(frame_main, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mostra le domande e le risposte
        for i, domanda in enumerate(self.domande):
            frame_domanda = ttk.Frame(scrollable_frame)
            frame_domanda.pack(fill=tk.X, pady=10, padx=10)
            
            # Numero domanda
            ttk.Label(frame_domanda, text=f"Domanda {i+1}:", font=("Arial", 12, "bold")).pack(anchor="w")
            
            # Testo domanda
            ttk.Label(frame_domanda, text=domanda["testo"], wraplength=700).pack(anchor="w", pady=(5, 10))
            
            # Risposta utente
            risposta_utente = self.risposte_utente.get(i, None)
            testo_risposta = "Non risposta"
            if risposta_utente is not None:
                testo_risposta = "VERO" if risposta_utente else "FALSO"
            
            # Risposta corretta
            risposta_corretta = "VERO" if domanda["risposta_corretta"] else "FALSO"
            
            # Risultato
            if risposta_utente is None:
                colore = "#999999"  # Grigio per non risposta
                risultato = "Non risposta"
            elif risposta_utente == domanda["risposta_corretta"]:
                colore = "#4CAF50"  # Verde per corretta
                risultato = "Corretta"
            else:
                colore = "#F44336"  # Rosso per errata
                risultato = "Errata"
            
            frame_risposta = ttk.Frame(frame_domanda)
            frame_risposta.pack(fill=tk.X, pady=5)
            
            ttk.Label(frame_risposta, text=f"La tua risposta: {testo_risposta}").pack(side=tk.LEFT, padx=(0, 20))
            ttk.Label(frame_risposta, text=f"Risposta corretta: {risposta_corretta}").pack(side=tk.LEFT, padx=(0, 20))
            ttk.Label(frame_risposta, text=risultato, foreground=colore).pack(side=tk.LEFT)
            
            # Separatore
            ttk.Separator(scrollable_frame, orient="horizontal").pack(fill=tk.X, padx=10, pady=5)
        
        # Pulsante per chiudere
        ttk.Button(frame_main, text="Chiudi", command=revisione_window.destroy).pack(pady=20)
    
    def reset_quiz(self):
        """Resetta il quiz per iniziare di nuovo"""
        # Reimposta variabili
        self.tempo_rimasto = self.tempo_totale
        self.timer_attivo = False
        self.domanda_corrente_indice = 0
        self.risposte_utente = {}
        
        # Reimposta l'interfaccia
        self.label_timer.config(text="Tempo: 30:00", fg="#000000")
        self.progress_tempo.config(value=self.tempo_totale)
        self.btn_inizia.config(state=tk.NORMAL)
        self.label_info.config(text="Clicca su INIZIA QUIZ per avviare il timer di 30 minuti")
        
        # Reimposta lo stile dei pulsanti nella mappa
        for btn in self.pulsanti_mappa:
            btn.config(style="")
        
        # Mostra la prima domanda
        self.mostra_domanda(0)
        
        # Reimposta la risposta selezionata
        self.risposta_var.set("")
        
        # Reimposta il checkbox per la revisione
        self.rivedi_var.set(False)

   
        
def main():
    try:
        from PIL import Image, ImageTk, ImageDraw
    except ImportError:
        messagebox.showerror("Errore", "La libreria PIL/Pillow non è installata. Installa la libreria con 'pip install Pillow'")
        exit(1)
    
    root = tk.Tk()
    # Imposta lo stile per i pulsanti di revisione
    style = ttk.Style()
    style.configure("Accent.TButton", background="#4CAF50", foreground="white")
    
    app = QuizPatente(root)
    root.mainloop()


main()
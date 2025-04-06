import json
import random

PATH = './qna.json'

def randomize_30_questions():
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            domande = json.load(file)
            
        domande_random = random.sample(domande, min(30, len(domande))) 
        return domande_random
    
    except Exception as e:
        print('Errore nel caricamento delle domande:', repr(e))

def extract_arguments():
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            domande = json.load(file)
            arguments = set()
            
            for domanda in domande:
                arguments.add(domanda.get('argomento'))
            
            return list(arguments)
    except Exception as e:
        print('Errore nel estrazione delle domande: ', repr(e))
        
def get_argument_question(argument):
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            domande = json.load(file)
        
        domande_per_argomento = []
        for domanda in domande:
            if domanda['argomento'] == argument:
                domande_per_argomento.append(domanda)
        
        return domande_per_argomento
    
    except Exception as e:
        print('Errore nel caricamento delle domande:', repr(e))
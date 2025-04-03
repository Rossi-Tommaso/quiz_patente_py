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

"""
Programa que escoge al azar 5 palabras en español del mini-diccionario del ejercicio anterior. Se pedirá que el usuario
teclee la traducción al inglés de cada una de las palabras y se comprobará si son correctas. Al final, se mostrará
cuántas respuestas son válidas y cuántas erróneas.

"""
import random

SPANISH_ENGLISH_DICT = {
    "uno": "one", "dos": "two", "tres": "three", "cuatro": "four", "cinco": "five", "seis": "six",
    "siete": "seven", "ocho": "eight", "nueve": "nine", "diez": "ten", "once": "eleven", "doce": "twelve",
    "trece": "thirteen", "catorce": "fourteen", "quince": "fifteen", "dieciséis": "sixteen",
    "diecisiete": "seventeen", "dieciocho": "eighteen", "diecinueve": "nineteen", "veinte": "twenty"
}

NUM_WORDS = 5

list_words_of_all_dict = list(SPANISH_ENGLISH_DICT.keys())
set_words = set()

while len(set_words) != NUM_WORDS:
    word = random.choice(list_words_of_all_dict)
    set_words.add(word)

answer_correct = 0
for n in set_words:
    traduction = input(f"Escribe la traduccion de {n}: ")
    if traduction == SPANISH_ENGLISH_DICT.get(n):
        answer_correct += 1

print(f"Has contestado bien {answer_correct} veces y has fallado {NUM_WORDS-answer_correct}")


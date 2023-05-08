"""
Mini-diccionario español-inglés que contiene 20 palabras (con su correspondiente traducción). El programa pedirá una
palabra en español y dará la correspondiente traducción en inglés.

Autor: Adrián González Martínez.
"""
SPANISH_ENGLISH_DICT = {
    "uno": "one", "dos": "two", "tres": "three", "cuatro": "four", "cinco": "five", "seis": "six",
    "siete": "seven", "ocho": "eight", "nueve": "nine", "diez": "ten", "once": "eleven", "doce": "twelve",
    "trece": "thirteen", "catorce": "fourteen", "quince": "fifteen", "dieciséis": "sixteen",
    "diecisiete": "seventeen", "dieciocho": "eighteen", "diecinueve": "nineteen", "veinte": "twenty"
}


def main():
    print("Diccionario")
    print("-------------")
    spanish_word = ""
    while spanish_word != "fin":
        spanish_word = input("Escribe palabra en español para saber la traducción('fin' para terminar)")
        if spanish_word not in SPANISH_ENGLISH_DICT:
            print("Esta palabra no está no el diccionario")
        else:
            print(SPANISH_ENGLISH_DICT.get(spanish_word))


if __name__ == '__main__':
    main()

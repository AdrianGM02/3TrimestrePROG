from question import Question
from util.menu import Menu

NUM_OPTIONS = 5


def crear_preguntas():
    print("Vamos a crear preguntas: ")
    print("--------------------------")
    numero_preguntas = int(input("Cuantas preguntas se van a crear: "))
    preguntas = []
    for i in range(numero_preguntas):
        statement = input("Indica el enunciado de la pregunta: ")
        titulo = f"Pregunta {i + 1}:"
        opciones = list()
        for j in range(NUM_OPTIONS):
            option_name = input("Indica el nombre de la opcion")
            option_score = int(input("Indica la puntuacion de la opcion"))
            opciones.append((option_name, option_score))
        puntuacion_base = int(input("Introduce la puntuacion de la pregunta(0 para poner la puntuación por defecto): "))
        if puntuacion_base != 0:
            preguntas.append(Question(titulo, statement, opciones, puntuacion_base))
        else:
            preguntas.append(Question(titulo, statement, opciones))


def mostrar_preguntas(lista):
    for i in range(len(lista)):
        print(f"{lista[i].name_question}: {lista[i].statement}")
        for t in range(len(lista[i].choice)):
            print(f"Opcion {t + 1}: {lista[i].choice[t][0]}")
        print("---------------------------------------------")
        elige_opcion = int(input("Elige una opcion(en número): "))
        print(f"La puntuación es: {lista[i].get_score(elige_opcion)}")


def main():
    menu = Menu("Crear Preguntas", "Terminar",
                title="Pregunta")
    while True:
        opc = menu.choose()
        match opc:
            case 1:
                mostrar_preguntas(crear_preguntas())
            case _:
                break
    print("Hasta la próxima :-)")

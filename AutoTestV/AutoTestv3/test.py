from question import Question
from util.menu import Menu
import xml.etree.ElementTree as ET
NUM_OPTIONS = 4


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
            nombre_opcion = input("Indica el nombre de la opcion")
            puntuacion_opcion = int(input("Indica la puntuacion de la opcion"))
            opciones.append((nombre_opcion, puntuacion_opcion))
        puntuacion_base = int(input("Introduce la puntuacion de la pregunta(0 para poner la puntuación por defecto): "))
        if puntuacion_base != 0:
            preguntas.append(Question(titulo, statement, opciones, puntuacion_base))
        else:
            preguntas.append(Question(titulo, statement, opciones))

    return preguntas


def cargar_objeto_desde_xml():
    intentar_si_archivo_existe("file_xml.xml")
    XML_FILE = "file_xml.xml"
    archivo = ET.parse(XML_FILE)
    root = archivo.getroot()

    lista_objetos = []
    for i in range(len(root)):
        titulo = root[i].get('name')
        statement = root[i].find('statement').text.strip()
        opciones = list()
        for r in range(len(root[i][1])):
            opciones.append((root[i][1][r].text.strip(), float(root[i][1][r].get('weight'))))
        puntuacion_base = float(root[i].attrib['base_score'])
        lista_objetos.append(Question(titulo, statement, opciones, puntuacion_base))

    return lista_objetos


def intentar_si_archivo_existe(nombre: str):
    try:
        with open(nombre, "r") as archivo:
            pass
    except FileNotFoundError:
        print("El archivo no existe")


def mostrar_preguntas(lista):
    for i in range(len(lista)):
        print(f"{lista[i].name_question}: {lista[i].statement}")
        for t in range(len(lista[i].choice)):
            print(f"Opcion {t + 1}: {lista[i].choice[t][0]}")
        print("---------------------------------------------")
        elige_opcion = int(input("Elige una opcion(en número): "))
        print(f"La puntuación es: {lista[i].get_score(elige_opcion)}")


def main():
    menu = Menu("Crear Preguntas", "Cargar Preguntas", "Terminar",
                title="Pregunta")
    while True:
        opc = menu.choose()
        match opc:
            case 1:
                mostrar_preguntas(crear_preguntas())
            case 2:
                mostrar_preguntas(cargar_objeto_desde_xml())
            case _:
                break
    print("Hasta la próxima :-)")


if __name__ == '__main__':
    main()

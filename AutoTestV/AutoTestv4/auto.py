"""
Necesitamos crear los ficheros (JSON o XML) donde guardar las preguntas del test. Editarlos directamente puede ser una
labor un poco engorrosa, así que vamos a hacer un programa que nos facilite la tarea.

Nuestro programa mostrará un menú con las siguientes opciones:

1. Crear fichero de test.

Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
Finalmente se creará el fichero correspondiente.
2. Seleccionar fichero de test.

Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.
3. Añadir pregunta al test.

Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
Comprobamos que los datos son correctos, para ello podríamos crear un objeto Question y si no lanza excepción es que
están bien.
Añadimos la pregunta al fichero en el formato que tenga (JSON o XML). HECHO
Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
fichero. HECHO

Autor: Adrián González Martínez

"""
import os
import sys
import xml.etree.ElementTree as ET
import json
from AutoTestv1.question import Question


def crear_fichero():
    nombre = comprobar_si_fichero_esta_bien_escrito()
    if comprobar_si_existe(nombre):
        nombre = opcion_usuario(nombre)
    if ".json" in nombre:
        crear_fichero_json(nombre)
    else:
        crear_fichero_xml(nombre)


def indicar_fichero():
    while True:
        nombre_archivo = input("Cual es el nombre del fichero: ")
        if nombre_archivo.find('.xml') == -1 and nombre_archivo.find('.json') == -1:
            print("El archivo tiene que ser un xml o json")
        else:
            if not comprobar_si_existe(nombre_archivo):
                print("El archivo no existe.")
                return
            else:
                print(f"Archivo {nombre_archivo} cargado.")
                return nombre_archivo


def comprobar_si_existe(nombre_archivo):
    if os.path.exists(nombre_archivo):
        return True
    return False


def opcion_usuario(nombre_archivo):
    while True:
        si_o_no = input("Este archivo ya existe, quieres sobreescribirlo:(S/N)").lower()
        if si_o_no == "s":
            return nombre_archivo
        else:
            print("No se ha sobreescrito el archivo")
            quieres_terminar = input("Quieres terminar o dar un nuevo nombre de fichero:(S/N)").upper()
            if quieres_terminar == "s":
                break
            else:
                nombre_nuevo_archivo = comprobar_si_fichero_esta_bien_escrito()
                return nombre_nuevo_archivo


def comprobar_si_fichero_esta_bien_escrito():
    while True:
        nombre_archivo = input("Cual es el nombre del fichero: ")
        if nombre_archivo.find('.xml') == -1 and nombre_archivo.find('.json') == -1:
            print("No se ha introducido correctamente el formato del archivo")
        else:
            break
    return nombre_archivo


def crear_fichero_xml(nombre_archivo):
    test = ET.Element("test")
    root = ET.ElementTree(test)
    with open(nombre_archivo, "wb") as file:
        root.write(file, encoding="utf-8", xml_declaration=True)


def crear_fichero_json(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        pass


def anadir_pregunta_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    name = input("Escribe el nombre de la pregunta: ")
    statement_text = input("Escribe el statement de la pregunta: ")
    base = input("Escribe la puntuacion que tiene la pregunta")
    list_options = []

    pregunta = ET.Element('question', {'name': name, 'base_score': base})
    statement = ET.SubElement(pregunta, "statement")
    statement.text = statement_text
    options = ET.SubElement(pregunta, "options")
    for o in range(4):
        name_option_text = input("Indica el nombre de la opcion: ")
        score_option = input("Indica la puntuacion de la pregunta: ")
        option = ET.SubElement(options, "option", {'base': score_option})
        option.text = name_option_text
        list_options.append((name_option_text, float(score_option)))
    comprobar_objeto_preguta(name, statement_text, list_options, base)
    root.append(pregunta)
    ET.indent(root, space='    ')
    tree.write(file_name, encoding='unicode')


def anadir_pregunta_json(nombre_fichero):
    name = input("Escribe el nombre de la pregunta: ")
    statement = input("Escribe el statement de la pregunta: ")
    base_score = float(input("Escribe la puntuacion de la pregunta: "))
    options = []
    for o in range(4):
        name_option = input("Escribe el nombre de la opcion: ")
        score_option = float(input("Escribe la puntuacion de la opcion: "))
        options.append((name_option, score_option))

    preguntas = []

    pregunta = {
        "name": name,
        "statement": statement,
        "options": options,
        "base_score": base_score

    }

    if os.stat(nombre_fichero).st_size > 0:
        with open(nombre_fichero, "rt") as fichero:
            data = json.load(fichero)
        preguntas = data
    preguntas.append(pregunta)

    comprobar_objeto_preguta(name, statement, options, base_score)

    with open(nombre_fichero, "wt") as fichero:
        json.dump(preguntas, fichero, indent=1)


def comprobar_objeto_preguta(name, statement, options, base_score):
    try:
        pregunta = Question(name, statement, options, base_score)

    except ValueError:
        print("No se ha podido crear el objeto, las parametros son incorrectos:", file=sys.stderr)
        exit(1)


def anadir_pregunta(nombre):
    if ".json" in nombre:
        anadir_pregunta_json(nombre)
    else:
        anadir_pregunta_xml()

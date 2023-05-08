"""
        Ejercicio 3:
            Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que
            también pasamos como parámetro, de manera que:
            * Si el programa no recibe el número de parámetros adecuado termina con un error 1.
            * Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que
                lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación
                no se haga.
            * Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de
                error y código 2.
            * Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina
                con un mensaje de error y código 3.
            * Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.
    Autor: Adrián González Martínez

"""
import sys
import string
import random


def numero_parametros_adecuado():
    if len(sys.argv) != 3:
        print("El numero de parámetros no es correcto: ", file=sys.stderr)
        sys.exit(1)


def quiere_continuar():
    continuar = input("Solo esta el archivo de origen, si continuas machacaras el archivo(S/N): ")
    if continuar.upper() == "N ":
        sys.exit(2)


def si_fichero_original_no_existe():
    try:
        with open(sys.argv[1], "r") as archivo:
            pass

    except FileNotFoundError:
        print('Error, no se ha encontrado el archivo de origen.', file=sys.stderr)
        sys.exit(2)


def si_fichero_destino_no_se_puede_escribir():
    try:
        with open(sys.argv[2], "w") as archivo:
            pass


    except FileExistsError:
        print("Hay un erro en el archivo destino", file=sys.stderr)
        exit(3)


def encriptar(mensaje: str, clave: int):
    alfabeto = string.ascii_lowercase + string.ascii_uppercase
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) + clave) % len(alfabeto)
            mensaje_cifrado += alfabeto[indice]
        else:
            mensaje_cifrado += letra

    return mensaje_cifrado


def comprobar():
    numero_parametros_adecuado()
    si_fichero_destino_no_se_puede_escribir()
    si_fichero_original_no_existe()


def main():
    comprobar()
    clave = random.randint(1, 9)
    if len(sys.argv) == 2:
        quiere_continuar()
        with open(sys.argv[1], "r") as archivo:
            cadenas = archivo.readlines()
            archivo.close()

        with open(sys.argv[1], "w") as archivo:
            pass

        with open(sys.argv[1], "w") as archivo:
            for cadena in cadenas:
                archivo.write(encriptar(cadena, clave))
    else:
        with open(sys.argv[1], "r") as archivo:
            cadenas = archivo.readlines()

        with open(sys.argv[2], "w") as archivo:
            for cadena in cadenas:
                archivo.write(encriptar(cadena, clave))


if __name__ == '__main__':
    main()

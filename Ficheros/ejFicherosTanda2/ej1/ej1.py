import sys


def ordenar_palabras(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        palabras = sorted(archivo.read().splitlines())

    with open(nombre_archivo, 'w') as archivo_salida:
        for i in palabras:
            archivo_salida.write(palabras[i])

    print(f"El archivo {nombre_archivo} ha sido ordenado alfabéticamente")


if len(sys.argv) > 1:
    nombre_archivo_entrada = sys.argv[1]
    ordenar_palabras(nombre_archivo_entrada)
else:
    print("Debe proporcionar el nombre del archivo como argumento en la línea de comandos.")

"""
3. Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero.
Tanto el nombre del fichero como la palabra se deben pasar como argumentos en la línea de comandos.

"""

import sys
fichero1 = sys.argv[1]

palabra = sys.argv[2]


with open(fichero1, 'rt') as f:
    prueba = f.read()

contador_palabra = prueba.count(palabra)

print(f"En el archivo {fichero1} hay {contador_palabra} ocurrencias de la palabra '{palabra}'")






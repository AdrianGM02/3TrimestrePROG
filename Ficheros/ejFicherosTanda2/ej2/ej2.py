"""

2. Escribe un programa que guarde en un fichero el contenido de otros dos ficheros, de tal forma que en el fichero
resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir, la primera línea será del primer
fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer fichero, etc.

Los nombres de los dos ficheros origen y el nombre del fichero destino se deben pasar como argumentos en la línea
de comandos.

Hay que tener en cuenta que los ficheros de donde se van cogiendo las líneas pueden tener tamaños diferentes.

Autor: Adrián González Martínez


"""

import sys

file_1 = sys.argv[1]
file_2 = sys.argv[2]
file_3 = sys.argv[3]

file1 = open(file_1, "rt")
lines_file1 = file1.readlines()
file1.close()
file2 = open(file_2, "rt")
lines_file2 = file2.readlines()
file2.close()

list_lines = ""
cont = 0

for i in range(0, len(lines_file1) + len(lines_file2)):
    if cont < len(lines_file1):
        list_lines += lines_file1[i]
    if cont < len(lines_file2):
        list_lines += lines_file2[i]
    cont += 1


with open(file_3, "wt") as new_file:
    new_file.writelines(list_lines)
    new_file.close()


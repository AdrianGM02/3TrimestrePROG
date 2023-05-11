"""
Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va extraer del mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

DNI: extrae los DNIs.
IP: extrae las direcciones IP.
MAT: extrae matrículas de coche con formato 0000XXX.
HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza con #.
FEC: extrae fechas con formato dd/mm/aaaa.
TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayusculas y minusculas, numeros, guiones y guiones bajos.
El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.





"""
import sys
import re

diccionario = {'HEX': r'\#[A-F0-9]+\b',
               'IP': r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
               'FEC': r'(([0-2][0-9]|[3][0-1])/([0][1-9]|1[0-2])/(\d{4}))',
               'DNI': r'\d{8}[A-HJ-NP-TV-Z]',
               'MAT': r'\d{4}[A-Z]{3}',
               'TWT': r'\@\w+'

               }


def extraer_informacion():
    comprobar_fichero()
    fichero = sys.argv[1]
    tipo_informacion = sys.argv[2].upper()

    with open(fichero, "rt") as fichero_:
        toda_informacion = fichero_.read()
        informacion_filtrada = re.findall(diccionario.get(tipo_informacion), toda_informacion)

    for i in informacion_filtrada:
        print(f"{tipo_informacion}: {i}")


def comprobar_fichero():
    if len(sys.argv) != 3:
        print("Los párametros no son correctos", file=sys.stderr)
        exit(1)
    if sys.argv[2].upper() not in diccionario.keys():
        print("El tipo de información que has indicado no se puede extraer", file=sys.stderr)
        exit(1)


def main():
    extraer_informacion()


if __name__ == '__main__':
    main()

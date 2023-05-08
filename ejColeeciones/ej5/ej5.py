"""Realiza un programa que sepa decir la capital de un país (en caso de conocer la respuesta) y que, además,
sea capaz de aprender nuevas capitales. En principio, el programa solo conoce las capitales de España, Portugal y
Francia. Estos datos deberán estar almacenados en un diccionario. Los datos sobre capitales que vaya aprendiendo el
programa se deben almacenar en el mismo diccionario. El usuario sale del programa escribiendo la palabra “salir


"""


paises = {"España": 'Madrid', "Portugal": "Lisboa", "Francia": "Paris"}

pais_para_saber_capital = ""

while pais_para_saber_capital.lower != "salir":
    print("PAISES Y CAPITALES")
    print("--------------------")
    pais_para_saber_capital = input("Introduce pais para saber capital(salir para salir): ")
    if pais_para_saber_capital in paises:
        print(f"La capital de {pais_para_saber_capital} es: {paises[pais_para_saber_capital]}")
    else:
        print("Este pais no esta en el diccionario")
        capital = input("Porfavor introduzca su capital para guardar esta informacion en el dic")
        paises[pais_para_saber_capital] = capital

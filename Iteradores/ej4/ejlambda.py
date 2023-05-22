# Definición de la clase Objeto
class Objeto:
    def __init__(self, number):
        self.number = number


# Creación de la lista de objetos
objetos = [Objeto(5), Objeto(2), Objeto(7), Objeto(1)]

# Ordenar la lista de objetos según el atributo "number"
objetos_ordenados = sorted(objetos, key=lambda x: x.number)

# Imprimir la lista ordenada
for objeto in objetos_ordenados:
    print(objeto.number)

"""Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra.
Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto,
deberás crear la clase Elemento. Cada elemento del carrito deberá contener el nombre del producto, su precio y la
cantidad (número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal
como la salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal."""


class Elemento:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value

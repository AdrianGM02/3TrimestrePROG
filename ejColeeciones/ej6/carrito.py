"""Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra.
Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto,
deberás crear la clase Elemento. Cada elemento del carrito deberá contener el nombre del producto, su precio y la
cantidad (número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal
como la salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal."""

from elemento import Elemento


class Carrito:
    def __init__(self):
        self.__lista = []

    def agregar(self, elemento: Elemento):
        if not self.__anadir_unidades(elemento):
            self.__lista.append(elemento)

    def __anadir_unidades(self, elemento: Elemento):
        for e in self.__lista:
            if e.nombre == elemento.nombre:
                e.cantidad += elemento.cantidad
                return True
            return False

    def numero_elementos(self):
        return len(self.__lista)

    def importe_total(self):
        sum_total = 0
        for n in self.__lista:
            sum_total += n.precio * n.cantidad
        return sum_total

    def __str__(self):
        str_ = "LISTADO DE PRODUCTOS EN LA CESTO\n" + \
               "______________________________________________\n"
        str_ += f"{self.__str_elemento()}"
        return str_

    def __str_elemento(self):
        str_ = ""
        for e in self.__lista:
            str_ += f"{e.nombre}, {e.cantidad}, {e.precio}\n"
        return str_

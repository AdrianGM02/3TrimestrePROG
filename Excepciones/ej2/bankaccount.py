"""
Ejercicio 2:
    Modifica el ejercicio de la cuenta corriente para que el método que almacena en un fichero el estado del
    objeto guarde el objeto entero y el que lo recupera lo restaure. En esta versión no le pasamos nombre de
    fichero al método a la hora de guardarlo, usará el número de cuenta corriente para ello.

"""
import random
import pickle

LEN_NUMERO = 10


class Esta_en_la_lista(ValueError):
    def __init__(self):
        super().__init__("El numero está en la base de datos")


class Saldo_Negativo(TypeError):
    def __init__(self):
        super().__init__(f"No puedes poner saldo negativo ")


class Numero_Negativo(ValueError):
    def __init__(self, numero):
        super().__init__(f"Este número {numero} es negativo")


class BankAccount:
    lista_numeros = []

    def __init__(self, saldo=0):
        numero = self.__crear_numero()
        if numero in self.lista_numeros:
            raise Esta_en_la_lista()
        self.__numero = numero
        self.__comprobar_saldo(saldo)
        self.__saldo = saldo
        self.__lista_movimientos = []

    @staticmethod
    def __crear_numero():
        numero = ""
        for i in range(1, LEN_NUMERO):
            numero += str(random.randint(0, 9))

        return int(numero)

    @staticmethod
    def __comprobar_saldo(numero):
        if numero < 0:
            raise Saldo_Negativo(numero)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_cuenta(self):
        return self.__numero

    def ingresar(self, cantidad: float):
        if cantidad < 0:
            raise Numero_Negativo(cantidad)
        self.__saldo += cantidad
        self.__lista_movimientos.append(f"Se ha ingresado {cantidad} en la cuenta {self.__numero}")

    def retirar(self, cantidad: float):
        if cantidad < 0:
            raise Numero_Negativo(cantidad)
        if (self.__saldo - cantidad) < 0:
            raise Saldo_Negativo()
        self.__saldo -= cantidad
        self.__lista_movimientos.append(f"Se ha retirado {cantidad} en la cuenta {self.__numero}")

    def transfer(self, cuenta: 'BankAccount', cantidad: float):
        self.retirar(cantidad)
        cuenta.__saldo += cantidad
        self.__lista_movimientos.append(
            f"Se ha transferido {cantidad} en la cuenta {cuenta.numero} desde la cuenta {self.__numero}")

    def movimientos(self):
        print(f"Movimientos de {self.__numero}")
        for i in range(len(self.__lista_movimientos)):
            print(self.__lista_movimientos[i])

    def convertir_objeto_a_archivo(self):
        nombre_fichero = str(self.__numero) + '.pkl'
        with open(nombre_fichero, 'wb') as f:
            pickle.dump(self, f)

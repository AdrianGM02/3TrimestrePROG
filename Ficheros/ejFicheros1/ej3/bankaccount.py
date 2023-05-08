"""Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la clase un
método para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un fichero elegido por el
cliente, y un nuevo constructor que reciba como parámetro un fichero como el anterior y cree el objeto con esos
datos. Pruébalo con un programa.



"""

from typeguard import typechecked
import random


@typechecked
class BankAccount:
    __list_account = []

    def __init__(self, balance: int = 0):
        number = BankAccount.__generate_number()
        if number in BankAccount.__list_account:
            raise ValueError("Este número está en la lista de cuentas")
        self.__number = number
        self.__balance = balance

    @staticmethod
    def __generate_number():
        number = ""
        for _ in range(10):
            number += str(random.randint(0, 9))
        return number

    @staticmethod
    def __negative_balance(number: int):
        if number < 0:
            return False
        return True

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def income(self, value: int):
        self.__balance += value

    def costs(self, value: int):
        final_balance = self.__balance - value
        if not BankAccount.__negative_balance(final_balance):
            raise ValueError("La cuenta no puede tener dinero negativo")
        self.__balance = final_balance

    def transfer(self, other: 'BankAccount', value: int):
        self.costs(value)
        other.__balance += value

    def input_file(self, name_file: str):
        with open('cuenta_bancaria.txt', 'wt') as cuenta:
            cuenta.write(f"{self.__number}")
            cuenta.write(f"{self.__balance}")


    def __repr__(self):
        return repr(self.__number) + repr(self.__balance)

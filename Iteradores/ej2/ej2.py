"""
2. Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de Eratóstenes

Autor: Javier Postigo Arévalo
Fecha: 15/05/2023
"""
from typeguard import typechecked
from collections.abc import Iterator


@typechecked
class PrimeIterator(Iterator):

    def __init__(self, number: int):
        self.__number = number
        self.__prime_number = 0
        self.__primes_iterators = self.sieve_of_eratosthenes(self.__number)

    def __next__(self):
        if self.__prime_number < len(self.__primes_iterators):
            elemento = self.__primes_iterators[self.__prime_number]
            self.__prime_number += 1
            return elemento
        else:
            raise StopIteration

    @staticmethod
    def sieve_of_eratosthenes(number):
        numeros = list(range(2, number+1))
        for i in numeros:
            for j in numeros:
                if j != i and j % i == 0:
                    numeros.remove(j)
        return numeros


if __name__ == '__main__':
    primes = list(PrimeIterator(50))
    print(primes)
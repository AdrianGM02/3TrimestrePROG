"""
 Escribe un programa que guarde en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

"""


def es_primo(numero):
    if numero < 2:
        return False
    for num in range(2, numero):
        if numero % num == 0:
            return False
    return True


primos = []

for n in range(1, 500):
    if es_primo(n):
        primos.append(n)

with open('primos.txt', 'w') as archivo_primos:
    for primo in primos:
        archivo_primos.write(f"{primo}\n")



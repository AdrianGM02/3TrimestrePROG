
USERS = {'usuario1': 'hola', 'usuario2' :  'caca', 'usuario3' : 'adios'}

numero_de_intentos = 0

while numero_de_intentos != 3:
    numero_de_intentos += 1
    usuario = input("Escribe el usuario: ")
    if usuario in USERS:
        for usuario in USERS:
            contrasena = input("Escribe la contraseña: ")
            if USERS[usuario] == contrasena:
                print("La contraseña es correcta")
                break
            else:
                numero_de_intentos += 1
                print("Intentalo de nuevo, la contraseña es incorrecta")

    else:
        print("El usuario es incorrecto")

    if numero_de_intentos == 3:
        print("Ha sido el ultimo intento, lo siento")




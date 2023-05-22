import auto
from util.menu import Menu
cash_register = Menu("Test", "Crear fichero test. ", "Seleccionar fichero Test. ", "Añadir pregunta al test")
archivo_ = None
while True:
    print("")
    print(f"Fichero cargado: {archivo_}")
    print("")
    match cash_register.choose():
        case 1:
            auto.crear_fichero()
        case 2:
            archivo_ = auto.indicar_fichero()
        case 3:
            if archivo_ is None:
                print("\nDebe cargar un fichero. \n")
            else:
                auto.anadir_pregunta(archivo_)
        case 4:
            print("Ha salido del programa...")
            exit(1)
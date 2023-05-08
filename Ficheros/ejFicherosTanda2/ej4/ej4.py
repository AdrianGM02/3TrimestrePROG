"""
4. Escribe un programa capaz de quitar los comentarios de un programa de Java.
Se utilizaría de la siguiente manera:
python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

Por ejemplo:
python quita-comentarios.py Holav1.java Holav2.java
crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.
P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de error
correspondiente.

"""


def main():
    with open("java.java", "rt") as file_to_read:
        file = file_to_read.read()

    str_without_comments_on_line = remove_comments_line(file, "//", "\n")
    str_without_comments = remove_comments_block(str_without_comments_on_line, "/*", "*/")

    try:
        with open("java_sin_comentarios.java", "w") as archivo:
            archivo.write(str_without_comments)
            print("Se escribió en el archivo correctamente.")
    except FileNotFoundError:
        print("El archivo no existe.")


def remove_comments_line(string_: str, initial_chr: str, final_chr: str):
    final_str = string_

    while True:
        if initial_chr not in final_str or final_chr not in final_str:
            break
        str_to_ch_initial = final_str[0:final_str.find(initial_chr)]
        str_from_final_chr = final_str[final_str.find(final_chr):]
        final_str = str_to_ch_initial + str_from_final_chr


    return final_str


def remove_comments_block(string_: str, initial_chr: str, final_chr: str):
    final_str = string_
    while True:
        if initial_chr not in final_str or final_chr not in final_str:
            break
        str_to_ch_initial = final_str[0:final_str.find(initial_chr)]
        str_from_final_chr = final_str[(final_str.find(final_chr) + 2):]
        final_str = str_to_ch_initial + str_from_final_chr

    return final_str


if __name__ == '__main__':
    main()

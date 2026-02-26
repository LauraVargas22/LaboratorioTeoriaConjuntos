from collections import Counter
import string
import modules.titles as t

def _leer_texto(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read().lower()


def graficar_frecuencias(ruta_archivo):
    texto = _leer_texto(ruta_archivo)
    
    letters = [c for c in texto if c.isalpha()]
    frequency = Counter(letters)

    alphabet = string.ascii_lowercase

    t.show_ingles()

    columns = 3
    rows = (len(alphabet) + columns - 1) // columns

    for i in range(rows):
        fila = ""
        for j in range(columns):
            index = i + j * rows
            if index < len(alphabet):
                letter = alphabet[index]
                quantity = frequency.get(letter, 0)
                fila += f"'{letter}': {quantity:<5}   "
        print(fila)


def contar_ocurrencias(ruta_archivo, palabra):
    texto = _leer_texto(ruta_archivo)
    return texto.count(palabra.lower())

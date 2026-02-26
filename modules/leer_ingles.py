from collections import Counter
import string
import modules.titles as t
import matplotlib.pyplot as plt

def _leer_texto(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read().lower()


def conteo_frecuencias(ruta_archivo):
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

def graficar_frecuencias(ruta_archivo):
    texto = _leer_texto(ruta_archivo)

    # Filtrar solo letras
    letras = [c for c in texto if c.isalpha()]
    frecuencias = Counter(letras)

    # Abecedario como LISTA (esto es clave)
    abecedario = list(string.ascii_lowercase)

    # Obtener frecuencias en el mismo orden
    valores = [frecuencias.get(letra, 0) for letra in abecedario]

    plt.figure()
    plt.bar(abecedario, valores)
    plt.title("Frecuencia de letras")
    plt.xlabel("Letras")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=0)
    plt.show()

def contar_ocurrencias(ruta_archivo, palabra):
    texto = _leer_texto(ruta_archivo)
    return texto.count(palabra.lower())

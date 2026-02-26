from collections import Counter
import string
import modules.titles as t
import matplotlib.pyplot as plt
import numpy as np

'Función para obtener la ruta del archivo, leer su contenido y convertirlo a minúsculas'
def _leer_texto(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read().lower()

'Función para imprimir la ocurrencia de cada letra del abcedario en el texto'
def conteo_frecuencias(ruta_archivo):
    texto = _leer_texto(ruta_archivo)

    letras = [c for c in texto if c.isalpha()]
    frecuencias = Counter(letras)

    abecedario = string.ascii_lowercase

    t.show_español()

    columnas = 3
    filas = (len(abecedario) + columnas - 1) // columnas

    for i in range(filas):
        fila = ""
        for j in range(columnas):
            indice = i + j * filas
            if indice < len(abecedario):
                letra = abecedario[indice]
                cantidad = frecuencias.get(letra, 0)
                fila += f"'{letra}': {cantidad:<5}   "
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

'Función para contar la ocurrencia de las palabras en el texto'
def contar_ocurrencias(ruta_archivo, palabra):
    texto = _leer_texto(ruta_archivo)
    return texto.count(palabra.lower())
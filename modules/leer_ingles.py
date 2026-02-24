from collections import Counter


def _leer_texto(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read().lower()


def graficar_frecuencias(ruta_archivo, top_n=10):
    texto = _leer_texto(ruta_archivo)
    frecuencias = Counter(texto)

    print("\nFrecuencia de caracteres (Inglés):")
    for caracter, cantidad in frecuencias.most_common(top_n):
        etiqueta = repr(caracter)
        print(f"{etiqueta:>6}: {cantidad}")


def contar_ocurrencias(ruta_archivo, palabra):
    texto = _leer_texto(ruta_archivo)
    return texto.count(palabra.lower())

import numpy as np
import matplotlib.pyplot as plt
import modules.leer_español as le
import modules.leer_ingles as li

def graficar_concurrencia(palabras, archivo_esp, archivo_ing):
    
    conteo_esp = []
    conteo_ing = []

    for palabra in palabras:
        c_esp = le.contar_ocurrencias(archivo_esp, palabra)
        c_ing = li.contar_ocurrencias(archivo_ing, palabra)

        conteo_esp.append(c_esp)
        conteo_ing.append(c_ing)

    x = np.arange(len(palabras))  # posiciones
    ancho = 0.35  # ancho de las barras

    plt.figure()

    plt.bar(x - ancho/2, conteo_esp, width=ancho, label="Español")
    plt.bar(x + ancho/2, conteo_ing, width=ancho, label="Inglés")

    plt.xticks(x, palabras, rotation=45)
    plt.xlabel("Palabras")
    plt.ylabel("Cantidad")
    plt.title("Concurrencia de palabras")
    plt.legend()

    plt.tight_layout()
    plt.show()
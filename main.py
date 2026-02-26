'''
Archivo principal para la ejecución del programa
'''

if (__name__=='__main__'):
    #Importación modulos
    import modules.mensajes as msg
    import modules.customs as cu
    import modules.titles as t
    import modules.menus as me
    import modules.salir as sa
    import modules.leer_español as le
    import modules.leer_ingles as li
    import modules.conteo_palabras as gc

isActive = True
while (isActive):
    try:
        cu.borrarPantalla()
        me.show_menu()
        opcMenu = int(input('Seleccione:__'))
        
        match opcMenu:
            case 1:
                """Idioma Español"""
                cu.borrarPantalla()
                le.conteo_frecuencias("Text/caracteres_esp.txt")
                le.graficar_frecuencias("Text/caracteres_esp.txt")
                cu.pausarPantalla()
            case 2:
                """Idioma Inglés"""
                cu.borrarPantalla()
                li.conteo_frecuencias("Text/caracteres_eng.txt")
                li.graficar_frecuencias("Text/caracteres_eng.txt")
                cu.pausarPantalla()
            case 3: 
                """Concurrencia de palabras"""
                cu.borrarPantalla()
                palabras = [
                    "science",
                    "ciencia",
                    "methods",
                    "metodos",
                    "las",
                    "the",
                    "is",
                    "es",
                ]

                archivo_esp = "Text/caracteres_esp.txt"
                archivo_ing = "Text/caracteres_eng.txt"

                t.show_concurrencia()
                print(f"{'Palabra':<10} {'Español':>10} {'Inglés':>10}")
                print("-" * 32)

                for palabra in palabras:
                    c_esp = le.contar_ocurrencias(archivo_esp, palabra)
                    c_ing = li.contar_ocurrencias(archivo_ing, palabra)
                    print(f"{palabra:<10} {c_esp:>10} {c_ing:>10}")

                gc.graficar_concurrencia(palabras, archivo_esp, archivo_ing)
               
                cu.pausarPantalla()
            case 4:
                # Opción Salir
                isActive = sa.validateData(msg.msgInfo)
            case _:
                print (msg.msgCase)
                cu.pausarPantalla()
        
    except ValueError:
        print (msg.msgExcept)
        cu.pausarPantalla()
        continue

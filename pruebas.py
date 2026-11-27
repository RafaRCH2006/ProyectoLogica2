
"""
PROYECTO: TEORIA DE CONJUNTOS Y RELACIONES BINARIAS

Programa interactivo para probar las clases Conjunto y Relacion.
"""

import os
from logica_conjuntos import Conjunto, Relacion


# =============================================
# FUNCIONES GENERALES
# =============================================

def limpiar_consola():
    """
    Limpia la pantalla de la terminal.
    Funciona en Windows, Linux y macOS.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """
    Espera a que el usuario presione ENTER
    antes de regresar al menu principal.
    """
    input("\nPresiona ENTER para regresar al menu principal...")
    limpiar_consola()


def convertir_elemento(elemento):
    """
    Convierte un elemento a entero cuando es posible.
    Si no es posible, conserva el texto.
    """
    try:
        return int(elemento)
    except ValueError:
        return elemento


def ingresar_conjunto(nombre):
    """
    Permite al usuario introducir los elementos de un conjunto.
    """
    print(f"\n===== INGRESAR CONJUNTO {nombre} =====")

    elementos = input(
        f"Introduce los elementos de {nombre}, separados por espacios: "
    )

    if elementos.strip() == "":
        return Conjunto()

    lista = []

    for elemento in elementos.split():
        lista.append(convertir_elemento(elemento))

    return Conjunto(lista)


# =============================================
# MENU PRINCIPAL
# =============================================

def menu():
    """
    Muestra las opciones disponibles del programa.
    """

    print("=========================================")
    print("       TEORIA DE CONJUNTOS")
    print("       Y RELACIONES BINARIAS")
    print("=========================================")

    print("\n--- OPERACIONES BASICAS ---")
    print("1. Mostrar conjuntos")
    print("2. Comprobar pertenencia")
    print("3. Agregar elemento")
    print("4. Eliminar elemento")
    print("5. Mostrar cardinalidad")
    print("6. Comprobar si esta vacio")
    print("7. Comparar conjuntos")

    print("\n--- OPERACIONES ENTRE CONJUNTOS ---")
    print("8. Union")
    print("9. Interseccion")
    print("10. Diferencia A - B")
    print("11. Diferencia B - A")
    print("12. Diferencia simetrica")
    print("13. Complemento de A")
    print("14. Complemento de B")

    print("\n--- OPERACIONES ESPECIALES ---")
    print("15. Conjunto potencia de A")
    print("16. Conjunto potencia de B")
    print("17. Producto cartesiano A x B")
    print("18. Producto cartesiano B x A")

    print("\n--- RELACIONES BINARIAS ---")
    print("19. Relacion de orden estricto (a < b)")
    print("20. Relacion de equivalencia (modulo 2)")
    print("21. Comprobar reflexividad")
    print("22. Comprobar simetria")
    print("23. Comprobar transitividad")
    print("24. Comprobar relacion de equivalencia")

    print("\n0. Salir")
    print("=========================================")


# =============================================
# PROGRAMA PRINCIPAL
# =============================================

def main():

    limpiar_consola()

    print("=========================================")
    print(" PROYECTO: TEORIA DE CONJUNTOS")
    print(" Y RELACIONES BINARIAS")
    print("=========================================")

    A = ingresar_conjunto("A")
    B = ingresar_conjunto("B")
    U = ingresar_conjunto("UNIVERSO")

    limpiar_consola()

    while True:

        menu()

        opcion = input("\nSelecciona una opcion: ")

        # =====================================
        # SALIR DEL PROGRAMA
        # =====================================

        if opcion == "0":

            limpiar_consola()
            print("=========================================")
            print("      FINALIZANDO PROGRAMA")
            print("=========================================")
            break

        # Limpiar la pantalla despues de seleccionar
        limpiar_consola()

        # =====================================
        # OPERACIONES BASICAS
        # =====================================

        if opcion == "1":

            print("========== CONJUNTOS ==========")

            print("\nConjunto A:", A)
            print("Conjunto B:", B)
            print("Universo U:", U)

        elif opcion == "2":

            print("========== PERTENENCIA ==========")

            conjunto = input(
                "Consultar conjunto A o B: "
            ).upper()

            elemento = convertir_elemento(
                input("Introduce el elemento: ")
            )

            if conjunto == "A":

                resultado = A.pertenece(elemento)

            elif conjunto == "B":

                resultado = B.pertenece(elemento)

            else:

                print("Conjunto no valido.")
                pausar()
                continue

            print("\n¿Pertenece?", resultado)

        elif opcion == "3":

            print("========== AGREGAR ELEMENTO ==========")

            conjunto = input(
                "Modificar conjunto A o B: "
            ).upper()

            elemento = convertir_elemento(
                input("Elemento que deseas agregar: ")
            )

            if conjunto == "A":

                ya_existe = A.pertenece(elemento)
                A.agregar(elemento)

            elif conjunto == "B":

                ya_existe = B.pertenece(elemento)
                B.agregar(elemento)

            else:

                print("Conjunto no valido.")
                pausar()
                continue

            if ya_existe:

                print("\nEl elemento ya existia en el conjunto.")

            else:

                print("\nElemento agregado correctamente.")

        elif opcion == "4":

            print("========== ELIMINAR ELEMENTO ==========")

            conjunto = input(
                "Modificar conjunto A o B: "
            ).upper()

            elemento = convertir_elemento(
                input("Elemento que deseas eliminar: ")
            )

            if conjunto == "A":

                existia = A.pertenece(elemento)
                A.eliminar(elemento)

            elif conjunto == "B":

                existia = B.pertenece(elemento)
                B.eliminar(elemento)

            else:

                print("Conjunto no valido.")
                pausar()
                continue

            if existia:

                print("\nElemento eliminado correctamente.")

            else:

                print("\nEl elemento no pertenece al conjunto.")

        elif opcion == "5":

            print("========== CARDINALIDAD ==========")

            print("\nCardinalidad de A:", A.cardinalidad())
            print("Cardinalidad de B:", B.cardinalidad())
            print("Cardinalidad de U:", U.cardinalidad())

        elif opcion == "6":

            print("========== CONJUNTOS VACIOS ==========")

            print("\n¿A esta vacio?", A.es_vacio())
            print("¿B esta vacio?", B.es_vacio())
            print("¿U esta vacio?", U.es_vacio())

        elif opcion == "7":

            print("========== IGUALDAD ==========")

            print("\n¿A es igual a B?", A == B)

        # =====================================
        # OPERACIONES ENTRE CONJUNTOS
        # =====================================

        elif opcion == "8":

            print("========== UNION ==========")

            print("\nA union B =", A.union(B))

        elif opcion == "9":

            print("========== INTERSECCION ==========")

            print("\nA interseccion B =", A.interseccion(B))

        elif opcion == "10":

            print("========== DIFERENCIA A - B ==========")

            print("\nA - B =", A.diferencia(B))

        elif opcion == "11":

            print("========== DIFERENCIA B - A ==========")

            print("\nB - A =", B.diferencia(A))

        elif opcion == "12":

            print("========== DIFERENCIA SIMETRICA ==========")

            print(
                "\nA diferencia simetrica B =",
                A.diferencia_simetrica(B)
            )

        elif opcion == "13":

            print("========== COMPLEMENTO DE A ==========")

            try:

                print("\nComplemento de A =", A.complemento(U))

            except ValueError as error:

                print("\nError:", error)

        elif opcion == "14":

            print("========== COMPLEMENTO DE B ==========")

            try:

                print("\nComplemento de B =", B.complemento(U))

            except ValueError as error:

                print("\nError:", error)

        # =====================================
        # CONJUNTO POTENCIA
        # =====================================

        elif opcion == "15":

            print("========== CONJUNTO POTENCIA DE A ==========")

            potencia = A.conjunto_potencia()

            for subconjunto in potencia:

                print(subconjunto)

            print("\nCantidad de subconjuntos:", len(potencia))

        elif opcion == "16":

            print("========== CONJUNTO POTENCIA DE B ==========")

            potencia = B.conjunto_potencia()

            for subconjunto in potencia:

                print(subconjunto)

            print("\nCantidad de subconjuntos:", len(potencia))

        # =====================================
        # PRODUCTO CARTESIANO
        # =====================================

        elif opcion == "17":

            print("========== PRODUCTO CARTESIANO A x B ==========")

            resultado = A.producto_cartesiano(B)

            print("\nResultado:")

            print(resultado)

            print("\nCantidad de pares:", len(resultado))

        elif opcion == "18":

            print("========== PRODUCTO CARTESIANO B x A ==========")

            resultado = B.producto_cartesiano(A)

            print("\nResultado:")

            print(resultado)

            print("\nCantidad de pares:", len(resultado))

        # =====================================
        # RELACIONES BINARIAS
        # =====================================

        elif opcion == "19":

            print("========== RELACION DE ORDEN ESTRICTO ==========")

            try:

                relacion = Relacion()

                relacion.generar_relacion(
                    A,
                    lambda a, b: a < b
                )

                print("\nRelacion a < b:")
                print(relacion)

                print(
                    "\nReflexiva:",
                    relacion.es_reflexiva(A)
                )

                print(
                    "Simetrica:",
                    relacion.es_simetrica()
                )

                print(
                    "Transitiva:",
                    relacion.es_transitiva()
                )

            except TypeError:

                print("\nError: esta relacion requiere elementos comparables.")

        elif opcion == "20":

            print("========== RELACION DE EQUIVALENCIA ==========")

            try:

                relacion = Relacion()

                relacion.generar_relacion(
                    A,
                    lambda a, b: a % 2 == b % 2
                )

                print("\nRelacion modulo 2:")
                print(relacion)

                print(
                    "\nReflexiva:",
                    relacion.es_reflexiva(A)
                )

                print(
                    "Simetrica:",
                    relacion.es_simetrica()
                )

                print(
                    "Transitiva:",
                    relacion.es_transitiva()
                )

                print(
                    "Es de equivalencia:",
                    relacion.es_de_equivalencia(A)
                )

            except TypeError:

                print("\nError: esta relacion requiere numeros enteros.")

        elif opcion == "21":

            print("========== REFLEXIVIDAD ==========")

            try:

                relacion = Relacion()

                relacion.generar_relacion(
                    A,
                    lambda a, b: a % 2 == b % 2
                )

                print(
                    "\n¿Es reflexiva?",
                    relacion.es_reflexiva(A)
                )

            except TypeError:

                print("\nError: esta relacion requiere numeros enteros.")

        elif opcion == "22":

            print("========== SIMETRIA ==========")

            try:

                relacion = Relacion()

                relacion.generar_relacion(
                    A,
                    lambda a, b: a % 2 == b % 2
                )

                print(
                    "\n¿Es simetrica?",
                    relacion.es_simetrica()
                )

            except TypeError:

                print("\nError: esta relacion requiere numeros enteros.")

        elif opcion == "23":

            print("========== TRANSITIVIDAD ==========")

            try:

                relacion = Relacion()

                relacion.generar_relacion(
                    A,
                    lambda a, b: a % 2 == b % 2
                )

                print(
                    "\n¿Es transitiva?",
                    relacion.es_transitiva()
                )

            except TypeError:

                print("\nError: esta relacion requiere numeros enteros.")

        elif opcion == "24":

            print("========== RELACION DE EQUIVALENCIA ==========")

            try:

                relacion = Relacion()

                relacion.generar_relacion(
                    A,
                    lambda a, b: a % 2 == b % 2
                )

                print(
                    "\n¿Es de equivalencia?",
                    relacion.es_de_equivalencia(A)
                )

            except TypeError:

                print("\nError: esta relacion requiere numeros enteros.")

        # =====================================
        # OPCION INVALIDA
        # =====================================

        else:

            print("Opcion no valida. Intenta nuevamente.")

        # Regresar al menu despues de cada operacion
        pausar()


# =============================================
# EJECUCION DEL PROGRAMA
# =============================================

if __name__ == "__main__":
    main()

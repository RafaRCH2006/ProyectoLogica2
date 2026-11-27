
"""
PROYECTO: TEORIA DE CONJUNTOS Y RELACIONES BINARIAS

Este archivo contiene las clases Conjunto y Relacion.

Los conjuntos se implementan utilizando listas y tuplas,
sin utilizar set(), frozenset() ni librerias externas.
"""


class Conjunto:
    """
    Representa un conjunto matematico sin elementos duplicados.
    """

    def __init__(self, elementos=None):
        """
        Inicializa un conjunto.
        """
        self.elementos = []

        if elementos is not None:
            for elemento in elementos:
                self.agregar(elemento)

    def pertenece(self, elemento):
        """
        Comprueba si un elemento pertenece al conjunto.
        """
        for actual in self.elementos:
            if actual == elemento:
                return True

        return False

    def agregar(self, elemento):
        """
        Agrega un elemento si no existe previamente.
        """
        if not self.pertenece(elemento):
            self.elementos.append(elemento)

    def eliminar(self, elemento):
        """
        Elimina un elemento si pertenece al conjunto.
        """
        if self.pertenece(elemento):
            self.elementos.remove(elemento)

    def cardinalidad(self):
        """
        Devuelve la cantidad de elementos del conjunto.
        """
        return len(self.elementos)

    def es_vacio(self):
        """
        Comprueba si el conjunto esta vacio.
        """
        return self.cardinalidad() == 0

    def __eq__(self, otro):
        """
        Comprueba si dos conjuntos tienen los mismos elementos.
        El orden no afecta la igualdad.
        """
        if not isinstance(otro, Conjunto):
            return False

        if self.cardinalidad() != otro.cardinalidad():
            return False

        for elemento in self.elementos:
            if not otro.pertenece(elemento):
                return False

        return True

    def __str__(self):
        """
        Representa el conjunto mediante notacion matematica.
        """
        if self.es_vacio():
            return "∅"

        return "{" + ", ".join(
            str(elemento) for elemento in self.elementos
        ) + "}"

    # =========================================
    # OPERACIONES ENTRE CONJUNTOS
    # =========================================

    def union(self, otro):
        """
        Devuelve un conjunto con los elementos de ambos conjuntos.
        """
        resultado = Conjunto(self.elementos)

        for elemento in otro.elementos:
            resultado.agregar(elemento)

        return resultado

    def interseccion(self, otro):
        """
        Devuelve los elementos que pertenecen a ambos conjuntos.
        """
        resultado = Conjunto()

        for elemento in self.elementos:
            if otro.pertenece(elemento):
                resultado.agregar(elemento)

        return resultado

    def diferencia(self, otro):
        """
        Devuelve los elementos de este conjunto que no estan
        presentes en el otro.
        """
        resultado = Conjunto()

        for elemento in self.elementos:
            if not otro.pertenece(elemento):
                resultado.agregar(elemento)

        return resultado

    def diferencia_simetrica(self, otro):
        """
        Devuelve los elementos que pertenecen a uno de los
        conjuntos, pero no a ambos.
        """
        diferencia_1 = self.diferencia(otro)
        diferencia_2 = otro.diferencia(self)

        return diferencia_1.union(diferencia_2)

    def complemento(self, universo):
        """
        Devuelve los elementos del universo que no pertenecen
        a este conjunto.

        Comprueba que el conjunto sea subconjunto del universo.
        """
        if not self.es_subconjunto(universo):
            raise ValueError(
                "El conjunto no es subconjunto del universo."
            )

        return universo.diferencia(self)

    # =========================================
    # PROPIEDADES DE LOS CONJUNTOS
    # =========================================

    def es_subconjunto(self, otro):
        """
        Comprueba si todos los elementos de este conjunto
        pertenecen al otro conjunto.
        """
        for elemento in self.elementos:
            if not otro.pertenece(elemento):
                return False

        return True

    def son_disjuntos(self, otro):
        """
        Comprueba si dos conjuntos no tienen elementos comunes.
        """
        for elemento in self.elementos:
            if otro.pertenece(elemento):
                return False

        return True

    # =========================================
    # CONJUNTO POTENCIA
    # =========================================

    def conjunto_potencia(self):
        """
        Genera todos los subconjuntos posibles.

        Algoritmo:
        1. Comienza con el conjunto vacio.
        2. Recorre cada elemento del conjunto original.
        3. Crea copias de los subconjuntos existentes.
        4. Agrega el elemento actual a esas copias.
        5. Incorpora los nuevos subconjuntos al resultado.

        Un conjunto con n elementos tiene 2 elevado a n
        subconjuntos.
        """
        subconjuntos = [Conjunto()]

        for elemento in self.elementos:

            nuevos = []

            for subconjunto in subconjuntos:

                nuevo = Conjunto(subconjunto.elementos)
                nuevo.agregar(elemento)

                nuevos.append(nuevo)

            subconjuntos.extend(nuevos)

        return subconjuntos

    # =========================================
    # PRODUCTO CARTESIANO
    # =========================================

    def producto_cartesiano(self, otro):
        """
        Genera todos los pares ordenados posibles entre
        los elementos de dos conjuntos.
        """
        resultado = []

        for elemento_a in self.elementos:

            for elemento_b in otro.elementos:

                resultado.append((elemento_a, elemento_b))

        return resultado


# =============================================
# CLASE RELACION
# =============================================

class Relacion:
    """
    Representa una relacion binaria mediante pares ordenados.
    """

    def __init__(self, pares=None):
        """
        Inicializa una relacion sin pares duplicados.
        """
        self.pares = []

        if pares is not None:
            for par in pares:
                self.agregar(par)

    def agregar(self, par):
        """
        Agrega un par ordenado si no existe previamente.
        """
        if par not in self.pares:
            self.pares.append(par)

    def pertenece(self, par):
        """
        Comprueba si un par ordenado pertenece a la relacion.
        """
        return par in self.pares

    def generar_relacion(self, conjunto_a, condicion):
        """
        Genera una relacion evaluando una condicion para
        cada par posible del producto cartesiano A x A.
        """
        self.pares = []

        for a in conjunto_a.elementos:

            for b in conjunto_a.elementos:

                if condicion(a, b):
                    self.agregar((a, b))

        return self

    def es_reflexiva(self, conjunto_a):
        """
        Comprueba que cada elemento este relacionado consigo mismo.
        """
        for elemento in conjunto_a.elementos:

            if not self.pertenece((elemento, elemento)):
                return False

        return True

    def es_simetrica(self):
        """
        Comprueba que si (a,b) pertenece a R,
        entonces (b,a) tambien pertenezca a R.
        """
        for a, b in self.pares:

            if not self.pertenece((b, a)):
                return False

        return True

    def es_transitiva(self):
        """
        Comprueba la transitividad.

        Si (a,b) y (b,c) pertenecen a R,
        entonces (a,c) tambien debe pertenecer a R.
        """
        for a, b in self.pares:

            for c, d in self.pares:

                if b == c:

                    if not self.pertenece((a, d)):
                        return False

        return True

    def es_de_equivalencia(self, conjunto_a):
        """
        Comprueba si la relacion es reflexiva,
        simetrica y transitiva.
        """
        return (
            self.es_reflexiva(conjunto_a)
            and self.es_simetrica()
            and self.es_transitiva()
        )

    def __str__(self):
        """
        Representa la relacion mediante sus pares ordenados.
        """
        if len(self.pares) == 0:
            return "∅"

        return "{" + ", ".join(
            str(par) for par in self.pares
        ) + "}"

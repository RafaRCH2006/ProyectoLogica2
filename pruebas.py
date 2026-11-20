from logica_conjuntos import Conjunto


print("===== PROYECTO: TEORIA DE CONJUNTOS =====")

# Crear conjuntos
A = Conjunto([1, 2, 2, 3, 4, 4, 5])
B = Conjunto([1, 2, 3, 4, 5])
C = Conjunto()

# Mostrar conjuntos
print("\n===== REPRESENTACION =====")

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

# Probar eliminacion
print("\n===== ELIMINAR ELEMENTOS =====")

A.eliminar(3)
print("A despues de eliminar el 3:", A)

A.eliminar(10)
print("A despues de intentar eliminar el 10:", A)

# Probar cardinalidad
print("\n===== CARDINALIDAD =====")

print("Cardinalidad de A:", A.cardinalidad())
print("Cardinalidad de B:", B.cardinalidad())
print("Cardinalidad de C:", C.cardinalidad())

# Probar conjunto vacio
print("\n===== CONJUNTO VACIO =====")

print("¿A esta vacio?", A.es_vacio())
print("¿C esta vacio?", C.es_vacio())

# Probar igualdad
print("\n===== IGUALDAD ENTRE CONJUNTOS =====")

print("¿A es igual a B?", A == B)
print("¿B es igual a B?", B == B)
print("¿C es igual a A?", C == A)
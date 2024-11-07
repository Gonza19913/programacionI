# Listas de ejemplo
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [10, 20, 30, 40]

# Determinar la longitud de la lista más larga
longitud_max = max(len(lista1), len(lista2))

# Rellenar las listas más cortas con ceros
lista1.extend([0] * (longitud_max - len(lista1)))
lista2.extend([0] * (longitud_max - len(lista2)))

# Sumar los elementos de las listas
suma_listas = [lista1[i] + lista2[i] for i in range(longitud_max)]

# Imprimir el resultado
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Suma de las listas:", suma_listas)

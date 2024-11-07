# Crear una lista de potencias de 2 usando list comprehension
potencias = [2 ** x for x in range(10)]

# Imprimir cada resultado en un formato específico
for exponente, valor in enumerate(potencias):
    print(f"{exponente} elevado a la 2 = {valor}")

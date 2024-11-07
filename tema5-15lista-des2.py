# Lista de códigos de producto en el inventario
inventario = ["A123", "B456", "C789", "D012", "E345", "F678", "G901", "H234", "I567", "J890", "K123", "L456"]

# Solicita al usuario el código a buscar
codigo = input("Introduce el código de producto: ").upper()  # Convierte a mayúsculas para comparación

# Verifica si el código está en la lista e informa su posición
if codigo in inventario:
    posicion = inventario.index(codigo)
    print(f"El código {codigo} se encuentra en la posición {posicion}.")
else:
    print(f"El código {codigo} no se ha encontrado en el inventario.")

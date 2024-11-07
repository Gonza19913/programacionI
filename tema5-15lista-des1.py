# Entrada de los tres números
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

# Comparaciones para determinar el mayor o si todos son iguales
if num1 == num2 == num3:
    print("Todos los numeros son iguales.")
elif num1 >= num2 and num1 >= num3:
    print(f"El numero mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")
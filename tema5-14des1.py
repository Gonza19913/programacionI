try:
    # Solicitar el primer número y convertirlo a entero
    num1 = int(input("Ingrese el primer número entero: "))
    
    # Solicitar el segundo número y convertirlo a entero
    num2 = int(input("Ingrese el segundo número entero: "))
    
    # Intentar realizar la división
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    
except ValueError:
    print("Error: Debe ingresar solo valores numéricos enteros.")
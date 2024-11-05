import math
import sys

# Configura el límite máximo de dígitos para evitar el error de conversión (opcional)
sys.set_int_max_str_digits(1000)  # Ajusta según el límite que quieras manejar

def calcular_factorial():
    try:
        # Solicitamos un número al usuario y lo convertimos a entero
        numero = int(input("Ingrese un numero entero positivo para calcular el factorial: "))
        
        print(f"Numero ingresado: {numero}")  # Mensaje de seguimiento
        
        # Comprobamos si el número es negativo
        if numero < 0:
            raise ValueError("Error: El numero no puede ser negativo.")
        
        # Validación de tamaño para evitar el cálculo de números excesivamente grandes
        if numero > 1000:
            raise OverflowError("Error: El numero es demasiado grande para calcular el factorial.")
        
        # Intentamos calcular el factorial
        resultado = math.factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    
    except ValueError as e:
        print(e)  # Muestra el mensaje de error si el número es negativo o no es entero
        
    except OverflowError as e:
        print(e)  # Mensaje específico para OverflowError

# Llamada a la función para prueba
calcular_factorial()

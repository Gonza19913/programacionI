import math

# Definimos la excepción personalizada
class NegativeNumberError(Exception):
    pass

def calcular_raiz_cuadrada():
    try:
        # Solicitamos un número al usuario y lo convertimos a float
        numero = float(input("Ingrese un numero para calcular su raiz cuadrada: "))
        
        # Verificamos si el número es negativo y lanzamos la excepción personalizada
        if numero < 0:
            raise NegativeNumberError("Error: No se puede calcular la raiz cuadrada de un numero negativo.")
        
        # Calculamos la raíz cuadrada si el número es válido
        resultado = math.sqrt(numero)
        print(f"La raiz cuadrada de {numero} es: {resultado}")
    
    except NegativeNumberError as e:
        print(e)  # Muestra el mensaje de la excepción personalizada

    except ValueError:
        print("Error: Debe ingresar un valor numerico valido.")

# Llamada a la función para prueba
calcular_raiz_cuadrada()

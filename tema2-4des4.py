#VERIFICAR SI UN NÚMERO DADO ES DIVISIBLE ENTRE CIERTOS DIVISORES 

# Función para verificar si un número es múltiplo de otros
def es_multiplo(divisores, numero):
    for divisor in divisores:
        if numero % divisor == 0:
            print("¿Es " + str(numero) + " multiplo de " + str(divisor) + "? Si")
        else:
            print("¿Es " + str(numero) + " multiplo de " + str(divisor) + "? No")
            
# Número dado para verificar
numero = 40

# Lista de números para verificar si el número dado es múltiplo de ellos
divisores = [2, 3, 5, 7, 9, 10, 11]            
            
es_multiplo(divisores, numero)

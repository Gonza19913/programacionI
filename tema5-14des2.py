def operar_lista(valores):
    resultados = []
    
    for valor in valores:
        try:
            # Intentamos convertir el valor a float antes de la operación
            valor = float(valor)
            # Intentamos dividir 100 por cada valor de la lista
            resultado = 100 / valor
            resultados.append(resultado)
        
        except ZeroDivisionError:
            print(f"Error: No se puede dividir entre cero para el valor {valor}.")
            resultados.append(None)  # Agrega un valor nulo si hay error
        
        except TypeError:
            print(f"Error: Tipo de dato invalido para el valor {valor}. Solo se permiten numeros.")
            resultados.append(None)
        
        except ValueError:
            print(f"Error: Valor invalido {valor}. Debe ser numerico.")
            resultados.append(None)
    
    return resultados

# Ejemplo de lista de prueba con diferentes tipos de valores
valores = [0, 10, 25, 50, 100, 'a', None, 'xyz']
resultados = operar_lista(valores)
print("Resultados:", resultados)


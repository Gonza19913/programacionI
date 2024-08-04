# Batalla Naval Jugador vs Jugador
import random

import numpy as np

DIMENSIONES_TABLERO = 5 # Tamaño del tablero (5x5) o se puede cambiar a otro tamaño 
CANTIDAD_BARCOS = 3
DISPARO_FALLIDO = "-" # Símbolo para representar un disparo fallido
DISPARO_ACERTADO = "1"
JUGADORES = ["J1", "J2"]

def crear_tablero(dimension):
    # Crea un tablero vacío con 0 (agua) usando numpy
    return np.full((dimension, dimension), '0', dtype=str)

def colocar_barcos(mar, cantidad_barcos):
    dimension = len(mar)
    barcos_colocados = 0
    # Coloca barcos aleatoriamente hasta alcanzar la cantidad especificada
    while barcos_colocados < cantidad_barcos:
        # Genera coordenadas aleatorias
        fila = random.randint(0, dimension - 1)
        columna = random.randint(0, dimension - 1)

        if mar[fila, columna] == "0":  # Verifica que la posición esté vacía
            mar[fila, columna] = "B" # Coloca el barco ('B' representa barco)
            barcos_colocados += 1
            

def imprimir_tablero(tablero):
    letras = 'ABCDE' # Letras para las filas
    # Imprime los numeros sobre el tablero
    print("  " + " ".join([str(i+1) for i in range(DIMENSIONES_TABLERO)]))
    for i in range(DIMENSIONES_TABLERO):
        # Imprime las letras de las columnas
        print(letras[i], " ".join(tablero[i, j] for j in range(DIMENSIONES_TABLERO)))

def convertir_coordenada(coordenada):
    letras = 'ABCDE'
    # Coordenadas es un arreglo con la letra y el numero fila y columna
    fila = letras.index(coordenada[0].upper())
    columna = int(coordenada[1]) - 1
    return fila, columna

def hacer_tiro(tablero, mar, fila, columna):
    #verifica si el disparo fue acertado
    if mar[fila, columna] == "B":
        print("¡Acierto!")
        tablero[fila, columna] = DISPARO_ACERTADO
        mar[fila, columna] = "0"  # Elimina el barco del mar
    else:
        print("¡Fallo!")
        # Actualiza la interface 
        tablero[fila, columna] = DISPARO_FALLIDO

def verificar_victoria(mar):
    #verifica si todos los barcos han sido hundidos
    #devuelve false si hay barcos en el tablero
    return not np.any(mar == "B")

# Inicializar tableros y mares de los jugadores
tablero_j1 = crear_tablero(DIMENSIONES_TABLERO)
tablero_j2 = crear_tablero(DIMENSIONES_TABLERO)
mar_j1 = crear_tablero(DIMENSIONES_TABLERO)
mar_j2 = crear_tablero(DIMENSIONES_TABLERO)

# Colocar barcos
colocar_barcos(mar_j1, CANTIDAD_BARCOS)
colocar_barcos(mar_j2, CANTIDAD_BARCOS)

turno = 0

while True:
    jugador_actual = JUGADORES[turno % 2]
    tablero_actual = tablero_j1 if jugador_actual == "J1" else tablero_j2
    mar_oponente = mar_j2 if jugador_actual == "J1" else mar_j1

    print(f"Turno de {jugador_actual}")
    imprimir_tablero(tablero_actual)
    mensaje = " ingresa tu movimiento (por ejemplo, A4): "
    movimiento = input(f"{jugador_actual},{mensaje}").strip().lower()
    if movimiento == 'salir':
        break

    try:
        fila, columna = convertir_coordenada(movimiento)
        if 0 <= fila < DIMENSIONES_TABLERO and 0 <= columna < DIMENSIONES_TABLERO:
            hacer_tiro(tablero_actual, mar_oponente, fila, columna)
            if verificar_victoria(mar_oponente):
                print(f"¡{jugador_actual} gana!")
                break
            turno += 1
        else:
            print("Movimiento fuera de rango. Inténtalo de nuevo.")
    except Exception:
        print("Movimiento inválido. Inténtalo de nuevo.")
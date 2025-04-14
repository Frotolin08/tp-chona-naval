import random as rand 
# Importando módulo para generar valores al azar. 
#https://www.w3schools.com/Python/module_random.asp


N: int = 5 # tamaño tablero
disparos_acertados: int = 0 # veces que el jugador le pega a un barco


# declaración de constantes
NUM_DISPAROS: int = 10
NUM_BARCOS: int = 10

# declarando tablero en términos de N
tablero: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
tablero_disparados: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]

# generación aleatoria de barcos
for i in range(NUM_BARCOS):
    x: int = rand.randint(0, N-1)
    y: int = rand.randint(0, N-1)
    tablero[x][y] = True

# for i in tablero:
#     print(i)


for i in range(NUM_DISPAROS): # iterando sobre cada disparo posible
    coords: str = input("Ingresar coordenadas para disparar (en formato 'x y').\n") # Ingreso de coords del jugador
    if (len(coords) != 3): # viendo que tenga el tamaño correcto https://www.w3schools.com/python/gloss_python_string_length.asp
        print("Input inválido.")
        continue

    coords_separadas: list[int] = coords.split()

    x: int = int(coords_separadas[0])
    y: int = int(coords_separadas[1])

    # el input se splittea y luego se usa esa lista para asignar valores a x & y
    #https://www.w3schools.com/python/ref_string_split.asp

    if (type(x) != int or type(y) != int or x >= N or y >= N): # checkeando que ambos sean ints y estén en el tablero
        print("Input inválido.")
        continue

    if (tablero[x][y] == True): # Hay un barco en esas coords
        tablero[x][y] = False # ya no está más en pie
        tablero_disparados[x][y] = True
        disparos_acertados += 1
        print("El disparo acertó a uno de los barcos.")
    else:
        print("El disparo no acertó.")

print(f"\nJuego finalizado. Se acertaron {disparos_acertados} tiros y se fallaron {NUM_DISPAROS - disparos_acertados}.")
print("\nTablero final (0 para vacío, b para barco y h para hundido): ")

for i in range(N): # iterando a través de las filas del tablero

    fila: str = "" # se va definiendo con el prox loop
    for j in range(N): # iterando a través de cada item de las filas
        if(tablero_disparados[i][j]): # hay barco hundido
            fila += "h "
        elif(tablero[i][j]): # hay barco en pie
            fila += "b "
        else:
            fila += "0 " # no había barco
    
    print(fila)





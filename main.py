import random as rand 
# Importando módulo para generar valores al azar. 
#https://www.w3schools.com/Python/module_random.asp


N: int = 5 # tamaño tablero
disparos_acertados: int = 0 # veces que el jugador le pega a un barco


# declaración de constantes
NUM_DISPAROS: int = 10
NUM_BARCOS: int = 9

multiplayer: bool = bool(int(input("Singleplayer (0) o Multiplayer (1)?\n"))) # definiendo modo de juego

if (not multiplayer):

    # declarando tablero en términos de N
    tablero: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]
    lista_disparados: list[bool] = [False for _ in range(NUM_BARCOS+1)]

    # generación aleatoria de barcos
    for i in range(1, NUM_BARCOS+1):
        size: int = rand.randint(1, 3)
        x: int = rand.randint(0, N-size)
        y: int = rand.randint(0, N-size)

        sentido: int = rand.randint(0, 1) # 0 significa horizontal, 1 significa vertical

        if (sentido == 0): 
            for j in range(size):
                if (tablero[x][y+j] == 0):
                    tablero[x][y+j] = i
                else:  break # si hay un barco donde se iba a generar este nuevo, se cancela la generación

        else:
            for j in range(size):
                if(tablero[x+j][y] == 0):
                    tablero[x+j][y] = i
                else:  break


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

        if (tablero[x][y] != 0 and not lista_disparados[tablero[x][y]]): # Hay un barco en esas coords y todavía no lo hundieron
            lista_disparados[tablero[x][y]] = True # registrando que ese barco fue hundido
            disparos_acertados += 1
            print("El disparo acertó a uno de los barcos.")
            
        else:
            print("El disparo no acertó.")

    print(f"\nJuego finalizado. Se acertaron {disparos_acertados} tiros y se fallaron {NUM_DISPAROS - disparos_acertados}.")

    print("\nTablero inicial:")
    for i in tablero:
        print(i)

    # sacando barcos hundidos del tablero
    for i in range(N):
        for j in range(N):
            if(lista_disparados[tablero[i][j]]):
                tablero[i][j] = 0

    print("\nTablero final: ")

    for i in tablero:
        print(i)





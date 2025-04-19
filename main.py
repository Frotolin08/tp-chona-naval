import random as rand 
# Importando módulo para generar valores al azar. 
#https://www.w3schools.com/Python/module_random.asp


N: int = 5 # tamaño tablero
disparos_acertados: int = 0 # veces que el jugador le pega a un barco


# declaración de constantes
NUM_DISPAROS: int = 10
NUM_BARCOS: int = 5


# definiendo funciones que se usan varias veces en ambos modos de juego

def creacionBarco(sentido: bool, tablero: list[list[int]], size: int, x: int, y: int):
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

def disparo(tablero: list[list[int]], disparos_acertados: int):
    coords: str = input() # Ingreso de coords del jugador

    if (len(coords) < 3): # viendo que tenga el tamaño correcto https://www.w3schools.com/python/gloss_python_string_length.asp
        print("Input inválido.")
        return

    coords_separadas: list[int] = coords.split()

    x: int = int(coords_separadas[0])
    y: int = int(coords_separadas[1])

    # el input se splittea y luego se usa esa lista para asignar valores a x & y
    #https://www.w3schools.com/python/ref_string_split.asp

    if (type(x) != int or type(y) != int or x >= N or y >= N): # checkeando que ambos sean ints y estén en el tablero
        print("Input inválido.")
        return

    if (tablero[x][y] != 0): # Hay un barco en esas coords y todavía no lo hundieron
        tablero[x][y] = 0 # registrando que ese barco fue hundido
        disparos_acertados += 1
        print("El disparo acertó a uno de los barcos.")

    else:
        print("El disparo no acertó.")

multiplayer: bool = bool(int(input("Singleplayer (0) o Multiplayer (1)?\n"))) # definiendo modo de juego

if (not multiplayer): # sección singleplayer

    # declarando tablero en términos de N
    tablero: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]

    # generación aleatoria de barcos
    for i in range(1, NUM_BARCOS+1):
        size: int = rand.randint(1, 3)
        x: int = rand.randint(0, N-size)
        y: int = rand.randint(0, N-size)

        sentido: bool = bool(rand.randint(0, 1)) # 0 significa horizontal, 1 significa vertical

        creacionBarco(sentido, tablero, size, x, y)

    for i in range(NUM_DISPAROS): # iterando sobre cada disparo posible
        print("Ingresar coordenadas para disparar (en formato 'y x').\n")
        disparo(tablero, disparos_acertados)

    print(f"\nJuego finalizado. Se acertaron {disparos_acertados} tiros y se fallaron {NUM_DISPAROS - disparos_acertados}.")

    print("\nTablero final: ")

    for i in tablero:
        print(i)




# multiplayer

else: 

    # declarando tablero en términos de N
    tablero: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]
    tablero_opp: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]

    disparos_acertados_opp: int = 0

    # ingresando posiciones de los barcos
    print("Jugador 1: Ingresar barcos \n(formato: 'y_inicial x_inicial sentido longitud', sentido siendo 0 para horizontal y 1 para vertical, y longitud estando entre 1 y 3).")

    for i in range(1, NUM_BARCOS+1):

        barco: str = input() # recolección de todos los datos
        datos: list[int] = barco.split()
        x: int = int(datos[0])
        y: int = int(datos[1])
        sentido: bool = bool(int(datos[2]))
        longitud: int = int(datos[3])

        # error handling
        if( (x > N-longitud and sentido == True) or (y > N-longitud and sentido == False) or longitud > 3 or x > N-1 or y > N-1):
            print("Input inválido.")
            continue

        creacionBarco(sentido, tablero, longitud, x, y)

        for i in tablero:
            print(i)

    print("\nJugador 2: Ingresar barcos \n(formato: 'y_inicial x_inicial sentido longitud', sentido siendo 0 para horizontal y 1 para vertical, y longitud estando entre 1 y 3).")

    for i in range(1, NUM_BARCOS+1):
        barco: str = input() # recolección de todos los datos
        datos: list[int] = barco.split()
        x: int = int(datos[0])
        y: int = int(datos[1])
        sentido: bool = bool(int(datos[2]))
        longitud: int = int(datos[3])

        # error handling
        if( (x > N-longitud and sentido == True) or (y > N-longitud and sentido == False) or longitud > 3 or x > N-1 or y > N-1):
            print("Input inválido.")
            continue

        creacionBarco(sentido, tablero_opp, longitud, x, y)

        for i in tablero_opp:
            print(i)

    # finalizada la creación de barcos de ambos bandos

    print(f"\nJugador 1: Tenés {NUM_DISPAROS} para derribar la máxima cantidad de barcos de Jugador 2.")
    print("Ingresar coordenadas para disparar (en formato 'x y').\n")
    for i in range(NUM_DISPAROS):
        disparo(tablero_opp, disparos_acertados)

    print(f"\nJugador 2: Tenés {NUM_DISPAROS} para derribar la máxima cantidad de barcos de Jugador 1.")
    print("Ingresar coordenadas para disparar (en formato 'x y').\n")
    for i in range(NUM_DISPAROS):
        disparo(tablero, disparos_acertados_opp)
    
    print(f"Juego finalizado. Jugador 1 acertó {disparos_acertados} tiros y Jugador 2 acertó {disparos_acertados_opp}. ")

    print("\nTablero final J1:")
    for i in tablero:
        print(i)

    print("\nTablero final J2:")
    for i in tablero_opp:
        print(i)






import random
#modulo para generar vaores al azar. Lo usé para generar las coordenadas aleatoreas. 
#https://www.w3schools.com/Python/module_random.asp


n:int=10
barcosRestantes:int = 5
tabla:list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]
#declarar las variables de la lista de lsitas para el tablero, la cantidad de barcos con los que se juega 
#y el tamaño del tablero

for x in range(0, barcosRestantes):
    x:int= random.randint(0, n-1)
    y:int= random.randint(0, n-1)
    if tabla[x][y] == True:
        continue
    else:
        tabla[x][y] = True
        
       #utilizar para ver las coordenadas de los barcos -> print("x= "+str(x)+" y= "+str(y))
    
#generar 2 enteros aleatoreos dentro de los valores aplicables para el tamaño del tablero y asignarles un barco    

for x in range(0, 10):
    print("ingrese la cordenada x que desea disparar")
    x:int = int(input())
    print("ingrese la cordenada y que desea disparar")
    y:int = int(input())
  
    #pedir que el jugador ingrese las cordenadas para el disparo que quiere realizar

    if(type(x) == int and type(y) == int and x<n and x>-1 and y<n and y>-1):
        #verificar si el valor ingresado es válido(entero, dentro del rango correcto)
        if(tabla[x][y] == True):
            #verificar si se le acertó a un barco o no
            print("Se disparó a un barco")
            tabla[x][y]= False
            barcosRestantes-=1
        else:
            print("se disparo al agua")
    else:
        print("se ingresó un valor de x o y incorrecto")
        continue




#anunciar cuantos barcos restaron
print("quedaron sin abatir "+str(barcosRestantes)+" barcos")



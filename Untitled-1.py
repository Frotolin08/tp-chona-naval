import random


n=10

tabla:list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

for x in range(0, 5):
    x= random.randint(0, n-1)
    y= random.randint(0, n-1)
    if tabla[x][y] == True:
        continue
    else:
        tabla[x][y] = True
    

for x in range(0, 10):
    print("ingrese la cordenada x que desea disparar")
    x = int(input())
    print("ingrese la cordenada y que desea disparar")
    y = int(input())

    if(type(x) == int and type(y) == int):
        if(tabla[x][y] == True):
            print("Se disparó a un barco")
            tabla[x][y]= False
        else:
            print("se disparo al agua")
    else:
        print("se ingresó un valor de x o y incorrecto")
        continue
for x in tabla:
    print(x)    


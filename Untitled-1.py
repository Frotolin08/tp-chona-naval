import random


n=10
barcosRestantes = 5
tabla:list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

for x in range(0, 5):
    x= random.randint(0, n-1)
    y= random.randint(0, n-1)
    if tabla[x][y] == True:
        continue
    else:
        tabla[x][y] = True
    print(str(x)+str(y))
    

for x in range(0, 10):
    print("ingrese la cordenada x que desea disparar")
    x = int(input())
    print("ingrese la cordenada y que desea disparar")
    y = int(input())

    if(type(x) == int and type(y) == int and x<10 and x>-1 and y<10 and y>-1):
        if(tabla[x][y] == True):
            print("Se disparó a un barco")
            tabla[x][y]= False
            barcosRestantes-=1
        else:
            print("se disparo al agua")
    else:
        print("se ingresó un valor de x o y incorrecto")
        continue




print("quedaron sin abatir "+str(barcosRestantes)+" barcos")



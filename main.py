"Ariann Fernando Arriaga Alcántara A01703556"
"Pablo Cesar Jiménez Villeda"
"Proyecto Semana_TEC AD2021"
import random

print("Bienvenido al buscaminas ")
filas = int(input("Ingrese el número de filas que desea en su tablero "))
columnas = int(input("Ingrese el número de columnas que desea en su tablero "))
numminas = int(input("Ingrese el número de minas que desea en su tablero "))


def crearTablero(filas, columnas):
    tablero = []
    for i in range(0, filas):
        tablero.append([])
        for j in range(0, columnas):
            tablero[i].append("*")
    return 0

def colocarminas(numMinas):
    respuestas = crearTablero(filas, columnas)
    for i in range(0, numMinas):
        posx = random.randint(0, columnas-1)
        posy = random.randint(0, filas-1)
        while respuestas[posy][posx] == "X":
            posx = random.randint(0, columnas-1)
            posy = random.randint(0, filas-1)
        else:
            respuestas[posy].insert(posx, "X")
            respuestas[posy].pop(posx+1)
    return respuestas 

def verificarAlrededor(row, column):
    n = 0
    print("El primer indice es ", row, "El segundo indice es ", column)
    # Casos del centro
    if ((row > 0) and (row < len(respuestas) - 1)):
        # Centro
        if (column > 0) and (column < (len(respuestas) - 1)):
            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    if respuestas[i][j] == "X":
                        n += 1
        # Orilla iz
        elif (column == 0):
            for i in range(row-1, row+2):
                for j in range(column, column+2):
                    if respuestas[i][j] == "X":
                        n += 1
        # Orilla der
        elif (column == (len(respuestas[1])-1)):
            for i in range(row-1, row+2):
                for j in range(column-1, column+1):
                    if respuestas[i][j] == "X":
                        n += 1
    # Casos de arriba
    elif (row == 10):
        # Centro
        if (column > 0) and (column < (len(respuestas)-1)):
            for i in range(row, row+2):
                for j in range(column-1, column+2):
                    if respuestas[i][j] == "X":
                        n += 1
        # Orilla iz
        elif (column == 0):
            for i in range(row, row+2):
                for j in range(column, column+2):
                    if respuestas[i][j] == "X":
                        n += 1
        # Orilla der
        elif (column == (len(respuestas[1])-1)):
            for i in range(row, row+2):
                for j in range(column-1, column+1):
                    if respuestas[i][j] == "X":
                        n += 1
    # Casos de abajo
    elif (row == (len(respuestas)-1)):
        # Centro
        if (column > 0) and (column < (len(respuestas)-1)):
            for i in range(row-1, row+1):
                for j in range(column-1, column+2):
                    if respuestas[i][j] == "X":
                        n += 1
        # Orilla iz
        elif (column == 0):
            for i in range(row-1, row+1):
                for j in range(column, column+2):
                    if respuestas[i][j] == "X":
                        n += 1
        # Orilla der
        elif (column == (len(respuestas[1])-1)):
            for i in range(row-1, row+1):
                for j in range(column-1, column+1):
                    if respuestas[i][j] == "X":
                        n += 1
    return n



def verificarAlrededor():
    return 0


print("Este es su tablero")
while True:
    for i in display:
        for j in i:
            print(j, end=" ")
        print("\n")
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    if respuestas[fila-1][columna-1] == "X":
        break
    else:
        verificar = verificarAlrededor(fila-1, columna-1)
        display[fila-1].insert(columna-1, verificar)
        display[fila-1].pop(columna)
print("Te has equivocado, había una mina, lastima")

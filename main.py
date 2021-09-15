import random

print("Bienvenido al buscaminas ")

def crearTablero(filas, columnas):
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
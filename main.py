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
"jijo mano"

def verificarAlrededor():
    return 0
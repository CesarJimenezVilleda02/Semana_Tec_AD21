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


display = crearTablero(filas, columnas)


def colocarminas():
    return 0


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
print("Te has equivocado, había una mina,lastima")

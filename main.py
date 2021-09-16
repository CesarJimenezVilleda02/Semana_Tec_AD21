"Ariann Fernando Arriaga Alcántara A01703556"
"Pablo Cesar Jiménez Villeda A01703517"
"Proyecto Semana_TEC AD2021"
import random
from threading import Thread
from playsound import playsound
import webbrowser


# Función para abrir archivo de música de fondo
def Fun_mus():
    playsound('Como_te_atreves.mp3')
    

# Definir función que llama audio
music = Thread(target=Fun_mus)
music.daemon = True
# Iniciar musica
music.start()
print("Bienvenido al buscaminas ")
# Inicializacion del estado inicial
filas = int(input("Ingrese el número de filas que desea en su tablero "))
columnas = int(input("Ingrese el número de columnas que desea en su tablero "))
numminas = int(input("Ingrese el número de minas que desea en su tablero "))
score = 0
rondas = 1
rondasParaGanar = (filas * columnas) - numminas 


def crearTablero(filas, columnas):
    tablero = []
    for i in range(0, filas):
        tablero.append([])
        for j in range(0, columnas):
            tablero[i].append(" * ")
    return tablero


display = crearTablero(filas, columnas)


def colocarminas():
    respuestas = crearTablero(filas, columnas)
    for i in range(0, numminas):
        posx = random.randint(0, columnas-1)
        posy = random.randint(0, filas-1)
        while respuestas[posy][posx] == "X":
            posx = random.randint(0, columnas-1)
            posy = random.randint(0, filas-1)
        else:
            respuestas[posy].insert(posx, "X")
            respuestas[posy].pop(posx+1)
    return respuestas


respuestas = colocarminas()


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


print("Este es su tablero")
while True:
    # Mostrar el tablero y el puntaje
    print("Tu puntuaje actual es de: ", score, "\n")
    for i in display:
        for j in i:
            print(j, end=" ")
        print("\n")
        for j in i:
            print('_', end='___')
        print("\n")
    # Usuario ingresa nueva locación
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    # Pierde
    if respuestas[fila-1][columna-1] == "X":
        print("Te has equivocado, había una mina. \nObtuviste un puntaje de: ", score)
        webbrowser.open('https://www.youtube.com/watch?v=UzdLXlDAHGc', new=1, autoraise=True)
        playsound('game_over.mp3')
        break
    # Gana
    elif rondas == rondasParaGanar:
         print("Felicidades haz ganado el juego: \nObtuviste un puntaje de: ", score)
         playsound('victory.mp3')
         webbrowser.open('https://www.youtube.com/watch?v=KXw8CRapg7k', new=1, autoraise=True)
         break
    # Sigue jugando
    else:
        verificar = verificarAlrededor(fila-1, columna-1)
        display[fila-1].insert(columna-1, " " + str(verificar) + " ")
        display[fila-1].pop(columna)
        score += verificar
        rondas += 1


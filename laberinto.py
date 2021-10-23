
# Clase del modulo  collections
from queue import Queue



def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    map = []
    map.append(["#","#","#","#","#","O","#"]) 
    map.append(["#"," "," "," "," "," ","#"]) 
    map.append(["#"," ","#","#","#","#","#"])  
    map.append(["#"," ","#"," ","#"," ","#"]) 
    map.append(["#"," ","#"," ","#"," ","#"]) 
    map.append(["#"," ","#"," ","#"," ","#"]) 
    map.append(["X"," "," "," "," "," ","#"]) 
    map.append(["#","#","#","#","#","#","#"]) 
    return map

def createMaze3():
    maze = []
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "O"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    # Vamos a procesar nuestro mazo y obtener la posicion de inicio "O" con Tuplas, haciendo funcion
    # del metodo enumerate -> [(0,"#"),(1," "),(2,"O")] 
    for i, value in enumerate(maze[0]):
        if value == "O":
            start = i
        
    # Start es nuestra varible que contine la posicion de inicio o la posicion de "O".
    i = start
    j = 0
    # Este for inspeccionara el string put o moves para filtrar los movimientos y aplicar una operacion.
    # La operacion que realice nos permitira evaluar si en la posicion que estamos existe una almuadilla o #
    # Cada vez que se pueda generar un moviento, este repetira el proceso y preguntara si es posible generar otro moviento.
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        # Preguntamos que i y j se encuentren dentro de nuestro rango.
        # SI j esta dentro de el tamaño de nuestro mazo, recordar que el tamaño es a base de las cantidad de listas que encuentran en nuestra lista. 
        # SI i no esta dentro del tamaño de la lista de indice 0 y es mayor igual a 0.   
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        # Si la posicion que se pretende generar se encuentra una almuadilla o # no se ejecuta la funcion
        elif (maze[j][i] == "#"):
            return False
    # agregaremos nuestro moviento si es true
    return True

# Funcion que se ejecutara hasta que se encuentre el final del camino X, se puede usar para la generacion de grafos 👈
def findEnd(maze, moves):
    # Vamos a procesar nuestro mazo y obtener la posicion de inicio "O" con Tuplas, haciendo funcion
    # del metodo enumerate -> [(0,"#"),(1," "),(2,"O")] 
    for i, pos in enumerate(maze[0]):
        if pos == "O":
            start = i
    # Start es nuestra varible que contine la posicion de inicio o la posicion de "O".
    # i es igual a movimeinto entre la lista, de lado a lado
    i = start
    # j es igual a movientos sobre listas, de lista en lista.
    j = 0
    
    # add = moves por lo tanto iniciamos sin ninungun movimiento.
    # Este for inspeccionara el string add o moves para filtrar los movimientos y aplicar una operacion  
    for move in moves:
        # Movimiento en left
        if move == "L":
            i -= 1
        # Movimiento en rigth
        elif move == "R":
            i += 1
        # Movimiento en  upp
        elif move == "U":
            j -= 1
        # Movimiento en down
        elif move == "D":
            j += 1
    # print("Valor de j:", j)
    # print("Valor de i:", i)
    
    # Preguntamos si la posicion del i,j es donde se encuentra nuestro punto final X
    if maze[j][i] == "X":
        print("Found: " + moves) # Si es encontrada, imprimimos los movimientos 

        printMaze(maze, moves) # Enviamos los movimientos a nuestra funcion imprimir asi como nuestro mapa.
        return True # Terminamos el ciclo de la funcion main.

    return False





def run():
    #Implementacion de cola, instacia nums.
    # Esta cola sigue la regla FIFO.
    nums = Queue()
    # Agregamos un primer valor vacio
    nums.put("")
    # Instanciamos la varible add.
    add = ""
    # Devolvemos el mazo en una lista de listas
    maze  = createMaze2()
    MOVEMENTS = ["L", "R", "U", "D"]
    while not findEnd(maze, add): 
        # Si no se encuentra el valor de X seguimos procesado las lineas de codigo.

        # Obtenemos y eliminamos el ultimo elemento de nuestra cola nums y se almacena en add
        add = nums.get()
        # Recurremos nuestra lista de posibles movimientos empezando de Left, right, upp y donw, hasta encontrar un movimiento
        # que pueda ejecutarse.
        for j in MOVEMENTS:
            # Put es la cocatenacion del ultimo elemento de nums y del movimiento.
            put = add + j
            # Validamos si es posible ejecutar el moviento.
            
            if valid(maze, put):
                # print(True)
                # print(put)
                # Si el movimeinto se puede hacer añadimos el moviento a nums
                nums.put(put)
            # Pruebas de funcionalidad en movimientos.
            # else:
            #     print(False)
            #     print(put)
            # breakpoint()
                
                



if __name__ == '__main__':
    run()

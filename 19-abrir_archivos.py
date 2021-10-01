# Existen varias extensiones de archivos 
# con los que podemos interactuar con 
# python (js,csv,py,css,json,xml).

# Para abrir un archivo seguimos las siguiente estructura

# with open(<ruta>, <modo_apertura>) as <nombre>

# with Es un manejador contextual, nos ayuda a controlar el flujo 
# del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

# open(ruta,modo_apertura): es una función que necesita de dos parámetros:

    # ruta: es donde se encuentra nuestro archivo en nuestro equipo
    # modo_de_apertura: como vamos a abrir el archivo, los modificadores son:
        # r → modo de lectura
        # w → modo de escritura (sobreescribe el archivo)
        # a → modo append (añade información al final del archivo)

        # r -> Solo lectura
        # r+ -> Lectura y escritura
        # w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
        # w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
        # a -> Añadido (agregar contenido). Crea el archivo si éste no existe
        # a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

# as <nombre> nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer

def read():
    numbers =[]
    with open('files/test.txt', 'r', encoding='utf-8') as f:
        # Leer cada linea
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['Lupita','Juan Manuel','Abraham','Andrea', 'Rocío']
    with open('files/names.txt','w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
def append_file():
    ages = [1,3,4,5]
    with open('files/age.txt','a', encoding='utf-8') as f:
        for age in ages:
            f.write(str(age))
            f.write('\n')
    
def run():
    read()
    write()
    append_file()

if __name__ == '__main__':
    run()
def run():
     # 🐍 ------ Abraham Baltzar García Moreno ------ 🐍
    # dict_classic = {} 
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         dict_classic[i] = i**3
    # print(dict_classic)
    #---------------------------------------------#
    
    #👉 Ejemplo #1 👈
    # Creacion de un diccionario con comprehension
    my_dict = {i : i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

     #---------------------------------------------#

    #👉 Ejemplo #2 👈
    # Diccionario cuyas llaves son los 1000 primeros numeros naturales con sus raices cuadradas como valores.
    my_dict_sqrt = {i : round(i**0.5, 2) for i in range(1, 1001)}
    print(my_dict_sqrt)

    #---------------------------------------------#
if __name__ == '__main__':
    run()
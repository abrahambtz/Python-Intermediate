def run():
    #------ Abraham Baltzar García Moreno -------- 👻
    # squares = []
    # squares_no_div3 = []
    # for i in range(1,101):
    #     squares.append(i**2)
    # print(squares)
    
    # for i in range(1,101):
    #     if i%3 != 0:
    #         squares_no_div3.append(i**2)
    
    # print(squares_no_div3)
    
    
    #---------------------------------------------#
    #👉 Ejemplo #1 👈
    # El bloque de codigo anterior se puede disminuir en la siguiente linea de codigo:
    squares_list_comprehensions = [i**2 for i in range(1, 101) if i%3 != 0]
    print(squares_list_comprehensions)

    #👉 Ejemplo #2 👈
    #List comprehension - Lista de multiplos de 4 que a la vez tambien son multiplos de 6 y de 9, hasta 5 digitos.
    multiples = [i for i in range( 1, 100000) if i%4 == 0 and i%6 and i%9 == 0] 
    

if __name__ == "__main__":
    run()
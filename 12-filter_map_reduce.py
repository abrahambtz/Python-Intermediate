from functools import reduce

def run():
    # Funciones de orden superior son aqullas funciones que reciben como parametro funciones.
    my_list = [1,2,3,4,5,6,7,8,9]
    print(my_list)
    odd = list(filter(lambda x: x%2 != 0, my_list))
    squares = list(map(lambda x: x**2, my_list))
    all_multiplied = reduce(lambda a, b: a*b, my_list)
    all_summation = reduce(lambda a, b: a+b, my_list)
    print(odd)
    print(squares)
    print(all_multiplied)
    print(all_summation) 
if __name__ == '__main__':
    run()

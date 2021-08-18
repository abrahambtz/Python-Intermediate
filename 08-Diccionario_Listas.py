def run():
    my_list = [1, 'Hi', True, 4.5]
    my_dicc = {
        "firstname": "abraham",
        "lastname": "garcia",
        "age": 22,    
    }
    super_list = [
        {
            "firstname": "abraham",
            "lastname": "garcia",
            "age": 22,    
        },
        {
            "firstname": "lupia",
            "lastname": "moreno",
            "age": 50,    
        },
        {
            "firstname": "jazmin",
            "lastname": "garcia",
            "age": 22,    
        },
        {
            "firstname": "paola",
            "lastname": "cortez",
            "age": 23,    
        },
    ]
    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1, 0, 1, 2],
        "float_nums" : [1.5, 2.5, 3.5],
    }
    #Imprimir super lista de diccionarios
    for values in super_list:
        for key, value in values.items():
            print(key + " : " + str(value)) 
    #Imprimir super diccionario de listas
    for key, value in super_dict.items():
        print("La llave es " + key + " el valor es " + str(value)) 
        
if __name__ == '__main__':
    run()
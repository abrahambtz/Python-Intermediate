def divisor(num):
    try:
        if num < 0:
            raise ValueError('Ingresa un numero mayor a 0')
        list = [i for i in range(1, num+1) if num % i == 0] 
        return list
    except ValueError as ve:
        print(ve)
        return 0
        


def run():
    while True:
        try:
            num = int(input('>'))
            print(divisor(num))
        except ValueError:
            print("Solo puedes ingresar numeros")
    
if __name__ == '__main__':
    run()
def divisor(num):
    list = [i for i in range(1, num+1) if num % i == 0] 
    return list
    
        


def run():
    while True:
    
        num = input('>')
        assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
        print(divisor(int(num)))
    
    
if __name__ == '__main__':
    run()
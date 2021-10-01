def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar strings")

if __name__ == '__main__':
    run()


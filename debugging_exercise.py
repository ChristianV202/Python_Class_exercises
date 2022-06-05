#Exercise. We're looking for a error message display when the number introduced by user is negative

def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("You have to enter a positive number")
    
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:               #Si en algun momento de la ejecucion de las tres lineas de arriba--
        print("Enter a number")   #--ocurre una excepcion ValueError, se ejecutara el except

if __name__ == '__main__':          #Entry Point
    run()
    


#Another possible solution
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:             #Estos son conocidos como ciclos 1-x. Es decir, la primera vez ocurre si o si, y luego el ciclo se rompe
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")


if __name__ == '__main__':
    run()

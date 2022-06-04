def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:               #Si en algun momento de la ejecucion de las tres lineas de arriba--
        print('Debes ingresar un numero')   #--ocurre una excepcion ValueError, se ejecutara el except

if __name__ == '__main__':          #Entry Point
    run()
    

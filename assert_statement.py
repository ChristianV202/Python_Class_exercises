def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
        num = input("Ingresa un numero: ")      #Elimine la funcion int() porque isnumeric() solo puede evaluar strings
        assert num.isnumeric(), "Debes ingresar un numero"   #Metodo de los strings que devuelve true o
        print(divisors(int(num)))                            # false si el string es un tipo de numero
        print("Termino mi programa")

if __name__ == '__main__':          #Entry Point
    run()
    
#Con este codigo pido un numero al usuario, y con num.isnumeric() me fijo si es un numero
#Si no lo es, salta una excepcion con el mensaje que puse

#Alternativa
def run():
        num = input("Ingresa un numero: ")     
        assert num.isnumeric() and int(num) > 0 , "Debes ingresar solo numeros positivos"   
        print(divisors(int(num)))                            
        print("Termino mi programa")
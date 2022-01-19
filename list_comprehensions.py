#Objetivo: Lista 100 numeros naturales al 2
def run():
    squares = []

    for i in range(1, 101):
        if i % 3 != 0:  #Guardamos el numero que no es divisible por 3
            squares.append(i**2)    #Metodo para agregar elementos a una lista
        
    print(squares)



if __name__ == '__main__':  #Entry point
    run()


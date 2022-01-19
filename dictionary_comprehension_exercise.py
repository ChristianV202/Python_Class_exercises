import math
#from path import sqrt tambien es posible
def run():
    my_dictionary = {i: math.sqrt(i) for i in range(1, 1001)}
    print(my_dictionary)


if __name__ == '__main__':
    run()

#Hay otras maneras de resolverlo en los comentarios de la clase dictionary comprehensions
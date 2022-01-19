'''
List Comprehension

my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = [i for i in my_list if i % 2 != 0]
print(odd)

'''

#Filter / High order function

my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)
#Filter es la funcion de alto orden que usamos
#Recibe dos parametros, un lambda y un iterable
#FILTRA lo que hay en el iterable de acuerdo a mi primer elemento, que es como una condicion
#Es necesario guardar el resultado en una lista

#LAMBDA
#Los elementos de la lista al iterarse, pasaran por X
#Evaluara si al dividir x por 2, el resto es distinto de 0. O sea, si es par o impar.
#Si es TRUE, guardara ese numero. Si es False, sigue de largo.


#Map

my_list = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, my_list))
print(squares)

#Recorre toda la lista y guarda todos los numeros elevados al 2



#Reduce

from functools import reduce

my_list = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)

#Regresa el numero 32
def palindrome(string):
    return string == string[::-1]


try:                        #Intenta lo siguiente
    print(palindrome(1))
except TypeError:           #Si sucede un TypeError haz lo siguiente
    print("Solo se pueden ingresar strings")

#Esto se ve en mas detalle tanto en el video de la clase como en las anotaciones del cuaderno
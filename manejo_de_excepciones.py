#TRY, EXCEPT

def palindrome(string):
    return string == string[::-1]


try:                        #Intenta lo siguiente
    print(palindrome(1))
except TypeError:           #Si sucede un TypeError haz lo siguiente
    print("Solo se pueden ingresar strings")

#Esto se ve en mas detalle tanto en el video de la clase como en las anotaciones del cuaderno



#RAISE, as ve

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
    

try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")


#FINALLY

try:
    f = open("archivo.txt") #se ve en detalle lo que es esto en proximas clases

finally:
    f.close()

#finalmente, suceda un error o no, cerramos el archivo con la funcion f.close()
#sucedera lo que ponemos con finally sin importar si se producen errores o no

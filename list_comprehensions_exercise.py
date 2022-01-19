def run():      #La lista va a comenzar con 36
    lista = [4*i for i in range(1, 10000) if i%9 == 0]
    print(lista)

if __name__ == '__main__':
    run()

#Hay varias maneras de resolverlo que se ven en los comentarios y en los archivos de clase
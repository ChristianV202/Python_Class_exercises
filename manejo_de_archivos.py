def read():
    numbers = []
    with open("./archivos_manejo/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:              #Recorremos cada linea dentro del archivo(leer)
            numbers.append(int(line))   #Agrego a numbers lo que hay en line pasado a integer
    print(numbers)


def write():
    names = ["Archer", "Gabriel", "Ariel"]
    with open("./archivos_manejo/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)      #Escribir en f el valor de name
            f.write("\n")       #Salto de linea


def run():
    write()


if __name__ == '__main__':
    run()
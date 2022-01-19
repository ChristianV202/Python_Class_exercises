#Vemos como se usan los lambda

def run():
    variable = lambda string: string == string[::-1]
    print(variable('ana'))

    
if __name__ == '__main__':
    run()
#Tenemos constantes en Python
from unicodedata import name

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #Usar ahora filter y map
    #all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    #all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    all_python_devs = list(filter(lambda name: name['language'] == 'python', DATA)) #lambda va a recorrer DATA, y a cada diccionario que encuentra, lo guarda en name. Despues busca la keyword 'language' dentro de cada name/diccionario y lo compara con mi condicion 'python'


    
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    old_people = list(map(lambda worker: worker | {'old': worker ['age'] > 70}, DATA))

    for worker in all_python_devs:
        print(worker)


if __name__ == '__main__':
    run()

#En este programa aprendemos a filtrar datos
#Usamos distintas tecnicas para separar trabajadores de acuerdo a categorias
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
    all_pythons_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_worker = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    

    
    # List comprehensions
    # Devuelve una lista de nombre empleados mayores de 18
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    #print(adults)
    
    adults = list(filter(lambda worker: worker['age'] > 18, DATA)) # Filtrer limpia y devuelve lo que cumpla con la condicion
    adults = list(map(lambda worker: worker['name'], adults)) # Map solo va a organizar de acuerdo.
    adults = list(map(lambda worker: {worker['name'], worker['age']}, DATA))
    # Unir diccionario con otro diccionario, de acuerdo lo que obtengamos en su condicion
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    

    # Reto: 

    all_python_devs_fm = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_fm = list(map(lambda worker: worker['name'], all_python_devs_fm))
    print(all_python_devs_fm)
    all_platzi_worker_fm = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_worker_fm = list(map(lambda worker: worker['name'], all_platzi_worker_fm))
    print(all_platzi_worker_fm)

    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(adults)
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]
    print(old_people)



    #print(old_people)
    # print(adults)
    # for i in old_people:
    #     print(i)
    #print(all_platzi_worker)
    #print(all_pythons_devs)

    

if __name__ == '__main__':
    run()
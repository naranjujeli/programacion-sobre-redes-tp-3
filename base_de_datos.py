# https://www.espn.co.uk/football/story/_/id/37633460/2022-world-cup-all-squad-lists-qatar

# Info de ejemplo
### Borrar y cargar con sus datos


import json
import random



data_file = "data.json"

def open_data(filepath):
    with open(filepath, 'r') as f:
        try:
            data = json.load(f)
            return data
        except:
            return {}
        
def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def obtener_codigo_por_pais(pais):
    
    data = open_data(data_file)
    try:
        data["paises"][pais]
        return data["paises"][pais]["code"]
    except KeyError:
        raise Exception("No existe tal pais")

def obtener_pais_por_codigo(codigo):

    data = open_data(data_file)
    for pais in data["paises"]:
        if codigo == data["paises"][pais]["code"]:
            return pais
    raise Exception("Ese codigo no pertenece a ningun pais")

def obtener_todo():
    return open_data(data_file)

def obtener_todos_los_paises():

    paises = []
    data = open_data(data_file)
    for pais in data["paises"]:
        paises.append(pais)
    return paises

def obtener_todos_los_codigos():

    codigos = []
    data = open_data(data_file)
    for pais in data["paises"]:
        codigos.append(data["paises"][pais]["code"])
    return codigos

def obtener_pais_random():

    data = open_data(data_file)
    paises = data["paises"]
    return random.choice(paises)

if __name__ == "__main__":

    result = obtener_pais_random()
    print(result)
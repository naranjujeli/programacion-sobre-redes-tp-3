# https://www.espn.co.uk/football/story/_/id/37633460/2022-world-cup-all-squad-lists-qatar

# Info de ejemplo
### Borrar y cargar con sus datos


import json
import random
import re



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
    return random.choice(list(paises.keys()))

def obtener_lista_de_paises_random(cantidad):

    resultado = []
    contador = 0
    while contador < cantidad:
        nuevo_pais = obtener_pais_random()
        if nuevo_pais not in resultado:
            resultado.append(nuevo_pais)
            contador+=1
    return resultado

def obtener_todos_los_paises_empezados_por(inicio):
    
    data = open_data(data_file)
    paises = data["paises"]
    paises = list(paises.keys())
    filtro = f"^{inicio}"
    resultado = []

    for pais in paises:
        bandera = re.search(filtro, pais)
        if bandera:
            resultado.append(pais)
    return resultado

def obtener_todos_los_paises_terminados_en(final):

    data = open_data(data_file)
    paises = data["paises"]
    paises = list(paises.keys())
    filtro = f"{final}$"
    resultado = []

    for pais in paises:
        bandera = re.search(filtro, pais)
        if bandera:
            resultado.append(pais)
    return resultado

def obtener_todos_los_paises_que_contienen_a(frase):

    data = open_data(data_file)
    paises = data["paises"]
    paises = list(paises.keys())
    filtro = f"{frase}"
    resultado = []

    for pais in paises:
        bandera = re.search(filtro, pais)
        if bandera:
            resultado.append(pais)
    return resultado

def obtener_todos_los_paises_que_tengan_tal_cantidad_de_letras_en_su_nombre(cantidad):

    data = open_data(data_file)
    paises = data["paises"]
    paises = list(paises.keys())
    resultado = []

    for pais in paises:
        if len(pais) == cantidad:
            resultado.append(pais)
    return resultado

def obtener_palabra_de_todos_los_paises_juntos_sin_espacios():

    data = open_data(data_file)
    paises = data["paises"]
    paises = list(paises.keys())
    resultado = ""

    for pais in paises:
        resultado += pais
    return resultado.replace(" ", "")



if __name__ == "__main__":

    result = obtener_palabra_de_todos_los_paises_juntos_sin_espacios()
    print(result)
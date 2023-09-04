# https://www.espn.co.uk/football/story/_/id/37633460/2022-world-cup-all-squad-lists-qatar

# Info de ejemplo
### Borrar y cargar con sus datos


import json
import random
import re

class DatabaseAccess:
    def __init__(self):
        self.__data_file_path = "data.json"

    def __open_data(self):
        with open(self.__data_file_path, 'r') as f:
            try:
                data = json.load(f)
                return data
            except:
                return {}
            
    def __save_data(self, data):
        with open(self.__data_file_path, 'w') as f:
            json.dump(data, f)

    def get_code_by_country(self, country):
        data = self.__open_data()
        try:
            data["countries"][country]
            return data["countries"][country]["code"]
        except KeyError:
            raise Exception("No existe tal pais")

    def get_country_by_code(self, code):

        data = self.__open_data()
        for pais in data["countries"]:
            if code == data["countries"][pais]["code"]:
                return pais
        raise Exception("Ese codigo no pertenece a ningun pais")

    def get_all(self):
        return self.__open_data()

    def get_all_countries(self):
        countries = []
        data = self.__open_data()
        for country in data["countries"]:
            countries.append(country)
        return countries

    def get_all_codes(self):

        codes = []
        data = self.__open_data()
        for country in data["countries"]:
            codes.append(data["countries"][country]["code"])
        return codes

    def get_random_country(self):
        data = self.__open_data()
        countries = data["countries"]
        return random.choice(list(countries.keys()))

    def get_random_countries(self, quantity):
        result = []
        count = 0
        quantity = int(quantity)
        while count < quantity:
            new_country = self.get_random_country()
            if new_country not in result:
                result.append(new_country)
                count += 1
        return result

    def get_all_countries_begginning_with(self, first_letter):
        
        data = self.__open_data()
        countries = data["countries"]
        countries = list(countries.keys())
        filter = f"^{first_letter}"
        result = []

        for country in countries:
            flag = re.search(filter, country)
            if flag:
                result.append(country)
        return result

    def get_all_countries_ending_with(self, last_letter):

        data = self.__open_data()
        countries = data["countries"]
        countries = list(countries.keys())
        filter = f"{last_letter}$"
        result = []

        for country in countries:
            flag = re.search(filter, country)
            if flag:
                result.append(country)
        return result

    def get_all_countries_containing(self, phrase):

        data = self.__open_data()
        countries = data["countries"]
        countries = list(countries.keys())
        filter = f"{phrase}"
        result = []

        for country in countries:
            flag = re.search(filter, country)
            if flag:
                result.append(country)
        return result

    def get_all_countries_with_n_letters(self, quantity):

        data = self.__open_data()
        countries = data["countries"]
        countries = list(countries.keys())
        result = []

        for country in countries:
            if len(country) == quantity:
                result.append(country)
        return result

    def get_all_countries_together(self):

        data = self.__open_data()
        countries = data["countries"]
        countries = list(countries.keys())
        result = ""

        for country in countries:
            result += country
        return result.replace(" ", "")
    
class EntradaConArgumento:

    def __init__(self, entrada):

        self.__entrada = entrada

    def __eq__(self, other):
        return other == self.__entrada
    
    def __str__(self):
        return self.__entrada

    @property
    def entrada(self):
        return self.__entrada
    
    @property
    def comando(self):
        return self.entrada.split(" ")[0]
    
    @property
    def number_of_arguments(self):
        return len(self.__entrada.split(" ")) - 1 
    
    def argumento(self, n=0):

        command = self.__entrada.split(" ")
        return command[n+1]

if __name__ == "__main__":
    database_access = DatabaseAccess()
    result = database_access.get_all_countries_with_n_letters(5)
    print(result)
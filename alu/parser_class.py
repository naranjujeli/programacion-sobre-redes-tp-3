import re

class Parser(object):

    def __init__(self):
        self._name = 'HTTP V1.1 Parser'
        self._version = 1.1
    
    def parse_request(self, message):
        # Este metodo parsea el string de un request en formato HTTP V1.1 y devuelve un objeto donde se indica:
        #   method:     string que indica el metodo usado (puede ser POST, GET, DELETE, UPDATE, etc)
        #   rute:       string con la url solicitada por el mensage a parsear
        #   parameters: diccionario con los nombre y valores de los parametros pasados en el request
        #   message:    string con el mensaje del request
        #   version:    version de HTTP parseada, en este caso, esta clase solo parsea version 1.1
        # p.parse_request('''GET server.get.message?t=45&id=123 HTTP/1.1''') -> {'method': 'GET', 'rute': 'server.send.message', 'parameters': {'t': 45, 'id': 123}, 'message': '', 'version': 1.1}

        ### COMPLETAR
        return {'method': '', 'rute': '', 'parameters': {}, 'message': '', 'version': 0.0}
    
    def parse_response(self, message):
        # Este metodo parsea el string de un response en formato HTTP V1.1 y devuelve un objeto donde se indica:
        #   status_code: numero entero de 3 digitos con el codigo de respuesta
        #   status:      string con el codigo de la respuesta
        #   parameters:  diccionario con los nombre y valores de los parametros del response
        #   message:     string con el mensaje del request
        #   version:     version de HTTP parseada, en este caso, esta clase solo parsea version 1.1

        ### COMPLETAR
        return {'status_code': 000, 'status': '', 'parameters': {}, 'message': '', 'version': 0.0}
    

    def first_validation(self, message):

        if "\n" in message:
            lines = message.partition("\n")
        else:
            return self.__second_validation(message)
        return lines
    
    def __second_validation(self, message):
        
        expresion = r'\s+'
        result = re.split(expresion, message)

        return result
    
    def __spaces(self, message):
        
        space_separated = r'(\S+)'
        results = re.findall(space_separated, message)
        return results

    def __get_method(self, message):
        
        method = re.search("(POST|GET|PUT|DELETE)", message)
        result = method.groups()
        return result[0]

    def __get_route(self, message):
        
        rute = re.search("[^\s]*\s([^\?\s]*)", message)
        result = rute.groups()
        return result[0]

    def __get_parameters(self, message):
        
        terms = self.__spaces(message)

        for term in terms:
            partitions = term.partition("?")
            try:
                index = partitions.index("?")
                parameters = partitions[index+1].split("&")
                return parameters
            except Exception as e:
                return []
            
    def __parameters_to_dict(self, parameters):
        
        result = {}
        for parameter in parameters:
            name = re.search("(.*)=", parameter)
            result_name = name.group()
            value = re.search("=(.*)", parameter)
            result_value = value.group()

            result[result_name] = result_value

        return result
    
    def without_spaces_in_the_begining(self, text):
        
        result = re.search("\s+(.*)", text)
        return result.groups()[0]


    


# para testear pueden usar los siguientes test:

# p.parse_request('''POST name HTTP/1.1''')                          -> {'method': 'POST', 'rute': 'name', 'parameters': {}, 'message': '', 'version': 1.1}
# p.parse_request('''POST server.send.message HTTP/1.1
#                    t: 56
#                    id: 123
# 
#                    Hola, este es el cuerpo del request.''')         -> {'method': 'POST', 'rute': 'server.send.message', 'parameters': {'t': 56, 'id': 123}, 'message': 'Hola, este es el cuerpo del request.', 'version': 1.1}

# p.parse_response('''HTTP/1.1 200 OK''')          -> {'status_code': 200, 'status': 'OK', 'parameters': {}, 'message': '', 'version': 1.1}
# p.parse_response('''HTTP/1.1 404 Not Found
#                     id: 123
#  
#                     No se encontro el id 123''') -> {'status_code': 404, 'status': 'Not Found', 'parameters': {id: 123}, 'message': 'No se encontro el id 123', 'version': 1.1}

if __name__ == "__main__":

    messages = [
        '''GET server.get.message?t=45&id=123 HTTP/1.1''', 
        '''POST name HTTP/1.1''', 
        '''HTTP/1.1 200 OK''', 
        '''POST server.send.message HTTP/1.1
           t: 56
           id: 123
 
           Hola, este es el cuerpo del request.''',
        '''HTTP/1.1 404 Not Found
                     id: 123
  
                     No se encontro el id 123'''
   ]
    
    p = Parser()
    for message in messages:
        result = p.first_validation(message)
        if result == None:
            pass
        else:
            for i in result:
                print(p.without_spaces_in_the_begining(i))
                print("<->")
        print("-----------------")

    
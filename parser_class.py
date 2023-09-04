import re

class Parser(object):

    def __init__(self):
        self._name = 'HTTP V1.1 Parser'
        self._version = 1.1
    
    def parse_request(self, message):
        # Este metodo parsea el string de un request en formato HTTP V1.1 y devuelve un objeto donde se indica:
        #   method:     string que indica el metodo usado (puede ser POST, GET, DELETE, UPDATE, etc)
        #   route:       string con la url solicitada por el mensage a parsear
        #   parameters: diccionario con los nombre y valores de los parametros pasados en el request
        #   message:    string con el mensaje del request
        #   version:    version de HTTP parseada, en este caso, esta clase solo parsea version 1.1
        # p.parse_request('''GET server.get.message?t=45&id=123 HTTP/1.1''') -> {'method': 'GET', 'route': 'server.send.message', 'parameters': {'t': 45, 'id': 123}, 'message': '', 'version': 1.1}

        method = self.__get_method(message)
        route = self.__get_route(message)
        parameters = self.__get_parameters(message)
        body = self.__get_body(message)
        
        return {'method': method, 'route': route, 'parameters': parameters, 'body': body, 'version': 1.1}
    
    def parse_response(self, message):
        # Este metodo parsea el string de un response en formato HTTP V1.1 y devuelve un objeto donde se indica:
        #   status_code: numero entero de 3 digitos con el codigo de respuesta
        #   status:      string con el codigo de la respuesta
        #   parameters:  diccionario con los nombre y valores de los parametros del response
        #   message:     string con el mensaje del request
        #   version:     version de HTTP parseada, en este caso, esta clase solo parsea version 1.1

        status_code = self.__get_status_code(message)
        status = self.__get_status(message)
        parameters = self.__get_parameters(message)
        body = self.__get_body(message)

        return {'status_code': status_code, 'status': status, 'parameters': parameters, 'message': body, 'version': 1.1}

    def __format_request_parameters(self, parameters:dict):
        formatted_parameters = ""
        for i in range(len(parameters.keys())):
            formatted_parameters += ("?" if i==0 else "&") + list(parameters.keys())[i] + "=" + list(parameters.values())[i]
        return formatted_parameters

    def format_request(self, body, method, route, parameters:dict):
        formatted_parameters = self.__format_request_parameters(parameters)
        return f"{method} {route}{formatted_parameters} HTTP/1.1\n\n{body}"
    
    def format_response(self, message, status="200 OK"):
        return f"HTTP/1.1 {status}\n\n{message}"

    def __get_method(self, message):
        
        method = re.search("([^\s]*)\s", message)
        result = method.groups()
        return result[0]

    def __get_route(self, message):
        
        route = re.search("^\w+ (\w+)(\?.+)? HTTP/1.1", message)
        result = route.groups()
        return result[0]

    def __get_parameters(self, message):

        method = self.__get_method(message)
        try:
            if method == "GET":
                parameters_in = self.__get_route(message)
                parameters = re.search("\?(.*)", parameters_in)
                parameters = parameters.groups()[0]
                parameters = parameters.split("&")
                dicts = self.__parameters_to_dict(parameters)
                return dicts
            parameters_in = re.findall("(\w+): (\w+)", message)
            parameters = {}
            for parameter in parameters_in:
                parameters[parameter[0]] = parameter[1]
            return parameters
        except AttributeError:
            return {}
    
    def __get_body(self, message):
        
        body = re.search("\n\s*\n(.*)", message)
        try:
            result = body.group()
            return result.strip()
        except:
            return ""
        
    def __get_status_code(self, message):

        status_code= re.search("(\d\d\d)", message)
        return status_code.group()
    
    def __get_status(self, message):

        n = "^"
        a = "\d\d\d (.*)"
        status = re.search(a, message)
        try:
            return status.groups()[0]
        except Exception as e:
            return e
            
    def __parameters_to_dict(self, parameters):
        
        a = "^"

        result = {}
        for parameter in parameters:
            name = re.search("(\w+)=", parameter)
            result_name = name.groups()[0]
            result_name.replace("=", "")
            value = re.search("=(\w+)", parameter)
            result_value = value.groups()[0]
            result_value.replace("=", "")

            result[result_name] = result_value

        return result

# para testear pueden usar los siguientes test:

# p.parse_request('''POST name HTTP/1.1''')                          -> {'method': 'POST', 'route': 'name', 'parameters': {}, 'message': '', 'version': 1.1}
# p.parse_request('''POST server.send.message HTTP/1.1
#                    t: 56
#                    id: 123
# 
#                    Hola, este es el cuerpo del request.''')         -> {'method': 'POST', 'route': 'server.send.message', 'parameters': {'t': 56, 'id': 123}, 'message': 'Hola, este es el cuerpo del request.', 'version': 1.1}

# p.parse_response('''HTTP/1.1 200 OK''')          -> {'status_code': 200, 'status': 'OK', 'parameters': {}, 'message': '', 'version': 1.1}
# p.parse_response('''HTTP/1.1 404 Not Found
#                     id: 123
#  
#                     No se encontro el id 123''') -> {'status_code': 404, 'status': 'Not Found', 'parameters': {id: 123}, 'message': 'No se encontro el id 123', 'version': 1.1}

if __name__ == "__main__":

    messages = [
       '''POST server.send.message HTTP/1.1
                    t: 56
                    id: 123
 
                    Hola, este es el cuerpo del request.'''
   ]

    p = Parser()
    for message in messages:
        result = p.get_body(message)
        print(result)
        print("--------------")
        

    
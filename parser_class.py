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
        route = re.search(" ([^\s|^\?]*)", message)
        return route.groups()[0]

    def __get_parameters(self, message):

        method = self.__get_method(message)
        if method == "GET":
            filter = "(\w+=[^&|^\s]*)[&\s]"
            parameters = re.findall(filter, message)
            result  = {}
            for parameter in parameters:
                key = parameter.split("=")[0]
                value = parameter.split("=")[1]
                result[key] = value
            return result
        else:
            filter = "\s+(.*: .*)\s*\n"
            parameters = re.findall(filter, message)
            result = {}
            for parameter in parameters:   
                key = parameter.split(":")[0]
                value = parameter.split(":")[1]
                result[key] = value.strip()
            return result

    def __get_body(self, message):
        
        body = re.search("\n\n(.*\n?)*", message)
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

if __name__ == "__main__":

    messages = [
       '''POST server.send.message HTTP/1.1
                    t: 56
                    id: 123
 
                    Hola, este es el cuerpo del request.''',
                    "GET acceso_base_de_datos?option=1&arg=0 HTTP/1.1"
   ]

    message = "GET acceso_base_de_datos?option=1&arg=0 HTTP/1.1"

    p = Parser()
    result = p.parse_request(messages[0])
    print(result)
    

 #''' POST '''
        

    
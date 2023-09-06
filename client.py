# Este script interactua con el usuario y envia mediante protocolo IP/TCP, HTTP y Sockets, las acciones que debe hacer servidor.py

import socket
from parser_class import Parser

DESTINATION_IP_ADDRESS = '127.0.0.1'
DESTINATION_PORT = 65432
parser = Parser()

def send_through_socket(http_message, connection):
    print("Enviando hacia el servidor:\n", http_message)
    connection.sendall(http_message.encode())

def get_name(socket_to_server):
    send_through_socket(parser.format_request("", "GET", "nombre", {}), socket_to_server)

def send_message(socket_to_server, mensaje):
    send_through_socket(parser.format_request(mensaje, "POST", "mandar_mensaje", {}), socket_to_server)

def read_message(socket_to_server):
    send_through_socket(parser.format_request("", "GET", "leer_mensaje", {}), socket_to_server)

def database_access(socket_to_server, option, arg="0"):
    send_through_socket(parser.format_request("", "GET", "acceso_base_de_datos", {"option": option, "arg": arg}), socket_to_server)

def ping(socket_to_server):
    send_through_socket(parser.format_request("", "GET", "ping", {}), socket_to_server)

def main():
    socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_to_server.connect((DESTINATION_IP_ADDRESS, DESTINATION_PORT))
    
    action = ""
    while action != "0":
        print('Ingrese una accion:\n0 = Salir\n1 = Nombre del Bot\n2 = Enviar mensaje\n3 = Leer ultimo mensaje\n4 = Acceso a la base de datos\n5 = Obtener ping con API de Discord')
        
        action = input()
        if action == "1":
            get_name(socket_to_server)
        elif action == "2":
            mensaje = input("Ingrese el contenido del mensaje:  ")
            send_message(socket_to_server, mensaje)
        elif action == "3":
            read_message(socket_to_server)
        elif action == "4":
            option = ""
            while not option in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                print('Elija una opción:\n1 = Obtener todos los paises y sus códigos\n2 = Obtener todos los países\n3 = Obtener todos los códigos\n4 = Obtener un código según su país\n5 = Obtener un país según su código\n6 = Obtener país aleatorio\n7 = Obtener lista aleatoria de países\n8 = Obtener países según inicial\n9 = Obtener países según última letra\n10 = Obtener países conteniendo una palabra\n11 = Obtener países de N letras\n12 = Obtener todos los países en una palabra')
                option = input()
                if option in ["4", "5", "7", "8", "9", "10", "11"]:
                    if option == "4":
                        arg = input("País: ")
                    elif option == "5":
                        arg = input("Código: ")
                    elif option == "7":
                        arg = input("Cantidad de países: ")
                    elif option == "8":
                        arg = input("Letra: ")
                    elif option == "9":
                        arg = input("Letra: ")
                    elif option == "10":
                        arg = input("Frase: ")
                    elif option == "11":
                        arg = input("Cantidad de letras: ")
                    database_access(socket_to_server, option, arg)
                else:
                    database_access(socket_to_server, option)
        elif action == "5":
            ping(socket_to_server)
        elif action != "0":
            print('Error, accion no valida.\n\n\n')
            continue
        elif action == "0":
            send_through_socket(parser.format_request("", "POST", "chau", {}), socket_to_server)
        data_from_server = socket_to_server.recv(5000)
        decoded_data = data_from_server.decode()
        parsed_data = parser.parse_response(decoded_data)
        if len(decoded_data) > 0:
            print("Respuesta del servidor:\n", parsed_data["message"])
    socket_to_server.close()

if __name__ == "__main__":
    main()
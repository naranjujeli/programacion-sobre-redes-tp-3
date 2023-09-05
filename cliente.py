# Este script interactua con el usuario y envia mediante protocolo IP/TCP, HTTP y Sockets, las acciones que debe hacer servidor.py

import socket
from parser_class import Parser

DESTINATION_IP_ADDRESS = '127.0.0.1'
DESTINATION_PORT = 65432
parser = Parser()

def send_through_socket(http_message, connection):
    connection.sendall(http_message.encode())

def get_name(socket_to_server):
    send_through_socket(parser.format_request(body="", method="GET", route="nombre", parameters={}), socket_to_server)

def send_message(socket_to_server, mensaje):
    send_through_socket(parser.format_request(body=mensaje, method="POST", route="mandar_mensaje", parameters={}), socket_to_server)

def read_message(socket_to_server):
    send_through_socket(parser.format_request(body="", method="GET", route="leer_mensaje", parameters={}), socket_to_server)

def database_access(socket_to_server, option, arg="0"):
    send_through_socket(parser.format_request(body="", method="GET", route="acceso_base_de_datos", parameters={"option": option, "arg": arg}), socket_to_server)

def main():
    socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_to_server.connect((DESTINATION_IP_ADDRESS, DESTINATION_PORT))
    
    action = ""
    while action != "0":
        print('Ingrese una accion:\n0 = Salir\n1 = Nombre del Bot\n2 = Enviar mensaje\n3 = Leer ultimo mensaje\n4 = Acceso a la base de datos')
        
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
                option = input("option: ")
                if option in ["4", "5", "8", "9", "10", "11"]:
                    if option == "4":
                        pass
                    arg = input("arg: ")
                    database_access(socket_to_server, option, arg)
                else:
                    database_access(socket_to_server, option)
        elif action != "0":
            print('Error, accion no valida.\n\n\n')
        data_from_server = socket_to_server.recv(5000)
        decoded_data = data_from_server.decode()
        if len(decoded_data) > 0:
            print("Respuesta del servidor:\n", decoded_data)
    

    socket_to_server.close()

if __name__ == "__main__":
    main()
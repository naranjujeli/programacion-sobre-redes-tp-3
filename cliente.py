# Este script interactua con el usuario y envia mediante protocolo IP/TCP, HTTP y Sockets, las acciones que debe hacer servidor.py

import socket

DESTINATION_IP_ADDRESS = '127.0.0.1'
DESTINATION_PORT = 65432

def obtener_nombre(socket_to_server):
    socket_to_server.sendall("nombre".encode())

def enviar_mensaje(socket_to_server, mensaje):
    socket_to_server.sendall(f"mandar_mensaje {mensaje}".encode())

def leer_mensaje(socket_to_server):
    socket_to_server.sendall("leer_mensaje".encode())

def acceso_base_de_datos(socket_to_server, acceso):
    # TODO
    pass

def main():
    socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_to_server.connect((DESTINATION_IP_ADDRESS, DESTINATION_PORT))
    
    action = -1
    while action != 0:
        print('''Ingrese una accion: 
                0 = Salir
                1 = Nombre del Bot
                2 = Enviar mensaje
                3 = Leer ultimo mensaje
                4 = Acceso a la base de datos
                ''')
        
        action = int(input())
        if action == 1:
            obtener_nombre(socket_to_server)

        elif action == 2:
            mensaje = input("Y el mensaje, capo? ")
            enviar_mensaje(socket_to_server, mensaje)

        elif action == 3:
            leer_mensaje(socket_to_server)

        elif action == 4:
            acceso_base_de_datos(socket_to_server, '')

        elif action != 0:
            print('Error, accion no valida.\n\n\n')

    socket_to_server.close()

if __name__ == "__main__":
    main()
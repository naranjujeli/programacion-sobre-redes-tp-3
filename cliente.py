# Este script interactua con el usuario y envia mediante protocolo IP/TCP, HTTP y Sockets, las acciones que debe hacer servidor.py

import socket

DESTINATION_IP_ADDRESS = '127.0.0.1'
DESTINATION_PORT = 65432

def obtener_nombre(s):
    s.sendall("nombre".encode())

def enviar_mensaje(s, mensaje):
    s.sendall(f"mandar_mensaje {mensaje}".encode())

def leer_mensaje(s):
    # TODO
    pass

def acceso_base_de_datos(s, acceso):
    # TODO
    pass

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DESTINATION_IP_ADDRESS, DESTINATION_PORT))
        s.sendall("All ready".encode())
        data = s.recv(1024)
        print("Response from the server:", data.decode())

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
                obtener_nombre(s)

            elif action == 2:
                mensaje = input("Y el mensaje, capo? ")
                enviar_mensaje(s, mensaje)

            elif action == 3:
                leer_mensaje(s)

            elif action == 4:
                acceso_base_de_datos(s, '')

            elif action != 0:
                print('Error, accion no valida.\n\n\n')

if __name__ == "__main__":
    main()
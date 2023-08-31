# Este script interactua con el usuario y envia mediante protocolo IP/TCP, HTTP y Sockets, las acciones que debe hacer servidor.py

import socket

DESTINATION_IP_ADDRESS = '127.0.0.1'
DESTINATION_PORT = 65432

def obtener_nombre():
    ### Completar
    pass

def enviar_mensaje(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DESTINATION_IP_ADDRESS, DESTINATION_PORT))
        s.sendall(message.encode())
        data = s.recv(1024)
        print("Response from the server:", data.decode())

def leer_mensaje():
    ### Completar
    pass

def acceso_base_de_datos(acceso):
    ### Completar
    pass

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
        obtener_nombre()

    elif action == 2:
        enviar_mensaje('Esto es un mensaje desde el cliente')

    elif action == 3:
        leer_mensaje()

    elif action == 4:
        acceso_base_de_datos('')

    elif action != 0:
        print('Error, accion no valida.\n\n\n')
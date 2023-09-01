# Este es el script principal del TP, se conecta con la API de discord para ordenarle que tiene que hacer el BOT
# Ademas permite que el script cliente.py tambien se conecte mediante sockets y usando este script como intermediario, meneje el BOT
# Por ultimo, es el unico script que puede acceder a la 'base de datos'

import socket
import discord
from parser_class import Parser

# Por cuestiones de seguridad el TOKEN no deberia estar en el codigo, tendria que estar oculto.
# Para este TP no vamos a tener en cuenta temas de seguridad.
def get_token():
    with open('TOKEN', 'r') as file:
        return file.readline()

DIRECCION_IP = "127.0.0.1"
PORT = 65432
TOKEN = get_token()
CHANNEL_ID = 1146923802664632453
client = discord.Client(intents=discord.Intents.all())
parser = Parser()
BOT_NAME = 'Shaggy'



async def send_response(conn, data):
    # data = parser.parse_request(data)

    if data['rute'] == 'nombre':
        conn.sendall(BOT_NAME.encode())
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"Mi nombre es: {BOT_NAME}")

    elif data['rute'] == 'mandar_mensaje':
        print('envia mensaje al canal de texto')
        ### Completar

    elif data['rute'] == 'leer_mensaje':
        print('obtiene el ultimo mensaje del chat')
        ### Completar
    
    elif data['rute'] == 'acceso_base_de_datos':
        print('accede a la base de datos')
        ### Completar

    else:
        conn.sendall(b'Ruta desconocida')

async def open_socket_to_connection():
    # Abrir la conexión al Cliente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((DIRECCION_IP, PORT))
        s.listen()
        connection, address = s.accept()
        with connection:
            print("Conectando a", address)
            while True:
                data = connection.recv(1024)
                decoded_data = data.decode('utf-8')
                print("Mensaje recibido:", decoded_data)
                connection.sendall("El mensaje fue recibido por el servidor".encode())
                await send_response(connection, {"rute": decoded_data})

@client.event
async def on_ready():
    await open_socket_to_connection()
    print('Bot conectado')
    await client.get_channel(CHANNEL_ID).send("Shaggy está en la casa")

@client.event
async def on_message(message):

    # Hay que chequear que el bot ignore sus propios mensajes, sino se puede crear un loop infinito
    if message.author == client.user: 
        return
    
    # Dependiendo del contenido del mensaje se va decidir que accion se hace

    print(f"Recibido el mensaje: {message.content}")

    if message.content == "hola":
        message.channel.send("hola")



def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()
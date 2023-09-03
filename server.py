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

IP_ADDRESS = "127.0.0.1"
PORT = 65432
TOKEN = get_token()
CHANNEL_ID = 1146923802664632453
discord_client = discord.Client(intents=discord.Intents.all())
discord_main_channel = None
parser = Parser()
BOT_NAME = 'Shaggy'

def get_channel_reference():
    discord_client.get_channel(CHANNEL_ID)

async def resolve_request(conn, data_from_client):
    # data_from_client = parser.parse_request(data_from_client)

    if data_from_client['route'] == 'nombre':
        conn.sendall(BOT_NAME.encode())
        discord_main_channel = discord_client.get_channel(CHANNEL_ID)
        await discord_main_channel.send(f"Mi nombre es: {BOT_NAME}")

    elif data_from_client['route'][:14] == 'mandar_mensaje':
        mensaje = data_from_client['route'][15:]
        discord_main_channel = discord_client.get_channel(CHANNEL_ID)
        await discord_main_channel.send(f"Nuevo mensaje: {mensaje}")

    elif data_from_client['route'] == 'leer_mensaje':
        discord_main_channel = discord_client.get_channel(CHANNEL_ID)
        
        ultimo_mensaje_del_chat = None
        historial = discord_main_channel.history(limit=1)
        async for mensaje in historial:
            ultimo_mensaje_del_chat = mensaje.content
        conn.sendall(ultimo_mensaje_del_chat.encode())
        await discord_main_channel.send(f"El último mensaje del chat es: {ultimo_mensaje_del_chat}")
    
    elif data_from_client['route'] == 'acceso_base_de_datos':
        print('accede a la base de datos')
        ### Completar

    else:
        conn.sendall(b'Ruta desconocida')

async def open_connection_to_client():
    # Abrir la conexión al Cliente
    socket_to_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_to_client.bind((IP_ADDRESS, PORT))
    socket_to_client.listen()
    connection, address = socket_to_client.accept()
    print("Conectando a", address)
    return connection

async def listen_to_connection(connection):
    while True:
        try:
            data_from_client = connection.recv(1024)
            decoded_data = data_from_client.decode('utf-8')
            print("Mensaje recibido:", decoded_data)

            await resolve_request(connection, parser.parse_request(decoded_data))
        except BrokenPipeError:
            return None

@discord_client.event
async def on_ready():
    connection_to_client = await open_connection_to_client()
    print('El bot está on-line')
    get_channel_reference()
    await discord_main_channel.send("Shaggy está en la casa")
    await listen_to_connection(connection_to_client)
    await discord_client.close()
    print('El bot fue apagado')

@discord_client.event
async def on_message(message):

    # Hay que chequear que el bot ignore sus propios mensajes, sino se puede crear un loop infinito
    if message.author == discord_client.user: 
        return
    
    # Dependiendo del contenido del mensaje se va decidir que accion se hace

    print(f"Recibido el mensaje: {message.content}")

    if message.content == "hola":
        message.discord_main_channel.send("hola")



def main():
    discord_client.run(TOKEN)

if __name__ == "__main__":
    main()

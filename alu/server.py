# Este es el script principal del TP, se conecta con la API de discord para ordenarle que tiene que hacer el BOT
# Ademas permite que el script cliente.py tambien se conecte mediante sockets y usando este script como intermediario, meneje el BOT
# Por ultimo, es el unico script que puede acceder a la 'base de datos'

import socket
import discord
from parser_class import Parser

# Por cuestiones de seguridad el token no deberia estar en el codigo, tendria que estar oculto.
# Para este TP no vamos a tener en cuenta temas de seguridad.
def get_token():
    return 'El token va aca'

direccion_ip = "127.0.0.1"
port = 65432              
token = get_token()
chanel_id = 10934545676603203311 ### Completar
client = discord.Client(intents=discord.Intents.all())
parser = Parser()
bot_name = ''   ### Completar



async def send_response(conn, data):
    data = parser.parse_request(data)

    if data['rute'] == 'nombre':
        conn.sendall(bot_name.encode())
        channel = client.get_channel(chanel_id)
        await channel.send(f"Mi nombre es: {bot_name}")

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

async def open_socket_to_conection():
    # Abrir la coneccion al Cliente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        ### Completar
        await send_response(None, None)

@client.event
async def on_ready():
    await open_socket_to_conection()
    print('Bot conectado')

@client.event
async def on_message(message):

    # Hay que chequear que el bot ignore sus propios mensajes, sino se puede crear un loop infinito
    if message.author == client.user: 
        return
    
    ### Completar
    # Dependiendo del contenido del mensaje se va decidir que accion se hace

client.run(token)
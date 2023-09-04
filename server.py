# Este es el script principal del TP, se conecta con la API de discord para ordenarle que tiene que hacer el BOT
# Ademas permite que el script cliente.py tambien se conecte mediante sockets y usando este script como intermediario, meneje el BOT
# Por ultimo, es el unico script que puede acceder a la 'base de datos'

import socket
import discord
from database_access import DatabaseAccess
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
database_access = DatabaseAccess()
parser = Parser()
BOT_NAME = 'Shaggy'

def send_through_socket(connection, message, status="200 OK"):
    connection.sendall(parser.format_response(message, status).encode())

async def resolve_request(connection, data_from_client):
    discord_main_channel = discord_client.get_channel(CHANNEL_ID)
    if data_from_client['route'] == 'nombre':
        await discord_main_channel.send(f"Mi nombre es: {BOT_NAME}")
        send_through_socket(connection, BOT_NAME)
    elif data_from_client['route'] == 'mandar_mensaje':
        message = data_from_client['body']

        await discord_main_channel.send(f"Nuevo mensaje: {message}")
        send_through_socket(connection, f"Mensaje enviado: {message}")
    elif data_from_client['route'] == 'leer_mensaje':
        last_message_in_chat = None
        messages_history = discord_main_channel.history(limit=1)
        async for message in messages_history: # sí, es un "async for", ni idea
            last_message_in_chat = message.content
        
        await discord_main_channel.send(f"El último mensaje del chat es: {last_message_in_chat}")
        send_through_socket(connection, last_message_in_chat)
    elif data_from_client['route'] == 'acceso_base_de_datos':
        try:
            option = data_from_client['parameters']['option'] # para abreviar
            if option == "1": # Todo
                all_data = database_access.get_all()["countries"]
                result = ""
                for i in range(len(all_data.keys())):
                    result += list(all_data.keys())[i] + " " + list(all_data.values())[i] + "\n"
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "2": # Países
                result = ""
                for country in database_access.get_all_countries():
                    result += country + "\n"
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "3": # Códigos
                result = ""
                for code in database_access.get_all_codes():
                    result += code + "\n"
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "4": # Código según país
                result = database_access.get_code_by_country(data_from_client["parameters"]["arg"])
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "5": # País según código
                result = database_access.get_country_by_code(data_from_client["parameters"]["arg"])
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "6": # País aleatorio
                result = database_access.get_random_country()
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "7": # Lista aleatoria de países
                result = database_access.get_random_countries()
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "8": # Países por inicial
                result = database_access.get_all_countries_begginning_with(data_from_client["parameters"]["arg"])
                discord_main_channel.send(result)
                send_through_socket(connection)
            elif option == "9": # Países por última letra
                result = database_access.get_all_countries_ending_with(data_from_client["parameters"]["arg"])
                discord_main_channel.send(result)
                send_through_socket(connection, result)
            elif option == "10": # Países que contienen...
                result = database_access.get_all_countries_containing(data_from_client["parameters"]["arg"])
                discord_main_channel.send(result)
                send_through_socket(connection)
            elif option == "11": # Países con N letras
                result = database_access.get_all_countries_with_n_letters(data_from_client["parameters"]["arg"])
                discord_main_channel.send(result)
                send_through_socket(connection)
            elif option == "12": # Paísestodojunto
                result = database_access.get_all_countries_together()
                discord_main_channel.send(result)
                send_through_socket(connection)
        except:
            discord_main_channel.send("Ha sucedido un error al acceder a la base de datos")
            send_through_socket(connection, "Ha sucedido un error al acceder a la base de datos", "500 Internal Server Error")
    else:
        send_through_socket(connection, 'Ruta desconocida', "404 Not Found")

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

    if message.content == "/hola":
        result = "hola"
    elif message.content == "/name":
        result = BOT_NAME
    elif message.content == "/all_conutrys":
        result = database_access.get_all_countries()
    elif message.content == "/all_database":
        result = database_access.get_all()
    elif message.content == "/all_codes":
        result = database_access.get_all_codes()
    elif message.content == "/random_country":
        result = database_access.get_random_country()
    elif message.content == "/all_countrys_combined":
        result = database_access.get_all_countries_together()
    message.chat.send(result)



def main():
    discord_client.run(TOKEN)

if __name__ == "__main__":
    main()

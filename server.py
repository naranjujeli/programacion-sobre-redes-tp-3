# Este es el script principal del TP, se conecta con la API de discord para ordenarle que tiene que hacer el BOT
# Ademas permite que el script cliente.py tambien se conecte mediante sockets y usando este script como intermediario, meneje el BOT
# Por ultimo, es el unico script que puede acceder a la 'base de datos'

import socket
import discord
from database_access import DatabaseAccess, EntradaConArgumento
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
    response = parser.format_response(message, status)
    print('Enviando al cliente:\n', response)
    connection.sendall(response.encode())

async def name_route(connection, discord_channel):
    await discord_channel.send(f"Mi nombre es: {BOT_NAME}")
    send_through_socket(connection, BOT_NAME)

async def send_message_route(connection, discord_channel, data_from_client):
    message = data_from_client['body']
    await discord_channel.send(f"Nuevo mensaje: {message}")
    send_through_socket(connection, f"Mensaje enviado: {message}")

async def read_message_route(connection, discord_channel):
    last_message_in_chat = None
    messages_history = discord_channel.history(limit=1)
    async for message in messages_history: # sí, es un "async for", ni idea
        last_message_in_chat = message.content
    await discord_channel.send(f"El último mensaje del chat es: {last_message_in_chat}"[:1999])
    send_through_socket(connection, last_message_in_chat)

async def database_access_route(connection, discord_channel, data_from_client):
    try:
        option = data_from_client['parameters']['option'] # para abreviar
        result = None
        if option == "1": # Todo
            all_data = database_access.get_all()["countries"]
            result = ""
            for i in range(len(all_data.keys())):
                result += list(all_data.keys())[i] + " " + list(all_data.values())[i]["code"] + "\n"
        elif option == "2": # Países
            result = ""
            for country in database_access.get_all_countries():
                result += country + "\n"
        elif option == "3": # Códigos
            result = ""
            for code in database_access.get_all_codes():
                result += code + "\n"
        elif option == "4": # Código según país
            result = database_access.get_code_by_country(data_from_client["parameters"]["arg"])
        elif option == "5": # País según código
            result = database_access.get_country_by_code(data_from_client["parameters"]["arg"])
        elif option == "6": # País aleatorio
            result = database_access.get_random_country()
        elif option == "7": # Lista aleatoria de países
            result = ""
            for country in database_access.get_random_countries(int(data_from_client["parameters"]["arg"])):
                result += country + "\n"
        elif option == "8": # Países por inicial
            result = ""
            for country in  database_access.get_all_countries_begginning_with(data_from_client["parameters"]["arg"]):
                result += country + "\n"
        elif option == "9": # Países por última letra
            result = ""
            for country in  database_access.get_all_countries_ending_with(data_from_client["parameters"]["arg"]):
                result += country + "\n"
        elif option == "10": # Países que contienen...
            result = ""
            for country in  database_access.get_all_countries_containing(data_from_client["parameters"]["arg"]):
                result += country + "\n"
        elif option == "11": # Países con N letras
            result = ""
            for country in  database_access.get_all_countries_with_n_letters(int(data_from_client["parameters"]["arg"])):
                result += country + "\n"
        elif option == "12": # Paísestodojunto
            result = database_access.get_all_countries_together()
        await discord_channel.send(result[:1999]) # Discord no permite más de 2000 caracteres
        send_through_socket(connection, result)
    except:
        error_message = "Ha sucedido un error al acceder a la base de datos"
        await discord_channel.send(error_message)
        send_through_socket(connection, error_message, "500 Internal Server Error")

async def ping_route(connection, discord_channel):
    result = "Ping: " + str(int(round(discord_client.latency, 3)*1000)) + "ms"
    await discord_channel.send(result)
    send_through_socket(connection, result)

async def resolve_request(connection, data_from_client):
    discord_channel = discord_client.get_channel(CHANNEL_ID)
    if data_from_client['route'] == 'nombre':
        await name_route(connection, discord_channel)
    elif data_from_client['route'] == 'mandar_mensaje':
        await send_message_route(connection, discord_channel, data_from_client)
    elif data_from_client['route'] == 'leer_mensaje':
        await read_message_route(connection, discord_channel)
    elif data_from_client['route'] == 'acceso_base_de_datos':
        await database_access_route(connection, discord_channel, data_from_client)
    elif data_from_client['route'] == 'ping':
        await ping_route(connection, discord_channel)
    elif data_from_client['route'] == 'chau':
        await discord_channel.send('Chau')
        send_through_socket(connection, 'Chau')
        return False
    else:
        send_through_socket(connection, 'Ruta desconocida', "404 Not Found")
    return True

async def open_connection_to_client():
    socket_to_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_to_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_to_client.bind((IP_ADDRESS, PORT))
    socket_to_client.listen()
    connection, address = socket_to_client.accept()
    print("Conectando a", address)
    return connection

async def listen_to_connection(connection):
    while True:
        try:
            data_from_client = connection.recv(5000)
            decoded_data = data_from_client.decode('utf-8')
            print("Mensaje recibido:\n", decoded_data)

            if not (await resolve_request(connection, parser.parse_request(decoded_data))):
                return None
        except BrokenPipeError:
            return None

@discord_client.event
async def on_ready():
    connection = await open_connection_to_client()
    print('El bot está on-line')
    await listen_to_connection(connection)
    await discord_client.close()
    print('El bot fue apagado')
    pass

@discord_client.event
async def on_message(message):
    # Hay que chequear que el bot ignore sus propios mensajes, sino se puede crear un loop infinito
    if message.author == discord_client.user: 
        return
    
    # Dependiendo del contenido del mensaje se va decidir que accion se hace

    print(f"Recibido el mensaje: {message.content}")

    entry = EntradaConArgumento(message.content)
    print("El bot recibió:", entry)
    help_menu = '''Todos los comandos empiezan con un /
    >name --> devovlera el nombre del bot
    >all_countries --> devolvera todos los paises de la base de datos
    >all_code --> devolvera todos los codigos de paises de la base de datos
    >random_country --> devolvera un paise random de la base de datos
    >all_countries_combined --> devolvera una string con todos los paises de la base de datos
    >code_by_country <pais> --> devolvera el codigo del pais asignado
    >country_by_code <codigo> --> devolvera el pais del codigo asignado
    >country_by_inicial <frase> --> devolvera todos los paises que empiezen con esa frase
    >country_by_ending <frase> --> devolvera todos los paises que terminen con esa frase
    >countries_containing <frase> --> delvovera todos los paises que contengan esa frase
    >random_list_of_countries <cantidad> --> devolver una lista con paises random del tamaño de la cantidad asignada
    >countries_with_n_letters <cantidad> --> devolvera todos los paises con tal cantidad de letras en su nombre
    '''

    result = None
    
    if entry == "/hola":
        result = "hola"
    elif entry == "/name":
        result = BOT_NAME
    elif message.content == "/all_countries arg arg":
        result = database_access.get_all_countries()
    elif entry == "/all_database":
        result = database_access.get_all()
    elif entry == "/all_codes":
        result = database_access.get_all_codes()
    elif entry == "/random_country":
        result = database_access.get_random_country()
    elif entry == "/all_countries_combined":
        result = database_access.get_all_countries_together()
    elif entry == "/help":
        result = help_menu
    elif entry.number_of_arguments == 1:
        if entry.comando == "/code_by_country":
            result = database_access.get_code_by_country(entry.argumento())
        elif entry.comando == "/country_by_code":
            result = database_access.get_country_by_code(entry.argumento())
        elif entry.comando == "/country_by_inicial":
            result = database_access.get_all_countries_begginning_with(entry.argumento())
        elif entry.comando == "/country_by_ending":
            result = database_access.get_all_countries_ending_with(entry.argumento())
        elif entry.comando == "/random_list_of_countries":
            result = database_access.get_random_countries(entry.argumento())
        elif entry.comando == "/countries_containing":
            result = database_access.get_all_countries_containing(entry.argumento())
        elif entry.comando == "/countries_with_n_letters":
            result = database_access.get_all_countries_with_n_letters(int(entry.argumento()))
    await message.channel.send(result)



def main():
    discord_client.run(TOKEN)

if __name__ == "__main__":
    main()

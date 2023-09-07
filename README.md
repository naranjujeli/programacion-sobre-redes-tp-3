# Tercer trabajo práctico de la materia Programación Sobre Redes

## Resumen

El objetivo de este proyecto es crear una interfaz que permita, desde un *host* cliente, controlar las acciones de un bot de [Discord](https://www.discord.com) a través de un servidor capaz de intermediar la API de Discord con aquel cliente. En este caso, la interfaz es completamente implementada por línea de comandos. 

En verdad, este desarrollo es tan solo una excusa para aprender sobre la utilización a bajo nivel de ***sockets*** y mensajes **HTTP**. El software cliente y el software servidor se comunican enviando, mediante un socket, peticiones y respuestas en formato HTTP (con el respectivo encabezado y cuerpo).

También es posible utilizar el bot via comandos por el *chat* de Discord, como se haría con un bot cualquiera.

### Funcionalidades

- **Mostrar el nombre**: El bot simplemente
- **Enviar un mensaje**: Darle al bot una cadena de texto y que la envie por el canal de Discord
- **Leer un mensaje**: El bot lee el último mensaje enviado en el chat y lo muestra
- **Acceder a datos**: Doce funcionalidades distintas que pretenden depender de una base de datos de consulta
- **Obtener ping**: Lograr que el bot muestre la latencia entre el servidor y la API de Discord en milisegundos

## Lado del servidor ([server.py](/server.py))

En el archivo ```server.py``` se puede encontrar todo el código que se ejecuta del lado del servidor. Lo que este programa hace es, primero, inicializar el bot usando el cliente de Discord (discord.py). Será necesario, para ello, el [TOKEN](#sobre-el-token) de inicio de sesión. 

Una vez el bot está on-line, se dispara el evento ```on_ready```. Aquí se espera hasta establecer una conexión con el cliente (```open_connection_to_client()```) y, a continuación, el servidor escucha eternamente en busca de mensajes de aquel *host* (```listen_to_connection()```). Cada vez que el servidor encuentra una trama de bytes, el *parser* es utilizado para desencriptarla, y dependiendo de la ruta del mensaje y de los parametros recibidos, la [acción posterior](#funcionalidades) cambiará.

También aquí están programados los comandos disponibles por chat.

NOTA: No es posible manipular al bot por consola y por chat al mismo tiempo porque el orden de ejecución no lo permite. Será necesario cambiar esto en el código previo a la ejecución.

## Lado del cliente ([client.py](/client.py))

El rol del programa ejecutado del lado del cliente es un poco más sencillo. Lo único que debe hacer es recibir por consola la opción que el usuario desea llevar a cabo, encriptar esta elección (con parámetros, si es que correspondiese) a HTTP y enviar el mensaje por medio del socket. En todos los casos recibirá una respuesta del servidor acusando recibo, aún si no hace falta un *body* con datos.

## Acceso a datos ([database_access.py](/database_access.py))

Este modulo define, en total, doce maneras distintas de acceder a los datos almacenados en [```data.json```](/data.json). Idealmente, esto sería logrado mediante una base de datos relacional, pero ya que los requisitos del Trabajo Práctico no comprenden este area, se decidió guardar todo en un solo archivo de contenidos fijos. Sin embargo, igualmente se logra abstraer el acceso a datos prolijamente.

Cabe aclararlo; el contenido de ```data.json``` es la lista de todos los países del mundo, cada uno con un respectivo código de dos letras que lo identifica de forma única.

## Clase Parser ([parser_class.py](/parser_class.py))

El *parser* es la parte central del proyecto. Tiene tanto la función de darle formato a los mensajes a enviar como la de desempacar correctamente los mensajes recibidos. Esto último se logra mediante el uso de expresiones regulares, que permiten separar los distintos apartados del mensaje (sobre todo del encabezado HTTP).

## Sobre el TOKEN

Discord se da cuenta automáticamente cuando un TOKEN de inicio de sesión de algún bot queda expuesto de forma pública en GitHub. Lo que hacen en consecuencia es inhabilitarlo junto con el bot por cuestiones de seguridad. Es por ello que lo almacenamos por separado y de forma privada.
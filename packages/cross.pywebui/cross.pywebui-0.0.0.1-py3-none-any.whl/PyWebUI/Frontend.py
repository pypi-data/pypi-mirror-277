import socket
import base64
import hashlib
import PyWebUI.Globals as Globals
from PyWebUI.utilities import util4code as u4c
from PyWebUI.utilities import util4string as u4s
import main_script as main_script;
import base64
#___________________
#===================
MAIN_VAR_NAME = 'main_script'
IP = Globals.app_config.ip
PORT = Globals.app_config.port
CONNECTIONS_NUM = 1  # only 1 device can connect (self device)
GUID = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
#__________________
#==================

client = None # globalized for send_message purposes
#__________________
#==================

def create_websocket_response_key(key):
    key = key + GUID
    sha1 = hashlib.sha1(key.encode())
    return base64.b64encode(sha1.digest()).decode()

def handshake(client_socket):
    try:
        request = client_socket.recv(1024).decode()
        headers = {}
        lines = request.split("\r\n")
        for line in lines:
            if ": " in line:
                header, value = line.split(": ", 1)
                headers[header] = value

        if "Sec-WebSocket-Key" in headers:
            response_key = create_websocket_response_key(headers["Sec-WebSocket-Key"])
            response = (
                "HTTP/1.1 101 Switching Protocols\r\n"
                "Upgrade: websocket\r\n"
                "Connection: Upgrade\r\n"
                f"Sec-WebSocket-Accept: {response_key}\r\n\r\n"
            )
            client_socket.send(response.encode())
        else:
            None
    except Exception:
        u4c.show_error()


def receive_message(client_socket):
    try:
        data = client_socket.recv(1024)
        print(data.decode())
        if not data:
            return None
    except UnicodeDecodeError:
        length = data[1] & 127
        if length == 126:
            length = int.from_bytes(data[2:4], byteorder='big')
            masks = data[4:8]
            message = data[8:]
        elif length == 127:
            length = int.from_bytes(data[2:10], byteorder='big')
            masks = data[10:14]
            message = data[14:]
        else:
            
            masks = data[2:6]
            message = data[6:]

        decoded_message = bytearray()
        for i in range(len(message)):
            decoded_message.append(message[i] ^ masks[i % 4])
        expression = f'getattr({MAIN_VAR_NAME}'+decoded_message.decode()
        print(u4s.get_asciiface('FROM JS => PY:'+expression, [150,150,0]))
        try:
            eval(expression)
        except Exception as e:
            
            u4c.show_error()
        
        return decoded_message.decode()
    except Exception as e:
        u4c.show_error()


def send_message(message):
    try:
        global client
        message = message.encode()
        length = len(message)
        if length <= 125:
            header = bytearray([129, length])
        elif length >= 126 and length <= 65535:
            header = bytearray([129, 126]) + length.to_bytes(2, byteorder='big')
        else:
            header = bytearray([129, 127]) + length.to_bytes(8, byteorder='big')
        
        client.send(header + message) if client is not None else None
        
    except Exception:
        u4c.show_error()

def client_handler(clientsocket, address):
    try:
        global client
        handshake(clientsocket)
        print(u4s.get_asciiface('CONNECTED TO FRONTEND',[0,255,0]))
        Globals.Flags.Launcher.frontend_connected = True
        while True:
            message = receive_message(clientsocket)
            if message is None:
                print(u4s.get_asciiface('Disconnected to frontend',[255,0,0]))
                clientsocket.close()
                handler0(clientsocket, address)
                break
    except Exception:
        pass

def handler0(clientsocket,address):
    client_handler(clientsocket, address)

def start_server():
    global client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    server_socket.bind((IP, PORT))
    server_socket.listen(CONNECTIONS_NUM)
    while True:
        try:
            # Accept a connection
            clientsocket, address = server_socket.accept()
            client = clientsocket
            handler0(clientsocket, address)
        except Exception as e:
            u4c.show_error()

#_______________________________________________
#===============================================
# DEFINING USER CALLABLES
def data(buffer: bytes) -> str:
    """
    Converts bytes into a format readable by the frontend's data encoder and JS' eval.

    Args:
        buffer (bytes): Can be bytes from image, text, sound, etc.
    
    Returns:
        string: bytes converted into utf-8 string
    """
    return base64.b64encode(buffer).decode('utf-8')

def eval_js(script:str) -> None:
    """
    Runs a JS script.

    Args:
        script (str): javascript code.
    """
    send_message(script)

def use_function(function_name: str, *args, **kwargs) -> None:
    """
    Uses a function from the frontend. 

    Args: 
        function_name (str): function name, including namespace if required.
        *args (any): passes arguments with unspecified keys but in order.
        **kwargs (any): passes arguments with specified keys and in no order.
    """
    def translator(value):
        if type(value) == bytes or type(value) == str:

            return f'\"{value}\"'
        else:
            return value
    try:
        args_str = ','.join([str(translator(x)) for x in args]) 
        args_str = args_str + ',' if len(args) > 0 else args_str
        
        kwargs_str = [f'{key}={translator(value)}' for key,value in zip(kwargs.keys(), kwargs.values())]
        kwargs_str = ','.join(kwargs_str)
        overall = f'{function_name}({args_str}{kwargs_str});'
        alt_overall = f'{function_name}(args:len({len(args)}), kwargs:len({len(kwargs)}))'
        print(u4s.get_asciiface('FROM JS <= PY:'+alt_overall, [150,150,0]))
        send_message(overall)
    except Exception:
        u4c.show_error()
#_______________________________________
#=======================================
Globals.frontend_api.eval_js = eval_js
Globals.frontend_api.use_function = use_function
Globals.frontend_api.data = data
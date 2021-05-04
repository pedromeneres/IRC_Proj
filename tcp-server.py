import socket, sys
import threading

bind_ip = '127.0.0.1'
bind_port = 9993

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print ('Listening on {}:{}'.format(bind_ip, bind_port))

def handle_client_message(message):
    print("Checking message[...]")
    print('Got {}'.format(message))
    if (message == 'Goodbye\n'):
        print("Ending[...]")
        return False
    print("Does not match. Continue[...]")
    return True



def handle_client_connection(client_socket):
    msg_from_client = client_socket.recv(1024)
    request = msg_from_client.decode()
    print ('Received {}'.format(request))
    msg_to_client='ACK'.encode()
    print (msg_to_client)
    client_socket.send(msg_to_client)
    client_socket.close()

while True:
    client_sock, address = server.accept()
    print ('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()

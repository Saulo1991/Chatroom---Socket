import socket
import pickle

HEADERSIZE = 16

host = '127.0.0.1'
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)

print(f"Server listening at port {port}")

while True:
    conn, addr = server.accept()
    print(f"Connection from {addr} has been established")
    
    d = {1: "Castanha", 2: "Do Pará"}
    msg = pickle.dumps(d)
    #dumps serializa aqui
    
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
    conn.send(msg)  #msg já é do tipo bytes, não é necessário converter novamente para bytes

    conn.close()  # Fechando a conexão após enviar a mensagem

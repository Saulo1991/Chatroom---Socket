import socket
import pickle

HEADERSIZE = 16

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = client.recv(16)
        if not msg:
            break
        
        if new_msg:
            try:
                msg_len = int(msg[:HEADERSIZE].strip())
                print(f"New message length: {msg[:HEADERSIZE].strip()}") 
            except ValueError:
                print("Error: Invalid message length")
                break
            new_msg = False
        
        full_msg += msg
        
        if len(full_msg) - HEADERSIZE == msg_len:
            print("Full message received")
            print(full_msg[HEADERSIZE:])
            
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            
            new_msg = True
            full_msg = b''
            break

    if not msg:
        break

client.close()

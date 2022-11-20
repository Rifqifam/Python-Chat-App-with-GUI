import socket  
import threading   

HOST = "172.20.10.3"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Got Connection With {str(address)}!")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Client Nickname is : {nickname}")
        broadcast(f"{nickname} is connected to the server! \n ".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is Running....")
receive()


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
# print ("Socket successfully created")

# port = 1234 #Portnya terserah lu         
 
# s.bind(('', port)) #Dikosongin == localhost == 127.0.0.1      
# print ("socket binded to %s" %(port))
 

# s.listen(100) #Maks client di queue   
# print ("socket is listening")           

# def broadcast(msg, c):
#     for client in clients:
#         if c != client:
#             client.send(msg.encode())

# def multi_thread(c, addr):
#     print('Got connection from', addr)
#     c.send('Thank you for connecting'.encode())
#     while True:
#         msg = c.recv(1024).decode()
#         if msg == "exit":
#             broadcast((f"{addr} left the chat!"), c)
#             c.close()
#             clients.remove(c)
#             break
#         broadcast((f"{addr}: {msg}"), c)

# clients = []

# while True:
#   c, addr = s.accept()    
#   clients.append(c)
#   threading._start_new_thread(multi_thread, (c, addr, ))


   
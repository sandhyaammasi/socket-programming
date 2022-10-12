import socket
import threading

HEADER = 64 # number to load the length of the message that we're gonna recieve
DISCONNECT_MSG = "!"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket needs a tuple =>family,type

#now BIND the socket created above to the address
serverSocket.bind(ADDR)

def handle_client(conn,addr): # handle individual connection between client and the server (one client and one server)
    print("new connection ", addr, "connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # recv => gotta give the number num of bytes we want to recieve from the client 
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(addr, " sent the message ",msg)

def start(): # handle new connection , distribute where they need to go
    
    serverSocket.listen()
    print(f"server socket is listening on {SERVER}")
    while True: #infinite loop to continue to listen 
        conn,addr = serverSocket.accept()  # will wait for new connection to the server, 
                                     # when new connection occurs , we store the address(server, port)info and an object(conn) that will allow us to send an object
        thread = threading.Thread(target = handle_client, args= (conn,addr))
        thread.start()
        print("Active connections ", threading.activeCount())


 
print("server starting.......")
start() 
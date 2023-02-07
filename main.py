import socket
import threading
import tkinter






class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.tcpsock.bind(("0.0.0.0",1234))

        while True:
            if self.tcpsock.listen: # si le serveur est en train d'écouté alors il peut prendre un port et accepté des client
                self.tcpsock.listen(10)
                print( "En écoute...")
                (clientsocket, (ip, port)) = self.tcpsock.accept() # la méthode accept est une méthode (synchrone) qui va permettre d'accepter les client
                newthread = ClientThread(ip, port, clientsocket)
                newthread.start()
            else: # sinon on sort de la boucle
                break


class ClientThread(threading.Thread): # cette classe est un thread

    list_of_client = [] # liste qui va contenir tous les socket qui ont été entendue par le serveur

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)

    def run(self): # cette fonction est appelé lorsqu'un client a réussi à ce connecter
   
        print("Connexion réussi")





class graphical_part:
    def __init__(self) -> None:
        pass
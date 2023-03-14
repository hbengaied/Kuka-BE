import socket
import threading
import tkinter
import xml.etree.ElementTree as ET

import XmlManager
import TopicTweet
import MovementManager

class Server(threading.Thread):

    kuka_connected = False

    KukaSocket = "" # au début c'est juste une chaine de caractère, aprés ce sera le socket du client

    ipServer = ""

    portServer = ""

    ipKuka = ""

    portKuka = ""

    def __init__(self , ipServer , portServer):
        threading.Thread.__init__(self)
        self.ipServer = ipServer
        self.portServer = portServer

    def run(self):
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.tcpsock.bind((self.ipServer,self.portServer))

        if self.tcpsock.listen: # si le serveur est en train d'écouté alors il peut prendre un port et accepté des client
            self.tcpsock.listen(10)
            print( "En écoute...")
            (clientsocket, (ipClient, portClient)) = self.tcpsock.accept() # la méthode accept est une méthode (synchrone) qui va permettre d'accepter les client
            # Lorsque le server a accepté une connection, alors je peut assigné le socket du client
            self.KukaSocket = clientsocket
            self.ipKuka = ipClient
            self.portKuka = portClient
            self.kuka_connected = True
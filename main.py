import socket
import threading
import tkinter

class Server(threading.Thread):

    kuka_connected = False

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.tcpsock.bind(("172.30.5.100",1234))

        while True:
            if self.tcpsock.listen: # si le serveur est en train d'écouté alors il peut prendre un port et accepté des client
                self.tcpsock.listen(10)
                print( "En écoute...")
                (clientsocket, (ip, port)) = self.tcpsock.accept() # la méthode accept est une méthode (synchrone) qui va permettre d'accepter les client
                newthread = ReceiveThread(ip, port, clientsocket)
                newthread.start()
                SendData.clientsocket = clientsocket # je définie le socket utilisé pour parler avec le robot

            else: # sinon on sort de la boucle
                break

# region thread qui va permettre de gérer la communication avec le robot
class ReceiveThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket


    def run(self): # cette fonction est appelé lorsque kuka a réussi à se connecter
   
        print("Connexion réussi")

        # je vais commencer à attendre la réception de donnée
        while True:
            self.data_received = self.clientsocket.recv(1024)
            with open("input.xml","w") as f:
                f.write(bytes.decode(self.data_received))


    def put_data_in_cache(self): # cette méthode servira à mettre les info que le kuka nous envoie dans un cache (qui pourra être lu par la suite)
        pass

    def send_data_to_kuka(self): # méthode qui va envoyé les donnée au robot 
        pass


class SendData():
    clientsocket = "" # cette objet va contenir le socket et u qu'il est utilisé qu'une seule fois, je la met en static

    def Send(self):
        self.clientsocket.sendall(b'hello')

# endregion


class graphical_part:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Menu")
        self.root.geometry("1000x600")
        self.Set_All_Widget()
        self.root.mainloop()

    def Set_All_Widget(self):
        # panel1 qui va contenir une config pour faire bouger le robot kuka manuellement
        # exemple de mvt => faire en sorte que le robot bouge selon l'axe x, y ou z
        self.panel = tkinter.PanedWindow(self.root , bg="#E6E6E6", width="1000", height="300")
        self.panel.place(x=0, y=0)

        #region objet panel 1
        self.label_title1 = tkinter.Label(self.panel , text="Configuration manuel :")
        self.label_title1.place(x=0,y=0)

        #region label -> x,y et z
        self.x = tkinter.Label(self.panel , text="Position en x :")
        self.x.place(x=50,y=40)

        self.y = tkinter.Label(self.panel , text="Position en y :")
        self.y.place(x=300,y=40)

        self.z = tkinter.Label(self.panel , text="Position en z :")
        self.z.place(x=550,y=40)
        #endregion

        #region all entry for location
        self.entry_x = tkinter.Entry(self.panel, width="10")
        self.entry_x.place(x=150,y=42)

        self.entry_y = tkinter.Entry(self.panel, width="10")
        self.entry_y.place(x=400,y=42)

        self.entry_z = tkinter.Entry(self.panel, width="10")
        self.entry_z.place(x=650,y=42)
        #endregion

        self.button_set_position_kuka = tkinter.Button(self.panel, text="Tap to move \n at this location")
        self.button_set_position_kuka.place(x=800,y=30)

        #endregion



server = Server()
server.start()

# graphical_part()
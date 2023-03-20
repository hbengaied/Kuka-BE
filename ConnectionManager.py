import socket
import threading
import xml.etree.ElementTree as ET
import XmlManager
import MovementManager as MM

class ReceiveThread(threading.Thread): # cette classe servira principalement à la reception de paquet et lorsqu'il recoit qqu chose alors il commence la conversation avec le kuka

    def __init__(self, ipclient, portClient, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ipclient
        self.port = portClient
        self.clientsocket = clientsocket


    def run(self): # cette fonction est appelé lorsque kuka a réussi à se connecter
   
        print("Connexion réussi")

        # je vais commencer à attendre la réception de donnée
        while True:
            self.data_received = self.clientsocket.recv(1024)

            f = open("input.xml","w")

            f.write(bytes.decode(self.data_received))

            f.close() # je m'assure que le fichier est bien fermé et donc que l'écriture est terminé avant de commencer à répondre au robot

            Conversation.Response(MM.Dictionnarie.Dico["h"]["X"],
            MM.Dictionnarie.Dico["h"]["Y"],
            MM.Dictionnarie.Dico["h"]["Z"],
            MM.Dictionnarie.Dico["h"]["A"],
            MM.Dictionnarie.Dico["h"]["B"],
            MM.Dictionnarie.Dico["h"]["C"]) # c'est ici qu'il commence l'échange avec le kuka
            Verification.Verif()

class SendData():
    clientsocket = "" # cette objet va contenir le socket qui est utilisé qu'une seule fois, je la met en static

    def Send():

        DataToSend = ""

        with open('output.xml','r') as f:
            DataToSend = f.read()

        SendData.clientsocket.sendall(DataToSend.encode('utf-8'))


class Conversation():
    @staticmethod
    def Response(PosX,PosY,PosZ,PosA,PosB,PosC):
        try:
            tree = ET.parse("input.xml") # je parse le fichier xml
            root = tree.getroot() # je prend la balise root du fichier

            ipoc_balise = "" # cette variable va contenir le timestamps que je devrais renvoyé au kuka
            for element in root: #pour chaque élement de la balise root, si le tag est IPOC alors je prend ce que contient la balise IPOC
                if element.tag == "IPOC":
                    ipoc_balise = element

            Data = { # j'initialise le dictionnaire de donnée à envoyé au robot, ATTENTION 
                "X" : PosX,
                "Y" : PosY,
                "Z" : PosZ, 
                "A" : PosA,
                "B" : PosB,
                "C" : PosC,
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data) # cette fonction sert à initialisé le fichier xml "output.xml"

            SendData.Send() # et juste aprés, il envoie le fichier xml
            
        except:
            print('une erreur de lecture est survenu je répondrai à la prochaine réception')


class Verification():
    @staticmethod
    def Verif():
        try:
            # parse the XML file
            tree = ET.parse('input.xml')

            # get the root element of the XML file
            root = tree.getroot()

            # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))
            print("X:", x)
            print("Y:", y)
            print("Z:", z)
            print("A:", a)
            print("B:", b)
            print("C:", c)
        except:
            print(' ')

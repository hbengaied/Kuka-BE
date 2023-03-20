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

            #Ici j'envoi la position qu'on veut atteindre
            Conversation.Response(MM.Dictionnarie.Dico["c"]["X"],
            MM.Dictionnarie.Dico["c"]["Y"],
            MM.Dictionnarie.Dico["c"]["Z"],
            MM.Dictionnarie.Dico["c"]["A"],
            MM.Dictionnarie.Dico["c"]["B"],
            MM.Dictionnarie.Dico["c"]["C"]) # c'est ici qu'il commence l'échange avec le kuka

            arrive = False
            while arrive == False :
                arrive = Verification.Verif(MM.Dictionnarie.Dico["c"]["X"],
                MM.Dictionnarie.Dico["c"]["Y"],
                MM.Dictionnarie.Dico["c"]["Z"],
                MM.Dictionnarie.Dico["c"]["A"],
                MM.Dictionnarie.Dico["c"]["B"],
                MM.Dictionnarie.Dico["c"]["C"])
            #Il printe pas c'est normal, je dois faire à o,2 pres
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!JE SUIS ARRIVE A LA POSITION DEMANDE !!!!!!!!!!!!!!!!!!!!!!!!")

            #Faire une boucle while qui va check si on y est enfin 
            #Print un Ok on y est quand c'est le cas pour le test

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
    def Verif(PosX,PosY,PosZ,PosA,PosB,PosC):
        TreeVerif = ET.parse("output.xml")
        root = TreeVerif.getroot()

        rist_element = root.find('RIst')
        x, y, z, a, b, c = None, None, None, None, None, None
        if rist_element is not None:
            x = float(rist_element.attrib['X'])
            y = float(rist_element.attrib['Y'])
            z = float(rist_element.attrib['Z'])
            a = float(rist_element.attrib['A'])
            b = float(rist_element.attrib['B'])
            c = float(rist_element.attrib['C'])
            # instructions à exécuter si l'élément est trouvé
        else:
            pass
        
        #CONVERTIR POS ET CE QUE LE ROBOT ENVOI EN FLOAT, FAIRE SOUSTRACTION ET METTRE UNE MARGE D'erreur a 0,02
        print("La valeur de X ou se trouve le robot",x)
        if x == PosX and y == PosY and z == PosZ and a ==PosA and b == PosB and c == PosC:
            return True
        return False





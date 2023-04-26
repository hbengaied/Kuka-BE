import socket
import threading
import xml.etree.ElementTree as ET
import XmlManager
import MovementManager as MM
import MouvementXandY as MXY
import VerificationDest as VD
import MouvementZ as MZ

class ReceiveThread(threading.Thread): # cette classe servira principalement à la reception de paquet et lorsqu'il recoit qqu chose alors il commence la conversation avec le kuka

    def __init__(self, ipclient, portClient, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ipclient
        self.port = portClient
        self.clientsocket = clientsocket
        MM.Phrase.Initialisation("kuka")

    def run(self): # cette fonction est appelé lorsque kuka a réussi à se connecter
        print("Connexion réussi")
        # je vais commencer à attendre la réception de donnée
        while True:
            self.data_received = self.clientsocket.recv(1024)
            f = open("input.xml","w")
            f.write(bytes.decode(self.data_received))
            f.close() # je m'assure que le fichier est bien fermé et donc que l'écriture est terminé avant de commencer à répondre au robot

            if MM.Phrase.Check == False :
                #Je donne les coord au robot en x et y auquel il doit se deplacer
                MXY.MouveMyXandY.MouveXandY(MM.Phrase.MyText[MM.Phrase.Compteur])
                #Si le robot a atteint les coord x et y et set check a true
                MM.Phrase.Check = VD.Verification.VerifXandY(MM.Phrase.MyText[MM.Phrase.Compteur])
            
            #Si le robot à atteint le x et y voulu on va cliquer sur la touche en bougeant le z
            if MM.Phrase.Check == True  and MM.Phrase.CheckDown == False :
                #Deplacement du robot en Z uniquement
                print("Je descend !!!")
                MZ.MoveMyZ.MoveZDown(MM.Phrase.MyText[MM.Phrase.Compteur])
                MM.Phrase.CheckDown = VD.Verification.VerifKeyClicked(MM.Phrase.MyText[MM.Phrase.Compteur])

            if MM.Phrase.CheckDown == True and MM.Phrase.CheckUp == False :
                # print("Jai pu cliquer sur la touche :", MM.Phrase.MyText[MM.Phrase.Compteur])
                #Ici lorsque la lettre voulu a été cliqué, on va relever l'outil de +75 en Z
                MZ.MoveMyZ.MoveZUp(MM.Phrase.MyText[MM.Phrase.Compteur])
                MM.Phrase.CheckUp = VD.Verification.VerifGoUp(MM.Phrase.MyText[MM.Phrase.Compteur])
                
             #Je vais passer caractere suivant    
            if MM.Phrase.CheckUp == True and MM.Phrase.Check == True and MM.Phrase.CheckDown == True :
                print("On incremente le compteur ")
                MM.Phrase.Compteur = MM.Phrase.Compteur +1
                MM.Phrase.Check = False
                MM.Phrase.CheckUp = False
                MM.Phrase.CheckDown = False
                #Ca c'est juste pour eviter un depassement index quand on arrive fin du mot ! Faut impltementer un autre truc plus propre et plus pro 
                if MM.Phrase.Compteur == MM.Phrase.TaillePhrase:
                    print("On recommence le mot pcq on vient d'arriver à la fin pour eviter le bug ! Merci de mettre une version plus propre pour gerer ce cas")
                    MM.Phrase.Compteur = 0

class SendData():
    clientsocket = "" # cette objet va contenir le socket qui est utilisé qu'une seule fois, je la met en static
    @staticmethod
    def Send():
        DataToSend = ""
        with open('output.xml','r') as f:
            DataToSend = f.read()

        SendData.clientsocket.sendall(DataToSend.encode('utf-8'))
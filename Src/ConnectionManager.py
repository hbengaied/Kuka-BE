import socket
import threading
import xml.etree.ElementTree as ET
import XmlManager
import MovementManager as MM
import MouvementXandY as MXY
import VerificationDest as VD
import MouvementZ as MZ
import Instruction as INSTRU

class ReceiveThread(threading.Thread): # cette classe servira principalement à la reception de paquet et lorsqu'il recoit qqu chose alors il commence la conversation avec le kuka

    def __init__(self, ipclient, portClient, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ipclient
        self.port = portClient
        self.clientsocket = clientsocket
        MM.Phrase.Initialisation("a")

    def run(self): # cette fonction est appelé lorsque kuka a réussi à se connecter
        print("Connexion réussi")
        # je vais commencer à attendre la réception de donnée
        while True:
            self.data_received = self.clientsocket.recv(1024)
            f = open("input.xml","w")
            f.write(bytes.decode(self.data_received))
            f.close() # je m'assure que le fichier est bien fermé et donc que l'écriture est terminé avant de commencer à répondre au robot
            

            if MM.Mouse.NewTweet == False :
                MM.Mouse.NewTweet = INSTRU.InstructionForRobot.OpenWritingSpace()
            #Si on a pas fini de taper notre text on va entrer uniquement dans le if
            if MM.Mouse.NewTweet == True and MM.Phrase.EndText == False :
                INSTRU.InstructionForRobot.InstructionClavier()
            
            if MM.Phrase.EndText == True and MM.Mouse.TabulationEight == False :
                MM.Mouse.TabulationEight = INSTRU.InstructionForRobot.ClickOnTabulation("t", 8)
            
            if MM.Phrase.EndText == True and MM.Mouse.TabulationEight == True and MM.Mouse.EnterClicked == False:
                #faire le deplacement vers le button entrer
                MM.Mouse.EnterClicked = INSTRU.InstructionForRobot.ClickOnEnter()

            if MM.Mouse.EnterClicked == True :
                print("Le tweet a été fait")
                exit()


            # else:
            #     #Si on a fini de taper notre text on deplacer la souris 
            #     #Deplacer la souris vers le point initial
            #     #Aller vers la ou on veut
            #     #Faire le clic -> Methode a dev mais c'est rapdie normalement
                
            #     #La souris se trouve en A et nous on veut aller en B
            #     if MM.Mouse.EndMouseMouvement == False : 
            #         MM.Mouse.EndMouseMouvement = INSTRU.InstructionForRobot.InstructionMouse("a", "b")
            #     #Ici on va aller vers le + pour faire le clic gauche
            #     if MM.Mouse.EndMouseMouvement == True and MM.Mouse.LeftClick == False :
            #         MM.Mouse.LeftClick = INSTRU.InstructionForRobot.ClicGauche("b")

            #     #Ici on est alle du point A au point B maintenant on aimerait remettre la souris sur le point A
            #     if MM.Mouse.LeftClick == True :
            #         MM.Mouse.EndMouseMouvementBis = INSTRU.InstructionForRobot.InstructionMouse("b", "a")

            #     if MM.Mouse.EndMouseMouvementBis == True :
            #         print("FIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNNNNNNN")


class SendData():
    clientsocket = "" # cette objet va contenir le socket qui est utilisé qu'une seule fois, je la met en static
    @staticmethod
    def Send():
        DataToSend = ""
        with open('output.xml','r') as f:
            DataToSend = f.read()

        SendData.clientsocket.sendall(DataToSend.encode('utf-8'))
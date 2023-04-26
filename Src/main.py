import tkinter


import Server as Serv
import ConnectionManager as CM
import TopicTweet
import MovementManager
import XmlManager as XM

if __name__ == "__main__":
    XM.XmlManager.DeleteFile()
    server = Serv.Server(ipServer="172.30.5.100" , portServer=1234) # j'instancie le server qui va écouté
    server.start() # je lance le serveur
    # Si le serveur détecte une nouvelle connection du robot alors je doit commencer la réception de paquet
    
    while(server.kuka_connected == False): # j'attent que le robot soit connecter
        pass
    # lorsque le kuka se connecte il sort de cette boucle et j'instancie la réception de paquet du kuka

    newthread = CM.ReceiveThread(server.ipKuka, server.portKuka, server.KukaSocket)
    newthread.start()
    CM.SendData.clientsocket = server.KukaSocket # je définie le socket utilisé pour parler avec le robot
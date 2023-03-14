import tkinter


import Server as Serv
import ConnectionManager as CM
import TopicTweet
import MovementManager


class GUI:
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


if __name__ == "__main__":
    server = Serv.Server(ipServer="0.0.0.0" , portServer=1234) # j'instancie le server qui va écouté
    server.start() # je lance le serveur
    # Si le serveur détecte une nouvelle connection du robot alors je doit commencer la réception de paquet
    
    while(server.kuka_connected == False): # j'attent que le robot soit connecter
        pass
    # lorsque le kuka se connecte il sort de cette boucle et j'instancie la réception de paquet du kuka

    newthread = CM.ReceiveThread(server.ipKuka, server.portKuka, server.KukaSocket)
    newthread.start()
    CM.SendData.clientsocket = server.KukaSocket # je définie le socket utilisé pour parler avec le robot

import tkinter
import threading
import tkinter.messagebox

class GUI(): # je crée un thread pour que le gui ne soit pas bloquant

    ActualLocation = {} # ceci est le dictionnaire qui va contenir le position actuelle du robot
    LocationToReach = {} # et ca c'est la position à atteindre

    # les prochaine variable vont contenir les bool, il me permettent de savoir quelle checkbox à été check
    SportCheck = False
    SignAztroCheck = False
    RandomCheck = False

    def __init__(self):
        self.CreateWindow()
        self.CreateWidgets()
        self.MaintainMainloop()

# création et configuration de la fénêtre
    def CreateWindow(self):
        self.root = tkinter.Tk()
        self.root.title('Configuration KUKA')
        self.root.geometry('500x200')
        # Association de la fonction on_closing() à l'événement de fermeture de la fenêtre
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

# méthode appelée lorsque la fenêtre est fermée
    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
            self.root.destroy()

# création des widgets
    def CreateWidgets(self):
        #region définition des variables pour les checkbox
        self.SportCheck = tkinter.IntVar() # 0 si c'est décocké, 1 si c'est coché
        self.SignAztroCheck = tkinter.IntVar() 
        self.RandomCheck = tkinter.IntVar() 
        #endregion

        #region création des checkbox
        self.checkboxSport = tkinter.Checkbutton(self.root, text="Sport", variable=self.SportCheck , command=lambda: self.on_checkbox_click(self.SportCheck))
        self.checkboxSport.place(x=20 , y= 20)

        self.checkboxSignAztro = tkinter.Checkbutton(self.root, text="Signe astronomique", variable=self.SignAztroCheck , command=lambda: self.on_checkbox_click(self.SignAztroCheck))
        self.checkboxSignAztro.place(x=20 , y= 40)

        self.checkboxRandom = tkinter.Checkbutton(self.root, text="Aléatoire", variable=self.RandomCheck , command=lambda: self.on_checkbox_click(self.RandomCheck))
        self.checkboxRandom.place(x=20 , y= 60)
        #endregion

# méthode appelée lorsqu'une case à cocher est cochée
    def on_checkbox_click(self , var):
        # Si la case à cocher correspondant à la variable var a été cochée,
        # on décoche les autres cases à cocher
        if var.get() == 1:
            if var is self.SportCheck:
                self.SignAztroCheck.set(0)
                self.RandomCheck.set(0)
            elif var is self.SignAztroCheck:
                self.SportCheck.set(0)
                self.RandomCheck.set(0)
            elif var is self.RandomCheck:
                self.SportCheck.set(0)
                self.SignAztroCheck.set(0)

# méthode qui va maintenir la fenêtre
    def MaintainMainloop(self):
        self.root.mainloop()

GUI()
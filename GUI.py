import tkinter as tk
import Data_to_tap.RequestManager as RM

class GUI:
    def __init__(self):
        # Crée une instance de Tkinter
        self.root = tk.Tk()

        # Crée le panel du haut
        self.frame_haut = tk.Frame(self.root)
        self.frame_haut.pack(side=tk.TOP, pady=10)

        # Crée la liste des choix
        self.liste = tk.Listbox(self.frame_haut)
        self.liste.pack(side=tk.LEFT, padx=10)

        # Ajoute des éléments à la liste
        self.liste.insert(1, "Hello world")
        self.liste.insert(2, "Pokemon")
        self.liste.insert(3, "Choix 3")

        # Crée le bouton pour valider le choix
        self.bouton_valider = tk.Button(self.frame_haut, text="Valider", command=self.valider)
        self.bouton_valider.pack(side=tk.LEFT, padx=10)

        # Crée le panel du bas
        self.frame_bas = tk.Frame(self.root)
        self.frame_bas.pack(side=tk.BOTTOM, pady=10)

        # Crée un Label pour afficher les coordonnées
        self.coord_label = tk.Label(self.frame_bas, text="Coordonnées: ")
        self.coord_label.pack()

        # Envoie une première coordonnée au robot KUKA
        self.nouvelle_coord = (1, 2, 3) # Exemple de coordonnée
        self.mettre_a_jour_coord(self.nouvelle_coord)

        # Lance la boucle principale de Tkinter
        self.root.mainloop()

    # Fonction pour mettre à jour les coordonnées dans le Label
    def mettre_a_jour_coord(self , coord):
        self.coord_label.configure(text="Coordonnées: {}".format(coord))

    # Fonction appelée lorsque le bouton est cliqué
    def valider(self):
        choix = self.liste.curselection() # Récupère l'indice de l'élément sélectionné dans la liste
        if choix:
            choix = self.liste.get(choix[0]) # Récupère la valeur de l'élément sélectionné
            print("Choix: ", choix)

GUI()

class Set_Data: # cette classe permet d'appeler les méthode pour récupéré ce que le robot doit taper
    @staticmethod
    def Ask_To_OpenAI():
        openAIRequester = RM.OpenAIRequester(key="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")
        response = openAIRequester.make_request(prompt="salut")

        if(response == None):
            pass
            # Je dois le mettre sur MongoDB
        else:
            pass
            # Je dois le mettre sur MongoDB
            # return response

    @staticmethod
    def Ask_To_Poke():
        pokeAPIRequester = RM.PokeAPIRequester()
        jsonResponse = pokeAPIRequester.make_request()

        mongoUpdater = RM.MongoDBUpdater("mongodb://127.0.0.1:27017/")

        name = jsonResponse["chain"]["species"]["name"]
        evolutions = jsonResponse["chain"]["evolves_to"]

        if len(evolutions) > 0:
            mongoUpdater.update_pokeApi(name , evolution = evolutions[0]["species"]["name"] )
        else:
            mongoUpdater.update_pokeApi(name , "nothing")
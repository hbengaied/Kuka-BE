import TopicTweet

class Dictionnarie: # cette classe ne va contenir juste les positions de chaque caractère utilisé
    Dico = {
        "h" : {
            "X" : "682.14",
            "Y" : "0.84",
            "Z" : "645.17", 
            "A" : "-175.98",
            "B" : "54.93",
            "C" : "-176.97",
        },
        "c" : {
            "X" : "682.14",
            "Y" : "0.84",
            "Z" : "545.17", 
            "A" : "-175.98",
            "B" : "54.93",
            "C" : "-176.97",
        },
        "b" : {
            "X" : "512.75",
            "Y" : "120.31",
            "Z" : "460.84", 
            "A" : "-170.76",
            "B" : "-4.22",
            "C" : "164.84",
        },

    }

class Phrase:
    MyText = ""
    Compteur = 0
    TaillePhrase = 0
    def Initialisation(MaPhrase):
        Phrase.MyText = MaPhrase
        Phrase.Compteur = 0
        Phrase.TaillePhrase = len(Phrase.MyText)

class MovementManager:
    # cette classe va gérer les mouvements du robot
    # Donc elle pourra savoir si la position a été atteinte ou non
    # elle pourra donner la nouvelle position à atteindreµ
    

    PositionToReached = False # cete variable me servira à dire si le robot à atteint sa cible pas

    def SetPositionsToReach(ArrayOfElement):

        firstelement = ""
        for element in ArrayOfElement: # je prend le caracteres qui sera tapé et je lui associe avec sa position
            try:
                element = element.lower() # pour l'instant je met en minuscule le carractère           
            except:
                pass # si une erreur survient, je décide de ne rien faire
            
        # MovementManager.PositionToReach = Dictionnarie.Dico["h"]



# MovementManager.SetPositionsToReach(TopicTweet.get_data_for_tweet.get_data_in_variable("basic")["Description"])
# Pos = MovementManager.PositionToReach
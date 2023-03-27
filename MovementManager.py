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
            "X" : "685.96",
            "Y" : "133.86",
            "Z" : "654.98", 
            "A" : "-177.42",
            "B" : "54.22",
            "C" : "179.57",
        },
        "z" : {
            "X" : "475.79",
            "Y" : "-90.28",
            "Z" : "691.05", 
            "A" : "-175.99",
            "B" : "54.93",
            "C" : "-176.98",
        },
        "k" : {
            "X" : "620.27",
            "Y" : "57.26",
            "Z" : "244.96", 
            "A" : "175.20",
            "B" : "2.26",
            "C" : "178.91",
        },
        "m" : {
            "X" : "620.28",
            "Y" : "57.25",
            "Z" : "264.63", 
            "A" : "175.20",
            "B" : "2.26",
            "C" : "178.91",
        },
        "i" : {
            "X" : "639.14",
            "Y" : "61.61",
            "Z" : "245.53", 
            "A" : "175.20",
            "B" : "2.24",
            "C" : "178.91",
        },
        "r" : {
            "X" : "633.30",
            "Y" : "138.78",
            "Z" : "245.29", 
            "A" : "175.20",
            "B" : "2.24",
            "C" : "178.91",
        },
        "o" : {
            "X" : "642.18",
            "Y" : "41.81",
            "Z" : "245.92", 
            "A" : "175.20",
            "B" : "2.23",
            "C" : "178.92",
        },
        "u" : {
            "X" : "637.65",
            "Y" : "83.08",
            "Z" : "245.78", 
            "A" : "175.20",
            "B" : "2.23",
            "C" : "178.92",
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
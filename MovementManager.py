import TopicTweet

class Dictionnarie: # cette classe ne va contenir juste les positions de chaque caractère utilisé
    Dico = {
        "a" : {
            "X" : "659.01",
            "Y" : "156.53",
            "Z" : "286.01", 
            "A" : "175.21",
            "B" : "2.27",
            "C" : "178.91",
        },
        "b" : {
            "X" : "620.04",
            "Y" : "66.61",
            "Z" : "283.29", 
            "A" : "175.21",
            "B" : "2.25",
            "C" : "178.91",
        },
        "c" : {
            "X" : "620.04",
            "Y" : "103.59",
            "Z" : "284.36", 
            "A" : "175.21",
            "B" : "2.25",
            "C" : "178.91",
        },
        "d" : {
            "X" : "640.41",
            "Y" : "113.10",
            "Z" : "285.19", 
            "A" : "175.21",
            "B" : "2.24",
            "C" : "178.92",
        },
        "e" : {
            "X" : "658.19",
            "Y" : "118.37",
            "Z" : "284.98", 
            "A" : "175.21",
            "B" : "2.24",
            "C" : "178.92",
        },
        "f" : {
            "X" : "638.89",
            "Y" : "94.42",
            "Z" : "285.29", 
            "A" : "175.21",
            "B" : "2.24",
            "C" : "178.92",
        },
        "m" : {
            "X" : "638.86",
            "Y" : "25.29",
            "Z" : "374.52", 
            "A" : "175.20",
            "B" : "2.22",
            "C" : "178.92",
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
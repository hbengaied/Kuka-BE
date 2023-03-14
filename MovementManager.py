import TopicTweet

class Dictionnarie: # cette classe ne va contenir juste les positions de chaque caractère utilisé
    Dico = {
        "h" : {
            "X":54,
            "Y":400,
            "Z":400,
            "A":52,
            "B":44,
            "C":5
        }
    }

class MovementManager:
    # cette classe va gérer les mouvements du robot
    # Donc elle pourra savoir si la position a été atteinte ou non
    # elle pourra donner la nouvelle position à atteindre
    PositionToReach = { # les valeurs par défaut sont mis aléatoirement par MOI
        "X":500,
        "Y":400,
        "Z":400,
        "A":52,
        "B":44,
        "C":5
    }

    PositionToReached = False # cete variable me servira à dire si le robot à atteint sa cible pas

    def SetPositionsToReach(ArrayOfElement):

        firstelement = ""
        for element in ArrayOfElement: # je prend le caracteres qui sera tapé et je lui associe avec sa position
            try:
                element = element.lower() # pour l'instant je met en minuscule le carractère           
            except:
                pass # si une erreur survient, je décide de ne rien faire
            
        MovementManager.PositionToReach = Dictionnarie.Dico["h"]



MovementManager.SetPositionsToReach(TopicTweet.get_data_for_tweet.get_data_in_variable("basic")["Description"])
Pos = MovementManager.PositionToReach
import xml.etree.ElementTree as ET
import MovementManager as MM


class Verification():
    #Cette méthode vérifie que le bras se trouve bien au dessus de la touche du clavier
    #que l'on veut appuyer, dans le if on vérifie que le X et le Y du robot, et que le x et le y
    #de la touche à appuyer on une différence de 0.3mm max
    @staticmethod
    def VerifXandY(lettre):
        try:
            # parse the XML file
            tree = ET.parse('input.xml')

            # get the root element of the XML file
            root = tree.getroot()

            # get the values of X, Y, Z, A, B, C from the RIst element
            rist = root.find('RIst')
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.Dictionnarie.Dico[lettre]["X"])
            PosY = float(MM.Dictionnarie.Dico[lettre]["Y"])
            PosA = float(MM.Dictionnarie.Dico[lettre]["A"])
            PosB = float(MM.Dictionnarie.Dico[lettre]["B"])
            PosC = float(MM.Dictionnarie.Dico[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 :
                return True
        except:
            pass
        return False

    #Cette méthode vérifie que le bras a bien appuyé sur la touche du clavier
    #dans le if on vérifie que le X,Y et le Z du robot, et que le x,y et z
    #de la touche qui vient d'être appuyé on une différence de 0.3mm max
    @staticmethod
    def VerifKeyClicked(lettre):
        try:
            tree = ET.parse('input.xml')
            root = tree.getroot()
            rist = root.find('RIst')

            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.Dictionnarie.Dico[lettre]["X"])
            PosY = float(MM.Dictionnarie.Dico[lettre]["Y"])
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"])
            PosA = float(MM.Dictionnarie.Dico[lettre]["A"])
            PosB = float(MM.Dictionnarie.Dico[lettre]["B"])
            PosC = float(MM.Dictionnarie.Dico[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False

    #Cette méthode vérifie que le bras c'est bien levé après avoir appuyé sur la touche du clavier
    #dans le if on vérifie que le X,Y et le Z du robot, et que le x,y et z
    #de la touche qui vient d'être appuyé on une différence de 0.3mm max
    #Cependant on ajoute +35 au Z de la touche afin que le robot se lève d'une distance minimal et max afin d'avoir une sécurité
    @staticmethod
    def VerifGoUp(lettre):
        try:
            tree = ET.parse('input.xml')
            root = tree.getroot()
            rist = root.find('RIst')

            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.Dictionnarie.Dico[lettre]["X"])
            PosY = float(MM.Dictionnarie.Dico[lettre]["Y"])
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"]) + 35
            PosA = float(MM.Dictionnarie.Dico[lettre]["A"])
            PosB = float(MM.Dictionnarie.Dico[lettre]["B"])
            PosC = float(MM.Dictionnarie.Dico[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False

    #Cette méthode vérifie que le bras c'est bien levé quand on sort de la souris
    #dans le if on vérifie que le X,Y et le Z du robot, et que le x,y et z
    #de la souris on une différence de 0.3mm max
    #Cependant on ajoute +100 au Z de la souris afin que le robot se léve d'une distance minimal et max afin d'avoir une sécurité
    @staticmethod
    def VerifGoUpMouse(lettre):
        try:
            tree = ET.parse('input.xml')
            root = tree.getroot()
            rist = root.find('RIst')

            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.MouseMouve.MousePos[lettre]["X"])
            PosY = float(MM.MouseMouve.MousePos[lettre]["Y"])
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"]) + 100
            PosA = float(MM.MouseMouve.MousePos[lettre]["A"])
            PosB = float(MM.MouseMouve.MousePos[lettre]["B"])
            PosC = float(MM.MouseMouve.MousePos[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                # print("Je viens de monter pour la souris")
                return True
        except:
            pass
        return False

    #Cette méthode vérifie que le bras est bien entré dans la souris
    #dans le if on vérifie que le X,Y et le Z du robot, et que le x,y et z
    #de la souris on une différence de 0.3mm max
    @staticmethod
    def VerifGoDownMouse(lettre):
        try:
            tree = ET.parse('input.xml')
            root = tree.getroot()
            rist = root.find('RIst')

            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            z = float(rist.get('Z'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.MouseMouve.MousePos[lettre]["X"])
            PosY = float(MM.MouseMouve.MousePos[lettre]["Y"])
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"])
            PosA = float(MM.MouseMouve.MousePos[lettre]["A"])
            PosB = float(MM.MouseMouve.MousePos[lettre]["B"])
            PosC = float(MM.MouseMouve.MousePos[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 and abs(PosZ-z)<0.3 :
                return True
        except:
            pass
        return False
    
    #Cette méthode est utilisé pour vérifier que l'on est au dessus de la souris
    #dans le if on vérifie que le X,Y du robot et que le x,y de la souris
    #on une différence de 0.3mm
    @staticmethod
    def VerifXandYMouse(lettre):
        try:
            tree = ET.parse('input.xml')
            root = tree.getroot()
            rist = root.find('RIst')
            
            x = float(rist.get('X'))
            y = float(rist.get('Y'))
            a = float(rist.get('A'))
            b = float(rist.get('B'))
            c = float(rist.get('C'))

            PosX = float(MM.MouseMouve.MousePos[lettre]["X"])
            PosY = float(MM.MouseMouve.MousePos[lettre]["Y"])
            PosA = float(MM.MouseMouve.MousePos[lettre]["A"])
            PosB = float(MM.MouseMouve.MousePos[lettre]["B"])
            PosC = float(MM.MouseMouve.MousePos[lettre]["C"])
            if abs(PosX-x) <0.3 and abs(PosY-y) <0.3 :
                return True
        except:
            pass
        return False
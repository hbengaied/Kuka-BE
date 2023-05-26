import MovementManager as MM
import ConnectionManager as CM
import xml.etree.ElementTree as ET
import XmlManager

class MoveMyZ():
    #Methode qui permet de faire descendre le bras sur la touche du clavier souhaité passé en arguement afin de procéder
    #au clic de la touche
    #Cette dernière prend une "lettre" qui contient les coords de la touche
    @staticmethod
    def MoveZDown(lettre):
        try:
            tree = ET.parse("input.xml")
            root = tree.getroot()
            ipoc_balise = ""
            for element in root:
                if element.tag == "IPOC":
                    ipoc_balise = element

            Data = {
                "X" : MM.Dictionnarie.Dico[lettre]["X"],
                "Y" : MM.Dictionnarie.Dico[lettre]["Y"],
                "Z" : MM.Dictionnarie.Dico[lettre]["Z"], 
                "A" : MM.Dictionnarie.Dico[lettre]["A"],
                "B" : MM.Dictionnarie.Dico[lettre]["B"],
                "C" : MM.Dictionnarie.Dico[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data)
            CM.SendData.Send()
            
        except:
            pass
    
    #Methode qui permet de faire monter le bras au dessus de la touche du clavier cliqué pour faire le prochain déplacement
    #Cette dernière prend une "lettre" qui contient les coords de la touche, et on ajoute +35 au Z qui est la marge de sécurité
    @staticmethod
    def MoveZUp(lettre):
        try:
            tree = ET.parse("input.xml")
            root = tree.getroot()

            ipoc_balise = ""
            for element in root:
                if element.tag == "IPOC":
                    ipoc_balise = element
            PosZ = float(MM.Dictionnarie.Dico[lettre]["Z"]) + 35
            StringPosZ = str(PosZ)
            Data = {
                "X" : MM.Dictionnarie.Dico[lettre]["X"],
                "Y" : MM.Dictionnarie.Dico[lettre]["Y"],
                "Z" : StringPosZ,
                "A" : MM.Dictionnarie.Dico[lettre]["A"],
                "B" : MM.Dictionnarie.Dico[lettre]["B"],
                "C" : MM.Dictionnarie.Dico[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data)
            CM.SendData.Send()
            
        except:
            pass
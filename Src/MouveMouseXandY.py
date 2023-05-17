import MovementManager as MM
import ConnectionManager as CM
import XmlManager
import xml.etree.ElementTree as ET

class MouveMyMouseXandY():
    @staticmethod
    #Si on veut que la souris aille à la position originale on lui donnera la lettre a
    # sinon pour l'endroit ou le boutton publier se trouve envoyer la touche b
    def MouseMouvementXandY(lettre, monint):
        try:
            tree = ET.parse("input.xml")
            root = tree.getroot()

            ipoc_balise = ""
            for element in root:
                if element.tag == "IPOC":
                    ipoc_balise = element
            
            PosZ = float(MM.MouseMouve.MousePos[lettre]["Z"]) + monint
            StringPosZ = str(PosZ)
            Data = {
                "X" : MM.MouseMouve.MousePos[lettre]["X"],
                "Y" : MM.MouseMouve.MousePos[lettre]["Y"],
                "Z" : StringPosZ,
                "A" : MM.MouseMouve.MousePos[lettre]["A"],
                "B" : MM.MouseMouve.MousePos[lettre]["B"],
                "C" : MM.MouseMouve.MousePos[lettre]["C"],
                "IPOC" : ipoc_balise.text
            }

            XmlManager.XmlManager.SetDataToSend(Data)
            CM.SendData.Send()
            
        except:
            pass

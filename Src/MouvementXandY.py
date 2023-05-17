import MovementManager as MM
import ConnectionManager as CM
import XmlManager
import xml.etree.ElementTree as ET

class MouveMyXandY():
    @staticmethod
    def MouveXandY(lettre):
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

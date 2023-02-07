import xml.etree.ElementTree as ET

root = ET.Element("root")

CONFIG = ET.SubElement(root, "CONFIG").text = "c'est la config qui va contenir l'ip et le port"

SEND = ET.SubElement(root, "SEND")
ET.SubElement(SEND,"ELEMENTS").text="pour les element que le robot peut send"

tree = ET.ElementTree(root)
tree.write("output.xml")

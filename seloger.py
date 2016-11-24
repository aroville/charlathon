import requests
from lxml import etree
import pandas as pd

baseurl = "http://ws.seloger.com/search.xml?tri=initial&idtypebien=2,1&pxmax=5000&idtt=1&cp=75"

results = pd.DataFrame(columns=["cp", "pays", "ville", "surface", "nbPiece",
                                "idTypeBien", "nbChambre", "prix"])

line = 0

def save_xml(url, n):
    xml_file = requests.get(url)
    open("xml" + str(n), "w+").write(xml_file.text)

def search(idtypebien, idtt, cp):
    url = "http://ws.seloger.com/search.xml?tri=initial&idtypebien=" + \
            str(idtypebien) + "&pxmax=2000000&idtt=" + str(idtt) + "&cp=" + \
            str(75)
    current = 1
    while True:
        if current == 1:
            new_url = url
        save_xml(new_url, current)
        tree = etree.parse(new_url)
        cur_line = results.shape[0]
        for field in results.columns:
            line = cur_line
            for s in tree.xpath("/recherche/annonces/annonce/" + field):
                results.set_value(line, field, s.text)
                line += 1
        new_url_tree = tree.xpath("/recherche/pageSuivante")
        if len(new_url_tree) ==  0:
            break
        new_url = new_url_tree[0].text
        current += 1
    return results



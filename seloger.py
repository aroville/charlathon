import requests
from lxml import etree
import pandas as pd

baseurl = "http://ws.seloger.com/search.xml?"

results = pd.DataFrame(columns=["cp", "pays", "ville", "surface", "nbPiece",
                                "idTypeBien", "nbChambre", "prix"])

line = 0

def save_xml(url, n):
    xml_file = requests.get(url)
    open("xml" + str(n), "w+").write(xml_file.text)

def search(idtypebien, idtt, cp):
    options = {
        'idtypebien': str(idtypebien),
        'pxmax': '500000',
        'idtt': str(idtt),
        'cp': str(cp).zfill(2)
    }
    params = '&'.join([k + "=" + v for k, v in options.items()])

    url = baseurl + params
    new_url = url

    while True:
        save_xml(new_url, current)
        tree = etree.parse(new_url)
        cur_line = results.shape[0]
        for field in results.columns:
            line = cur_line
            for s in tree.xpath("/recherche/annonces/annonce/" + field):
                results.set_value(line, field, s.text if s is not None else 'NA')
                line += 1
        new_url_tree = tree.xpath("/recherche/pageSuivante")
        if len(new_url_tree) == 0:
            break
        new_url = new_url_tree[0].text
    return results



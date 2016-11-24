import requests
from lxml import etree
import pandas as pd
from multiprocessing import Pool

baseurl = 'http://ws.seloger.com/search.xml?'
cols = ["cp", "pays", "ville", "surface", "nbPiece", "idTypeBien",
        "nbChambre", "prix"]


def search(args):
    idtypebien = str(args[0])
    idtt = str(args[1])
    cp = str(args[2]).zfill(2)

    options = {
        'idtypebien': idtypebien,
        'idtt': idtt,
        'cp': cp
    }

    params = '&'.join([k + "=" + v for k, v in options.items()])

    url = baseurl + params
    print(url)
    new_url = url
    current = 1
    results = pd.DataFrame(columns=cols)

    while True:
        tree = etree.parse(new_url)
        cur_line = results.shape[0]

        for field in results.columns:
            l = cur_line
            for s in tree.xpath("/recherche/annonces/annonce/" + field):
                results.set_value(l, field, s.text if s is not None else 'NA')
                l += 1
        new_url_tree = tree.xpath("/recherche/pageSuivante")
        if len(new_url_tree) == 0:
            break
        new_url = new_url_tree[0].text
        current += 1
    return results

pool = Pool()
results_tot = pool.map(search, [
    [idtypebien, idtt, cp]
    for idtypebien in [1, 2, 4, 6, 7, 8, 9]
    for idtt in [1, 2]
    for cp in range(1, 96)
    ])


df_tot = pd.DataFrame(results_tot[0])
for df in results_tot[1:]:
    df_tot.append(df)

df_tot.to_csv('res.csv')

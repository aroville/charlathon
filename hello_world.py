import requests
import xml.etree.ElementTree as ET
import multiprocessing

url_base = 'http://ws.seloger.com/search.xml?'


def get_data(cp, type_bien):
    options = {
        'idtypebien': str(type_bien),
        'pxmax': '500000',
        'idtt': '2',
        'cp': str(cp).zfill(2)
    }

    params = '&'.join([k + "=" + v for k, v in options.items()])
    xml_file = requests.get(url_base + params)
    open('resp.xml', 'w+').write(xml_file.text)
    tree = ET.parse('resp.xml')
    root = tree.getroot()
    for prix in root.iter('prix'):
        print(prix.text)

for type_bien in [1, 2]:
    for cp in range(1, 96):

pool.map(get_data,
    [cp, type_bien]
    for type_bien in [1,2]
    for cp in range(1, 96))
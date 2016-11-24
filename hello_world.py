import requests
import xml
import xml.etree.ElementTree as ET

url_base = 'http://ws.seloger.com/search.xml?'

options = {
    'idtypebien': '2,1',
    'pxmax': '500000',
    'idtt': '2',
    'cp': '75',
    'tri': 'initial'
}

params = '&'.join([k + "=" + v for k, v in options.items()])
xml_file = requests.get(url_base + params)
open('resp.xml', 'w+').write(xml_file.text)
tree = ET.parse('resp.xml')
root = tree.getroot()
for prix in root.iter('prix'):
    print(prix)

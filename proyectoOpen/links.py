from requests_html import HTMLSession
import pandas as pd
session = HTMLSession()


headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

r = session.get('https://tembiapo.mopc.gov.py/')
script = r.html.xpath('//script')[1].text

split = script.split(' ')

urls = []

for e in split:
     if e.startswith("'/"):
         url = e.split(("'}"))[0][2:]
         urls.append(url)

urlPrincipal = "https://tembiapo.mopc.gov.py/"
cabeceras = []
columns = []
resultado = []
diccionario = {}

for e in urls:
    urlCompleto = "https://tembiapo.mopc.gov.py/%s" % e
    r = session.get(urlCompleto,
     verify=False,
    headers=headers)
    table = r.html.find('#info', first=True)

    if cabeceras != 1:
        for e in table.find('label'):
         columns.append(e.text)

    cells = []
    for e in table.find('p'):
        cells.append(e.text)

    cabeceras = 1

    for i,e in enumerate(columns):
        diccionario[columns[i]] = cells[i]

    resultado.append(diccionario)
    diccionario={}

df = pd.DataFrame(
        resultado)
df.to_csv('result.csv', index=False)
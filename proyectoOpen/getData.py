from requests_html import HTMLSession
session = HTMLSession()

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

r = session.get('https://tembiapo.mopc.gov.py/obras/42-pavimentacion-de-tramos-alimentadores-de-la-red-vial-nacional-paquete-n-1-lote-2',
                 verify=False,
                 headers=headers)

table = r.html.find('#info', first=True)


columns = []
for e in table.find('label'):
     columns.append(e.text)

cells = []
for e in urls:
     columns.append(e.text)

print(columns)
print(cells)
from bs4 import BeautifulSoup
import requests

page = 1

url = "https://ristekdikti.go.id/perguruan-tinggi/?&per-page=5&page={}".format(page)
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content)

table = soup.find("table")

data = []

rows=list()

for row in table.find_all('tr'):
    cols = row.find_all(['th', 'td'])
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
contents = data[1:]

class Database(object):
    def __init__(self):
        self.nama = content[0]
        self.alamat = content[2]
    
FULL_DATA = []

for content in contents:
    data = Database()
    s = data.__dict__
    FULL_DATA.append(s)

data = FULL_DATA

print(data)

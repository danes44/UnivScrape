from bs4 import BeautifulSoup
import requests
import re
import json

page = 0

class Database(object):
    def __init__(self):
        self.nama = content[0]
        self.alamat = content[2].split("Telp")[0]
        self.telepon = re.findall(r"Telp: ([0-9-]+)", content[2])
        self.email = re.findall(r"Email: ([^@]+@[^@]+\.[^@]+)Website", content[2])
        self.website = re.findall(r"Website: (?:|http[s]?:\/\/)((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)", content[2])
    
FULL_DATA = []

def scrape(page=page):
    url = "https://ristekdikti.go.id/perguruan-tinggi/?&per-page=5&page={}".format(page)
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content)
    table = soup.find("table")

    data = []

    for row in table.find_all('tr'):
        cols = row.find_all(['th', 'td'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
        
    contents = data[1:]

    return contents

# Use only 177 pages because more than those pages, the data contain universities abroad (other countries)

while page<178:
    print(page)
    try:
        contents = scrape(page)

        for content in contents:
            data = Database()
            s = data.__dict__
            FULL_DATA.append(s)

        data = FULL_DATA
    except:
        print("None")
        break
    page=page+1

f= open("data.json","w+")
f.write(json.dumps(data, indent=4))
f.close()
import requests
from bs4 import BeautifulSoup
def find_names():
    req = requests.get("https://manganato.com/")
    soup = BeautifulSoup(req.content, "html.parser")
    titles = soup.find_all('h3',class_='item-title')
    with open('titles.txt','w') as fil:
        for i in titles:
            text = i.text
            fil.write(text)
    print('written to file')
if __name__ == '__main__':
    find_names();
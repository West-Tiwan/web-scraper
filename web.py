import requests
from bs4 import BeautifulSoup
req = requests.get("https://manganato.com/")
soup = BeautifulSoup(req.content, "html.parser")
titles = soup.find_all('h3',class_='item-title')
for i in titles:
    print( i.text + '\n' )
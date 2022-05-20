## SETUP ##
import requests
from bs4 import BeautifulSoup
from classes import *

URL = 'https://caldining.berkeley.edu/menus/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
## END SETUP ##

def setup(url=URL, test=False):
    # dining_halls = [HTMLElement(soup, 'li', 'location-name')]
    # dining_halls = soup.find_all('li', class_='location-name')
    dining_halls = [HTMLElement(el) for el in dining_halls]
    for el in dining_halls:
        test and print(str(el))

if __name__ == '__main__':
    URL = 'https://example.html'
    setup(URL, True)
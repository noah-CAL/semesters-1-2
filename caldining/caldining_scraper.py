## SETUP ##
import requests
from bs4 import BeautifulSoup
from classes import *

URL = 'https://caldining.berkeley.edu/menus/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
## END SETUP ##

# def setup():
# """Returns a list containing DiningHall objects that correspond
# to ['Cafe 3', 'Clark Kerr Campus', etc...]
# >>> halls = setup() 
# >>> for d_hall in halls: print(d_hall.name)
# Cafe 3
# Clark Kerr Campus
# Crossroads
# Foothill
# """

# Grab the HTML of each dining hall
# dining_hall_elements = [DiningHall(el) for el in HTMLElements(soup, 'li', 'location-name')]
dining_hall_elements = HTMLElements(soup, DiningHall, 'li', class_='location-name')
print(dining_hall_elements)

# Create dining hall object
for dining_hall in dining_hall_elements:
    # for each dining hall, grab the breafast / lunch / dinner / brunch menus
    # print(soup.find_all('li', class_='preiod-name'))
    mealtime_elements = HTMLElements(soup, HTMLElement, 'li', class_='period-name')
    # print(mealtime_elements)

    for mealtime in mealtime_elements:
        station_elements = HTMLElements(mealtime.get_html(), 'div', 'cat-name')
        station_elements.filter(
            lambda station: station.get_text().strip() not in FoodStation.BANNED_STATIONS
        )
        stations = [FoodStation(el) for el in station_elements]
        print(stations)
        for station in stations:
            food_elements = HTMLElements(station.get_html(), 'li', 'recip')
            for food in food_elements:
                pass
                
                

        ## CREATE THE OBJECT ##
        # dining_halls = [DiningHall(name) for name in dining_hall_elements]
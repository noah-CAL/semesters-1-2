class HTMLElement:
    """Defines a data abstraction to handle HTML and english text of an object"""

    def __init__(self, html):
        """HTML_TAG and CLASS_ are used to query the BS4 html page"""
        self.html = html
        self.text = self.html.find('span').text
    
    def get_html(self):
        return self.html

    def get_text(self):
        return self.text

    def __str__(self) -> str:
        return self.text
    
class HTMLElements:
    """Defines a data abstraction to handle collections of HTMLElement objects"""

    def __init__(self, soup, object_class, html_tag, class_=''):
        """HTML_TAG and CLASS_ are used to query the BS4 html page"""
        assert (object_class is DiningHall
             or object_class is FoodStation
             or object_class is FoodItem
             or object_class is HTMLElement), f'{object_class} must be DiningHall, FoodStation, FoodItem, or HTMLElement!'
        assert class_, f'class_ can\'t be empty!'
        self.elements = [
            object_class(el)    # Wrap the element in the specified class
            for el in [         # Create HTMLElement objects for each occurance of search query
                html for html in soup.find_all(html_tag, class_=class_)
            ]
        ]
        print(self.elements)
    
    def get_elements(self):
        """Returns a list containing HTMLElement objects"""
        return self.elements

    def filter(self, filter) -> None:
        """Removes HTMLElement from collection if filter(element) == False"""
        for element in self.elements:
            if not filter(element):
                # print(f'removed {element.get_text()}')
                self.elements.remove(element)
    
    def __str__(self):
        """Returns a newline-separated string of the text of each object"""
        return '\n'.join([element.get_text() for element in self.elements])
    
    def __iter__(self):
        return iter(self.get_elements())

class DiningHall(HTMLElement):
    def __init__(self, html_element):
        super().__init__(html_element)
        assert (self.text == 'Cafe 3'
            or self.text == 'Crossroads'
            or self.text == 'Clark Kerr Campus'
            or self.text == 'Foothill'), f'{self.text}: incorrect campus name!'
        self.stations = {
            'breakfast':[],
            'lunch':[],
            'dinner':[],
            'brunch':[]
        }
    
    def add_station(self, station, mealtime) -> None:
        assert type(station) == FoodStation, f'{station} must be a station object!'
        assert mealtime in ['breakfast', 'lunch', 'dinner', 'brunch'], (
                f'{mealtime} must be breakfast lunch dinner or brunch!'
        )
        self.stations[mealtime].append(station)

    def get_stations(self, mealtime) -> list:
        """Returns a list of the stations at this dining hall at the specified time"""
        return self.stations[mealtime]

class FoodStation(HTMLElement):
    """
    Contains a list of foods offered at this station 
    for the specified mealtime breakfast, lunch, dinner, etc.
    """
    BANNED_STATIONS = [
        # CAFE 3
        'HOT CEREAL',
        'PASTRIES',
        'FRUIT',
        'KOSHER DELI',
        'KOSHER DELI (Per Request)',
        'SALADS',
        'DESSERT',
        'SOUPS',
        # CLARK KERR CAMPUS
        'SOUP & SALAD'
        # CROSSROADS
        'HOT MORNING GRAINS',
        'BREAKFAST BREAD',
        'DAILY RICE',
        'BEAR FIT',
        'SALADS',
        'DELI',
        # FOOTHILL
        'DAILY RICE',
        'DAILY HOT GRAINS',
        'FIT BOWL',
        'DELI',
        'FIT BOWL',
        'MAIN LINE VEGGIE',
    ]
    def __init__(self, html_element):
        super().__init__(html_element)
        assert self.text not in FoodStation.BANNED_STATIONS, f'{self.text} is a banned food station!'
        self.food_items = []

    def add_food(self, food_item):
        """
        # >>> station = FoodStation('<span>Station</span>')
        # >>> station.add_food(FoodItem("fish tacos"))
        # >>> station.get_foods[0].get_name()
        # 'fish tacos'
        # >>> station.add_food('h')
        # Traceback (most recent call last):
        # ...
        # AssertionError: h must be of type FoodItem!
        # >>> station.add_food(FoodItem("biscuits"))
        """
        assert type(food_item) == FoodItem, f'{food_item} must be of type FoodItem!'
        self.food_items.append(food_item)
    
    def get_foods(self) -> list:
        """Returns a list of all FoodItems that belong to this particular station"""
        return self.food_items
    
    def filter_foods(self, tags: list) -> list:
        """Returns a list of FoodItems that contain every in TAGS"""
        # TODO implement error checking on this function
        foods = []
        for food in self.food_items:
            if all([tags in food_tags for food_tags in food.get_tags()]):
                foods.append(food)
        return foods

    def get_foods(self, time):
        """Returns a list of the food_items in this food station"""
        return self.food_items

class FoodItem (HTMLElement):
    def __init__(self, html_element):
        super().__init__(html_element)
        self.tags = []
    
    def get_name(self):
        """Returns a string representation of the name of the food"""
        return self.name
    
    def get_tags(self):
        """Returns a list of the tags associated with the food"""
        return self.tags

    def add_tags(self, *tags):
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)
from bs4 import BeautifulSoup
import bs4
from requests.sessions import get_netrc_auth

class HTMLElement:
    """Defines a data abstraction that pairs a SOUP object with english text representation"""
    def __init__(self, soup, tag, class_):
        self.html, self.text = HTMLElement.gen_html_and_text(soup, tag, class_)

    @staticmethod
    def gen_html_and_text(soup, tag: str, class_: str) -> str:
        """Takes in a SOUP Tag and queries the HTML with TAG and CLASS_ to retrieve the appropriate text"""
        assert type(soup) is bs4.element.Tag, f'{soup} SOUP argument must be of type bs4.element.Tag'
        html = soup.find_all(tag, class_)
        text = html.find('span').get_text()
        return html, text

    def get_text(self, soup):
        return self.text

    def get_html(self):
        return self.soup

    def __str__(self) -> str:
        return self.get_text()
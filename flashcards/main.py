from bs4 import BeautifulSoup

with open('roster.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

roster = soup.find_all(class_='member')
for member in roster:
    name = member.find('span').get_text()
    image_url = member.find('img')['src']
    print(name, image_url, sep='||')

import requests

URL = open('keys/gcal-key.txt','r').readline()

r = requests.get(URL)
print(r)
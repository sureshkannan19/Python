import requests
from datetime import datetime

time = datetime.now()
response = requests.get('http://api.open-notify.org/astros.json')
print("Time taken:", datetime.now() - time)
json = response.json()
print(json)

def greeting(name):
    print("Hello, " + name)

for person in json["people"]:
    greeting(person['name'])


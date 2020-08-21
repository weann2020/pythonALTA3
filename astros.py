import requests


astros = (requests.get('http://api.open-notify.org/astros.json')).json()

number = astros["number"]

print(f"People in space: {number}")

#for x in range(len(astros["people"])):
for x in range(number):
    print(astros["people"][x]["name"] + " on the " + astros["people"][x]["craft"])

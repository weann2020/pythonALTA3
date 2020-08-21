import requests
import wget


date = input("Enter the date of APOD in format of YYYY-MM-DD: ")

image = input("Would you like the image in HD or SD? ")

url = 'https://api.nasa.gov/planetary/apod?date='+date+'&api_key=Odhtl3AdNc2QxIiFSb6ZkjQoghsuoqLs7UvgLz0X'

APOD = (requests.get(url)).json()

#print(APOD)
print(APOD["date"])
print(APOD["title"])
print(APOD["explanation"])


if image =="HD":
    url1 = APOD["hdurl"]
else:
    url1 = APOD["url"]

wget.download(url1, out='/home/student/mycode/')

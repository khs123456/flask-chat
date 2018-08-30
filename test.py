import requests

url = "https://api.thecatapi.com/v1/images/search?mime_type=jpg"

req = requests.get(url).json()

print(req[0]['url'])


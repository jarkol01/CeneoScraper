import requests

url = 'https://www.ceneo.pl/101052360/opinie-1'

response = requests.get(url)
print(response.text)
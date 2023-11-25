import requests


endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={'Title':'king'}) #API -> method

print(response.json())
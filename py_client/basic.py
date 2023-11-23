import requests


endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={'abc':123},json={"query":"Hello King!"}) #API -> method

print(response.json())
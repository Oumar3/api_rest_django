import requests

endpoint = "http://127.0.0.1:8000/api/api/"

data = {'name':'ANANAS','content':'JUSTE ANANAS','price':320}

re = requests.get(endpoint,json=data)

print(re.json())
print(re.status_code)


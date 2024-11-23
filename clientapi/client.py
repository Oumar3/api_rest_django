import requests

endpoint = "http://127.0.0.1:8000/api/?age=10"

data = {
        'name':'ANANAS',
        'content':'JUSTE ANANAS',
        'price':320
    }

re = requests.get(endpoint)

print(re.json())
print(re.status_code)


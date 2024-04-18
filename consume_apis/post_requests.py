import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())


# If you don’t use the json keyword argument to supply the JSON data, 
# then you need to set Content-Type accordingly and serialize the JSON manually.
import json 

headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
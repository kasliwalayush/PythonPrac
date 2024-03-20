import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

response_json = json.loads(response.text)

print(response_json)

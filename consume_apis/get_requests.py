# Get reuqests:
import requests

api_url = "https://api.sampleapis.com/codingresources/codingResources"
response = requests.get(api_url)
#print(response.json())

# Other things to view in response:
print(response.status_code, response.headers["Content-Type"])
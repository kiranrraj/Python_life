import requests

url = 'http://api.github.com'

response = requests.get(url)
print(response.headers['date'])
print(response.headers['server'])
print(response.headers['status'])
print(response.headers['cache-control'])
print(response.headers['content-type'])
print(response.json()['current_user_url'])
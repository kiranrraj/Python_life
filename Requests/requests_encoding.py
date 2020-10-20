import requests

response = requests.get('http://httpbin.org/')

print(f"Response Code : {response.status_code}")
print(f"Encoding type : {response.encoding}")
print(f"Elapsed time : {response.elapsed}")
print(f"Response URL : {response.url}")

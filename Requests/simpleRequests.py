import requests
r = requests.get('https://xkcd.com/353/')
print(f"Requested url :{r.url}")
# print(r.text)
print(f"Encoding type : {r.encoding}")
print(f"Status code : {r.status_code}")
print(f"Header : {r.headers['Content-Type']}")
# print(r.headers.get('Content-Type'))
import requests

r = requests.get('http://httpbin.org/get')
jsonOut = r.json()
print(r.url)
print(f"Arguments passed to the url :{jsonOut['args']}")


payload = {'fname':'kiran', "lname":"raj"}
r = requests.get('http://httpbin.org/get', params=payload)
jsonOutwArgs = r.json()
print(f"Arguments passed to the url :{jsonOutwArgs['args']}")

payload = {'fname':'kiran', "lname":"raj"}
r = requests.post('http://httpbin.org/post', params=payload)
print(f"Date from header : {r.headers['Date']}")
print(f"Content type from header : {r.headers['Content-Type']}")
print(f"Content length from header : {r.headers['Content-Length']}")

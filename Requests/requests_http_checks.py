import requests

r = requests.get('http://httpbin.org/get')
jsonOut = r.json()
print("---------------------------------------")
print(f"URL : {r.url}")
print(f"Arguments passed to the url :{jsonOut['args']}")
print("---------------------------------------")

payload = {'fname':'kiran', "lname":"raj"}
r = requests.get('http://httpbin.org/get', params=payload)
getRes = r.json()
print(f"URL : {r.url}")
print(f"Arguments passed to the url :{getRes['args']}")
print("---------------------------------------")

payload = {'fname':'kiran', "lname":"raj"}
r = requests.post('http://httpbin.org/post', data=payload)
postRes = r.json()
print(f"URL : {r.url}")
print(f"Date from header : {r.headers['Date']}")
print(f"Content type from header : {r.headers['Content-Type']}")
print(f"Content length from header : {r.headers['Content-Length']}")
print(f"Arguments posted to the url :{postRes['form']}")
print("---------------------------------------")

payload = {'fname':'kiran', "lname":"raj", "initials":"r"}
r = requests.post('http://httpbin.org/post', data=payload)
postRes = r.json()
print(f"URL : {r.url}")
print(f"Date from header : {r.headers['Date']}")
print(f"Content type from header : {r.headers['Content-Type']}")
print(f"Content length from header : {r.headers['Content-Length']}")
print(f"Arguments posted to the url :{postRes['form']}")
print("---------------------------------------")


# Output

# ---------------------------------------
# URL : http://httpbin.org/get
# Arguments passed to the url :{}
# ---------------------------------------
# URL : http://httpbin.org/get?fname=kiran&lname=raj
# Arguments passed to the url :{'fname': 'kiran', 'lname': 'raj'}
# ---------------------------------------
# URL : http://httpbin.org/post
# Date from header : Fri, 02 Oct 2020 17:34:48 GMT
# Content type from header : application/json
# Content length from header : 503
# Arguments posted to the url :{'fname': 'kiran', 'lname': 'raj'}
# ---------------------------------------
# URL : http://httpbin.org/post
# Date from header : Fri, 02 Oct 2020 17:34:49 GMT
# Content type from header : application/json
# Content length from header : 525
# Arguments posted to the url :{'fname': 'kiran', 'initials': 'r', 'lname': 'raj'}
# ---------------------------------------
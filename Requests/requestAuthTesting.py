import requests

r = requests.get('http://httpbin.org/basic-auth/kiran/12345678',
auth= ('kiran', '12345678'))
print(r.text)
print(f"Status code : {r.status_code}")
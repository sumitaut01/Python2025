import requests
r = requests.get("https://api.github.com")
print(r.status_code)


data = r.json()
print(data['name'])

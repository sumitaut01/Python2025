import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Hulk_Hogan'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0 Safari/537.36"
}

data = requests.get(url, headers=headers)

# Check status
print("Status code:", data.status_code)

soup = BeautifulSoup(data.text, 'lxml')

# Example: print the title of the page
print(soup.title.text)

print(soup)
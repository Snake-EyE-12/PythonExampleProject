from bs4 import BeautifulSoup
import requests

url = "https://mcstacker.net/?cmd=give#google_vignette"
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

select = soup.find("select", id="GiveItem0")

options = select.find_all("option")

items = [
    {
        "text": opt.get_text(strip=True),
        "value": opt.get("value")
    }
    for opt in options
]

print(items)

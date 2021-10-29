import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.youtube.com/watch?v=O6nnVHPjcJU")

soup = BeautifulSoup(req.content,"html.parser")

res = soup.title
print(res.prettify())
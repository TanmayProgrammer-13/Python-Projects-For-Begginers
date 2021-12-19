#Importing Modules
import requests
from bs4 import BeautifulSoup

# Acessing HTML Page Or Website
url = input('Enter the URL: ')
r = requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
print(soup.prettify())




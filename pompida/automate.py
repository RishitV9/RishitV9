from bs4 import BeautifulSoup
import requests
import os

sites = "biologyclass.club"

print("Checking: " + sites)
html = requests.get("https://" + sites)
soup = BeautifulSoup(html.text, 'html.parser')

if 'Web Page Blocked' not in soup.title:
    f = open("unbocked.html", 'w')
    f.write(soup.prettify())
    f.close()

os.system("node serve.js")

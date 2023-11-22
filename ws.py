from bs4 import BeautifulSoup
import requests

site = requests.get(
    "https://www.uol.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

# print(soup.prettify())

# temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(soup)
print(soup.title.string)
print(soup.a.string)
print(soup.find('Katia'))

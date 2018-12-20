from bs4 import BeautifulSoup
import requests

adres_strony = 'https://wallpaperlist.com'

zrodlo_strony = requests.get(adres_strony).content

parser = BeautifulSoup(zrodlo_strony, 'html.parser')

obrazki = parser.find_all('img')

for obraz in obrazki:
    adres_obrazka = adres_strony +obraz['src']
    print(adres_strony + obraz['src'])
    dane_obrazka = requests.get(adres_strony).content



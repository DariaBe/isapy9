from modul import przywitanie as moje_przywitanie
import Zadanie_4


moje_przywitanie.czesc('Daria')
Zadanie_4.rysuj_piramide()

import csv
import pickle

with open('adresy.csv', 'r+', newline='') as csvfle:
    reader = csv.reader(csvfle)
    for row in reader:
        print(row)

    writer = csv.writer(csvfle)
    writer.writerow(['Jan', 'Kowalski', 'Sopot', '123-432-111'])

with open('adresy.pickle', 'rb+') as picklefle:
    dane = (pickle.load(picklefle))
    print(dane)
    # lista = [1, 2 , 3]
    # pickle.dump(lista, picklefle)

import string
import pickle

def otworz_plik():
    plik = input('Podaj nazwę pliku: ')
    try:
        with open(plik) as kant:
            return kant.read()
    except:
        print('Wystąpił jakiś błąd')
        return otworz_plik()


def zapisz_plik(kant):
    plik = 'wyniki.txt'
    try:
        with open(plik, 'wb+') as wyniki_plik:
            pickle.dump(kant, wyniki_plik)
    except Exception as e:
        print(e)


znaki = string.ascii_letters
kant = otworz_plik()
print(kant)

dlugosc = len(kant)
stats = {'dlugosc' : dlugosc}

for znak in znaki:
    ilosc = kant.count(znak)
    stats[znak] = ilosc

zapisz_plik(stats)

with open('wyniki.txt', 'rb+') as wyniki_plik:
    print(pickle.load(wyniki_plik))
try:
    dane = otworz_plik('kant.txt')
except:
    print('Wystąpił jakiś błąd')


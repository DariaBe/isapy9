napis = 'aaa'
przypisanie_napis = napis

napis = 'xxx'

print(napis)
print(przypisanie_napis)



lista = ['aaa', 'bbb', 'ccc', 'dddd']
przypisanie = lista


#
# print(lista)
# print(przypisanie)

import copy

lista = ['aaa', 'bbb', 'ccc', 'dddd']
przypisanie = lista

kopia_indeksami = lista[:]
kopia_konstruktorem = list(lista)
kopia_metoda = lista.copy()
kopie_biblioteka = copy.copy(lista)

lista[0] = 'xxx'

print(lista)
print(przypisanie)
print(kopia_indeksami)
print(kopia_konstruktorem)
print(kopia_metoda)
print(kopie_biblioteka)


# def wyslietl_napis(napis, koniec='.'):
#     print(napis + koniec)
#
# wyslietl_napis('Ala')
# wyslietl_napis(koniec=)

tekst = "Ala ma kota"

print(tekst.count('a'))


def policz_literke(litera='a', tekst='Ala ma kota'):
    return tekst.count(litera)

print(policz_literke())

def policz_literke(litera='a', tekst='Ala ma kota'):
    litera = litera.lower()
    tekst = tekst.lower()
    return tekst.count(litera)

print(policz_literke())


def policz_literke(litera='a', tekst='Ala ma kota'):
    litera = litera.lower()
    tekst = tekst.lower()
    i = 0
    for litera_w_tekscie in tekst:
        if(litera_w_tekscie == litera):
            i += 1
    return i

print(policz_literke('m'))

def do_nothing(x, y, imie='Ola', wiek=18):
    return x, y, imie, wiek


# do_nothing(1, 2)
do_nothing(1, 2, 'Iza')
do_nothing(1, 2, 'Iza', 22)
# do_nothing(1, 2, imie='Iza', 22)
do_nothing(1, 2, imie='Iza', wiek=22)
do_nothing(1, 2, wiek=22, imie='Iza')

def dodaj(x, y,):
    suma = x + y
    # return suma

wynik = dodaj(2, 3)
print(wynik)


def znajdz_duze_liter(napis):
    zmienna = []
    for litera in napis:
        if(litera.isupper()):
            zmienna.append(litera)
    return zmienna
wynik = znajdz_duze_liter('ZDanie Z dużyMi LiteRAmi')
print(wynik)
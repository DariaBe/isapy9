import string

with open('kant.txt', 'r') as kant:
    dane = kant.read()
    print(dane)
    dlugosc = len(dane)
    print('Tekst ma {} znaki.'.format(dlugosc))
    wszystkie_litery = string.ascii_letters
    ilosc_spacji = dane.count(' ')
    ilosc_wyrazow = ilosc_spacji + 2
    print('Tekst ma {} wyrazów.'.format(ilosc_wyrazow))
    kropka = dane.count('.')
    wykrzyknik = dane.count('!')
    znak_zapytania = dane.count('?')
    ilosc_zdan = kropka + wykrzyknik + znak_zapytania
    print('Tekst ma {} zdania.'.format(ilosc_zdan))

    print('Ilość poszczególnych liter: ')

    for znak in wszystkie_litery:
        ilosc_znakow = dane.count(znak)
        print(znak, ilosc_znakow)

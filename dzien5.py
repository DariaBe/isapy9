slownik = {'imie': ['Łukasz', 'Ola', 'Ala' ],
           'nazwiska': ['Falkowicz', 'Kowalska', "Malinowska"]
}

miasta = {'miasta': ['Warszawa', 'Gdańsk', 'Sopot', 'Kraków']}

print(type(slownik))
print(slownik)

for klucz, wartosc in slownik.items():
    print(klucz)
    for i in wartosc:
        print('\t -> ' + i)

slownik.update(miasta)

print(slownik)

for index, imie in enumerate(slownik['imie']):
    nazwisko = slownik['nazwiska'][index]
    miasto = miasta['miasta'][index]
    print('Mam na imię: {} nazwisko {} i mieszkam w {}'.format(imie, nazwisko, miasto))

def wyswietl_slownik():
    for index, imie in enumerate(slownik['imie']):
        nazwisko = slownik['nazwiska'][index]
        miasto = miasta['miasta'][index]
        print('Mam na imię: {} nazwisko {} i mieszkam w {}'.format(imie,nazwisko,miasto))


plik = open('dane.txt', 'r+')
licznik = int(plik.readline()) + 1
print(licznik)
plik.seek(0)
plik.write(str(licznik))
plik.close()

imie = input('Podaj imię: ')
tresc = input('Podaj treść: ')
plik = open ('dane', 'a+')
plik.write(str(imie))
plik.write(str(tresc))
plik.close()

imie = 'Jola'
def zmien_imie():
    imie ='Teresa'

print(imie)
zmien_imie()
print(imie)


plik = open('kant.txt', 'r')
plik.readline()
print(str.count(plik))
plik.close()
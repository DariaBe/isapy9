napis  = "encyklopedia"

zmienna = f"To jest napis: {napis}"
print (zmienna)

napis = 50

zmienna = "To jest napis: " + str(napis)
print(zmienna)

zmienna = 013.639000
print("wartośćto : %s" % zmienna)
print("wartośćto : %f" % zmienna)
print("wartośćto : %d" % zmienna)

print("Ala ma {} koty i {} psy".format(3, 2))
print("Ala ma {ilosc} koty i 2 {nazwa}".format(ilosc=3, nazwa='psy'))

szerokosc = 10
wysokosc = 20

print('+' + ("-" * szerokosc) + '+')
print(('|' + (" " * szerokosc) + '|\n')*wysokosc, end='')
print('+' + ("-" * szerokosc) + '+')

import string

liczba = 123456

if(liczba % 3 == 0):
    print("podzielna przez 3")
elif(liczba % 5 == 0):
    print("podzilena przez 5")
else:
    print("nie podzielna")

range1= range(1,4)
lista1 = [1,2,3]

print(lista1)
print(range1)
# lista2 = ["kwiatek", "doniczka", "ziemia", "woda"]
# lista3 = list(1)
# lista7 = list(range(2,5))

lista = [
    [1,2,3],
    [4,5,6,"napis"],
    [7,8,9]
]
print(lista[1][3][1])

x = 0
while(x < 10):
    print("Coś")
    x += 1


decyzja = None
while(decyzja != 'T'):
    decyzja = input("wybierz 'T' aby zamknąć program:")


lista_2d = [
    [1,2,3],
    [4,5,6, "NAPIS"],
    [7,8,9]
]

lista_2d[1][3] = lista_2d[1][2] *5
print(lista_2d)

print("Policzę dla ciebie do 100")
i=1
while (i <= 100):
    print(str(i)  + ' ', end='') # print bez nowych linii
    # print(i)
    i += 1

x = 2
while(x * 2 <= 40):
    print(x)
    x += 1

print((('#' * ilosc_znakow) + '\n') * wysokosc, end=' ')

print(' ' * (wysokosc-1) + '#' * 1)
print(' ' * (wysokosc-2) + '#' * 3)
print(' ' * (wysokosc-3) + '#' * 5)
print(' ' * (wysokosc-4) + '#' * 7)
print(' ' * (wysokosc-5) + '#' * 9)

print('  ' + '#')
print(' ' + '###')
print('#' * ilosc_znakow)
# print((('#' * ilosc_znakow) + '\n') * wysokosc, end=' ')


liczby = range(0, 50)
for liczba in liczby:
    print(liczba)

liczby = range(0, 50)
for liczba in liczby:
    if(liczba % 2 != 0):
        continue
    print(liczba)

lista_imion = ['Ola', 'Ala', 'Tomek', 'Jan']
for i, imie in enumerate(lista_imion):
    print("Na pozycji: {} jest imię {}".format(i, imie))


lista_nazwisk = ['Kowalska', 'Malinowska', 'Iksinski', 'Igrekowski']

for i, y in zip(lista_imion, lista_nazwisk):
    print("Mam na imię {}, a na nazwisko {}".format(i, y))



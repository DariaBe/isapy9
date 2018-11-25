#1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)

wzorF = "TempF = 32 + 9/5 * TempC"

print(wzorF)

TempC = input("Podaj tempraturę w stopniach Celcjusza: ")

TempC = float(TempC)

TempF = 32 + 9/5 * TempC

print(TempF)

#2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)

wzorC = "TempC = 5/9 * (TempF - 32)"

print(wzorC)

TempF = input("Podaj tempraturę w stopniach Fahrenheita: ")

TempF = float(TempF)

TempC = 5/9 * (TempF - 32)

print(TempC)

#3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)

r = input("Podaj dłogość promienia: ")

r = float(r)

wzor = "3.14 * r**2"

print(wzor)

pole_powierzchni = 3.14 * r ** 2

print(pole_powierzchni)

#4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby

liczba = input("Podaj liczbę: ")

print(liczba[0] +" "+ liczba[-1])


#6. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny. Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.

podana_liczba = input("Podaj liczbę w systemie binarnym: ")

liczba_1 = int(podana_liczba[0]) * 32
liczba_2 = int(podana_liczba[1]) * 16
liczba_3 = int(podana_liczba[2]) * 8
liczba_4 = int(podana_liczba[3]) * 4
liczba_5 = int(podana_liczba[4]) * 2
liczba_6 = int(podana_liczba[5]) * 1

print(liczba_1 + liczba_2 + liczba_3 + liczba_4 + liczba_5 + liczba_6)

#7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.

liczba = input("Podaj liczbę całkowitą: ")

liczba = float(liczba)

sprawdzenie = (liczba % 2)


if sprawdzenie == 0 :
    print("Podana liczba jest liczbą parzystą.")

else:
    print("Podana liczba jest liczbą nieparzystą.")



#8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7

liczba = input("Podaj liczbę całkowitą: ")

liczba = float(liczba)

podzielna_przez_3 = liczba % 3

#print(podzielna_przez_3)

podzielna_przez_5 = liczba % 5

#print(podzielna_przez_5)

podzielna_przez_7 = liczba % 7

#print(podzielna_przez_7)

if podzielna_przez_3 == 0 or podzielna_przez_5 == 0 or podzielna_przez_7 == 0:
    print("Liczba jest podzielna przez 3 lub 5 lub 7.")
else:
    print("liczba nie jest podzielna przez 3 lub 5 lub 7.")


#9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7

liczba = input("Podaj liczbę całkowitą: ")

liczba = float(liczba)

podzielna_przez_3 = liczba % 3

#print(podzielna_przez_3)

podzielna_przez_5 = liczba % 5

#print(podzielna_przez_5)

podzielna_przez_7 = liczba % 7

#print(podzielna_przez_7)

if podzielna_przez_3 == 0 and podzielna_przez_5 == 0 and podzielna_przez_7 == 0:
    print("Liczba jest podzielna przez 3 i 5 i 7.")
else:
    print("Liczba nie jest podzielna przez 3 i 5 i 7.")

#10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

rok = input("Podaj rok: ")

rok = int(rok)

czy_przestępny = rok % 4


if czy_przestępny == 0:
    print("Podany rok jest rokiem przestępnym.")

else:
    print("Podany rok nie jest rokiem przestępnym.")

#5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#    | (bok)
 #   - (góra/dół)
  #  + (wierzchołek)

szerokosc = 5
wysokosc = 20

print('+' + ("-" * szerokosc) + '+')
print(('|' + (" " * szerokosc) + '|\n')*wysokosc, end='')
print('+' + ("-" * szerokosc) + '+')

wysokosc = input("Podaj wysokość piramidy: ")
wysokosc = int(wysokosc)



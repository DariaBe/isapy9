# 1) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)

lista = ['col1', 'col2', 'col3', 'col4']
ilosc_argumentow = len(lista)
max_ilosc_liter = max(lista, key = len)
max_ilosc_liter = len(max_ilosc_liter)


print(('+' + '-' * (max_ilosc_liter + 2)) * ilosc_argumentow + '+')

for i in lista:
    print(('| ' + i), end=' ')

print('|')
print(('+' + '-' * (max_ilosc_liter + 2)) * ilosc_argumentow + '+')


def rysowanie_tabeli(lista=[]):
    """Ta fukncja przyjmuje listę w parametrze i rysuje tabelę"""
    ilosc_kolumn = input('Podaj ilość kolumn: ')
    ilosc_kolumn = int(ilosc_kolumn)
    for i in ilosc_kolumn:

    ilosc_argumentow = len(lista)
    max_ilosc_liter = max(lista, key=len)
    max_ilosc_liter = len(max_ilosc_liter)
    print(('+' + '-' * (max_ilosc_liter + 2)) * ilosc_argumentow + '+')
    for i in lista:
        print(('| ' + i), end=' ')
    print('|')
    print(('+' + '-' * (max_ilosc_liter + 2)) * ilosc_argumentow + '+')


rysowanie_tabeli(['col1', 'col2', 'col3'])

# 2) Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.


kwota = input("Podaj kwotę: ")
kwota = float(kwota)
monety = [5, 2, 1, 0.5, 0.2, 0.1]

for num in monety:
    if kwota // num > 0:
        print("Otrzymasz {} monety {} złotowe".format(kwota // num, num))
        kwota = kwota - (kwota // num * num)
        kwota = (round(kwota, 1))
    else:
        continue


# 3) Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####

wysokosc = input("Podaj wysokość piramidy: ")
wysokosc = int(wysokosc)


for i in range(1, wysokosc * 2, 2):
    print(' ' * (wysokosc - 1) + '#' * i)
    wysokosc = wysokosc - 1


# 4) Kalkulator do wyliczania wieku psa.
#  Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
# Np: 15 ludzkich lat to 73 psie lata

wiek_psa = (input("Podaj wiek psa: "))
wiek_psa = float(wiek_psa)

if(wiek_psa <= 2):
    print(wiek_psa * 10.5)
elif(wiek_psa >= 2):
    print((wiek_psa - 2) * 4 + 21)
else:
    print("Chyba nie masz psa")
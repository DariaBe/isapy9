"""imie = input("Jak masz na imie")
imie = imie.strip( )
dlugosc = len(imie)
ostatni_litera_imienia = imie[dlugosc-1]
print("Cześć")
print(imie.upper())
print(imie[-1:])
print("Twoje imie ma: " + str(dlugosc) + " liter")
print("Twoja ostatnia litera imienia to : " + ostatni_litera_imienia
      """

"""imie = input("Jak masz na imie")
imie = imie.strip( )
dlugosc = len(imie)
ostatni_litera_imienia = imie[dlugosc-1]
print("Cześć")
print(imie.upper())
ostatnia_litera = imie[-1:]
if(ostatnia_litera == 'a'):
    print("Witam Panią")
else:
    print("Witam Pana")"""


wyraz = 'encyklopedia'

print(wyraz[2:8],
      wyraz[8:],
      wyraz[1:7:2],
      )

lista1 = [1, 2, 3]
lista2 = ["kwiatek", "doniczka", "ziemia", "woda"]
lista3 = []
lista4 = [1, "dwa", 3, 4]
lista5 = list("dwa piętnaście")
lista6 = list(1)
lista7 = list(range(0,20,3))

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista7)
# print(lista1)
# print(lista1)

lista = [ [1,2,3],[4,5,6],[7,8,9] ]
# lista = [
#
# [1,2,3],
# [4,5,6],
# [7,8,9]
#
# ]

print(lista[1][2])

lista = [
    [1,2,3],
    [4,5,6,"napis"],
    [7,8,9]
]
print(lista[1][3][1])

lista.append(['lalala'])

print(lista)
lista[1][3] = lista[1][2]*5

print(lista)
lista[3].extend('tak')
print(lista)

lista[1][2] = 'zwariuje'
print(lista)

krotka1 = (1, 2, 3)
krotka2 = ("kwiatek", "doniczka", "ziemia", "woda")
krotka3 = ()
krotka4 = (1, "dwa", 3, 4)
krotka5 = tuple("dwa")
# krotka6 = tuple(1)
krotka7 = list(range(2,5))

print(krotka1, krotka2,krotka3,krotka4,krotka5,krotka7)

wyrazy = ("raz", "dwa", "trzy")
a, b, c = wyrazy

print(a)

ieie = 'Jola'
def zmien_imie():
    ieie = 'Teresa'

print(ieie)

zmien_imie()
print(ieie)

osoby = {"studenci": ["Ala", "Jan", "Ania"], "wykladowcy": ["doktor", "profesor"]}
print(osoby["studenci"][1])

osoby["wykladowcy"].append("magister")
print(osoby)
osoby["administracja"] = ["pani Basia z dziekanatu"]
print(osoby)

osoby.update({"ochrona":"Impel"})
print(osoby)


print(osoby.keys)
print(osoby.values)

for key, item in osoby.items():
    print(key, item)
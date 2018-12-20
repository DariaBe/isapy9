
class NaszeKrzeslo(object):
    def __init__(self, nazwa = 'Wing', ilosc_nog = 4, material = 'sklejka', kolor = 'jasny', cena_netto = 20, marza = 10):
        self.ilosc_nog = ilosc_nog
        self.ilosc_podlokietnikow = 0
        self.oparcie = True
        self.wymiary = (80,40,40)
        self.producent = 'Bodzio'

        self.kolor = kolor
        self.material = material
        self.cena_netto = cena_netto
        self.nazwa = nazwa

        self.marza = marza

    def cena_sprzedarzy(self):
        return self.cena_netto * (1+100/self.marza)

    def cena_brutto(self):
        return self.cena_sprzedarzy() * 1.23

    def cena_brutto_euro(self):
        return self.cena_brutto() * 4.3

    def __str__(self):
        return 'Nazywam się {} i kosztuję {}'.format(self.nazwa, self.cena_brutto())

    def __add__(self, other):
        return self.cena_netto + other.cena_netto

    def __lt__(self, other):
        if self.ilosc_nog < other.ilosc_nog:
            return '{} jest bardziej stabilny.'.format(other.nazwa)
        else:
            return '{} jest bardziej stabilny.'.format(self.nazwa)

    def __str__(self):
        return 'Jestem {} za 10 zł i mam {} nóg'.format(self.nazwa, self.ilosc_nog)


# print((obiekt_1.cena_netto))
# print(obiekt_1.cena_brutto())
# print(obiekt_1.cena_brutto_euro())
# print(obiekt_1)
obiekt_2 = NaszeKrzeslo('Wing Lux', 8, 'drewno', 'ciemny', 1000000, 50)
# print((obiekt_2.cena_netto))
# print(obiekt_2.cena_brutto())
# print(obiekt_2.cena_brutto_euro())
obiekt_1 = NaszeKrzeslo()

print((obiekt_1 < obiekt_2))
print((obiekt_1 + obiekt_2))
print(obiekt_2)
print(obiekt_1)

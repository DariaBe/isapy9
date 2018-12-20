# -*- coding: utf-8 -*-

class Magister(object):
    def witaj(self):
        return 'Dzień dobry Magistrze!'
class Inzynier(object):
    def witaj(self):
        return 'Dzień dobry Inżynierze!'

class Zwierze(object):
    def __init__(self, ilosc_nog = 4, siersc = True, wasy = True):
        self.ilosc_nog = ilosc_nog
        self.siersc = siersc
        self.wasy = wasy

    def witaj(self):
        return 'Grrr'

class Czlowiek(Zwierze, Magister, Inzynier):
    def __init__(self, ilosc_nog = 2):
        self.ilosc_nog = ilosc_nog
    # def witaj(self):
    #     return 'Dzień dobry'
class Student(Czlowiek):
    pass
class Kot(Zwierze):
    pass
class Kaczka(Zwierze):
    pass
class Pies(Zwierze):
    pass
class Bokser(Pies):
    pass
class Jamnik(Pies):
    pass



zwierze = Zwierze()
print(zwierze.witaj())
czlowiek = Czlowiek()
print(czlowiek.witaj())
student = Student()
print(student.witaj())
bokser = Bokser()
print(bokser.ilosc_nog)
print(czlowiek.ilosc_nog)
print(czlowiek.witaj())
kot = Kot()
print(kot.siersc)
kaczka = Kaczka()


# -*- coding: utf-8 -*-

# Przepisanie dziennika z zajęć 7-9 na wersję obiektową.
# Proponuje zrobić klasę "Dziennik" a w atrybutach np trzymać handler do otwartego pliku (plik_dz), wpisy.
# Dzięki temu np gdy otworzymy plik w konstruktorze do będziemy mieli handler dostępny w każdej metodzie obiektu.
# Funkcja zapytaj() niech będzie poza klasą i steruje programem czyli wywoływaniem odpowiednich metod z obiektu.

from modul.wysylka import wyslij_emaila
from modul.tabela import wartosci_w_tabeli
import pickle
import datetime


class Dziennik():
    def __init__(self, plik_z_naszym_dziennikiem = 'dziennik.dz'):
        self.plik_dziennika = plik_z_naszym_dziennikiem
        self.plik_dz = self.otworz_dziennik()
        self.zawartosc_pliku = self.przeczytaj_plik()
        self.ilosc_wpisow = len(self.zawartosc_pliku)

    def __del__(self):
        self.plik_dz.close()

    @classmethod
    def Ala(cls):
        return cls('dziennik_ala.dz')

    @classmethod
    def Jan(cls):
        return cls('dziennik_jan.dz')


    def otworz_dziennik(self):
        """Funkcja otwiera plik dzinnika i zwraca handler do pliku w trybie zapis/odczyt
           :param self:
           :return:"""
        try:
            dziennik = open(self.plik_dziennika, 'rb+')
            return dziennik
        except FileNotFoundError:
            dziennik = open(self.plik_dziennika, 'wb+')
            return self.otworz_dziennik()


    def przeczytaj_plik(self):
        """Funckja z otwartego pliku czyta dane i zwraca je w postaci listy słowników
            :param self:
            :return lista słowników:
            """
        try:
            dane = pickle.load(self.plik_dz)
            return dane
        except:
            return []


    @staticmethod
    def poprawnosc_daty():
        """Funkcja sprawdza, czy podana przez użytkownika wartośc reprezentuje datę
            :param:
            :return: data"""
        try:
            data = input('Podaj datę w formacie RRRR-MM-DD: ')
            data = data.strip()
            datetime.datetime.strptime(data, '%Y-%m-%d')
            return data
        except ValueError:
            if not data:
                print('Nie podałeś daty. Data jest wymagana')
                return Dziennik.poprawnosc_daty()
            else:
                print('Podana wartość nie reprezentuje daty.')
                return Dziennik.poprawnosc_daty()

    def dodaj_wpis(self):
        """Funkcja pyta użytkownika o dane o podanie daty i treści nowego wpisu po czym dodaje go do aktualnej listy plików.
            Funkcja wymusza podanie poprawnej daty w formacie RRRR-MM-DD.
            :param self:
            :return:"""

        data = self.poprawnosc_daty()
        tresc = input('Podaj tresc: ')
        nowy_wpis = {'data': data, 'tresc': tresc}

        stare_wpisy = self.zawartosc_pliku
        nowe_wpisy = stare_wpisy

        try:
            nowe_wpisy.append(nowy_wpis)
        except:
            print('Nie było żadnego wpisu. Dodaj pierwszy wpis: ')
            nowe_wpisy = []
            nowe_wpisy.append(nowy_wpis)

        self.plik_dz.seek(0)
        pickle.dump(nowe_wpisy, self.plik_dz)
        print('Wpis został dodany prawidłowo.')

    def usun_wpis(self):
        """Funkcja usuwa wpis z dziennika na podstawie numeru podanego przez użytkownika
            a po usunięciu wysyła mail informacyjnego
            :param self:
            :return:
            """

        print('Ilość wpisów w dzienniczku to: {}'.format(self.ilosc_wpisow))
        wpis_do_usuniecia = int(input('Podaj wpis do usunięcia: '))

        if wpis_do_usuniecia <= self.ilosc_wpisow and wpis_do_usuniecia > 0:
            del (self.zawartosc_pliku[wpis_do_usuniecia - 1])
            indeks_do_usuniecia = wpis_do_usuniecia - 1
            self.plik_dz.seek(0)

            temat = 'Usunięto wpis'
            tresc = 'Usunięto wpis o indeksie: {}'.format(indeks_do_usuniecia)
            tresc = tresc + '\n  a dla użytkownika jest to wpis numerze: {}'.format(wpis_do_usuniecia)

            wyslij_emaila(temat, tresc)
            pickle.dump(self.zawartosc_pliku, self.plik_dz)
            print('Usunąłem wpis.')
        else:
            print('Nie ma takiego wpisu.')

    def wyszukaj_fraze(self):
        """Funkcja w otwartym dzienniku szuka wpisu, na podstawie wybranego klucza,
            zawierającego podaną przez użytkownika frazę.
            Wyświetla również podsumowanie wyszukiwania
            :param self:
            :return:"""

        pytanie = input('Jeśli chcesz wyszukać wpis na podstawie daty wpisz "data", '
                        'jeśli na podstawie treści wpisz "treść". '
                        '\nCo wybierasz?')
        pytanie = pytanie.strip(' ')
        pytanie = pytanie.lower()

        if pytanie == 'data':
            data = self.poprawnosc_daty()
            znaleziono_cos = False
            ilosc_wynikow = 0
            for wpis in self.zawartosc_pliku:
                if data in wpis['data']:
                    znaleziono_cos = True
                    ilosc_wynikow += 1
                    print('Data wyszukanego wpisu to: {}, a jego treść to: {}'.format(wpis['data'], wpis['tresc']))

            if ilosc_wynikow == 0:
                print('W całym dzienniku nie ma takiej frazy.')
            else:
                print('Ilość wpisów: {}'.format(ilosc_wynikow))
        elif pytanie == 'treść' or pytanie == 'tresc':
            fraza = input("Podaj wyszukiwaną frazę: ")
            fraza = fraza.strip(' ')
            znaleziono_cos = False
            ilosc_wynikow = 0
            for wpis in self.zawartosc_pliku:
                if fraza in wpis['tresc']:
                    znaleziono_cos = True
                    ilosc_wynikow += 1
                    print('Data wyszukanego wpisu to: {}, a jego treść to:'.format (wpis['data'], wpis['tresc']))

            if ilosc_wynikow == 0:
                print('W całym dzienniku nie ma takiej frazy.')
            else:
                print('Ilość wpisów: {}'.format(ilosc_wynikow))
        else:
            print('Wpisałeś niepoprawną wartość. Spróbuj jeszcze raz.')
            return self.wyszukaj_fraze()


def wyswietl_menu():
    """Funkcja wyświetla menu
        :return:"""
    print('Mój dziennik 1 \n'
            '1 Wyświetlanie: \n'
            '2 Dodaj: \n'
            '3 Usuń: \n'
            '4 Szukaj: \n'
            '5 Wyjdź: \n')


def zapytaj():
    """Funkcja do wywoływania zadań oczekiwanych przez użytkownika
        :return"""

    decyzja = input('Co wybierasz?')
    if decyzja == '1':
        print('Oto moje wpisy')
        wpisy = dziennik.zawartosc_pliku
        wartosci_w_tabeli(wpisy)
        # dziennik.zamknij_dziennik()
    if decyzja == '2':
        print('Dodawanie wpisu')
        dziennik.dodaj_wpis()
        # dziennik.zamknij_dziennik()
    if decyzja == '3':
        print('Usuwanie wpisu')
        dziennik.usun_wpis()
        # dziennik.zamknij_dziennik()
    if decyzja == '4':
        print('Wyszukaj')
        dziennik.wyszukaj_fraze()
        # dziennik.zamknij_dziennik()
    elif decyzja == '5':
        exit()


while True:
    wyswietl_menu()
    dziennik = Dziennik()
    zapytaj()
    del (dziennik)


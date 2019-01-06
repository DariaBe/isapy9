# -*- coding: utf-8 -*-

# Przepisanie dziennika z zajęć 7-9 na wersję obiektową.
# Proponuje zrobić klasę "Dziennik" a w atrybutach np trzymać handler do otwartego pliku (plik_dz), wpisy.
# Dzięki temu np gdy otworzymy plik w konstruktorze do będziemy mieli handler dostępny w każdej metodzie obiektu.
# Funkcja zapytaj() niech będzie poza klasą i steruje programem czyli wywoływaniem odpowiednich metod z obiektu.

from modul.wysylka import wyslij_emaila
from modul.tabela import wartosci_w_tabeli
import pickle
import datetime


def otworz_dziennik(plik_dziennika):
    """Funkcja otwiera plik dzinnika i zwraca handler do pliku w trybie zapis/odczyt
       :param plik_dziennika:
       :return:"""
    dziennik = open(plik_dziennika, 'rb+')
    return dziennik


plik_dziennika = 'dziennik.dz'


class Dziennik():
    def __init__(self):
        self.plik_dz = otworz_dziennik(plik_dziennika)
        self.zawartosc_pliku = self.przeczytaj_plik()
        self.ilosc_wpisow = len(self.zawartosc_pliku)

    def __len__(self):
        return self.zawartosc_pliku

    def przeczytaj_plik(self):
        """Funckja z otwartego pliku czyta dane i zwraca je w postaci listy słowników
            :param plik_dz:
            :return:
            """
        try:
            dane = pickle.load(self.plik_dz)
            return dane
        except:
            print('Błąd')

    def zamknij_dziennik(self):
        """Funkcja zamyka plik dzinnika
            :param plik_dz:
            :return:"""
        self.plik_dz.close()

    def poprawnosc_daty(self):
        try:
            data = input('Podaj datę w formacie RRRR-MM-DD: ')
            data = data.strip()
            datetime.datetime.strptime(data, '%Y-%m-%d')
            return data
        except ValueError:
            if not data:
                print('Nie podałeś daty. Data jest wymagana')
                return self.poprawnosc_daty()
            else:
                print('Podana wartość nie reprezentuje daty.')
                return self.poprawnosc_daty()

    def dodaj_wpis(self):
        """Funkcja pyta użytkownika o dane o podanie daty i treści nowego wpisu po czym dodaje go do aktualnej listy plików.
            Funkcja wymusza podanie poprawnej daty w formacie RRRR-MM-DD.
            :param plik_dz:
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
            :param plik_dz:
            :return:
            """
        wpisy = self.zawartosc_pliku
        ilosc_wpisow = self.ilosc_wpisow
        print('Ilość wpisów w dzienniczku to: {}'.format(ilosc_wpisow))
        wpis_do_usuniecia = int(input('Podaj wpis do usunięcia: '))

        if wpis_do_usuniecia <= ilosc_wpisow and wpis_do_usuniecia > 0:
            del (wpisy[wpis_do_usuniecia - 1])
            indeks_do_usuniecia = wpis_do_usuniecia - 1
            self.plik_dz.seek(0)

            temat = 'Usunięto wpis'
            tresc = 'Usunięto wpis o indeksie: {}'.format(indeks_do_usuniecia)
            tresc = tresc + '\n  a dla użytkownika jest to wpis numerze: {}'.format(wpis_do_usuniecia)

            wyslij_emaila(temat, tresc)
            pickle.dump(wpisy, self.plik_dz)
            print('Usunąłem wpis.')
        else:
            print('Nie ma takiego wpisu.')

    def wyszukaj_fraze(self):
        """Funkcja w otwartym dzienniku szuka wpisu, na podstawie wybranego klucza,
            zawierającego podaną przez użytkownika frazę.
            Wyświetla również podsumowanie wyszukiwania
            :param plik_dz:
            :return:"""

        pytanie = input('Jeśli chcesz wyszukać wpis na podstawie daty wpisz "data", '
                        'jeśli na podstawie treści wpisz "treść". '
                        '\nCo wybierasz?')
        pytanie = pytanie.strip(' ')
        pytanie = pytanie.lower()
        wpisy = self.zawartosc_pliku

        if pytanie == 'data':
            data = self.poprawnosc_daty()
            znaleziono_cos = False
            ilosc_wynikow = 0
            for wpis in wpisy:
                if data in wpis['data']:
                    znaleziono_cos = True
                    ilosc_wynikow += 1
                    print('Data wyszukanego wpisu to: {}, a jego treść to: {}'.format(wpis['data'], wpis['tresc']))

            if ilosc_wynikow == 0:
                print('W całym dzienniku nie ma takiej frazy.')
            else:
                print('Ilość wpisów: {}'.format(ilosc_wynikow))
        elif pytanie == 'treść' or pytanie == 'tresc':
            # wpisy = przeczytaj_plik(plik_dz)
            fraza = input("Podaj wyszukiwaną frazę: ")
            fraza = fraza.strip(' ')
            znaleziono_cos = False
            ilosc_wynikow = 0
            for wpis in wpisy:
                # if index, wpis in enumerate(wpisy):
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

    dziennik = Dziennik()

    decyzja = input('Co wybierasz?')
    if decyzja == '1':
        print('Oto moje wpisy')
        wpisy = dziennik.zawartosc_pliku
        wartosci_w_tabeli(wpisy)
        dziennik.zamknij_dziennik()
    if decyzja == '2':
        print('Dodawanie wpisu')
        # plik_dz = otworz_dziennik(plik_dziennika)
        dziennik.dodaj_wpis()
        dziennik.zamknij_dziennik()
    if decyzja == '3':
        print('Usuwanie wpisu')
        plik_dz = otworz_dziennik(plik_dziennika)
        dziennik.usun_wpis()
        dziennik.zamknij_dziennik()
    if decyzja == '4':
        print('Wyszukaj')
        plik_dz = otworz_dziennik(plik_dziennika)
        dziennik.wyszukaj_fraze()
        dziennik.zamknij_dziennik()
    elif decyzja == '5':
        exit()


while True:
    wyswietl_menu()
    zapytaj()


# import sys
# import os
#
#
# print(sys.path)
# print(os.getcwd())


from modul.wysylka import wyslij_emaila
import pickle
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
import pprint
import datetime


def otworz_dziennik(plik_dziennika):
    """Funkcja otwiera plik dzinnika i zwraca handler do pliku w trybie zapis/odczyt
       :param plik_dziennika:
       :return:"""
    dziennik = open(plik_dziennika, 'rb+')
    return dziennik


def zamknij_dziennik(plik_dz):
    """Funkcja zamyka plik dzinnika
        :param plik_dz:
        :return:"""
    plik_dz.close()


def dodaj_wpis(plik_dz):
    """Funkcja pyta użytkownika o dane o podanie daty i treści nowego wpisu po czym dodaje go do aktualnej listy plików.
        Funkcja wymusza podanie poprawnej daty w formacie RRRR-MM-DD.

        :param plik_dz:
        :return:"""

    try:
        data = input('Podaj datę: ')
        datetime.datetime.strptime(data, '%Y-%m-%d')
    except ValueError:
        print('Podana wartość nie reprezentuje daty. Podaj datę w formacie RRRR-MM-DD.')
        return dodaj_wpis(plik_dz)

    tresc = input('Podaj tresc: ')
    nowy_wpis = {'data': data, 'tresc': tresc}

    stare_wpisy = przeczytaj_plik(plik_dz)
    nowe_wpisy = stare_wpisy

    # lista = []
    # lista.append(stare_wpisy)
    # if stare_wpisy == None:
    #     nowe_wpisy = []
    try:
        nowe_wpisy.append(nowy_wpis)
    except:
        print('Nie było żadnego wpisu. Dodaj pierwszy wpis: ')
        nowe_wpisy = []
        nowe_wpisy.append(nowy_wpis)

    plik_dz.seek(0)
    pickle.dump(nowe_wpisy, plik_dz)
    print('Wpis został dodany prawidłowo.')

def usun_wpis(plik_dz):
    """Funkcja usuwa wpis z dziennika na podstawie numeru podanego przez użytkownika
        a po usunięciu wysyła mail informacyjnego
        :param plik_dz:
        :return:
        """
    wpisy = przeczytaj_plik(plik_dz)
    ilosc_wpisow = len(wpisy)
    print('Ilość wpisów w dzienniczku to: {}'.format(ilosc_wpisow))
    wpis_do_usuniecia = int(input('Podaj wpis do usunięcia: '))


    if wpis_do_usuniecia <= ilosc_wpisow and wpis_do_usuniecia > 0:
        del(wpisy[wpis_do_usuniecia-1])
        indeks_do_usuniecia = wpis_do_usuniecia - 1
        plik_dz.seek(0)

        temat = 'Daria'
        tresc = 'Usunięto wpis o indeksie: {}'.format(indeks_do_usuniecia)
        tresc = tresc + '\n  a dla użytkownika jest to wpis numerze: {}'.format(wpis_do_usuniecia)

        wyslij_emaila(temat, tresc)
        pickle.dump(wpisy, plik_dz)
        print('Usunąłem wpis.')
    else:
        print('Nie ma takiego wpisu.')


# def wyslij_emaila(temat, tresc):
#
#     mail = MIMEMultipart()
#     mail['Subject'] = temat
#     mail['To'] = 'isapy@o2.pl'
#     mail['From'] = 'isapy@int.pl'
#
#     body = MIMEText(tresc)
#     mail.attach(body)
#
#     serwer = smtplib.SMTP('poczta.int.pl')
#     serwer.login('isapy@int.pl', 'isapython;')
#     serwer.send_message(mail)
#     serwer.quit()
#
#     print('Wysłano email ')


def wyswietl_menu():
    """Funkcja wyświetla menu
        :return:"""
    print('Mój dziennik 1 \n'
          '1 Wyświetlanie: \n'
          '2 Dodaj: \n'
          '3 Usuń: \n'
          '4 Szukaj: \n'
          '5 Wyjdź: \n')


def przeczytaj_plik(plik_dz):
    """Funckja z otwartego pliku czyta dane i zwraca je w postaci listy słowników
        :param plik_dz:
        :return:
        """
    try:
        dane = pickle.load(plik_dz)
        return dane
    except:
        print('Błąd')


def wyszukaj_fraze(plik_dz):
    """Funkcja w otwartym dzienniku szuka wpisu zawierającego w tresc zadaną przez użytkownika frazę
        Wyświetla również podsumowanie wyszukiwania
        :param plik_dz:
        :return:"""
    wpisy = przeczytaj_plik(plik_dz)
    fraza = input("Podaj wyszukiwaną frazę: ")

    znaleziono_cos = False
    ilosc_wynikow = 0
    for wpis in wpisy:
    # if index, wpis in enumerate(wpisy):
        if fraza in wpis['tresc']:
            znaleziono_cos = True
            ilosc_wynikow += 1
            print(wpis['tresc'])

    if ilosc_wynikow == 0:
        print('W całym dzienniku nie ma takiej frazy.')
    else:
        print('Ilość wpisów: {}'. format(ilosc_wynikow))


def zapytaj():
    """Funkcja do wywoływania zadań oczekiwanych przez użytkownika
        :return"""
    decyzja = input('Co wybierasz?')
    if decyzja == '1':
        print('Oto moje wpisy')
        plik_dz = otworz_dziennik(plik_dziennika)
        wpisy = przeczytaj_plik(plik_dz)
        pprint.pprint(wpisy)
        zamknij_dziennik(plik_dz)
    if decyzja == '2':
        print('Dodawanie wpisu')
        plik_dz = otworz_dziennik(plik_dziennika)
        dodaj_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == '3':
        print('Usuwanie wpisu')
        plik_dz = otworz_dziennik(plik_dziennika)
        usun_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == '4':
        print('Wyszukaj')
        plik_dz = otworz_dziennik(plik_dziennika)
        wyszukaj_fraze(plik_dz)
        zamknij_dziennik(plik_dz)
    elif decyzja == '5':
        exit()


plik_dziennika = 'dziennik.dz'

while True:
    wyswietl_menu()
    zapytaj()

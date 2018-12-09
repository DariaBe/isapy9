decyzja = None
while(decyzja == None):
    decyzja = input('Witaj w Multitool Python Program by iSA \n' 
                    'Wybierz program który Cię interesuje:\n'
                    '1) Rysowanie prostokąta o zadanych parametrach \n'
                    '2) Obliczanie pola powierzchni koła \n'
                    '3) Przeliczanie C->F \n'
                    '4) Przeliczanie F->C \n'
                    '5) Zwacanie pierwszej i ostatniej cyfry zadanej liczby \n'
                    '6) Przeliczanie podanej liczby w systemie binarnym na system dziesiętny \n'
                    '7) Sprawdzanie czy podana liczba jest liczbą parzystą \n'
                    '8) Sprawdzanie czy podana liczba jest podzielna przez 3 lub 5 lub 7 \n'
                    '9) Sprawdzanie czy podana liczba jest podzielna przez 3 i 5 i 7 \n'
                    '10) Sprawdzenie czy podany rok jest rokiem przestępnym \n'
                    '11) Rysowanie piramidy o zadanej wysokości \n'
                    '12) Obliczanie wieku psa \n'
                    '13) Rozmienianie pieniędzy \n'
                    '14) Rysowanie tabeli \n'
                    'X) Wyjście z programu \n'
                    'Twój wybór: ')


    if decyzja == '1':
        def rysuj_prostokat():
            """Ta funkcja rysuje prostokąt o zadanych wymiarach za pomocą znaków"""
            szerokosc = input('Podaj szerokość prostokąta: ')
            szerokosc = szerokosc.strip(' ')
            wysokosc = input('Podaj wysokość prostokąta: ')
            wysokosc = wysokosc.strip(' ')
            if szerokosc.isnumeric() and wysokosc.isnumeric():
                szerokosc = int(szerokosc)
                wysokosc = int(wysokosc)
                print('+' + ("-" * szerokosc) + '+')
                print(('|' + (" " * szerokosc) + '|\n')*wysokosc, end='')
                print('+' + ("-" * szerokosc) + '+')
            else:
                print('Jedna lub obie z podanych wartości nie są liczbami całkowitymi. Spróbuj jeszcze raz.')
                return rysuj_prostokat()


        rysuj_prostokat()

    elif decyzja == '2':
        def pole_kola():
            """Ta funkcja oblicza polę powierzchni koła o zadanym promieniu"""
            r = input('Podaj długość promienia: ')
            r = r.strip(' ')
            try:
                r = float(r)
                print(r)
                print('pole koła = 3.14 * r**2')
                wzor = 3.14 * r**2
                print('Pole koła wynosi: {} cm2.'.format(round(float(wzor), 2)))
                return wzor
            except ValueError:
                print('Podana wartość nie jest liczbą. Spróbuj jezcze raz.')
                return pole_kola()


        pole_kola()

    elif decyzja == '3':
        def przeliczanie_temperatur_c_f():
            """Ta funkcja przelicza temperaturę w stopniach Celcjusza na temperaturę w stopniach Fahrenheita"""
            temp_c = input('Podaj temperaturę w stopniach Celcjusza: ')
            temp_c = temp_c.strip(' ')
            try:
                temp_c = float(temp_c)
                print('TempF = 32 + 9/5 * TempC')
                temp_f = 32 + 9/5 * temp_c
                print('Podana temperatura przeliczona na stopnie Fahrenheita wynosi: {} F.'. format(round(float(temp_f), 1)))
                return temp_f
            except ValueError:
                print('Podana wartość nie jest liczbą. Spróbuj jezcze raz.')
                return przeliczanie_temperatur_c_f


        przeliczanie_temperatur_c_f()

    elif decyzja == '4':
        def przeliczanie_temperatur_f_c():
            """Ta funkcja przelicza temperaturę w stopniach Fahrenheita na temperaturę w stopniach Celcjusza"""
            temp_f = input('Podaj temperaturę w stopniach Fahrenheita: ')
            temp_f = temp_f.strip(' ')
            try:
                temp_f = float(temp_f)
                print('TempC = 5/9 * (TempF - 32)')
                temp_c = 5 / 9 * (temp_f - 32)
                print('Podana temperatura przeliczona na stopnie Celcjusza wynosi: {} C.'.format(round(float(temp_c), 1)))
                return temp_c
            except ValueError:
                print('Podana wartość nie jest liczbą. Spróbuj jezcze raz.')
                return przeliczanie_temperatur_f_c


        przeliczanie_temperatur_f_c()

    elif decyzja == '5':
        def pierwsza_i_ostatnia():
            """Ta funkcja podaje pierwszą i ostatnią cyfrę zadanej liczby"""
            liczba = input('Podaj liczbę całkowitą: ')
            liczba = liczba.strip(' ')
            try:
                liczba = int(liczba)
                liczba = str(liczba)
                print('Pierwszą cyfrą liczby {} jest {}, a ostatnią {}.'. format(liczba, liczba[0], liczba[-1]))
            except ValueError:
                print('Podana wartość nie jest liczbą całkowitą. Spróbuj jezcze raz.')
                return pierwsza_i_ostatnia()


        pierwsza_i_ostatnia()

    elif decyzja == '6':
        def przeliczanie_liczby():
            """Ta funkcja przelicza liczbę zapisaną w formacie binarnym na system dziesiętny,
            przy założeniu że wpisywane jest zawsze tylko 6 znaków"""
            podana_liczba = input('Podaj liczbę w systemie binarnym składającą się z 6 znaków: ')
            podana_liczba = podana_liczba.strip(' ')
            try:
                liczba_1 = int(podana_liczba[0]) * 32
                liczba_2 = int(podana_liczba[1]) * 16
                liczba_3 = int(podana_liczba[2]) * 8
                liczba_4 = int(podana_liczba[3]) * 4
                liczba_5 = int(podana_liczba[4]) * 2
                liczba_6 = int(podana_liczba[5]) * 1
                liczba_dziesietna = liczba_1 + liczba_2 + liczba_3 + liczba_4 + liczba_5 + liczba_6
                print('Wartość podanej liczby przeliczonej na system dziesiętny to {}.'.format(liczba_dziesietna))
            except ValueError:
                print('Podana wartość nie jest liczbą w systemie binarnym. Spróbuj jezcze raz.')
                return przeliczanie_liczby()


        przeliczanie_liczby()

    elif decyzja == '7':
        def czy_parzysta():
            """Ta funkcja sprawdza czy podana liczba całkowita jest liczbą parzystą czy nieparzystą"""
            liczba = input('Podaj liczbę całkowitą: ')
            liczba = liczba.strip(' ')
            try:
                liczba = float(liczba)
                sprawdzenie = (liczba % 2)
                if sprawdzenie == 0:
                    print('Podana liczba jest liczbą parzystą.')
                else:
                    print('Podana liczba jest liczbą nieparzystą.')
            except ValueError:
                print('Podana wartość nie jest liczbą całkowitą. Spróbuj jezcze raz.')
                return czy_parzysta()


        czy_parzysta()

    elif decyzja == '8':
        def podzielna_3_5_lub_7():
            """Ta funkcja sprawdza czy podana liczba całkowita jest podzielna przez 3 lub 5 lub 7"""
            liczba = input('Podaj liczbę całkowitą: ')
            liczba = liczba.strip(' ')
            try:
                liczba = float(liczba)
                podzielna_przez_3 = liczba % 3
                podzielna_przez_5 = liczba % 5
                podzielna_przez_7 = liczba % 7
                if podzielna_przez_3 == 0 or podzielna_przez_5 == 0 or podzielna_przez_7 == 0:
                    print('Liczba jest podzielna przez 3 lub 5 lub 7.')
                else:
                    print('Liczba nie jest podzielna przez 3 lub 5 lub 7.')
            except ValueError:
                print('Podana wartość nie jest liczbą całkowitą. Spróbuj jezcze raz.')
                return podzielna_3_5_lub_7()


        podzielna_3_5_lub_7()

    elif decyzja == '9':
        def podzielna_3_5_i_7():
            """Ta funkcja sprawdza czy podana liczba całkowita jest podzielna przez 3 i 5 i 7"""
            liczba = input('Podaj liczbę całkowitą: ')
            liczba = liczba.strip(' ')
            try:
                liczba = float(liczba)
                podzielna_przez_3 = liczba % 3
                podzielna_przez_5 = liczba % 5
                podzielna_przez_7 = liczba % 7
                if podzielna_przez_3 == 0 and podzielna_przez_5 == 0 and podzielna_przez_7 == 0:
                    print('Liczba jest podzielna przez 3 i 5 i 7.')
                else:
                    print('liczba nie jest podzielna przez 3 i 5 i 7.')
            except ValueError:
                print('Podana wartość nie jest liczbą całkowitą. Spróbuj jezcze raz.')
                return podzielna_3_5_i_7()


        podzielna_3_5_i_7()

    elif decyzja == '10':
        def sprawdzenie_roku():
            """Ta funkcja sprawdza, czy podany rok jest rokiem przestępnym"""
            rok = input('Podaj rok: ')
            rok = rok.strip(' ')
            try:
                rok = int(rok)
                czy_przestepny = rok % 4
                if czy_przestepny == 0:
                    print('Podany rok jest rokiem przestępnym.')
                else:
                    print('Podany rok nie jest rokiem przestępnym.')
            except ValueError:
                print('Podana wartość nie jest rokiem. Spróbuj jezcze raz.')
                return sprawdzenie_roku()


        sprawdzenie_roku()

    elif decyzja == '11':
        def rysuj_piramide():
            """Ta funkcja rysuje piramidę z '#' o zadanej wysokości"""
            wysokosc = input('Podaj wysokość piramidy: ')
            wysokosc = wysokosc.strip(' ')
            if wysokosc.isnumeric():
                wysokosc = int(wysokosc)
                for i in range(1, wysokosc * 2, 2):
                    print(' ' * (wysokosc - 1) + '#' * i)
                    wysokosc = wysokosc - 1
            else:
                print('Podana wartość nie jest liczbą całkowitą. Spróbuj jeszcze raz.')
                return rysuj_piramide()


        rysuj_piramide()

    elif decyzja == '12':
        def przeliczanie_wieku_psa():
            """Ta funkcja wylicza wiek psa na podstawie poniższych danyhc:
            Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata"""
            wiek_psa = input('Podaj wiek psa: ')
            wiek_psa = wiek_psa.strip(' ')
            try:
                wiek_psa = float(wiek_psa)
                if wiek_psa <= 2 and wiek_psa > 0:
                    print(wiek_psa * 10.5)
                else:
                    print((wiek_psa - 2) * 4 + 21)
            except ValueError:
                print('Podana wartość nie jest wiekiem psa. Spróbuj jezcze raz.')
                return przeliczanie_wieku_psa()


        przeliczanie_wieku_psa()

    elif decyzja == '13':
        def rozmienić_na_monety():
            """Ta funkcja przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety:
            5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej"""
            kwota = input('Podaj kwotę, którą chcesz rozmienić na monety: ')
            kwota = kwota.strip(' ')
            try:
                kwota = float(kwota)
                monety = [5, 2, 1, 0.5, 0.2, 0.1]
                for i in monety:
                    if kwota // i > 0:
                        print('Otrzymasz {} monety {} złotowe'.format(kwota // i, i))
                        kwota = kwota - (kwota // i * i)
                        kwota = (round(kwota, 1))
                    else:
                        continue
            except ValueError:
                print('Podana wartość nie jest kwotą. Spróbuj jezcze raz.')
                return rozmienić_na_monety()


        rozmienić_na_monety()

    elif decyzja == '14':
        def rysowanie_tabeli(lista=[]):
            """Ta fukncja przyjmuje listę w parametrze i rysuje tabelę"""
            ilosc_kolumn = input('Podaj ciąg wartości, które mają pojawić się w tabeli: ')
            ilosc_kolumn = ilosc_kolumn.strip(' ')
            for i in ilosc_kolumn:
                lista.append('col' + i)
            ilosc_kolumn = len(lista)
            max_ilosc_liter = max(lista, key=len)
            max_ilosc_liter = len(max_ilosc_liter)
            print(('+' + '-' * (max_ilosc_liter + 2)) * ilosc_kolumn + '+')
            for i in lista:
                print(('| ' + i), end=' ')
            print('|')
            print(('+' + '-' * (max_ilosc_liter + 2)) * ilosc_kolumn + '+')


        rysowanie_tabeli()

    elif decyzja == 'X':
        pass


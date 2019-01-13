def wartosci_w_tabeli (wpisy):

    for indeks, wpis in enumerate(wpisy):
        print(('+' + '-' * 4 + '+' + '-' * 12 + '+' + '-' * 30 + '+'))
        numer = str(indeks + 1)
        dlugosc_tekstu = len(wpis['tresc'])
        if indeks < 9:
            print('| ' + numer + '. | ' + wpis['data'] + ' ' + '| ' + wpis['tresc'] + (29 - dlugosc_tekstu) * ' ' + '|')
        else:
            print('| ' + numer + '.| ' + wpis['data'] + ' ' + '| ' + wpis['tresc'] + (29 - dlugosc_tekstu) * ' ' + '|')

    print(('+' + '-' * 4 + '+' + '-' * 12 + '+' + '-' * 30 + '+'))





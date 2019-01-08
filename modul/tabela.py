def wartosci_w_tabeli (wpisy):

    for indeks, wpis in enumerate(wpisy):
        print(('+' + '-' * 4 + '+' + '-' * 12 + '+' + '-' * 30 + '+'))
        numer = str(indeks + 1)
        if indeks < 9:
            print('| ' + numer + '  | ' + wpis['data'] + ' ' + '| ' + wpis['tresc'])
        else:
            print('| ' + numer + ' | ' + wpis['data'] + ' ' + '| ' + wpis['tresc'])

    print(('+' + '-' * 4 + '+' + '-' * 12 + '+' + '-' * 30 + '+'))


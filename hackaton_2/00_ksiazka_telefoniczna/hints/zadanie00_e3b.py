import json


def wczytaj_nowy_wpis(lista):
    imie = input('Podaj imie: ')
    numer = input('Podaj numer: ')

    try:
        numer = int(numer)
    except ValueError:
        print('Podano niepoprawny numer.')
    else:
        wpis = {'imie': imie, 'numer': numer}
        lista.append(wpis)


def wczytaj_liste_wpisow():
    try:
        with open('ksiazka_numerow.json', mode='r') as plik:
            lista_numerow = json.load(plik)
            print(f'Wczytano {len(lista_numerow)} wpisów.')
            return lista_numerow
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    lista_numerow = wczytaj_liste_wpisow()
    wczytaj_nowy_wpis(lista_numerow)

    with open('ksiazka_numerow.json', mode='w') as plik:
        json.dump(lista_numerow, plik)

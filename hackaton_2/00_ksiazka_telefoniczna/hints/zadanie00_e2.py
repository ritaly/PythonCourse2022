import json


def wczytaj_nowy_wpis(lista):
    imie = input('Podaj imie: ')
    numer = int(input('Podaj numer: '))
    wpis = {'imie': imie, 'numer': numer}
    lista.append(wpis)


lista_numerow = []

wpis = {'imie': 'Jimi', 'numer': 1234}
lista_numerow.append(wpis)

wczytaj_nowy_wpis(lista_numerow)

with open('ksiazka_numerow.json', mode='w') as plik:
    json.dump(lista_numerow, plik)

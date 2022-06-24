import json

wpis = {'imie': 'Jimi', 'numer': 1234}

lista_numerow = []

lista_numerow.append(wpis)

with open('ksiazka_numerow.json', mode='w') as plik:
    json.dump(lista_numerow, plik)

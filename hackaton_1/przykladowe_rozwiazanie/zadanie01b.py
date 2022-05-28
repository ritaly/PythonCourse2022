def kupno(kwota, przedmiot, ekwipunek):
    print(f'Harcerz kupił {przedmiot} za {kwota}zł.')
    ekwipunek['pieniądze'] -= kwota
    ekwipunek['sprzęt'].append(przedmiot)


ekwipunek = {'pieniądze': 120.50,
             'sprzęt': ['kompas', 'latarka', 'śpiwór'],
             'prowiant': ['jabłko', 'woda', 'batonik', 'batonik']}

print(ekwipunek)

kupno(29.99, 'karimata', ekwipunek)

print(ekwipunek)

print('Harcerz zjadł batonik.')
ekwipunek['prowiant'].remove('batonik')

print(ekwipunek)
ile_rzeczy = len(ekwipunek['sprzęt']) + len(ekwipunek['prowiant'])
print(f'Harcerz ma {ile_rzeczy} przedmiotów w plecaku.')

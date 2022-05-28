ekwipunek = {'pieniądze': 120.50,
             'sprzęt': ['kompas', 'latarka', 'śpiwór'],
             'prowiant': ['jabłko', 'woda', 'batonik', 'batonik']}

print(ekwipunek)

print('Harcerz kupił karimatę za 29.99zł.')
ekwipunek['pieniądze'] -= 29.99
ekwipunek['sprzęt'].append('karimata')

print(ekwipunek)

print('Harcerz zjadł batonik.')
ekwipunek['prowiant'].remove('batonik')

print(ekwipunek)
ile_rzeczy = len(ekwipunek['sprzęt']) + len(ekwipunek['prowiant'])
print(f'Harcerz ma {ile_rzeczy} przedmiotów w plecaku.')

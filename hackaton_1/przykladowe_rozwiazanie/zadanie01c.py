def kupno(kwota, przedmiot, ekwipunek):
    if kwota >= ekwipunek['pieniądze']:
        print(f'Harcerza nie stać na {przedmiot} za {kwota}zł :(')
        return

    print(f'Harcerz kupił {przedmiot} za {kwota}zł.')
    ekwipunek['pieniądze'] -= kwota
    ekwipunek['sprzęt'].append(przedmiot)


ekwipunek = {'pieniądze': 120.50,
             'sprzęt': ['kompas', 'latarka', 'śpiwór'],
             'prowiant': ['jabłko', 'woda', 'batonik', 'batonik']}

print(ekwipunek)

kupno(29.99, 'karimata', ekwipunek)
kupno(6000, 'elektryczna hulajnoga', ekwipunek)

print(ekwipunek)

print('Harcerz zjadł batonik.')
ekwipunek['prowiant'].remove('batonik')

print(ekwipunek)
ile_przedmiotow = len(ekwipunek['sprzęt']) + len(ekwipunek['prowiant'])
print(f'Harcerz ma {ile_przedmiotow} przedmiotów w plecaku.')

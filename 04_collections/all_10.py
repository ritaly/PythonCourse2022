n = int(input('Podaj liczbę od 1 - 10 '))

dict_squares = {}
for v in range(1, n + 1):
    dict_squares[v] = v * v

print(dict_squares)
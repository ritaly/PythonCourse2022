n = int(input("Podaj liczbę od 1 do 10 -> "))
tab = [['_'] * n] * n

for row in tab:
    for i in row:
        print(i, end=' ')
    print()

for letter in "string":
    if letter == "i":
        break

    print(letter)

print("Koniec")

print('------------------')

for letter in "string":
    if letter == "i":
        continue

    print(letter, end='**')
    print('----')

print("Koniec")

print('-----------------')

while True:
    x = int(input('---> Podaj liczbę od 1 do 10'))

    if 1 <= x <= 10:
        break
    else:
        print('To nie jest liczba od 1 do 10')

print('Jestem poza pętlą WHILE ')

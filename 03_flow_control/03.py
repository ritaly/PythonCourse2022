txt = input('Podaj dowolny ciąg znaków -> ')

counter_num = 0
counter_up = 0
counter_low = 0

for l in txt:
    if l.isdigit():
        counter_num += 1
        continue

    if l.isupper():
        counter_up += 1
        continue

    if l.islower():
        counter_low += 1

print(f'Text: {txt}')
print("Cyfry", counter_num)
print("Duże litery", counter_up)
print("Małe litery", counter_low)
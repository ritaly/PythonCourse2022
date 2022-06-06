
def is_card(number):
    return number.isdigit() and 13 <= len(number) <= 16


def is_visa(number):
    return len(number) in [13, 16] and number[0] == '4'


def is_mastercard(number):
    if len(number) == 16 and (51 <= int(number[0:2]) <= 55 or int(number[0:4]) in range(2221, 2720 + 1)): # 2720 + 1 -> bo range (start do end = n+1)
        return True
    else:
        return False


def is_american_express(number):
    return len(number) == 15 and number.startswith(('34', '37'))


def main():
    while True:
        number = input('Podaj nr karty do sprawdzenia? -> ').replace(' ', '')
        if is_card(number):
            break
        else:
            print("To nie jest prawidłowy nr karty!")

    if is_visa(number):
        print("To jest Visa")
    elif is_mastercard(number):
        print("To jest master card")
    elif is_american_express(number):
        print('To jest American Express')
    else:
        print("Nie znany typ karty")


main()

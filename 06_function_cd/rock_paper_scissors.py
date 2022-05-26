import random

# wygrany: (przegrany)
WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES = ('k', 'p', 'n', 'j', 's')


def get_comp_choice():
    return random.choice(CORRECT_VALUES)


def get_user_choice():
    while True:
        user_choice = input('Podaj wartość k - kamień, p - papier , n - nożyce, s - Spock, j - jaszczurka: ')
        if user_choice in CORRECT_VALUES:
            break

    return user_choice


def show_result(comp, user):
    if user == comp:
        print('Remis')
    elif comp in WINNERS[user]:
        print('Wygrywa użytkownika')
    else:
        print('Wygrywa komputer')


def main():
    while True:
        print('**** GRA K-P-N ****')

        comp = get_comp_choice()
        user = get_user_choice()
        print(f'komputer {comp}, user {user}')
        show_result(comp, user)

        play_again = input("Czy zagrać ponownie? [T / N] -> ")
        if play_again.upper() == 'N':
            break

    print('Dzięki za grę!')

main()
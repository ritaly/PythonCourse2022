import random

def get_quote(filename):
    with open(f'{filename}.txt') as fopen:
        content = fopen.readlines()

    quote = random.choice(content)
    return quote


def show(quote):
    quote = quote.strip('\n')
    quote = quote.split(' - ') # [cytat, autor]
    lenth = len(quote[0]) + 20

    print('\nQuote of the day is:\n')
    print('*' * lenth)
    print(quote[0].center(lenth))
    print(f'~ {quote[1]} ~'.center(lenth))
    print('*' * lenth)


def main():
    filename = input("Your file name: ")
    quote = get_quote(filename)
    show(quote)

main()
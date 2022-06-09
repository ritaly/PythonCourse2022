text = "Abrakadabra"
magic = "hokus pokus"
letter = "Welcome to Hogward"

def find_longest_word(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def choice(words):
    return words[1]

def show(text):
    print('*' * 50)
    print(text.center(50))
    print('*' * 50)


def main():
    print(find_longest_word(['ala', 'ma', 'kota']))
    print('HELLO')


if __name__ == '__main__':
    main()
# Stwórz własną implementację stosu LIFO. Klasa stos (Stack)
# Wśród metod powinny się znaleźć takie jak:
#  - wyswietlenie stosu,
#  - dodanie elementu do stosu (push),
#  - wyjęcie elementu ze stosu (get).
# Utwórz kilka obiektów klasy Stos z różnymi parametrami.


class Stack: # Last in first out
    def __init__(self, lifo=[]):
        self.lifo = lifo

    def show(self):
        print('Stack -->', self.lifo)

    def push(self, item):
        self.lifo.append(item)

    def get(self):
        return self.lifo.pop(-1)

def main():
    q = Stack([3, 2, 7, 9, 'txt'])
    q.show()
    q.push('rita')
    q.show()
    x = q.get()
    print('wyjęto -->', x)
    q.show()
    x = q.get()
    print('wyjęto -->', x)
    q.show()

if __name__ == '__main__':
    main()

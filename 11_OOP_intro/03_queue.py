# Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak:
#  - wyswietlenie kolejki,
#  - sprawdzenie czy jest pusta,
#  - dodanie elementu do kolejki (put),
#  - wyjęcie elementu z kolejki (get).
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.


class Queue: # Fifo first in - first out
    def __init__(self, fifo=[]):
        self.fifo = fifo

    def show(self):
        print('Queue -->', self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, item):
        self.fifo.append(item)

    def get(self):
        return self.fifo.pop(0)

def main():
    q = Queue([3, 2, 7, 9, 'txt'])
    q.show()
    print(q.is_empty())
    q.put('rita')
    q.show()
    x = q.get()
    print('wyjęto -->', x)
    q.show()

if __name__ == '__main__':
    main()

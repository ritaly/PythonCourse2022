## Zadanie na rozgrzewkę:
Zadanie opisane jest w oddzielnym pliku: zadanie_01.md

## Propozycje zadań warsztatowych:

### Wisielec:
Program, będący implementacją gry "wisielec".
- Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
- Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
- Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
- W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.

### Książka adresowa:
Program przechowujący danę kontaktowe znajomych/klientów.
- Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
    - Wyświetlenie wszystkich wpisów
    - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
    - Usunięcie wpisu
    - Zakończenie pracy programu
- Program powinien na starcie mieć już wprowadzone kilka wpisów.

### Generator imienia dla Wojownika RPG:
- Konieczność użycia modułu `random`.
- Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
- Pomysł jest zainspirowany grą: http://progressquest.com/play/roster.html
- Imię musi zaczynać się od wielkiej litery.
- Program można kontynuować używając pomysłu poniżej.

### Historyjka a'la RPG:
- Konieczność użycia modułu `random`.
- Program wypisuje kolejne "przygody" bohatera.
- Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami, np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."
- Historyjka ma mieć zadaną długość i ma być możliwie losowa.

### Wojna karciana:
- Zasady: https://pl.wikipedia.org/wiki/Wojna_(gra_karciana)
- Konieczność użycia modułu `random`.
- Program rozdaje karty i drukuje informacje o przebiegu rozgrywki
- Pomysły na uproszczenie gry:
    - zamiast implementować talię kart, używamy liczb (0, 1, 2 ... 9, 10, 11) dla (2, 3, 4, ... Q, K, A)
    - aby gra kończyła się wcześniej, rozdajemy tylko 10 kart
    - dwa tryby: zdobyte karty dochodzą do "ręki", lub są odkładane i nie wykorzystywane

### Quiz
- Stwórz grę, która zawiera pytania z wiedzy ogólnej (Trivial pursuit)
- Konieczność użycia modułu `random`.
  

### Kółko i krzyżyk:
Program będący implementacją gry w "kółko i krzyżyk" dla dwóch graczy.
Wpisz w google "tic tac toe game" i zagraj z google.
- Zacznij od zaprojektowania rozgrywki
- Możliwość nazwania graczy inaczej niż X / O
- Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
    - Konieczność użycia modułu `random`.

Przykładowo rozgrywka mogłaby wyglądać tak:


       1   2   3
    A  . | . | .
    B  . | . | .
    C  . | . | .

    Player X, mark position: A1

       1   2   3
    A  X | . | .
    B  . | . | .
    C  . | . | .

    Player O, mark position: B2

       1   2   3
    A  X | . | .
    B  . | O | .
    C  . | . | .

    Player X, mark position: B1

    ...

       1   2   3
    A  X | O | X
    B  X | O | X
    C  O | X | O

    Draw!

    Would you like to continue? [yes/no]:

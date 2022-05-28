# Zadanie 01
Napisz program, który będzie zarządzał ekwipunkiem harcerza.

1. Program rozpoczyna się od zdefiniowania słownika `ekwipunek`. Słownik ten:
    - posiada klucz `pieniądze`, który przechowuje wartość typu `float`
    - posiada klucz `sprzęt`, który przechowuje listę przedmiotów. Każdy przedmiot jest typu `str`.
    - posiada klucz `prowiant`, który przechowuje listę jadalnych rzeczy.
    - przykład:

```python
ekwipunek = {'pieniądze': 120.50,
             'sprzęt': ['kompas', 'latarka', 'śpiwór'],
             'prowiant': ['jabłko', 'woda', 'batonik', 'batonik']}

```

2. Program ma wypisać cały ekwipunek na ekran (bez formatowania)

3. Harcerz kupił karimatę za 29.99zł. Wyświetl poprzednie zdanie na ekranie. Odejmij tę kwotę od jego pieniędzy i dodaj karimatę do listy przedmiotów. Ponownie wypisz ekwipunek po zmianach.

4. Harcerz zjadł batonik. Wyświetl to zdanie na ekranie a następnie usuń batonik z listy prowiantu. Ponownie wypisz ekwipunek po zmianach. Lista ma wbudowaną metodę `remove()`, która jako parametr przyjmuje wartość elementu do usunięcia (a nie indeks!). Użyj tej metody.

5. Program ma wypisać ile rzeczy (prowiant + przedmioty) Harcerz ma w plecaku. Komunikat może brzmieć: "Harcerz ma 7 przedmiotów w plecaku.

# Rozszerzenie:
Napisz funkcję `kupno()`, która będzie przyjmowała trzy parametry: `kwota`, `przedmiot`, `ekwipunek`. Funkcja nie będzie zwracała żadnej wartości.
- Funkcja ta ma wyświetlić na ekranie komunikat "Harcerz kupił (przedmiot) za kwotę (kwota) zł".
- Funkcja ma odjąć z ekwipunku odpowiednią kwotę i dodać przedmiot.
- Dodaj w programie jeszcze jedną rzecz, którą harcerz kupi.

# Rozszerzenie 2:
Dodaj do napisanej powyżej funkcji sprawdzanie, czy Harcerz ma pieniądze na zakup. Jeśli nie, wyświetl na ekranie stosowny komunikat i nie wprowadzaj żadnych zmian w ekwipunku. Aby zakończyć wykonywanie funkcji użyj wyrażenia `return` bez żadnej wartości do zwrócenia.

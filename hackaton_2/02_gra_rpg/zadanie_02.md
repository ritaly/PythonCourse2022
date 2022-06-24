# Zadanie 02 - gra RPG

Przypomnij sobie zadanie z pierwszego hackatonu

> Historyjka a'la RPG:
> - Konieczność użycia modułu `random`.
> - Program wypisuje kolejne "przygody" bohatera.
> - Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami, np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Vohenal V Waleczny poszedł do tawerny aby zasnąć."
> - Historyjka ma mieć zadaną długość i ma być możliwie losowa.

Jeżeli zadanie zostało zrobione na hackatonie 1, można wykorzystać jego kod.

Przygody bohatera opisuj po angielsku, by uniknąć problemów leksykalnych.

1. Gracz powinen mieć ekwipunek, z którego można wyciągać i dodawać elementy.
2. Gracz powinen móc sterować swoim bohaterem zamiast losować zdania.
3. Postęp gracza powien zależeć od jego wyborów oraz czynników losowych
4. Gracz ma zmienny poziom energii
5. Stwórz conajmniej jeden moduł.
6. Stwórz obsłuż conajmniej jeden Wyjątek.

Przykład, którym można się zainspirować, a nawet "pożyczyć" kolejność zdarzeń:
https://spyze.pl/Rayneven/

- Implementacja gry dowolna. Przykładowa propozycja etapów impementacji poniżej.

- Zastosuj wyrażenie `if __name__ == '__main__'` do odzielenia wykonywanego kodu od definicji funkcji.


### Etap 1:
Stwórz - bohatera:
- Użytkownik może podać płeć wojownika, rasę oraz imię lub je wylosować z listy.
- Generator imion bohatera powinen brać pod uwagę płeć bohatera oraz rasę i zwracać wygenerowane imię zgodnie z założoną konwencją.
- Generator imion powinen znajdować sie w oddzielnym module.
- Bohater powinen mieć dostępny ekwipunek oraz 10 stopniowy poziom energii. Sposób implamentacji dobierz na podstawie całości.

### Etap 2:
Wewnątrz skryptu stwórz funkcję, która wyświetlać menu główne.
- W menu użytkownik może:
    - wybrać nową grę,
    - kontynuować grę,
    - natychmiastowo zakończyć program
     
(ponieważ część funkcji nie będzie jeszcze zaimplementowana np. zapis - można użyć instrukcji ``pass``).


### Etap 3: 
Stwórz logikę poruszania się po grze.
- Przygody bohatera powinny odbywać w sposób bardziej kontrollowany 
- Bohater powinen móc odwiedzić conajmniej 5 różnych lokalizacji, w których będzie mógł odbyć różne akcje i od nich będzie zależała rozgrywka
- Osobna funkcja powinna być odpowiedzialna za budowanie zdań

Bohater wybiera z menu opcję podróży do miasta lub lasu - wybór: miasto.

Opowieść o bohaterze:

> "Vohenal V Waleczny wyruszył do miasta aby odpocząć od nadmiaru przygód."

Dalszy wybór użytkownika.

> "Dotarłeś do miasta. Gdzie się teraz udasz: 1 / 2"

W mieście nasz bohater wybiera dalszą drogę - wejść do tawerny czy odwiedzić handlarza - wybór: tawerna.

> "Vohenal V Waleczny wszedł do tawerny"

Wylosuj dalszą przygodę użytkownika np.

> "W tawernie trwała bójki. Vohenal V Waleczny dobył miecza, ale został raniony. Traci 2 punktów życia".

> "W tawernie trwały obchody urodzin króla. Jouxdrien bierze w nich udział, wykorzystuje darmowy posiłek, +2 punkty energii"


### Etap 4:

Stwórz rodzaj ekwipunku, który bohater ma lub, który może zakupić i w jakiej cenie.

> "Vohenal V Waleczny kupił od handlarza topór, o sile rażenia 50 - zapłacił 30 złotych monet"

- Ekwipunek może być słownikiem zawierającym jedzenie, pieniądze i sprzęt. 
    - Pieniądze będą wartością liczbową. 
    - Jedzenie i sprzęt powinny zawierać słowniki `produkt: wartość`
        - jeżeli w ekwipunku znajduje się ciasto to dostarcza +1 punkt energii
        - jeżeli w ekwipunku znajduje się miecz to ma on siłę rażenia 15, topór siła rażenia 50.
- Oczywiście inny sposób zdefiniowania ekwipunku wchodzi w grę np. lista zawierająca krotki 2 elementowe etc.

Ekwipunek i akcje ekwipunku mogą być osobnym modułem.

### Etap 5: 

Weź pod uwagę, że niektóre zasoby bohatera są zużywalne.
- Uwzględnij energię traconą na np. podróże, przygody. Stwórz funkcje usuwającą energię.
- Jedzenie powinno być usuwane po wykorzystaniu. Stwórz funkcję usuwającą element z ekwipunku
- Pamiętaj dodać sposób na odzyskanie energii - jedzenie albo sen (sen doładowuje dowolny poziom energii do max). Stwórz funkcję dodającą energię z pożywienia oraz funkcję snu.

> "Po 4 godzinach w lesie bohater poczuł się głodny. Zjadł batonika"

### Rozszerzenie

Po każdej akcji wyświetl poziom energii gracza. np.

[ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ] 100%

[ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ] 30%

Dzięki temu gracz nie zapomni uzupełniać energii.


### Etap 6:

Pozwól graczowi umrzeć. 
- Bohater, który nie będzie jadł i spał wyczerpuje energię. Poziom 0 oznacza koniec gry.
- Dodaj inny sposób uśmiercenia bohatera. 
    - Przykładowo: ratowanie ksieżniczki, walka ze smokiem. Wygrana lub zwycięstwo powinny być losowane.
    

### Rozszerzenia

#### Dodaj kolorów
Skorzystaj z modułów `import color` albo `import colorama`. Pokoloruj output przygód bohatera
- np. wysoki stan baterii na zielono, niski na czerwono
- jedzenie będzie miało inny kolor niż pieniądze czy broń

#### Dodaj elementy wizualne
Dodaj elementy walki wizualnej np. jeśli gracz spotka w lesie groźnego węża możemy go narysować w konsoli

```python
snake = """

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/


"""
```


a gdy gracz pokona węża:

```python
snake = """

 
                         ____
                      >---   \\
   ____________         \ x x /
-=:___________/          ¯¯¯¯¯


"""
```

*To jest odcięta głowa, można narysować ładniej lub znaleźć gotowiec jako ascii art.*

#### Odczyt i zapis
Dodaj do menu możliwość zapisu gry i odczytu z pliku.

Opracuj sposób zapisu gry. Może być to przykładowo:
- stan wszystkich zasobów gracza oraz jego imię plik `imie_bohatera_resources.json`
- wszystkie dotychczasowe zdania przygód gracza `imie_gracza_story.txt`

Znając format zapisu dodaj odczyt. Pamiętaj obsłużyć potencjalne błędy.


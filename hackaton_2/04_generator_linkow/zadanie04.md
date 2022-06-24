# Zadanie 04 - generator linków

Zapoznaj się z dokumentacją przykładowego [programu parterskiego](https://program-partnerski.helion.pl/dokumentacjapp.pdf).

### Etap 1
Stwórz skrypt, w którym obierzesz od klienta:
- numer id klienta - to kod numeryczny, pięciocyfrowy np. 90412
- link do produktu

### Rozszerzenie

Zapoznaj się z wyrażeniami regularnymi, by przetestować czy podany input jest linkiem

### Etap 2
Napisz funkcję, która pobiera od użytkownika lub sama rozpoznaje jakiego typu został podany url.

URL jakie obsługuje funkcja:
- strona główna
- strona produktu
- strona promocji
- dodanie zestawu do koszyka
- link do kategorii
-  ...

### Etap 3

Użytkowników może wielokrotnie dodać link do przekształcenia w link dedykowany.

### Etap 4

Użytkownik może zapisać wszystkie do tej pory zrobione linki do pliku `txt` lub `csv`

### Rozszerzenia
- Użytkownik podaje plik `.txt` lub `.csv` z listą książek. Każda książka znajduje sięw nowym wierszu.
- Otrzymuje plik wynikowy z listą dedykowanych linków.
- Zmodyfikuj program tak, by w pliku wynikowym pierwsza kolumna zawierała link oryginalny, druga `-`, a trzecia link dedykowany.
- Kod powinen analogicznie działać dla innych domen grupy helion np. ebookpoint czy videopoint.

W razie problemów ze zrozumieniem zajrzyj do pliku `test.txt` w folderze hints.


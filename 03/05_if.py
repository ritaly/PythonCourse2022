# Stwórz zmienną password.
# Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 małą literę,
# 1 dużą literę
# i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Podaj hasło -> ")

if len(password) < 8:
    print("Hasło jest za krótkie, powinno zawierać conajmniej 8 znaków")

if password.isalnum() and (password.isdigit() or password.isalpha()):
    print('Hasło powinno zawierać cyfry i litery')

if password.isalnum() and password.islower():
    print('Hasło zawiera tylko małe litery, powinno zawierać conajmniej 1 dużą literę')

if password.isalnum() and password.isupper():
    print('Hasło zawiera tylko duże litery, powinno zawierać conajmniej 1 małą literę')




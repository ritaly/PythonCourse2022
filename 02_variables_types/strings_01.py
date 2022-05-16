# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

word = 'dlugieslowo'
# print(word[5])
# len(word)
# len(word)/2
# len(word)//2

mid_id = len(word)//2
prev_id = mid_id -1
next_id = mid_id + 1

new_word1 = word[prev_id] + word[mid_id] + word[next_id]

# word[prev_id:next_id] -> 'ie'
new_word2 = word[prev_id:next_id+1]

print(new_word1)
print(new_word2)



def add_book(books):
    title = input('Podaj książke: ')
    grade = input(f'Oceń książkę {title}')
    books.append((title, grade))


def get_book(books):
    counter = len(books)
    while True:
        index = int(input('Podaj nr książki -> '))
        # if index > counter or index <= -counter:
        #     print('Nie mamy tylu książek na liście')
        # else:
        #     break
        if 0 < index <= counter:
            print('Mamy to!')
            break
        else:
            print('Nie mamy takiej książki na liście')
            print('--- spróbuj jeszcze raz ---')

    index -= 1
    print(books[index])

# ---
# books = [('LOTR', '10'), ('HP', '9 '), ('TypeScript', '6'), ('BAM', '7'), ('powieść', '8')]
books = []
num = int( input('Ile książek chcesz dodać? ') )
for _ in range(num):
    add_book(books)
print(books)

get_book(books)



# def add_books_dict(books_dict):
#     title = input('Podaj książke: ')
#     grade = input(f'Oceń książkę {title}')
#     books_dict[title] = grade
#
# my_books = {
#     "LOTR": 9
# }
# add_books_dict(my_books)
# print(my_books)
#
# books_list = []
# for k, v in my_books.items():
#     books_list.append([k, v])
#
# print(books_list)




# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024
page = 100
book_strings = 50
symbols = 24
one_symbol = 4
book_weight = page * book_strings * symbols * one_symbol
count_books = round(disk_size / book_weight)
print("Количество книг, помещающихся на дискету:", count_books)

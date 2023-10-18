# TODO Найдите количество книг, которое можно разместить на дискете
FLOPPY_VOLUME_MB = 1.44
PAGES_BOOK = 100
LINES_PAGE = 50
SYMBOLS_LINES = 25
S_WEIGHT_BYTES = 4
floppy_volume_bytes = FLOPPY_VOLUME_MB * 1024**2
symbols_in_the_book = PAGES_BOOK * LINES_PAGE * SYMBOLS_LINES
volume_book = symbols_in_the_book * S_WEIGHT_BYTES
amount_books = int(floppy_volume_bytes // volume_book)
print("Количество книг, помещающихся на дискету:", amount_books)

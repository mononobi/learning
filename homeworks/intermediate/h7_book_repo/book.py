
class Book:
    def __init__(self, original_title, isbn, book_type, genre, classification, cover_image, edition, pages, publisher):
        # validate input data: isbn and classification may have algorithm, pages must be int,
        self.original_title = original_title.title()
        self.isbn = isbn
        self.type = book_type
        self.genre = genre
        self.classification = classification
        self.cover_image = cover_image
        self.edition = edition
        self.pages = pages
        self.publisher = publisher

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if len(value) == 13:
            self._isbn = value
        else:
            raise Exception('Bad ISBN format.')



book1 = Book('122', '1234567891011', 'book', 'fiction', '1.1.1', 'a.jpg', '1st', '152', 'Cheshmeh')
print(book1.isbn)



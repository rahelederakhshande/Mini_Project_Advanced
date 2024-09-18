class Book:
    def __init__(self, id_, title, author, isbn):
        self.id_ = id_
        self.title = title
        self.author = author
        self.__isbn = isbn

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, new_isbn):
        self.__isbn = new_isbn
        if new_isbn is not None and isinstance(new_isbn, str):
            self.__isbn = new_isbn
        else:
            raise ValueError("invalid")
        
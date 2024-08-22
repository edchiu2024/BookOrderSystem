from author import Author

class Book:

    def __init__(self, title, author, price):

        self.title=title
        self.author=author
        self.price=price

    def get_info(self):
        return f"Book title:{self.title}, author name: {self.author.name}, price: {self.price}"


class PhysicalBook(Book):
    def __init__(self, title, author, price, weight):
        super().__init__(title, author, price)
        self.weight=weight

    def get_info(self):
        return f"{super().get_info()}, weight: {self.weight}"
    

class eBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size=file_size

    def get_info(self):
        return f"{super().get_info()}, file size is {self.file_size}"
    

class AudioBook(Book):
    def __init__(self, title, author, price, duration):
        super().__init__(title, author, price)
        self.duration=duration

    def get_info(self):
        return f"{super().get_info()}, duration is {self.duration}"    
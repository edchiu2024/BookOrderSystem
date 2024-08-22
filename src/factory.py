from book import PhysicalBook, eBook, AudioBook
from author import Author  


class BookFactory:
    @staticmethod
    def create_book(book_type, title, author_name, price, **kwargs):

        author = Author(author_name, kwargs.get('biography', ''))
        print(f"Inside create_book: Type: {book_type}, Title: {title}, Author: {author}, Price: {price}, Extra: {kwargs}")

        if book_type == "PhysicalBook":
            return PhysicalBook(title, author, price, kwargs.get('weight'))
        elif book_type=='eBook':
            return eBook(title, author, price, kwargs.get('file_size'))
        elif book_type=='AudioBook':
            return AudioBook(title, author, price, kwargs.get('duration'))
        else:
            raise ValueError(f"Unknown book type: {book_type}")



#test cases

'''if __name__=="__main__":
    from author import Author

    author = Author("George Orwell", "British writer and journalist")
    factory= BookFactory()

    physical_book = factory.create_book("PhysicalBook", "1984", author, 6.99, weight=0.5)
    print(physical_book.get_info())


    book2 = factory.create_book("eBook", "Animal Farm", author, 5.99, file_size=2)
    print(book2.get_info())

    book3 = factory.create_book("AudioBook", "Harry Potter and the Sorcerer's Stone", author, 9.99, duration=8)
    print(book3.get_info())
'''

from book import Book


class Bookstore:
    def __init__(self):
        self.books=[]


    def add_book(self, book):
        self.books.append(book)


    def search_books_by_title(self, title):

        matching_books=[]
        for book in self.books:
            if title.lower() in book.title.lower():
                matching_books.append(book)
        return matching_books
    
    def search_books_by_author(self, author_name):

        matching_books=[]
        for book in self.books:
            if author_name.lower() in book.author.name.lower():
                matching_books.append(book)
        return matching_books
    

    def list_books(self):
        book_info_list=[]
        for book in self.books:
            book_info_list.append(book.get_info())
        return book_info_list
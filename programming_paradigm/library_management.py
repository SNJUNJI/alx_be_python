class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        :param title: The title of the book (str)
        :param author: The author of the book (str)
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """
        Check out the book if available.
        
        :return: True if successfully checked out, False otherwise
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """
        Return the book, making it available again.
        
        :return: True if successfully returned, False if it wasn't checked out
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """
        Check if the book is available.
        
        :return: True if available, False if checked out
        """
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        :param book: A Book instance to add
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title if available.
        
        :param title: The title of the book (str)
        :return: True if successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False  # Book not found or already checked out
    
    def return_book(self, title):
        """
        Return a book by title.
        
        :param title: The title of the book (str)
        :return: True if successfully returned, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False  # Book not found or not checked out
    
    def list_available_books(self):
        """
        List all available books in the library, indented for display.
        """
        for book in self._books:
            if book.is_available():
                print(f"   {book.title} by {book.author}")
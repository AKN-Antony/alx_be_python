# Library System Implementation (Combined)
# Demonstrating Inheritance and Composition

class Book:
    """Base class representing a book"""
    def __init__(self, title, author):
        """Initialize book with title and author"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of the book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book"""
    def __init__(self, title, author, file_size):
        """Initialize ebook with additional file_size attribute"""
        super().__init__(title, author)
        self.file_size = file_size  # in KB
    
    def __str__(self):
        """String representation of the ebook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical book"""
    def __init__(self, title, author, page_count):
        """Initialize print book with additional page_count attribute"""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of the print book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books"""
    def __init__(self):
        """Initialize library with empty books list"""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library's collection"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Can only add Book objects to the library")
    
    def list_books(self):
        """Print details of all books in the library"""
        if not self.books:
            print("The library has no books yet")
            return
        
        for book in self.books:
            print(book)


def main():
    """Demonstrate the library system functionality"""
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    main()
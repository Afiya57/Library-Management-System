class library:
  def __init__(self):
    self.no_of_books = 0
    self.books = []
    
  def add_book(self, book):
    self.books.append(book)
    self.no_of_books = len(self.books)
    
  def show_info(self):
    print(f"The library has {self.no_of_books} books. The books are:")
    for book in self.books:
      print(book)


l1 = library()
l1.add_book("Harry Potter")
l1.add_book("Forty Rules of Love")
l1.add_book("To kill a mockingbird")
l1.add_book("1984")
l1.add_book("The Great Gatsby")
l1.add_book("Pride and Prejudice")
l1.add_book("The Catcher in the Rye")
l1.add_book("The lord of the rings")
l1.add_book("The chronicles of narnia")
l1.add_book("The hobbit")
l1.show_info()
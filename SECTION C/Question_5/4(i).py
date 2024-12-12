class python:
    def __init__(self):
      self.book = []

    def add_book(self, title, author, pages):
       self.book.append({'title': title, 'author': author, 'pages': pages})

       

    def is_available(self, title):
        for book in self.book:
            if book['title'] == title:
                return book['available']
        return False

    def borrow_book(self, title):
        for book in self.book:
            if book['title'] == title and book['available']:
                book['available'] = False
                return f"You've borrowed {title}."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self.book:
            if book['title'] == title:
                book['available'] = True
                return f"You've returned {title}."
        return f"{title} not found in the library."

python = python()
python.add_book("1984", "George Orwell","100")
print(python.borrow_book("1984"))
print(python.is_available("1984"))
python.return_book("1984")




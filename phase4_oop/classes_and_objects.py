class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        print(f"{self.title} was written by {self.author}")

book1 = Book("Shatterproof Bond", "Charan")
book1.get_details()
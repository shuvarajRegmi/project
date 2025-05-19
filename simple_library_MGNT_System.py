class library:
    def __init__(self):
        self.nbooks=0
        self.book=[]
        
    def addbook(self,book):
        self.book.append(book)
        self.nbooks=len(self.book)
        
    def show_info(self):
        print(f"The library has {self.nbooks} books. The books are")
        for book in self.book:
            print(book)

li=library()
li.addbook("Harry Potter")
li.addbook("English")
li.addbook("Math II")
li.addbook("MCA")
li.addbook("C")
li.addbook("Account")
li.show_info()
        
        
        
        
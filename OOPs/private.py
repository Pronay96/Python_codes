class Book:
    # Private variables
    __book_name = None
    __book_price = None
    __author_name = None

    def __init__(self, name, price, author):
        self.__book_name = name
        self.__book_price = price
        self.__author_name = author

    # Constructing the private variables
    # Getter
    def get_book_name(self):
        return self.__book_name

    # Setter
    # def set_book_name(self, nm):
    #     self.__book_name = nm

    # Getter
    def get_book_price(self):
        return self.__book_price

    # Setter
    def set_book_price(self, new_price):
        self.__book_price = new_price

    # Getter
    def get_author_name(self):
        return self.__author_name

    # Setter
    # def set_author_name(self,auth):
    #     self.__author_name = auth


name = input("Enter the book name: ")
price = float(input("Enter the price: "))
author = input("Enter the author's name: ")
print("\n")

book_obj = Book(name,price,author)

print("Book details before price renewal:")
print(f"Book Name: {book_obj.get_book_name()}")
print(f"Book price: {book_obj.get_book_price()}")
print(f"Author Name: {book_obj.get_author_name()}")

print("\n")
new_price = float(input("Enter the new price: "))
print("\n")

book_obj.set_book_price(new_price)

print("Book details after price renewal:")
print(f"Book Name: {book_obj.get_book_name()}")
print(f"Book price: {book_obj.get_book_price()}")
print(f"Author Name: {book_obj.get_author_name()}")
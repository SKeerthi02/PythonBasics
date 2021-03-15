from abc import ABC, abstractmethod
from enum import Enum

import self as self

"""
Enums and constants
"""


class BookStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOANED = 3
    LOST = 4


class AccountStatus(Enum):
    ACTIVE, CLOSED, BLACKLISTED, CANCELLED, NONE = 1, 2, 3, 4, 5


class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIOBOOK, EBOOK, NEWSPAPER, JOURNAL = 1, 2, 3, 4, 5, 6


class ReservationStatus(Enum):
    WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4


class Constants:

    self.MAX_BOOKS = 5
    self.MAX_DAYS = 10


"""
Address of the library and person details
"""
class Address:
    def __init__(self, street, city, state, zipcode, country):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country


class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone


"""
Account class defining an interface
"""


class Account(ABC):
    def __init__(self, id_, password, person, status):
        self.__id = id_
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        pass


"""
extends account class
"""


class Librarian(Account):
    def __init__(self, id_, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_book_items(self, book_item):
        pass

    def block_member(self, member_id):
        pass

    def un_block(self, member_id):
        pass

    def issue_card(self, name, phone, email):
        pass


class Member(Account):
    def __init__(self, id_, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id_, password, person, status)

    def get_total_books(self, member_id):
        pass

    def reserve_book(self, book_id, member_id):
        pass

    def increment_book(self, member_id):
        pass

    def checkout_book(self, book_id, member_id):
        if self.get_total_books(member_id) >= Constants.MAX_BOOKS:
            return False

    def check_fine(self, member_id):
        if Fine.fine_applicable(member_id):
            return Fine.caluclate(member_id)
        return 0

    def return_book(self, member_id, book_id):
        amount = self.check_fine(member_id)
        BookItem.status = BookStatus.AVAILABLE

    def renew_book(self, member_id, book_id):
        pass



class BookReservation:
    def __init__(self, date, barcode, member_id):
        self.__date = date
        self.__barcode = barcode
        self.__member_id = member_id

    def fetch_reservation_details(self):
        pass


class BookLending:
    def __init__(self, member_id, book_id, status, date, deu_date):
        self.__member_id = member_id
        self.__book_id = book_id
        self.__status = status
        self.__creation_date = date
        self.__deu_date = deu_date

    def lend_book(self, book_id, barcode):
        self.__book_id = book_id
        self.__barcode = barcode

    def get_lending_details(self, barcode):
        pass

class Fine:

    def __init__(self, book_id, data):
        self.__book_id = book_id
        self.__date = data

    def fine_applicable(self, barcode):
        pass

    def caluclate(self, barcode):
        pass


class Book:
    def __init__(self, book_id, title, published, isbn, author):
        self.__book_id = book_id
        self.__title = title
        self.__published = published
        self.__ISBN = isbn
        self.__author = author


class BookItem(Book):
    def __init__(self, book_id, title, published, isbn, author, barcode, status, placed_at):
        super().__init__(book_id, title, published, isbn, author)
        self.__barcode = barcode
        self.status = status
        self.__placed_at = placed_at

    def checkout(self, member_id):
        pass


class Rack:
    def __init__(self, book_id, place):
        self.book_id = book_id
        self.place = place

    def get_place(self, book_id):
        pass


class Search(ABC):

    def search_by_title(self, title):
        pass

    def search_by_author(self, authorname):
        pass

    def search_by_published_date(self, date):
        pass


class Catalog(Search):
    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date

    def search_by_author(self, authorname):
        pass

    def search_by_published_date(self, date):
        pass

    def search_by_title(self, title):
        pass


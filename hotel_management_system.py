from enum import Enum
from abc import ABC, abstractmethod

class RoomStyle(Enum):
    STANDARD = 1
    DELUXE = 2
    FAMILY_SUITE = 3
    BUSINESS_SUITE = 4

class RoomStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    OCCUPIED = 3
    OTHER = 4


class BookingStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CHECKED_IN = 4
    CHECKED_OUT = 5
    CANCELLED = 6


class AccountType(Enum):
    MEMBER = 1
    GUEST = 2
    MANAGER = 3
    RECEPTIONIST = 4

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    BLOCKED = 3

class PaymentType(Enum):

    UNPAID = 1
    PAID = 2
    PENDING = 3
    REFUNDED = 4


class Address:
    def __init__(self, name, street, city, state, zipcode, country):
        self.__name = name
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__country = country


class Account:
    def __init__(self, id_, password, status=AccountStatus.ACTIVE):
        self.__id = id_
        self.__password = password
        self.status = status

    def change_password(self, new_password):
        pass


class Person(ABC):
    def __init__(self, name, email, phone, account):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__account = account


class Guest(Person):
    def __init__(self, name, email, phone, account):
        super().__init__(name, email, phone, account)
        self._total_rooms = 0

    def book_rooms(self, room_id):
        pass

    def get_booking(self, email):
        pass


class Receptionist(Person):

    def __init__(self, name, email, phone, account):
        super().__init__(name, email, phone, account)

    def search_bookings(self, booking_id):
        pass

    def search_members(self, email):
        pass

    def create_booking(self, details):
        pass


class Server(Person):
    def __init__(self, name, email, phone, account):
        super().__init__(name, email, phone, account)

    def serve_room(self, room_number):
        pass

class Hotel:
    def __init__(self, name,):
        self.__name = name
        self.__locations = []


class HotelLocation:
    def __init__(self, address, branch_id):
        self.__branch_id = branch_id
        self.__location = address

    def get_rooms(self):
        pass

class Room:

    def __init__(self, room_number, room_style, status, price, is_smoking):
        self.__room_number = room_number
        self.__style = room_style
        self.__status = status
        self.__booking_price = price
        self.__is_smoking = is_smoking

    def is_room_availble(self):
        pass

    def check_in(self):
        pass

    def check_out(self):
        pass

    def search(self):
        pass


class RoomHouseKeeping:

    def __init__(self, description, duration, house_keeper):
        self.__description = description
        self.__duration = duration
        self.__house_keeper = house_keeper

    def add_house_keeping(self, room):
        pass

class RoomBooking:
    def __init__(self, reservation_number, start_date, end_date, booking_status):
        self.__reservation_number = reservation_number
        self.__start_date = start_date
        self.__end_date = end_date
        self.__booking_status = booking_status

        self.checkin = None
        self.checkout = None
        self.__guest_id = 0
        self.__room = None
        self.__invoice = None

    def fetch_details(self, reservation_numer):


class RoomCharge(ABC):
    def __init__(self):
        bill = 0

    def add_invoice(self, invoice):
        pass

class Amenity(RoomCharge):
    def __init__(self, bill):
        bill = 0
    def add_invoice(self, invoice):
        pass

class RoomService(RoomCharge):
    def __init__(self, bill):

    def add_invoice(self, invoice):
        pass


class KitchedService(RoomCharge):
    def __init__(self, bill):

    def add_invoice(self, invoice):
        pass





class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library({self.city}, {self.street}, "
            f"{self.zip_code}, {self.open_hours}, {self.phone})"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee({self.first_name} {self.last_name}, phone: {self.phone})"


class Student:
    def __init__(self, first_name, last_name, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Student({self.first_name} {self.last_name})"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = pages

    def __str__(self):
        return (
            f"Book({self.author_name} {self.author_surname}, "
            f"{self.publication_date}, {self.library.city})"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        titles = ", ".join(str(b) for b in self.books)
        return (
            f"Order({self.order_date}, employee={self.employee}, "
            f"student={self.student}, books=[{titles}])"
        )

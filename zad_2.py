class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library({self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone})"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
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
    def __init__(self, first_name, last_name, birth_date,
                 city, street, zip_code, phone):
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
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library          # obiekt Library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book({self.author_name} {self.author_surname}, {self.publication_date}, {self.library.city})"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee        # obiekt Employee
        self.student = student          # obiekt Student
        self.books = books              # lista Book
        self.order_date = order_date

    def __str__(self):
        books_titles = ", ".join(str(b) for b in self.books)
        return (f"Order({self.order_date}, employee={self.employee}, "
                f"student={self.student}, books=[{books_titles}])")


# Biblioteki
lib1 = Library("Kraków", "Długa 10", "31-000", "8:00-18:00", "123-456-789")
lib2 = Library("Warszawa", "Prosta 5", "00-001", "9:00-20:00", "987-654-321")

# Pracownicy
emp1 = Employee("Anna", "Nowak", "2020-01-01", "1990-05-10",
                "Kraków", "Długa 10", "31-000", "111-111-111")
emp2 = Employee("Jan", "Kowalski", "2019-03-15", "1985-02-20",
                "Warszawa", "Prosta 5", "00-001", "222-222-222")
emp3 = Employee("Ewa", "Wiśniewska", "2021-07-01", "1992-09-30",
                "Kraków", "Krótka 3", "31-002", "333-333-333")

# Studenci
st1 = Student("Piotr", "Lis", "2000-01-01", "Kraków", "Lea 1", "30-001", "444-444-444")
st2 = Student("Maria", "Zając", "1999-04-12", "Warszawa", "Ogrodowa 2", "00-002", "555-555-555")
st3 = Student("Kasia", "Bąk", "2001-09-09", "Kraków", "Miodowa 7", "31-003", "666-666-666")

# Książki
b1 = Book(lib1, "2010", "Adam", "Mickiewicz", 300)
b2 = Book(lib1, "2015", "Henryk", "Sienkiewicz", 400)
b3 = Book(lib2, "2020", "Olga", "Tokarczuk", 250)
b4 = Book(lib2, "2018", "J.K.", "Rowling", 500)
b5 = Book(lib1, "2005", "Stanisław", "Lem", 350)

# Zamówienia
order1 = Order(emp1, st1, [b1, b2, b5], "2025-01-10")
order2 = Order(emp2, st3, [b3, b4], "2025-01-11")

print(order1)
print(order2)

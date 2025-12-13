from library_app.models import Library, Employee, Student, Book, Order

lib1 = Library("Kraków", "Długa 10", "31-000", "8:00-18:00", "123-456-789")
lib2 = Library("Warszawa", "Prosta 5", "00-001", "9:00-20:00", "987-654-321")

emp1 = Employee("Anna", "Nowak", "2020-01-01", "1990-05-10",
                "Kraków", "Długa 10", "31-000", "111-111-111")
emp2 = Employee("Jan", "Kowalski", "2019-03-15", "1985-02-20",
                "Warszawa", "Prosta 5", "00-001", "222-222-222")
emp3 = Employee("Ewa", "Wiśniewska", "2021-07-01", "1992-09-30",
                "Kraków", "Krótka 3", "31-002", "333-333-333")

st1 = Student("Piotr", "Lis", "2000-01-01", "Kraków", "Lea 1", "30-001", "444-444-444")
st2 = Student("Maria", "Zając", "1999-04-12", "Warszawa", "Ogrodowa 2",
              "00-002", "555-555-555")
st3 = Student("Kasia", "Bąk", "2001-09-09", "Kraków", "Miodowa 7",
              "31-003", "666-666-666")

b1 = Book(lib1, "2010", "Adam", "Mickiewicz", 300)
b2 = Book(lib1, "2015", "Henryk", "Sienkiewicz", 400)
b3 = Book(lib2, "2020", "Olga", "Tokarczuk", 250)
b4 = Book(lib2, "2018", "J.K.", "Rowling", 500)
b5 = Book(lib1, "2005", "Stanisław", "Lem", 350)

order1 = Order(emp1, st1, [b1, b2, b5], "2025-01-10")
order2 = Order(emp2, st3, [b3, b4], "2025-01-11")

ORDERS = [order1, order2]

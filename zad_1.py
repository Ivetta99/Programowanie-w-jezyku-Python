class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        return avg > 50


student1 = Student("Ola", [93, 71, 58])
student2 = Student("Jan", [21, 45, 19])

print(student1.is_passed())
print(student2.is_passed())

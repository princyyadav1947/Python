# 1: Student Management System
print("1: Student Management System")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        self.display_details()
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


student1 = Student("Khushi", 19, 101, "AIPA")

student1.display_student()

# --------------------------------------------------------------------------------------------------------
# 2: Bank Account System (Single Inheritance)
print("2: Bank Account System (Single Inheritance)")
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited Amount:", amount)


class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest:", interest)

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")


account1 = SavingAccount(12345, 10000, 5)

account1.deposit(2000)
account1.display()
account1.calculate_interest()

# ------------------------------------------------------------------------------------------------------

# 3: Family Assets (Multilevel Inheritance)
print("3: Family Assets (Multilevel Inheritance)")
class Grandfather:
    def house(self):
        print("Grandfather has a house")


class Father(Grandfather):
    def bike(self):
        print("Father has a bike")


class Son(Father):
    def laptop(self):
        print("Son has a laptop")


s1 = Son()

s1.house()
s1.bike()
s1.laptop()

#------------------------------------------------------------------------------------------------------

# 4: Employee Hierarchy (Multilevel Inheritance)
print("4: Employee Hierarchy (Multilevel Inheritance)")
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_salary(self):
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        self.get_name()
        self.get_salary()
        print("Team Size:", self.team_size)


m1 = Manager("Khushi", 30000, 5)

m1.display()

# ---------------------------------------------------------------------------------------------------
# 5: College Management (Hierarchical Inheritance)
print("5: College Management (Hierarchical Inheritance)")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display_student(self):
        self.display_person()
        print("Marks:", self.marks)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print("Subject:", self.subject)


s1 = Student("Khushi", 18, 85)
t1 = Teacher("Ramesh", 35, "Python")

print("Student Details:")
s1.display_student()

print("Teacher Details:")
t1.display_teacher()
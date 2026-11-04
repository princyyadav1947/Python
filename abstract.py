# from abc import ABC,abstractmethod

# class Payment(ABC): 

#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CreditCard(Payment):

#     def pay(self,amount):
#         print("Paid", amount, "using Credit Card")

# class Cash(Payment):

#     def pay(self,amount):
#         print("Paid",amount,"using Cash")

# class UPI(Payment):

#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# p1 = CreditCard()
# p2 = Cash()
# p3 = UPI()

# p1.pay(500)
# p2.pay(800)
# p3.pay(1000)


# from abc import ABC,abstractmethod

# class Vehicle(ABC):

#       @abstractmethod
#       def drive(self):
#             pass

# class Bike(Vehicle):

#       def drive(self):
#             print("Bike is moving")

# class Car(Vehicle):

#       def drive(self):
#             print("Car is moving")

# class Bus(Vehicle):

#       def drive(self):
#             print("Bus is moving")

# bike = Bike()
# car = Car()
# bus = Bus()

# car.drive()
# bike.drive()
# bus.drive()


#Exercise 2: Bank Account

# from abc import ABC,abstractmethod

# class BankAccount(ABC):

#     @abstractmethod
#     def deposit(self, amount):
#         pass

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

# class SavingsAccount(BankAccount):

#     def deposit(self, amount):
#         print("Deposited in Savings Account:", amount)

#     def withdraw(self, amount):
#         print("Withdrawn from Savings Account:", amount)

# class CurrentAccount(BankAccount):

#     def deposit(self, amount):
#         print("Deposited in current account:", amount)

#     def withdraw(self, amount):
#         print("Withdrawn from Current account:", amount) 

# s1 = SavingsAccount()
# c1 = CurrentAccount() 

# print("Savings Account:")
# s1.deposit(2000)
# s1.withdraw(1000)
# print("Remaining Balance:")

# print("\nCurrent Account:")
# c1. deposit(3000)
# c1.withdraw(2000)
# print("Remaining Balance:")


#Exercise 3: Notification System

# from abc import ABC,abstractmethod

# class Notification(ABC):

#     @abstractmethod
#     def send_Notification(self):
#         pass

# class EmailNotification(Notification) :
#     def send_Notification(self):
#         print("Sending Email Notification")

# class SMSNotification(Notification):
#     def send_Notification(self):
#         print("Sending SMS Notification")

# class WhatsAppNotification(Notification):
#     def send_Notification(self):
#         print("Sending WhatsApp Notification")


# e = EmailNotification()
# e.send_Notification()

# s = SMSNotification()
# s.send_Notification()

# w = WhatsAppNotification()
# w.send_Notification()


#Exercise 4: Institute Management

# from abc import ABC,abstractmethod

# class Person(ABC):

#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

#     @abstractmethod
#     def display_details(self):
#         pass

# class Student(Person):
#     def __init__(self, name, age, course):
#         super()._init_(name, age)
#         self.course = course

#     def display_details(self):
#         print("\n Student Details")
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course",self.course)

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super()._init_(name,age)
#         self.subject = subject

#     def display_details(self):
#         print("\n Teacher Details")
#         print("Name:",self.name)
#         print("Age:", self.age)
#         print("Subject:", self.subject)

# class Principal(Person):
#     def __init__(self, name, age, experience):
#         super()._init_(name,age)
#         self.experience = experience

#     def display_details(self):
#         print("\n Principal Details")
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Experience",self.experience, "years")

# s1 = Student("Princy", 17, "AIPA")
# t1 = Teacher("Ankit Yadav", 28, "Computer Science")
# p1 = Principal("Anita Sharma", 45, 20)

# s1.display_details()
# t1.display_details()
# p1.display_details()


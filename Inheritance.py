#1. Single Inheritance

class Animal():

    def property(self):
        print("Animal has 4 legs")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

d=Dog()

d.property()
d.bark()


# Multiple inheritance

class Father():

    def skill1(self):
        print("Driving")

class Mother():

    def skill2(self):
                print("Cooking")

class Child(Father, Mother):

    def Qualities(self):
        print("Inherited skills from parents:")

x=Child
x.Qualities()
x.skill1()
x.skill2()


# multilevel inheritance

class Grandfather:
    def house(self):
        print("Grandfather's House")


class Father(Grandfather):
    def bike(self):
        print("Father's Bike")


class Son(Grandfather):
    def laptop(self):
        print("Son's Laptop")


class Grandson(Father, Son):
    def car(self):
        print("Grandson's Car")


# Son object
s = Son()
s.house()
s.laptop()

# Grandson object
g = Grandson()
g.house()
g.bike()
g.laptop()
g.car() 


#Hierarchical  inheritance

class Institute():

    def name(self):
        print("NSTIW Allahabad")

class Teacher(Institute):
            pass 

class Student(Institute):
            pass 

class Housekeeping(Institute):
            pass

t=Teacher()
s=Student()
h=Housekeeping()

s.name()
t.name()
h.name()

# Parent Class
class Hospital:

    def hospital_name(self):
        print("City Care Hospital")

    def location(self):
        print("Prayagraj, Uttar Pradesh")


# Child Class 1
class Doctor(Hospital):

    def doctor_details(self):
        print("Name: Dr. Rahul")
        print("Department: Cardiology")


# Child Class 2
class Nurse(Hospital):

    def nurse_details(self):
        print("Name: Priya")
        print("Department: Emergency")


# Child Class 3
class Receptionist(Hospital):

    def receptionist_details(self):
        print("Name: Anjali")
        print("Department: Reception")


# Creating Objects
d = Doctor()
n = Nurse()
r = Receptionist()


# Calling Methods
print("Doctor Details:")
d.hospital_name()
d.location()
d.doctor_details()

print("\nNurse Details:")
n.hospital_name()
n.location()
n.nurse_details()

print("\nReceptionist Details:")
r.hospital_name()
r.location()
r.receptionist_details()
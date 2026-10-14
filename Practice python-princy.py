# Rectangle pattern
# for i in range(4):
#     for j in range(6):
#         print("*", end=" ")
#     print()

#Increasing triangle

# for i in range(1, 8):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#Number square

# for i in range(4):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print()

#Multiplication tables(1 to 10)

# for i in range(1, 11):
#     print("Table of", i)

#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

    # print()

#Classroom seating(5 Rows x 8 Seats)

# for row in range(1, 6):
#     for seat in range(1, 9):
#         print("R" + str(row) + "S" + str(seat), end=" ")  #R means Row, S means Seat
#     print()

#Prime numbers(2 to 50)

# for num in range(2, 51):
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

    # if is_prime:
    #     print(num, end=" ")

#7. Pattern challenge
#Print a centered pyramid using stars:

# rows = 5

# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")

#     for k in range(2 * i - 1):
#         print("*", end="")

#     print()


#NEW PRACTICE
# 1. Greeting function

def greet():
    print("Welcome to Python")

greet()

def greeting(name):
    print("Welcome,", name)

student_name = input("Enter student name: ")
greeting(student_name)


#2. Addition function

def add(a,b):
    return a+b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
answer =add(num1, num2)
print("Sum:", answer)

 
#3. Even or odd

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter an integer: "))
answer = even_odd(num)

print("Number is:", answer)


#4. Factorial calculator

def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    return fact

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    answer = factorial(num)
    print("Factorial:", answer)


#5. Largest of three numbers

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

answer = largest(num1, num2, num3)
print("Largest number:", answer)

#6. Grade calculator

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

marks = float(input("Enter marks (0-100): "))
grade = calculate_grade(marks)

print("Grade:", grade)


#7. List statistics

def calculate_total(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_minimum(numbers):
    return min(numbers)

def find_maximum(numbers):
    return max(numbers)

numbers = [10, 20, 30, 40, 50]

print("Total:", calculate_total(numbers))
print("Average:", calculate_average(numbers))
print("Minimum:", find_minimum(numbers))
print("Maximum:", find_maximum(numbers))


#8. Banking application

balance = 1000

def deposit(amount):
    global balance

    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Enter a valid amount.")

def withdraw(amount):
    global balance

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")

def display_balance():
    print("Current balance:", balance)

while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        display_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")


#9. Student record processor

students = [
    {"name": "Princy", "marks": [80, 75, 90]},
    {"name": "Raj", "marks": [35, 40, 30]},
    {"name": "Nancy", "marks": [60, 70, 65]},
    {"name": "Ayushi", "marks": [90, 85, 95]}
]

def calculate_average(marks):
    return sum(marks) / len(marks)

def is_passing(marks):
    average = calculate_average(marks)
    return average >= 40

def display_students(student_list):
    for student in student_list:
        average = calculate_average(student["marks"])

        if is_passing(student["marks"]):
            status = "Pass"
        else:
            status = "Fail"

        print("Name:", student["name"])
        print("Average:", average)
        print("Status:", status)
        print("------------------")

def passing_students(student_list):
    result = []

    for student in student_list:
        if is_passing(student["marks"]):
            result.append(student["name"])

    return result

display_students(students)

print("Passing students:", passing_students(students))
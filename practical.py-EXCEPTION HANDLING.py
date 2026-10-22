# Practical 1: Safe Division Calculator

# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     result = num1 / num2
#     print("Result:", result)

# except ValueError:
#     print("Error: Please enter valid numbers.")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

#Practical 2: Positive Number Validator

# try:
#     number = float(input("Enter a number: "))

#     if number < 0:
#         raise ValueError("Negative numbers are not allowed.")

#     print("Valid number:", number)

# except ValueError as e:
#     print("Error:", e)

#Practical 3: List Index Handling

# numbers = [10, 20, 30, 40, 50]

# print("List:", numbers)

# try:
#     index = int(input("Enter an index (0-4): "))
#     print("Value:", numbers[index])

# except ValueError:
#     print("Error: Please enter an integer.")

# except IndexError:
#     print("Error: Index is out of range.")

#Practical 4: Dictionary Lookup

# student = {
#     "name": "Princy",
#     "trade": "AIPA",
#     "marks": 85
# }

# key = input("Enter a key (name, trade, marks): ")

# try:
#     print("Value:", student[key])

# except KeyError:
#     print("Error: Key not found in dictionary.")


#Practical 5: File Reading

# filename = input("Enter filename: ")

# try:
#     with open(filename, "r", encoding="utf-8") as file:
#         content = file.read()
#         print("\nFile Content:")
#         print(content)

# except FileNotFoundError:
#     print("Error: File not found.")

# except PermissionError:
#     print("Error: Permission denied.")

#Practical 6: Integer Input Validation

# while True:
#     try:
#         number = int(input("Enter an integer: "))
#         print("Valid integer:", number)
#         break

#     except ValueError:
#         print("Invalid input! Please enter an integer.")

# print("Program completed.")

#Practical 7: Custom Exception

# class InsufficientBalanceError(Exception):
#     pass

# balance = 5000

# try:
#     print("Available Balance:", balance)
#     amount = float(input("Enter withdrawal amount: "))

#     if amount <= 0:
#         raise ValueError("Withdrawal amount must be positive.")

#     if amount > balance:
#         raise InsufficientBalanceError(
#             "Insufficient balance! Withdrawal not allowed."
#         )

#     balance = balance - amount

#     print("Withdrawal successful!")
#     print("Remaining Balance:", balance)

# except ValueError as e:
#     print("Invalid input:", e)

# except InsufficientBalanceError as e:
#     print("Transaction failed:", e)


#Practical 8: Employee Salary Validation

# try:
#     salary = float(input("Enter employee salary: "))

#     if salary < 0:
#         raise ValueError("Salary cannot be negative.")

#     print("Valid salary:", salary)

# except ValueError as e:
#     print("Invalid salary:", e)
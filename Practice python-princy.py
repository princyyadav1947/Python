# Rectangle pattern
for i in range(4):
    for j in range(6):
        print("*", end=" ")
    print()

#Increasing triangle

for i in range(1, 8):
    for j in range(i):
        print("*", end=" ")
    print()

#Number square

for i in range(4):
    for j in range(1, 5):
        print(j, end=" ")
    print()

#Multiplication tables(1 to 10)

for i in range(1, 11):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()

#Classroom seating(5 Rows x 8 Seats)

for row in range(1, 6):
    for seat in range(1, 9):
        print("R" + str(row) + "S" + str(seat), end=" ")  #R means Row, S means Seat
    print()

#Prime numbers(2 to 50)

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

#7. Pattern challenge
#Print a centered pyramid using stars:

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
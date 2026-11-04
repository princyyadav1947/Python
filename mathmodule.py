# from abc import ABC, abstractmethod
# import math

# # Abstract Class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass


# # Circle Class
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius


# # Rectangle Class
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# # Square Class
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side


# # Creating Objects
# c = Circle(5)
# r = Rectangle(10, 4)
# s = Square(6)

# # Display Areas
# print("Area of Circle =", round(c.area(), 2))
# print("Area of Rectangle =", r.area())
# print("Area of Square =", s.area())
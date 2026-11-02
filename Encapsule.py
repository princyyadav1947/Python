class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary


    def get_salary(self):
        return self.__salary
    
    def inc__salary(self,amount):
        if amount >0:
            self.__salary += amount
            print("Salary updated")
        else:
            print("Invalid amount")

emp= Employee("Princy",25,50000)
print("Salary:", emp.get_salary())

emp.inc__salary(8000)
print("New Balance: ,emp.get_salary()")


class Employee:

    def __init__(self, emp_id, name, department, salary):

        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.__salary = salary 

    def display_details(self):

            print("Employee ID:", self.emp_id)
            print("Employee Name:", self.name) 
            print("Department:", self.department)
            print("Salary:", self.__salary)

    def get_salary(self):

         return self.__salary


    def update_salary(self,new_salary):

     if new_salary > 0:
         self.__salary = new_salary
         print("Salary updated successfully!")
     else:
         print("Invalid salary amount!")

    emp1 = Employee(101, "Princy", "IT", 30000)

    print("__Employee Details")
    emp1. display_details()

    print("\n---Updating salary---")
    emp1.update_salary(35000)

    print("Updated Salary:", emp1.get_salary())


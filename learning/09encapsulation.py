# 31. What is encapsulation?
#
# Hiding internal data via naming convention:
#
# _var (protected)
#
# __var (name-mangled/private)


# 3. Private members
# Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data.
#
# In Python, private members are defined with a double underscore prefix (e.g., self.__salary). Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) to prevent direct access.
#
# Example: This example shows how a private attribute (__salary) is accessed within the class using a public method, demonstrating that private members cannot be accessed directly from outside the class.


class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Fedrick", 50000)
print(emp.name)

#print(emp.__salary) # private variable . accessing this way will result into error

# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\09encapsulation.py", line 17, in <module>
#     print(emp.__salary)
#           ^^^^^^^^^^^^
# AttributeError: 'Employee' object has no attribute '__salary'
# Fedrick


print(emp.show_salary()) #Salary: 50000

class Demo:

    def __init__(self, name, age,branch="IT"):
        if name is None:
            print("Name cannot be None")
        if name not in ["Sumit","John"]:
            print("Name must be 'Sumit,John'")

        if age is None:
            raise ValueError("Age cannot be None")

        self.name = name
        self.age = age
        self.branch = branch

    def __str__(self):
        return f"{self.name} {self.age} {self.branch}"




d=Demo("John", 18) #
print(d)#John 18 IT

d1=Demo(None    , 18) #Name cannot be None
print(d1)

d2=Demo("Sumit"    , None)
print(d2)
#   File "D:\Resurrection 2025\Python2025\learning\09classobjectnotinitialized.py", line 9, in __init__
#     raise ValueError("Age cannot be None")
# ValueError: Age cannot be None



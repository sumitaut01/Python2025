class demo():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
     return self.a + self.b

# kind of tostring()
    def __str__(self):
        return f"{self.a} and {self.b} has been provided"

d=demo(2,3)
print(d) #2 and 3 has been provided

del d # deleting from emory
print(d)
#
# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\22SpecialDunder.py", line 18, in <module>
#     print(d)
#           ^
# NameError: name 'd' is not defined. Did you mean: 'id'?
# 85. Explain property decorator.
# Turns methods into read-only attributes.

class Circle:
    def __init__(self,radius,r):
        self.radius = radius
        self._r=r
    @property
    def area(self): return 3.14*self._r**2

    @property #Getter
    def radius(self):
     return self._radius

    @radius.setter #Setter
    def radius(self,radius):
        if radius==0:
            raise ValueError("Radius cannot be less than zero")
        self._radius=radius


c=Circle(1,2)
print(c.radius) #

c1=Circle(0,2)

#   File "D:\Resurrection 2025\Python2025\learning\57propertydecorators.py", line 26, in <module>
#     c1=Circle(0,2)
#   File "D:\Resurrection 2025\Python2025\learning\57propertydecorators.py", line 7, in __init__
#     self.radius = radius
#     ^^^^^^^^^^^
#   File "D:\Resurrection 2025\Python2025\learning\57propertydecorators.py", line 19, in radius
#     raise ValueError("Radius cannot be less than zero")
# ValueError: Radius cannot be less than zero


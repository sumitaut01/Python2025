# 106. What is the difference between @property and normal method?
#
# @property lets you access a method like an attribute.

class Circle:
    def __init__(self, r): self.r = r
    @property
    def area(self): return 3.14 * self.r ** 2

c = Circle(5)
print(c.area)  # no brackets
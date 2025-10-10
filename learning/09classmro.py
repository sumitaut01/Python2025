class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        self.area = self.pi * radius * radius # notice that field does not necessarily has to be created in constructor
        # pi is referenced with self, we could have used Circle.pi also
        self.area2=self.pi * radius * radius *10



c=Circle(12)

print(c.area) #452.15999999999997
print(c.area2) #4521.599999999999
print(c.radius) #12

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self,param1,param2): pass

class Rectangle(Shape):
    def area(self,param1,param2)->None:
        print("rectangle area",param1*param2)


r=Rectangle()
r.area(10,20) #rectangle area 200
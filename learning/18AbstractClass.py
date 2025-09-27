from abc import abstractmethod, ABC

class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass


class Implementation(AbstractClass):
    def method1(self):
        print("method1 implemented")

    def method2(self):
        print("method2 implemented")


    def method3(self):
        print("new with method3 implemented")



c=Implementation()
c.method1() #method1 implemented
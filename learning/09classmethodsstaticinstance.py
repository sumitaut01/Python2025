class Demo:
    count = 0

    def __init__(self):
        print(Demo.count)
        Demo.count += 1
        print(Demo.count)

    @staticmethod
    def stat():
        print(f"Static → doesn’t know about class or instance {Demo.count}")
       # count not accesible this way print(f"Static → doesn’t know about class or instance {count}")

    @classmethod
    def cls(cls):
        print(f"Class → can access count: {cls.count}")

    @classmethod
    def myclassMethid(cls):
        print(f"Class → can access count: {cls.count}")

    def inst(self):
        print(f"Instance → can access count: {self.count}")


d1 = Demo()
d2 = Demo()

d1.inst()       # Instance → can access count: 2
Demo.cls()      # Class → can access count: 2
Demo.stat()     # Static → doesn’t know about class or instance

Demo.myclassMethid()  #Class → can access count: 2

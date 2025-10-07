
class vehicle():
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
        print("from parent constructor")

    def parentmethod(self):
        print("Parent method")

    
class child(vehicle):
    def __init__(self,name,capacity):
        vehicle.__init__(self,name,capacity)
        print("from child constructor")


    def childmethod(self):
            print("Child method")
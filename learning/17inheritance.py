

class Parent:
    name="sumit"
    def __init__(self,first,second):
        self.first = first
        self.second = second
        print("inside parent constructor")

    def displayparent(self):
        print(self.first,self.second,Parent.name)



class Child(Parent):
    def __init__(self):
        print("inside child constructor")
        Parent.__init__(self,3,4)





c=Child()
c.displayparent()
# inside child constructor
# inside parent constructor
# 3 4 sumit
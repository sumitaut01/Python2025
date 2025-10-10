class parent():
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
        print("from parent constructor")

    def parentmethod(self):
        print("Parent method")


class child(parent):
    def __init__(self,name,capacity):
        parent.__init__(self,name,capacity)
        print("from child constructor")

    def __str__(self):
        return "Child "+self.name + " capacity = " + str(self.capacity)


    def childmethod(self):
            print("Child method")

    def loopwork(self):
        for i in range(10):
            print(i)

    def addsum(self,a:int,b:int)->int:
        return a+b


    # def loopwork_more(self):
    #     for i in range(10):
    #         print(i)

p=parent(name="sumit",capacity=100)
c=child(name="amit",capacity=200)

print(isinstance(p,parent)) #True
print(isinstance(c,child)) #true
print(isinstance(p,child)) #False

print(c) #Child amit capacity = 200   because of dunder methods

p=c
print(isinstance(p,child)) #True

c.loopwork()
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print(c.addsum(1,2)) #3


# list

mylst=range(10)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

mylst2=[x*100 for x in range(1,10)]
print(mylst2) #[100, 200, 300, 400, 500, 600, 700, 800, 900]
print(type(mylst2)) #<class 'list'>


#tuple

print('---tuple start')
mytpl=(1,2,3,4)
print(type(mytpl)) #<class 'tuple'>
print(mytpl) #(1, 2, 3, 4)

print(mytpl[0]) #1
print(mytpl[-1]) #4

print('---tuple end')


#dict

mydic={ "name":"sumit"    ,
        "capacity":100}
print(type(mydic))
print(mydic)

print(mydic["name"]) #sumit



#set

myset={1,2,2,3}
print(type(myset)) #<class 'set'>
print(myset) #<class 'set'>

myset.add(100)
print(myset) #{1, 2, 3, 100}

# myset.remove(12)
# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\00Rough.py", line 114, in <module>
#     myset.remove(12)
#     ~~~~~~~~~~~~^^^^
# KeyError: 12

#method outside class does not need self

def myMethod(x:int):
    print(x)

myMethod(100) #100



class A:

    def sum(self,x:int,y:int)->int:
        return x+y

class B:
    def sum(self,x:str,y:str)->str:
        return x+y


class C(A,B):
    pass
c = C()

print(C.mro()) #[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

class D(B,A):
    pass
d = D()
print(D.mro()) #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]





# dont need self when outside function
#needs self when inside class
def sayHi():
    print("hi")

sayHi()#hi


def sumNum(num1, num2):
    c=num1+num2
    return c



print(sumNum(2,3)) #5


# we can mention return type
# None when void
def multiply(num1, num2)->int:
    c=num1*num2
    return c
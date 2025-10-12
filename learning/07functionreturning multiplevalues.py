
def func1():
    return "sumit",32

def func2():
    return ("sumit",32) # still same as func1


name,age=func1()
print(name,age) #sumit 32

data=func1()
print(type(data)) #<class 'tuple'>


print( f"{data[0]} and {data[1]}") #sumit and 32


#Python automatically creates a tuple when you return comma-separated values.

# If you had more or fewer variables than tuple elements, it would raise:
# ValueError: too many values to unpack (expected 2)



print(data == ("sumit", 32)) #True

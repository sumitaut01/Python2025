#//dont require variable declaration type explicity
#String can be in single or double
print('hi')
print("hi")

x=12
print(x)

#we can still declare it. putting string value in int in such case will jus give warning
xx:int=12
print(xx)

yy='sumit'

print(yy)

b,c,d=1,2,"neha"
print(b,c,d)

#print(x+yy) does not work like this

#'{}{}'.format(yy+x)


#python does not have null or undefined
#it has None

x = None
print(x)         # None
print(x is None) # True

print(type(x)) #<class 'NoneType'>



print(5/2) #2.5
print(5//2) #2

print(type(5/2)) #<class 'float'>
print(type(5//2)) #<class 'int'>


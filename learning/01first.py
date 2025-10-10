#//dont require variable declaration type explicity
print('hi')

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

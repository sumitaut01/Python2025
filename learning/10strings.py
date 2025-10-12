
str="sumit";
print(str)

print(id(str))
# sumit
# 2290839903024


str=str+" raut";
print(str)
print(id(str))
# sumit raut
# 2290842890544



print(str*2)#sumit rautsumit raut

print(str+"new") #sumit rautnew
print(str)#sumit raut


#join
print("*"*3)
mylist=["a",'b','c']
print(" ".join(mylist))




#slicing
str2=('abcdedgh')

print(str2[0:3]) #abc
print(str2[:3]) #abc

print(str2[1:-1]) #bcdedg
print(str2[3]) #d


print( "D" in str2) #false

x= "A B C D"

y=x.split(' ')
print(y) #['A', 'B', 'C', 'D']

print(y[0]) #A
print(y[-1]) #D

mylistx = [1, 2, 3]
print(" ".join(map(str, mylistx)))  # → 1 2 3








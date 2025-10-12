# tuple is same as list. However its immutable
# ()

#tuple cant be changed once assigned
a=(1,2,3)
print(a) #(1, 2, 3)

#a[0]=22  //not possible

data=list(range(1,10,1))
print(data)
print(type(data)) #<class 'list'>

data=tuple(data)
print(data)
print(type(data)) #<class 'tuple'>


data=([1,2],(3,4),"name")
print(data) #([1, 2], (3, 4), 'name')
print(type(data))#<class 'tuple'>



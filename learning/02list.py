# similar to array

value=[ 1,2,3]

print(len(value)) #3

print(value[0])#1

#mix values allowed
value1=[1, "sumit","neha"]
print(value1[1])#sumit


print(value[-1])#3

print(value[0:2])#[1,2]

value[0]=0
print(value)#[0, 2, 3]

value.insert(0,99)
print(value)#[99, 0, 2, 3]


value2=[ 5,6,"Neha"]

value3=value1+value2
print(value3) #[1, 'sumit', 'neha', 5, 6, 'Neha']


value3.append(99)
print(value3) #[1, 'sumit', 'neha', 5, 6, 'Neha', 99]

print(value3.insert(0,00)) #[0, 1, 'sumit', 'neha', 5, 6, 'Neha', 99]
print(value3)


print('range-------')
print(range(10))
print(range(0,10))
print(range(0,10,2))
# range-------
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

data=list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data)


data1=list(range(1,10)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data1)


data2=list(range(1,10,1))
print(data2) #[1, 2, 3, 4, 5, 6, 7, 8, 9]



data3=[1,2,3,4,5,6,7,8,9,10]
print(data3[0])
print(data3[-1])



var = data3[1:3] # start from 1st index: go till 3-1
print(var) #[2, 3]


print(data3[1:10:2]) #[2, 4, 6, 8, 10]




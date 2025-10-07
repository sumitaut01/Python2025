from random import shuffle

data="this is spart 1234"

print('is' in data) #true
print(data.find('is')) #2

print(data[0]) #t
print(data[-1]) #4


#Arithmatic

x=3
x+=3
print(x) #6

y=44


# list

lst=[1,2,3,'sagar']
print(lst)  #[1, 2, 3, 'sagar']

for item in lst:
    print(item)
    # 1
    # 2
    # 3
    # sagar

print(len(lst)) #4
print(lst[0:1]) #1

print(1 in lst) #true


k={"name":"John","age":18}
print(k)

print( "age" in k) #true

print(k.values())  #dict_values(['John', 18])
print(k.keys())   #dict_keys(['name', 'age'])




data=[1,2,3,4]

print(min(data)) #1
print(max(data)) #4


#shuffle







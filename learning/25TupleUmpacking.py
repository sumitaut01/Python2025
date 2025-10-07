

data=[('sumit',100),('neha',200)]

print(data) #[('sumit', 100), ('neha', 200)]
print(data[0]) #('sumit', 100)
print(data[0][0]) #sumit

for emp,salary in data:
    print(emp,salary)

#sumit 100
#neha 200



for emp,salary,invalid in data:
    print(emp,salary,invalid)

# ValueError: not enough values to unpack (expected 3, got 2)
# [('sumit', 100), ('neha', 200)]
# ('sumit', 100)

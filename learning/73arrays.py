import array as arr

# stores same type

a = arr.array('i', [1, 2, 3])

# accessing First Araay
print(a[0])

# adding element to array
a.append(5)
print(a)
#array('i', [1, 2, 3, 5])

#insert(index,value)

a.insert(3,4)
#array('i', [1, 2, 3, 4, 5])
print(a)



#mixed type will result in below
#b = arr.array('i', [1, 2, "sumit"])
#   File "D:\Resurrection 2025\Python2025\learning\73arrays.py", line 15, in <module>
#     b = arr.array('i', [1, 2, "sumit"])
# TypeError: 'str' object cannot be interpreted as an integer
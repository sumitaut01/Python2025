# range()

range(10)  # 0..9  excldes last

print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1,10) # 1..9

print(list(range(1,10)) ) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1,10,2) #

print(list(range(1,10,2))) #[1, 3, 5, 7, 9]

print(list(range(2,10,2))) #[2, 4, 6, 8]

print(list(range(10,1,-1))) #[10, 9, 8, 7, 6, 5, 4, 3, 2]

print(list(range(-10,-5)))  #[-10, -9, -8, -7, -6]


#for loop

for i in range(10): print(i)

for i in range(1,10): print(i)  # 1 to 9
for i in range(1,11): print(i) # 1 to 10

for i in range(0,21,2): print(i) # even number upto 20

print('reverse')
for i in range(20,0,-2): print(i)


#while loop

i=1
while i<10:

    print(i)
    i = i + 1
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


#jumping statements
#break
#continue



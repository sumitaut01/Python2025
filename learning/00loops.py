str="sumit raut"

for char in str:
    print(char)

for i in range(len(str)):
    print('{} {}'.format(i,str[i]))

for i,val in enumerate(str):
    print(i,val)

# 0 s
# 1 u
# 2 m
# 3 i
# 4 t
# 5
# 6 r
# 7 a
# 8 u
# 9 t

#convert even to upper and odd to lower
def myfunc(str):
    temp = ""
    for i in range(len(str)):
        if (i + 1) % 2 == 0:
            temp = temp + str[i].upper()
        else:
            temp = temp + str[i].lower()
    return temp

print(myfunc("this is sparta")) #tHiS Is sPaRtA


n = 4
for i in range(0, n):
    print(i)


# anything in single or double quotes
from openpyxl.descriptors import String

name="sumit"
lastname='raut'

print(name[0]) #s

for s in name:
    print(s)

# s
# u
# m
# i
# t

for i in range(3):
   print(name[i])

   # s
   # u
   # m

print("-----")
for i in range(2,3):
   print(name[i]) #m


   print(name[:2]) #0 to 2-1


   print(name.upper())
   print(name.lower())
   print(name.capitalize()) #Sumit
   print(len(name)) #5

   print('   sumit    raut   '.strip())  #sumit    raut

   print('sumit'*3) #sumitsumitsumit




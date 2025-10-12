
def sqruare(num):
    return num*num

#notice that function is passed without ()
print(map(sqruare, [1,2,3,4])) #<map object at 0x000001C4226569B0>

mapx=map(sqruare, [1,2,3,4])
for x in mapx:
    print(x)
# 1
# 4
# 9
# 16





nums = [1,2,3,4]
list(map(lambda x:x*x, nums))       # [1,4,9,16]
list(filter(lambda x:x%2==0, nums)) # [2,4]
from functools import reduce  # not required to be first line
reduce(lambda a,b:a+b, nums)        # 10

nums = [1,2,3,4]
list(map(lambda x:x*x, nums))       # [1,4,9,16]
list(filter(lambda x:x%2==0, nums)) # [2,4]
from functools import reduce  # not required to be first line
reduce(lambda a,b:a+b, nums)        # 10

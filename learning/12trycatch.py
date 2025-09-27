
a=11
try:
    a/0
except:
    raise ValueError("item is less than 1")

finally:
    print("executed finally")

1




age=20

try:
    if(age<21):
        raise ValueError("age should be less than 21")
    if(age is not int):
        raise TypeError("age should be int")

except(ValueError,TypeError):
    print("age should be int and greater than 21")

else:
    age=21
    print("going ahead with default age")
finally:
    print("finally")



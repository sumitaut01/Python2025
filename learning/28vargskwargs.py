# 13. What are *args and **kwargs?
# *args: The special syntax *args in function definitions is used to pass a variable number of arguments to a function.
# Python program to illustrate *args for a variable number of arguments:

def fun(*argv):
    for arg in argv:
        print(arg)

def sumwork(*anything):
    res=0
    for arg in anything:
        res = res+arg
    return res

def addition(*anything):
    return sumwork(*anything)

print(addition(1,2,3)) #6
print(addition(1,2,3,4)) #10

fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Output
# Hello
# Welcome
# to
# GeeksforGeeks




# **kwargs: The special syntax **kwargs in function definitions is used to pass a variable length argument list.
# We use the name kwargs with the double star **.

# key value pairs


def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))

# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')

# Output
# s1 == Geeks
# s2 == for
# s3 == Geeks
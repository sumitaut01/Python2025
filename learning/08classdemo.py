# () after class name are not mandatory unless you are inheriting

class Calculator:
    def __init__(self):
        print("constructor called")



    def sum(self):
        return "sum called"

obj= Calculator()
print(obj.sum()) #5

#
# 🧠 Example 2 — With parentheses (explicit base class)
# class Demo(object):  # same as above
#     def show(self):
#         print("Hello from Demo")
#
#
# This is identical to the first one, because all classes in Python 3 automatically inherit from object.
#
# 🧩 In Python 2, this wasn’t the case — so class Demo: was an old-style class, and class Demo(object): was a new-style class.
# In Python 3, everything is new-style, so the parentheses are optional.

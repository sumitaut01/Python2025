# 101. What is the __del__ method in Python?
#
# __del__ is a destructor method — called when an object is about to be destroyed by the garbage collector.
# Example:

class Demo:
    def __del__(self):
        print("Object deleted")

obj = Demo()
del obj #Object deleted


# ⚠️ Use sparingly; Python’s garbage collector usually handles cleanup automatically.
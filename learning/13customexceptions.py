# 8. What are custom exceptions?
# Subclass Exception:

class MyError(Exception):
    pass


age=19
if age<20:
    raise MyError("age should be more than 20")
#
#   File "D:\Resurrection 2025\Python2025\learning\13customexceptions.py", line 11, in <module>
#     raise MyError("age should be more than 20")
# MyError: age should be more than 20
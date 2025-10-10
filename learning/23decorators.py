# 15. What are decorators?
#
# Functions that modify other functions’ behavior.


def log(func):
    def wrapper(*a, **k):
        print("Start"); res = func(*a, **k); print("End"); return res
    return wrapper

@log
def task(): print("Running")

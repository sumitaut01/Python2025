# 1️⃣ What are iter() and next() in Python?
#
# They are two built-in functions that make any object iterable (loopable).
# They form the iterator protocol, which Python uses behind every for loop.
# 🔹 The iterator protocol
#
# Any object that implements:
# __iter__() → returns an iterator
# __next__() → returns the next value
# ...can be used in a for loop, or anywhere Python expects something iterable.
#import iterable
from selenium import webdriver

# 2️⃣ The iter() function
# iter(obj) tries to call obj.__iter__().
# ✅ It converts any iterable (like list, tuple, string, file, generator, etc.) into an iterator.
# Example:

nums = [10, 20, 30]
it = iter(nums)
print(it)       # <list_iterator object at 0x...>



# 3️⃣ The next() function
# next(it) calls the iterator’s __next__() method.
# It returns the next item from the iterator sequence.
# Example:

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30


#After the last item:
print(next(it))  # ❌ Raises StopIteration
# So these two lines are the heart of how Python loops work:
#it = iter(iterable)
while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break


# This is exactly what Python does behind a for loop:
# for value in iterable:
#     print(value)

#4️⃣ Example: using iter() + next() manually
names = ["Sumit", "Neha", "Amit"]
itr = iter(names)

print(next(itr))  # Sumit
print(next(itr))  # Neha
print(next(itr))  # Amit
print(next(itr))  # StopIteration

# Every call to next() returns one element.
# After all items are exhausted, StopIteration signals the loop to s

# 5️⃣ Where is this used in real Python code?
# Every for, list comprehension, generator, and even functions like zip(), map(), range() — internally use iterators.
# Example:

for x in [1,2,3]:
    print(x)


#is internally:
it = iter([1,2,3])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break



#6️⃣ You can make your own iterator class
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            val = self.current
            self.current += 1
            return val

for i in Counter(1, 5):
    print(i)


# ✅ Output:
#
# 1
# 2
# 3
# 4
# 5
#
#
# So any object that defines these two methods becomes iterable.

# 7️⃣ Connection to Generators
# A generator is just a shortcut to create an iterator.
def gen():
    yield 1
    yield 2

#is equivalent to:
class Gen:
    def __iter__(self): return self
    def __next__(self):
    # logic for yielding 1, then 2, then StopIteration


#So:
g = gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # StopIteration


# ✅ That’s why generators automatically support iter() and next().
# 🧩 8️⃣ How it connects to real automation / scripting
# ✅ File reading
f = open("data.txt")
it = iter(f)

print(next(it))  # reads first line
print(next(it))  # reads second line


# 💡 File objects are iterators — they read one line at a time.
# ✅ Selenium data loops
# When reading test data:

#webdriver driver = webdriver.Firefox()
# rows = driver.find_elements("xpath", "//table/tr")
# it = iter(rows)
# for row in it:
#     print(row.text)


#Under the hood, it’s calling iter() and next() to loop through the web elements.

# 🧠 Summary
# Function	Purpose	Internally Calls	Raises
# iter(obj)	Get iterator from iterable	obj.__iter__()	TypeError if not iterable
# next(iterator)	Get next element	iterator.__next__()	StopIteration when done
# ✅ Analogy
#
# Think of an iterator like a TV remote.
# iter() gives you the remote control 🎮
# next() moves to the next channel 📺
# When channels end → StopIteration 🚫
#
# Quick practical example for interview:
# nums = [10, 20, 30]
# itr = iter(nums)
# print(next(itr))  # 10
# print(next(itr))  # 20
# print(next(itr))  # 30
#
#
# ✅ Everything in Python that can be looped over follows this protocol — from lists to files to generators.
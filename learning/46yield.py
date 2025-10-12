
def myfunc():
    for i in range(5):
        yield i


value = myfunc()
print(type(value)) #<class 'generator'>
print(value) #<generator object myfunc at 0x0000019F04EE5B40>

print(next(value)) #0
print(next(value)) #1
print(next(value))#2
print(next(value))#3
print(next(value))#4


# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\46yield.py", line 17, in <module>
#     print(next(value))
#           ~~~~^^^^^^^
# StopIteration
print(next(value))


# 1️⃣ What is yield in Python?
#
# yield is used inside a function to make it a generator function.
# 👉 It’s similar to return, but instead of ending the function immediately,
# it pauses the function — saving its state — and returns a value temporarily.
# Later, you can resume the function right from where it left off.

# 2️⃣ So what’s a generator function?
#
# When a function has yield in it, it doesn’t return a normal value.
# Instead, it returns a generator object — something you can iterate over.


# 3️⃣ yield vs return
# Feature	return	yield
# Ends function?	✅ Yes	❌ No (pauses)
# Returns	Single value	Sequence (lazy)
# Memory use	All at once	One item at a time
# Reusability	Can’t resume	Can resume
# Used in	Normal functions	Generator functions


# Example comparison
# # Using return
# def get_numbers_return():
#     return [1,2,3]

# # Using yield
# def get_numbers_yield():
#     for i in [1,2,3]:
#         yield i
#
#
# ✅ Both can be looped:
#
# for x in get_numbers_yield(): print(x)
#
#
# But:
#
# return → creates full list in memory
#
# yield → generates one value at a time

# 4️⃣ Why use yield?
#
# Efficiency!
# It’s perfect for handling:
#
# Huge datasets
#
# File or API streaming
#
# Infinite sequences
#
# Because you don’t store everything in memory at once.




# Example: Big range
def count_upto(n):
    for i in range(1, n+1):
        yield i

for x in count_upto(5):
    print(x)


# ✅ Efficient — doesn’t build the entire list [1,2,3,4,5] in memory.
# Each number is generated on demand.
#
# 🧩 5️⃣ Real-world use — reading large files
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("data.log"):
    print(line)


# ✅ Instead of reading the whole file into memory,
# it reads one line at a time — extremely memory-efficient.
#
# 🧩 6️⃣ In PyTest / Automation context
#
# You’ve already seen this 👇

# @pytest.fixture
def setup():
    print("Setup browser")
    yield
    print("Teardown browser")


# Here:
#
# Code before yield = setup
#
# Code after yield = teardown
#
# When the test finishes, control returns after yield, and teardown executes.
#
# ✅ yield is PyTest’s elegant way to implement setup + teardown in one function.
#
# 🧩 7️⃣ You can even send values into a generator
#
# Advanced use:
#
# def counter():
#     x = 0
#     while True:
#         x += 1
#         n = yield x
#         if n:
#             x = n
#
# g = counter()
# print(next(g))    # 1
# print(next(g))    # 2
# print(g.send(10)) # 11
#
#
# 💡 Here, send() pushes data back into the generator.
#
# 🧠 Summary
# Concept	Meaning
# What it does	Turns a function into a generator
# Behavior	Pauses instead of exiting
# Memory use	Low — generates data lazily
# Used for	Streaming, big data, fixtures
# Syntax	yield <value>
# Difference from return	Doesn’t end the function; resumes later
# 🔹 Quick analogy:
#
# return → like a one-time message delivery 📬
# yield → like a subscription that sends you messages one by one 📨
#
# ✅ Real Automation Usage
#
# In PyTest fixtures, it’s the backbone for setup/teardown:
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# That yield splits the fixture into:
#
# Setup: before yield
#
# Teardown: after yield
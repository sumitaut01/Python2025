# 1️⃣ What is enumerate()?
#
# enumerate() is a built-in Python function that lets you loop through a sequence (like a list, tuple, or string) and automatically keep track of the index of each item.
#
# It saves you from writing manual counters like:

# i = 0
# for item in list:
#     print(i, item)
#     i += 1
#
#
# #✅ Instead, just use:
#
# for i, item in enumerate(list):
#     print(i, item)

#2️⃣ Syntax
# enumerate(iterable, start=0)
#
#
# iterable → any sequence (list, tuple, string, etc.)
#
# start → optional starting index (default is 0)
#
# ✅ Returns an enumerate object, which is an iterator that yields (index, value) pairs.


#3️⃣ Simple Example
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


#✅ Output:
#
# 0 apple
# 1 banana
# 2 cherry


# Here, index is automatically provided by enumerate().



#4️⃣ With custom starting index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


#✅ Output:

# 1 apple
# 2 banana
# 3 cherry


#💡 Use this when you want counting to start from 1 (like human-readable lists or table rows).
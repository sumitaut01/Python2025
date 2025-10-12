# 1️⃣ What is a generator in Python?
#
# A generator is a special type of iterator that allows you to generate values on the fly — one at a time — instead of creating and storing the entire collection in memory.
#
# ✅ In short:
# A generator produces a stream of data lazily, rather than holding it all at once.
#
# 🔹 Normal function vs Generator function
# Type	Created using	Returns	Stores all data?	Example
# Normal function	def + return	Single value	Yes	return [1,2,3]
# Generator function	def + yield	Generator object	No	yield 1, yield 2

def counter():
    for i in range(1, 4):
        yield i

gen = counter()
print(gen)       # <generator object counter at 0x...>

print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3

#Each call to next() resumes the function and produces the next value.
#
# 2️⃣ How are generators different from lists / normal iterables?
# Aspect	List / Tuple	Generator
# Evaluation	Eager (creates all items immediately)	Lazy (creates one item at a time)
# Memory	Stores all items in RAM	Only one at a time
# Syntax	[x*x for x in range(5)]	(x*x for x in range(5))
# Type	<class 'list'>	<class 'generator'>
# Best for	Small data	Large / infinite streams


import sys

nums_list = [i for i in range(1000000)]
nums_gen = (i for i in range(1000000))

print(sys.getsizeof(nums_list))  # ~8,000,000 bytes
print(sys.getsizeof(nums_gen))   # ~100 bytes


#Generato can be created in below ways
# A. Using yield (generator function)
def square_numbers(n):
    for i in range(n):
        yield i * i

for num in square_numbers(5):
    print(num)


# ✅ Each yield produces the next value.



# B. Using generator expression (short syntax)
# Like list comprehension, but with () instead of [].

gen = (x*x for x in range(5))
print(type(gen))   # <class 'generator'>
print(list(gen))   # [0, 1, 4, 9, 16]


# ✅ Short and elegant for simple sequences.


# 🧩 4️⃣ Why are generators useful?
#
# They are ideal for large or infinite data streams where you don’t want to store everything in memory.
#
# ✅ Example: file reading
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("access.log"):
    print(line)


# 💡 Reads one line at a time → super memory efficient.


#Would you like me to show how Python internally treats a generator object (with __iter__() and __next__() methods), so you can clearly see how it acts like a special iterator under the hood?
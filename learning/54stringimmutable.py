# 69. What are Python strings immutable?
#
# Because they are stored in interned memory pools; changing would create new objects.
# lower(), upper(), split(), join(), strip(), replace(), startswith(), endswith().

# 1️⃣ What does immutable mean?
# Immutable means:
# Once an object is created, its value cannot be changed in place.
# Instead, any "change" you try to make creates a new object in memory.


s = "sumit"
print(id(s))  # memory address of 'sumit' #2928874308784

s = s + " sagar"
print(id(s))  # memory address of new string #2928879040432

# the id() changes → meaning it’s a new object.
# Hence, Python strings are immutable.


# Contrast with mutable types
# Example with a list (mutable):
lst = [1, 2, 3]
print(id(lst)) #2310171895296

lst.append(4)
print(id(lst)) #2310171895296


# 5️⃣ Consequences of immutability
# Behavior	Explanation
# Cannot modify characters directly	'str'[0] = 'x' → ❌ TypeError
# Fast hashing	Immutable objects can be safely used as dict keys or set members
# Thread-safe	Since they can’t be changed, no concurrency issues
# Memory overhead	Frequent concatenation creates new objects



# 6️⃣ Why Python designers made strings immutable
#
# ✅ Efficiency and safety — strings are heavily reused internally by Python.
# ✅ Hashability — since strings don’t change, they can safely be used as keys in dictionaries:
#
# data = {"name": "sumit"}  # works because str is immutable
#
#
# ✅ Thread safety — immutability avoids accidental modifications in multi-threaded programs.
# ✅ Caching optimization — Python often interns strings (reuses identical string objects).
#
# 🔹 Example of string interning
# a = "hello"
# b = "hello"
# print(a is b)  # True, both point to same memory
#
#
# ✅ Because both strings are identical and immutable, Python stores just one copy.



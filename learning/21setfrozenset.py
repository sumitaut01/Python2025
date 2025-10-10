# Creating a Set
# Using curly braces
#will not have index
fruits = {"apple", "banana", "cherry"}
print(fruits)         # {'banana', 'cherry', 'apple'}
print(type(fruits))   # <class 'set'>

# Using set() constructor
nums = set([1, 2, 3, 3])
print(nums)           # {1, 2, 3} (duplicates removed)

# 🧩 2. Key Properties
#
# ✅ Unordered (no index/position)
#
# ✅ No duplicates allowed
#
# ✅ Mutable (you can add/remove elements)
#
# ✅ Elements must be hashable (e.g., int, str, tuple).
#
# 🧩 3. Common Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union → {1, 2, 3, 4, 5}
print(a & b)   # intersection → {3}
print(a - b)   # difference → {1, 2}
print(a ^ b)   # symmetric difference → {1, 2, 4, 5}

# 🧩 4. Modifying a Set
s = {1, 2}
s.add(3)          # {1, 2, 3}
s.remove(2)       # {1, 3}
s.discard(10)     # safe remove (no error if not found)
s.update([4, 5])  # {1, 3, 4, 5}

# 🧩 5. Frozenset (Immutable Set)
#
# Python also has frozenset, which is immutable (like Java’s Collections.unmodifiableSet).

fs = frozenset([1, 2, 3])
# fs.add(4)  ❌ AttributeError

# 📌 Summary
#
# ✅ Yes, Python has set.
#
# set = mutable, unordered, no duplicates.
#
# frozenset = immutable version.
#
# Supports union, intersection, difference, etc. (just like Java’s Set).
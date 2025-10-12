# 1️⃣ What is slicing in Python?
# Slicing is used to extract a portion (subsequence) of data from a sequence type.
# ✅ Applies to:
#
# list
# tuple
# str
# range
# bytes, bytearray
#
# Basically, anything that is a sequence (ordered and indexable).
#
# Syntax:
# sequence[start : stop : step]
#
# start → index to begin (default = 0)
# stop → index to stop (exclusive)
# step → jump or stride (default = 1)

nums = [10, 20, 30, 40, 50, 60]

print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]
print(nums[3:])      # [40, 50, 60]
print(nums[::2])     # [10, 30, 50]
print(nums[::-1])    # [60, 50, 40, 30, 20, 10]



# What is range() in Python?
# range() is a built-in immutable sequence used to represent a range of integers — often used in loops.
#
# Syntax:
# range(start, stop, step)
#
# ✅ Applies only to integers, not strings or lists directly.
# (You can convert it into a list using list(range(...)))
#
# Example 2:
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(range(1, 6)))     # [1, 2, 3, 4, 5]
print(list(range(2, 10, 2))) # [2, 4, 6, 8]

# ust like slicing, stop is exclusive.
# So range(1, 6) gives numbers 1 → 5.


# Example 3: Parallel usage
data = ['a','b','c','d','e']

for i in range(1,4):   # range
    print(i, data[i])  # slice-like iteration


# Output:
# 1 b
# 2 c
# 3 d
#
# ✅ range(1,4) behaves similar to indices used in data[1:4].


#
# 5️⃣ Summary Table
# Aspect	Slicing	Range
# Works on	Sequences (list, tuple, str)	Numbers only
# Syntax	[start:stop:step]	range(start, stop, step)
# Stop value	Exclusive	Exclusive
# Missing data	Returns empty sequence	Returns empty range
# Errors	None (safe)	None (safe)
# Mutable	Returns new copy (except strings)	Immutable
# Example	[1,2,3,4][1:3] → [2,3]	range(1,4) → 1,2,3
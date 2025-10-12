fruits = ["apple", "banana", "cherry"]
enum_obj = enumerate(fruits)

print(list(enum_obj)) #[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# 6️⃣ Why use enumerate()?
# ❌ Old style (manual counter):
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1

#✅ Better (Pythonic way):
for i, fruit in enumerate(fruits):
    print(i, fruit)


# ✅ Cleaner
# ✅ Less error-prone
# ✅ More readable

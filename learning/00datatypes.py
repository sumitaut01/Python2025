# Numeric (int, float, complex)
#
# Sequence (str, list, tuple)
#
# Mapping (dict)
#
# Set (set, frozenset)
#
# Boolean  (True/False)   notice the first capital letter
#
# NoneType    ///like null




# Python Data Types with Examples
# 1. Numeric Types
int #(Integer)
x = 10

float #(Decimal)
pi = 3.14

complex
z = 2 + 3j


#2. Text Type
str #(String)
name = "Alice"
print(name)

#3. Sequence Types
list #(Ordered, mutable collection)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

tuple #(Ordered, immutable collection)
dimensions = (1920, 1080)

range
r = range(5)  # 0,1,2,3,4


#4. Mapping Type
dict #(Dictionary)
scores = {"Alice": 90, "Bob": 85}
print(scores["Alice"])

#5. Set Types
set
myset = {1, 2, 3}


frozenset
frozen = frozenset([1, 2, 3])

#6. Boolean Type
bool
is_active = True
print(is_active)

#7. None Type
#NoneType
nothing = None
print(nothing)

#8. Binary Types
bytes, bytearray, memoryview


b = b"hello"              # bytes
arr = bytearray(5)        # bytearray
mv = memoryview(b"hello") # memoryview
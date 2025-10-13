#
#memoryview
#bytes
#bytearray

# memoryview, bytes, and bytearray.
#
# They’re not used daily in simple scripting — but they’re essential when dealing with:
# File I/O
# Networking (sockets, protocols)
# Image/audio/video data
# Performance-sensitive code
# Let’s break them down cleanly, with examples and relationships 👇


# 1️⃣ bytes — Immutable sequence of bytes
# Think of bytes as a read-only sequence of 8-bit numbers (0–255).

#Example:


data = bytes([65, 66, 67, 68])
print(data)          # b'ABCD'
print(type(data))    # <class 'bytes'>

# Here:
#
# Each integer (65–68) is an ASCII code.
#
# b'ABCD' is how Python displays byte literals.

# You can also create bytes from strings:
b = "hello".encode('utf-8')
print(b)             # b'hello'
print(list(b))       # [104, 101, 108, 108, 111]
#
#
# 💡 .encode() converts a string → bytes
# and .decode() does the opposite.

# Immutable means:
# b[0] = 72   # ❌ TypeError: 'bytes' object does not support item assignment
#
#
# You can’t modify bytes in place.

# ✅ Use case:
# When you need raw binary data that won’t change (e.g., reading a file from disk).
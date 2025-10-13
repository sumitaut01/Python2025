# 3️⃣ memoryview — Window (view) into existing binary data
#
# memoryview doesn’t copy data — it gives you a zero-copy view of another bytes-like object.
# This makes it super efficient for large binary data.
#
# Example:
ba = bytearray(b"HELLO")
mv = memoryview(ba)

print(mv[0])      # 72  (ASCII of 'H')
print(bytes(mv[:3]))  # b'HEL'

# modify original through the view
mv[0] = 90         # 90 = 'Z'
print(ba)          # bytearray(b'ZELLO')


#✅ Changing the memoryview updates the original data — no extra memory copy.

# So:
# Object	Mutable?	Copy made?	Typical Use
# bytes	❌ No	Yes	Read-only binary data
# bytearray	✅ Yes	Yes	Writable binary data
# memoryview	✅ (depends on source)	❌ No	Efficient “view” into existing bytes
# 🧩 4️⃣ Visual analogy

#Think of it like this 👇

# File on disk → bytes  (immutable copy)
#                 ↓
#            bytearray  (editable copy)
#                 ↓
#            memoryview (window into memory, no copy)

# 🧩 5️⃣ Real examples
# Example 1 — Reading file as bytes
with open("photo.jpg", "rb") as f:
    data = f.read()  # bytes object
print(type(data))  # <class 'bytes'>

# Example 2 — Modify first few bytes of file buffer
with open("photo.jpg", "rb") as f:
    ba = bytearray(f.read())

ba[0:3] = b'XYZ'   # modify header

# Example 3 — Zero-copy slicing with memoryview
buf = bytearray(b"ABCDEFGH")
view = memoryview(buf)
print(bytes(view[2:5]))   # b'CDE'
view[2:5] = b'123'        # modify original
print(buf)                # bytearray(b'AB123FGH')

#
# 💡 No copying — you edited the same buffer in memory.
#
# 🧠 6️⃣ Performance Notes
#
# bytes is fastest for reading/static data.
#
# bytearray is best for building or mutating data.
#
# memoryview avoids extra copies, ideal for large data like files, streams, or shared buffers.
#
# ✅ TL;DR Summary
# Feature	bytes	bytearray	memoryview
# Mutable	❌ No	✅ Yes	✅ (if source is mutable)
# Type	Immutable sequence of bytes	Mutable byte sequence	Lightweight view over buffer
# Copy when sliced?	✅ Yes	✅ Yes	❌ No
# Typical use	Read-only binary data	Editable binary data	Zero-copy access to binary data
# Example	b"data"	bytearray(b"data")	memoryview(ba)
# Quick example recap
b = b"hello"                        # bytes
ba = bytearray(b)                   # bytearray (mutable)
mv = memoryview(ba)                 # memoryview (no copy)

mv[0] = 72                          # modify through view
print(ba)                           # bytearray(b'Hello')
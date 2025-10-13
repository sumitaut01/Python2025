# 2️⃣ bytearray — Mutable version of bytes
#
# bytearray behaves like bytes, but you can modify its contents.

#Example:
ba = bytearray([65, 66, 67])
print(ba)         # bytearray(b'ABC')

ba[0] = 90        # change first byte (65→90)
print(ba)         # bytearray(b'ZBC')

ba.append(68)
print(ba)         # bytearray(b'ZBCD')


# ✅ You can:
#
# Modify elements
#
# Append/remove
#
# Slice/replace data
#
# You can convert between types:
b = bytes(ba)      # bytearray → bytes
ba2 = bytearray(b) # bytes → bytearray


# ✅ Use case:
# When you need to build or modify binary data (like constructing network packets, image buffers, etc.)
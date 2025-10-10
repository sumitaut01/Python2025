# 73. What are raw strings?
#
# Used to ignore escape characters.

path = r"C:\new\folder"

# 74. Explain f-strings, format(), and % formatting.
name="Sumit"
print(f"Hello {name}")            # f-string
print("Hello {}".format(name))    # format
print("Hello %s" % name)          # old style
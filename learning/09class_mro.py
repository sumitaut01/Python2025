# 29. Explain multiple inheritance.
#
# Class can inherit from multiple parents; uses MRO to resolve conflicts.

# 30. How does super() work?
#
# Calls next class in MRO chain.
# Used for cooperative multiple inheritance.



# 102. What is method resolution order (MRO)?
#
# MRO determines the order in which base classes are searched when executing a method.
# Check it using:
#
# print(MyClass.mro())
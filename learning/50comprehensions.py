# 54. What are comprehensions in Python?
#
# Compact syntax for creating collections.

List: [x*x for x in range(5)]

Set: {x*x for x in range(5)}

Dict: {x:x*x for x in range(5)}

Generator: (x*x for x in range(5))
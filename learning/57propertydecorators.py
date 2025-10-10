# 85. Explain property decorator.
#
# Turns methods into read-only attributes.

class Circle:
    def __init__(self,r): self._r=r
    @property
    def area(self): return 3.14*self._r**2
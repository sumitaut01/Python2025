s=set()

print(type(s)) #<class 'set'>
print(len(s)) #0
print(s) #set()

s.add(1)
s.add(3)
print(s) # {1}

s2={1,2}

print(s.intersection(s2)) #1
print(s.union(s2)) #{1, 2, 3}
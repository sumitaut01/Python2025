from collections import defaultdict

a={'name': 'sumit'}
print(a)

print(a['name']) #sumit

#print(a['xxxx'])
# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\31defaultdictionary.py", line 9, in <module>
#     print(a['xxxx'])
#           ~^^^^^^^^
# KeyError: 'xxxx'


b=defaultdict(lambda :0)
b['xxxx']=1
print(b)  #defaultdict(<function <lambda> at 0x00000264D3C1D080>, {'xxxx': 1})
print(b['xxxx']) #1

print(b['yyy']) #0

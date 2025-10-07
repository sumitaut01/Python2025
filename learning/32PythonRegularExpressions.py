import re

text='this is a good day. card num is 1234-5678-123'


text=re.findall(r'\d+',text)

print(text) #['1234', '5678', '123']


text='this is a good day. card num is 1234-5678-123'
text=re.findall(r'\d{4}',text)
print(text) #['1234', '5678']


text='this is a good day. card num is 1234-5678-123'

text=re.findall(r'\d{4}',text)
print(text) #['1234', '5678']


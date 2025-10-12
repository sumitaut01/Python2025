
# pass just way to avoid syntax error
class MyClass:
    pass

print(MyClass()) #<__main__.myclass object at 0x000001EA101452B0>

c=MyClass()
print(c) #<__main__.myclass object at 0x000001647F2C91D0>

class MyDog:
    species = 'Mammal' #Class level. common for all instances
    def __init__(self,breed,name):
        self.breed=breed
        self.dog_name=name  # notice we have used different instance variable

#d=MyDog()
#print(d.breed)
# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\08Classmore.py", line 17, in <module>
#     d=MyDog()
# TypeError: MyDog.__init__() missing 1 required positional argument: 'breed'

d=MyDog("labrador","motu")
print(d.breed) #labrador

dd=MyDog("labrador","motu",)
print(dd.breed,dd.dog_name,MyDog.species) #labrador motu Mammal


ddd=MyDog(name="lakwa",breed="desi")
print(ddd.breed,ddd.dog_name,MyDog.species) #desi lakwa Mammal


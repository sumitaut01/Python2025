a={"name":"sumit",'age':20, 'city':'bhandara'}
print(a) #{'name': 'sumit', 'age': 20, 'city': 'bhandara'}
print(a["name"])#sumit

print(a.get("name")) #sumit

a.update({"name":"sumitupdated"}) #sumitupdated
print(a.get("name")) #sumitupdated



# print(a["nonexisting"]) #KeyError
# Traceback (most recent call last):
#   File "D:\Resurrection 2025\Python2025\learning\06dictionary.py", line 6, in <module>
#     print(a["nonexisting"])
#           ~^^^^^^^^^^^^^^^
# KeyError: 'nonexisting'



for k in a:
    print(k,a[k])

# name sumitupdated
# age 20
# city bhandara


print("-----")
print(a.pop("city")) #bhandara
print(a) #{'name': 'sumitupdated', 'age': 20}


#create on runtime
dict={}

dict["name"]= "sumit"
dict["age"]= 35
print(dict)  #{'name': 'sumit', 'age': 35}


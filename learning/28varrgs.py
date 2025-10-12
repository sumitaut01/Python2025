# *args or *anythingwillwork
# Collects extra positional parameters into a tuple.
def demo_args(*args):
    print(args)

demo_args(1, 2, 3, "hello") #(1, 2, 3, 'hello')
demo_args(1, 2) #(1, 2)



#**kwargs → Variable Keyword Arguments
#Collects extra named parameters into a dictionary.

def introduce(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

introduce(name="Neha", role="QA", tool="Selenium")
# name = Neha
# role = QA
# tool = Selenium


print("---------------------")
def print_both(*args,**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

    for d in args:
        print(d)

    #  inprogress print('printing {} {}'.format(args[0], kwargs['name']))

print_both(1,2,3, {"name":"sumit","age":35})

print_both(1,2,3, name="sumit",age=35)

# name = sumit
# age = 35
# 1
# 2
# 3


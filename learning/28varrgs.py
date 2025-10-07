
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
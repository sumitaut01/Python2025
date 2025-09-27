class demo:
    name="sumit" # class level variable
    def __init__(self,data):
        print('constructor called')
        self.data = data #fields instance

    def methodx(self):
        print(demo.name)
        print(self.data)


#calling 
d=demo(3)
#d.methodx(self)  no need of self.. error outs if used
d.methodx()
# constructor called
# sumit
# 3

class Demo:
    @staticmethod
    def stat(): print("static")

    @classmethod
    def cls(cls): print("class", cls)

    def inst(self): print("instance", self)

print(Demo.stat()) #print("static")
print(Demo.cls())

d=Demo()
print(d.inst())
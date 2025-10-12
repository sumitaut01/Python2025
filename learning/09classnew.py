class Work:
    def show(self):
        d = Work()
        d.name = "sumit"
        d.age = 35
        return d


def main():
    dd = Work()
    dd = dd.show()
    print(f"{dd.name} and {dd.age}")  # sumit and 35


# main body code

ddd = Work()
ddd = ddd.show()
print(f"{ddd.name} and {ddd.age}") #sumit and 35

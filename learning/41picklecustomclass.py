import pickle

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

emp = Employee("Sumit", 101)

# Serialize
with open("emp.pkl", "wb") as f:
    pickle.dump(emp, f)

# Deserialize
with open("emp.pkl", "rb") as f:
    e = pickle.load(f)

print(e.name, e.id) #Sumit 101


# What is pickle in Python?
#
# 👉 pickle is a built-in Python module used for serialization and deserialization of Python objects.
#
# In simple words:
#
# Serialization (Pickling) → Convert a Python object into a byte stream (so it can be saved to a file or sent over a network).
#
# Deserialization (Unpickling) → Convert the byte stream back into a Python object.


import pickle

data = {"name": "Sumit", "age": 30, "tools": ["Selenium", "PyTest"]}

#Ser
with open("data.pkl", "wb") as f:   # write in binary mode
    pickle.dump(data, f)

#dese
with open("data.pkl", "rb") as f:   # read in binary mode
    loaded_data = pickle.load(f)

print(loaded_data)

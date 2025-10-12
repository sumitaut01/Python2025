# 1️⃣ What is a dataclass in Python?
#
# A dataclass is a special kind of class introduced in Python 3.7+ that’s meant for storing data — like configuration, request payloads, or model objects — without writing all the boilerplate code (like __init__, __repr__, __eq__, etc.).
#
# So instead of writing this manually:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# ✅ You can just write:

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

#
# And Python auto-generates all those methods for you! 🔥
#
# 🧠 2️⃣ What does @dataclass do behind the scenes?
#
# When you decorate a class with @dataclass, Python automatically adds:
#
# __init__() → to initialize fields
#
# __repr__() → to print readable string
#
# __eq__() → to compare objects
#
# (optionally) __hash__() and __lt__, __gt__, etc. if needed
#
# 🔹 Example:
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Sumit", 35)
p2 = Person("Sumit", 35)
p3 = Person("Neha", 28)

print(p1)        # Person(name='Sumit', age=35)
print(p1 == p2)  # True  (auto-generated __eq__)
print(p1 == p3)  # False


# ✅ You didn’t have to write __init__, __repr__, or __eq__ manually.
# The decorator did it all.
#
# 🧩 3️⃣ Syntax Explained
@dataclass
class Person:
    name: str
    age: int


# @dataclass → a decorator that transforms the class automatically
#
# name: str and age: int → type hints (annotations)
#
# You can still use defaults or computed fields.
#
# 🧩 4️⃣ With default values
@dataclass
class Person:
    name: str
    age: int = 25  # default value

p = Person("Sumit")
print(p)  # Person(name='Sumit', age=25)


# ✅ Works like a normal default argument in a constructor.
#
# 🧩 5️⃣ With __post_init__ (custom initialization logic)
#
# If you want extra setup after initialization,
# use a special hook called __post_init__.
#
# Example:

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

p = Person("Sumit", 35)    # OK
p2 = Person("Neha", -1)    # ❌ ValueError


# ✅ You don’t override __init__() — you use __post_init__() for custom logic.
#
# 🧩 6️⃣ Comparison example
#
# Dataclasses make comparisons super easy:

p1 = Person("Sumit", 35)
p2 = Person("Sumit", 35)
p3 = Person("Neha", 35)

print(p1 == p2)   # True (same data)
print(p1 == p3)   # False


# If this were a normal class, p1 == p2 would return False (because they’re two different objects).
# But dataclasses automatically implement __eq__() to compare by values. ✅
#
# 🧩 7️⃣ Making it “frozen” (immutable dataclass)
#
# You can make your dataclass immutable, so attributes can’t be modified after creation.

@dataclass(frozen=True)
class Person:
    name: str
    age: int

p = Person("Sumit", 35)
# p.age = 40   # ❌ dataclasses.FrozenInstanceError


# ✅ Useful when you want read-only data objects — like configuration or constants.
#
# 🧩 8️⃣ Using order=True (for sorting)
#
# Dataclasses can even generate comparison methods (<, >, etc.) automatically.

@dataclass(order=True)
class Person:
    name: str
    age: int

p1 = Person("Sumit", 35)
p2 = Person("Neha", 28)

print(p1 > p2)  # True, because 35 > 28

# 🧩 9️⃣ With default factories (like lists or dicts)
#
# If your field is a mutable type, use field(default_factory=...)

from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)

t = Team("QA")
t.members.append("Sumit")
t.members.append("Neha")
print(t)  # Team(name='QA', members=['Sumit', 'Neha'])


# ✅ Prevents the "mutable default argument" bug.
#
# 🧩 10️⃣ Why use dataclasses (advantages)
# Benefit	Description
# ✅ Less code	Auto-creates init, repr, eq
# ✅ Readable	Easy to print and debug
# ✅ Safe defaults	Supports field factories
# ✅ Immutable option	frozen=True
# ✅ Comparable	order=True
# ✅ Cleaner than NamedTuple	Mutable and type-annotated
# //1️⃣ What happens when Python sees a yield

# Whenever Python sees yield inside a function, it does not treat it as a normal function anymore.
# Instead, it compiles it as a generator function — something that produces values one by one.
#
# So instead of running immediately, it returns a generator object.

def demo():
    print("Step 1")
    yield 10
    print("Step 2")
    yield 20
    print("Step 3")
    yield 30

g = demo()
print(g)
#<generator object demo at 0x...>

# 2️⃣ When you call next(g)
#
# Every call to next() tells Python:
#
# “Run this function until the next yield, then pause and give me that value.”


#Step-by-step execution
print(next(g))

#
# ✅ Output:
#
# Step 1
# 10


# 💡 Explanation:
#
# Function starts from the top.
#
# Prints “Step 1”
#
# Encounters yield 10 → pauses and returns 10
#
# Function state is frozen at that point (variables, line number, etc.)


# Next call
print(next(g))


# ✅ Output:
#
# Step 2
# 20


# Now execution resumes right after the previous yield.
#
# 🔹 Third call
print(next(g))


# ✅ Output:

# Step 3
# 30

# 🔹 Fourth call
print(next(g))

#
# 🚫 There’s nothing left to yield — so it raises:
#
# StopIteration
#
# ✅ So the complete output:
# Step 1
# 10
# Step 2
# 20
# Step 3
# 30
# Traceback (most recent call last):
#   ...
# StopIteration
#
# 🧩 3️⃣ How Python remembers where it left off
#
# Behind the scenes, Python stores:
#
# The instruction pointer (which line to resume)
#
# The local variables inside the function
#
# The stack frame of the function
#
# So when you call next() again, Python just resumes execution right after the last yield.
#
# It’s like pressing pause ▶️ and play ⏸️ on a movie.
#
# 🧩 4️⃣ Using for loop (instead of manual next())
#
# Whenever you loop:
#
# for x in demo():
#     print(x)
#
#
# Python does this internally:
#
# g = demo()
# while True:
#     try:
#         value = next(g)
#         print(value)
#     except StopIteration:
#         break
#
#
# ✅ So the for loop automatically handles the StopIteration for you.
#
# 🧩 5️⃣ How this looks in memory (visualized)
# Call demo()     → creates generator object
# |
# | next(g) → executes till first yield (returns 10)
# | next(g) → resumes → executes till next yield (returns 20)
# | next(g) → resumes → executes till next yield (returns 30)
# | next(g) → StopIteration → end
#
#
# Each yield point acts like a checkpoint in memory.
#
# 🧩 6️⃣ You can even pass data into a generator
# def echo():
#     val = yield "Start"
#     while True:
#         val = yield f"You said: {val}"
#
# g = echo()
# print(next(g))       # "Start"
# print(g.send("Hi"))  # "You said: Hi"
# print(g.send("Bye")) # "You said: Bye"
#
#
# ✅ Here:
#
# send() both resumes and sends data back into the function
#
# val = yield receives the data next time the generator resumes
#
# This is how coroutines work — the foundation for async programming in Python.
#
# 🧩 7️⃣ Real use: PyTest fixtures
# @pytest.fixture
# def driver():
#     print("🔹 setup browser")
#     driver = webdriver.Chrome()
#     yield driver
#     print("🔹 teardown browser")
#     driver.quit()
#
# What happens internally:
#
# Fixture runs until yield → creates driver (setup)
#
# Test runs using the driver
#
# After test completes, execution resumes after yield → teardown runs
#
# ✅ Exactly the same pause–resume mechanism we saw earlier.
#
# 🧠 In short
# Keyword	Action	Behavior
# yield	Pause function & return value	Remembers state
# next()	Resume execution until next yield	Controlled iteration
# StopIteration	Raised automatically at the end	Handled by for
# send()	Resume and pass data in	Enables coroutines
# Use Case	Streams, PyTest fixtures, large data	Efficient, lazy
# 🧩 Quick analogy
#
# Think of yield like a bookmark in a novel 📖
#
# return means you closed the book and threw it away.
#
# yield means you put a bookmark and can open it tomorrow right where you left off.
#
#Would you like me to show a step-by-step visual execution trace of how variables persist and resume across multiple yield calls — kind of like a timeline diagram showing before/after state at each next()? It’s very helpful for interviews and debugging generators.
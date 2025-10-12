

def main():
    age=int(input("Enter your age: "))



if __name__=="__main__":
    main()

# The meaning of __name__
#
# Every Python file (module) automatically gets a built-in variable called __name__.
# When you run the file directly →
# __name__ becomes "__main__"
# When you import the file as a module →
# __name__ becomes the module’s name (like "my_module")




# 3️⃣ Why we use if __name__ == "__main__":
#
# It tells Python:
#
# “Run this block only if this file is executed directly,
# not when it’s imported somewhere else.”
#
# ✅ In other words:
#
# When run directly → code inside executes
#
# When imported → code inside is skipped
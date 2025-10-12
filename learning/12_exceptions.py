try:
    x = 5 / 1
except ZeroDivisionError:
    print("Division by zero")
else:
    print("This runs when no exception. No error, result =", x)
finally:
    print("Done.always runs")

# This runs when no exception. No error, result = 5.0
# Done


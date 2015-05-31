print("Y = 3x^2 - 5x + 10")

try:
    x = float(input("Value for x: "))
except ValueError:
    print("That's not an acceptable value")
    quit()

y = 3 * x**2 - 5 * x + 10

print("Y=%f" % y)
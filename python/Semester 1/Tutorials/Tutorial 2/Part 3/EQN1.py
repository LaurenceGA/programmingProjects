print("Y = 3x^2 - 5x + 10")

def findY(X):
    print("Y=%.3f" % (3 * X**2 - 5 * X + 10))

try:
    x = float(input("Value for x: "))
except ValueError:
    print("That's not an acceptable value")
    quit()

findY(x)

#y = 3 * x**2 - 5 * x + 10

#print("Y=%f" % y)
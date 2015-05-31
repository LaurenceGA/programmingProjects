print("C = Sqrt(x^2 - 5y)")

try:
    x = float(input("Value for x: "))
    y = float(input("Value for y: "))
except ValueError:
    print("That's not an acceptable value")
    quit()

try:
    c =  (x**2 - 5*y)**0.5
except:
    print("Those two values don't work.")

print("C=%f" % c)
import math

rawInp = input("What is the radius of the sphere?\n>>>")

radius = 1

try:
    radius = float(rawInp)
except ValueError:
    print("Not an acceptable value.")
    quit()

volume = ((4*math.pi)/3) * radius**3

print("The volume is %.2f units" % volume)
import math

def sphereVol(rad):
    return ((4*math.pi)/3) * rad**3

rawInp = input("What is the radius of the sphere?\n>>>")

radius = 1

try:
    radius = float(rawInp)
except ValueError:
    print("Not an acceptable value.")
    quit()

print("The volume is %.2f units" % sphereVol(radius))
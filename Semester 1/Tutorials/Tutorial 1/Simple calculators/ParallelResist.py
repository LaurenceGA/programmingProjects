try:
    r1 = float(input("Resistance of first resistor: "))
    r2 = float(input("Resistance of second resistor: "))
    r3 = float(input("Resistance of third resistor: "))
except ValueError:
    print("Invalid values.")

combResist = 1/((1/r1)+(1/r2)+(1/r3))

print("This combined resistance is %.3f ohms" % combResist)
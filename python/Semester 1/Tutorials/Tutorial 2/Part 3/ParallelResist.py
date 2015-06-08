def combResist(res1, res2, res3):
    return 1/((1/res1)+(1/res2)+(1/res3))

try:
    r1 = float(input("Resistance of first resistor: "))
    r2 = float(input("Resistance of second resistor: "))
    r3 = float(input("Resistance of third resistor: "))
except ValueError:
    print("Invalid values.")

combResist = combResist(r1, r2, r3)

print("This combined resistance is %.3f ohms" % combResist)
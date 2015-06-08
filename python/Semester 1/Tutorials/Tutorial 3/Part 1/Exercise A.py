def cube(x):
    return x**3

cubeSum = 0

for i in range(10):
    ii = i+1
    iCube = cube(ii)
    cubeSum += iCube
    print("%d\t%d" % (ii, iCube))

print("Total:", cubeSum)
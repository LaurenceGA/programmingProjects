def cube(x):
    return x**3

cubeSum = 0
maxNum = 10

i = 1

while i < maxNum+1:
    iCube = cube(i)
    cubeSum += iCube
    print("%d\t%d" % (i, iCube))
    i += 1

"""
for i in range(10):
    ii = i+1
    iCube = cube(ii)
    cubeSum += iCube
    print("%d\t%d" % (ii, iCube))
"""
print("Total:", cubeSum)
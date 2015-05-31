i = 0
total = 1

while i < 101:
    cube = i**3
    print("%d\t%d" % (i, cube))
    total += cube
    i += 10

print ("Total: %d" % total)
import random
import math
import time


def estimatePi(n):
    k = 0
    for n in range(n):
        xr = random.random() * 2
        yr = random.random() * 2
        d = math.sqrt((xr - 1.0)*(xr - 1.0) + (yr-1.0)*(yr-1.0))
        if d < 1:
            k += 1
    print("Finished in %f seconds" % (time.clock()))

    return (4 * k / n)

ePI = estimatePi(1000)
print(ePI)
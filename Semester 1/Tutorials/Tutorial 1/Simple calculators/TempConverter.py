try:
    cTemp = float(input("Temperature in degrees centigrade: "))
except ValueError:
    print("That is not an acceptable temperature")
    quit()

fTemp = cTemp * 9 / 5 + 32

print('That temperature is %.2F degrees Fahrenheit' % fTemp)
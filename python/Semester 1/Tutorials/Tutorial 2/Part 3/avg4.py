def avg4():
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number: "))
        n4 = float(input("Enter fourth number: "))
    except ValueError:
        print("Invalid input")

    return (n1+n2+n3+n4)/4

print(avg4())
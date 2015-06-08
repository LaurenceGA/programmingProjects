def avg():
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number: "))
    except ValueError:
        print("Invalid input")

    print((n1+n2+n3)/3)

avg()
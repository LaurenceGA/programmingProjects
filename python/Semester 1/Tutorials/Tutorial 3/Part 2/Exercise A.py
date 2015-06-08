def getTax(ammount, tax):
    return ammount * tax / 100

itemName = input("What is the name of the item?\n>>>")
try:
    itemPrice = float(input("How much does the item cost?\n>>>"))
except ValueError:
    print("That's not a valid input!")
    quit()

for i in range(5, 30, 5):
    print("%d%% tax on %s costing $%.2f is $%.2f" % (i, itemName, itemPrice, getTax(itemPrice, i)))
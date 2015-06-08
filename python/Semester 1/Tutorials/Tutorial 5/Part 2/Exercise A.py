def printNumberBlock(start, limit, copies):
    for i in range(copies):
        printRow(start, limit)
        print()

def printRow(start, limit):
    for i in range(limit-start+1):
        print(i + start, end="\t")

try:
    limit = int(input("What is the limit\n>>>"))
    copies = int(input("How many copies\n>>>"))

    printNumberBlock(3, limit, copies)
except ValueError:
    print("Nope.")
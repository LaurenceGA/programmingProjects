marklist = []
sum = 0

try:
    numOfMarks = int(input("Marks to Enter\n>>>"))
except:
    print("Not a valid input")
    quit()

for i in range(numOfMarks):
    try:
        mark = float(input("Enter mark: "))
    except:
        print("Not an accpetable value")
        break
    marklist.append(mark)
    sum += mark

print("Marks: ", marklist)
print("Average mark is %d" % sum/numOfMarks)
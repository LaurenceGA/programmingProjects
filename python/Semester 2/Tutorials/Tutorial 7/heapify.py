import random

# Set up some Python Lists
# <List creation reduced in size>
shortlist = [0] + [random.randrange(0, 1000) for i in range(100)]
longlist = [0] + [random.randrange(0, 10000) for i in range(10000)]
superlonglist = [0] + [random.randrange(0, 1000000) for i in range(1000000)]


def shiftdown(alist, j):
    swap_count = 0

    temp = alist[j]

    # 2*j tests for a left child
    while 2*j <= len(alist)-1:
        child = 2*j

        # if there is a right child, is it bigger?
        if child < len(alist)-1 and alist[child + 1] > alist[child]:
            child += 1

        # move child up?
        if alist[child] > temp:
            alist[j] = alist[child]
            swap_count += 1
        else:
            break  # Exit while loop

        j = child
    # insert original alist[j] in correct spot
    alist[j] = temp
    return swap_count


# You need to implement this function.
# Your function should heapify the input list 
# and increment the step count for each unit of work carried out.
def heapify(alist):
    stepcount = 0

    # n/2 is the index of parent of last node
    for j in range((len(alist)-1)/2, 0, -1):
        stepcount += shiftdown(alist, j)

    return stepcount

shortlistcount = heapify(shortlist)
longlistcount = heapify(longlist)
superlonglistcount = heapify(superlonglist)

for i in range(len(shortlist)):
    print shortlist[i],
    
print '\n'

print 'Heapify took ' + str(shortlistcount) + ' steps on the list of length ' + str(len(shortlist)-1)
print 'Heapify took ' + str(longlistcount) + ' steps on the list of length ' + str(len(longlist)-1)
print 'Heapify took ' + str(superlonglistcount) + ' steps on the list of length ' + str(len(superlonglist)-1)

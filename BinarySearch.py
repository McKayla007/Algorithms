# Binary Search

# Bubble Sort
def bubblesort(items, n):
    swapped = True
    while n>0 and swapped == True:
        swapped = False
        n = n-1
        for index in range(0, n):
        
            if items[index] > items[index+1]:
                temp = items[index]
                items[index] = items[index+1]
                items[index+1] = temp
                swapped = True
    print("Sorted list:", items)
    return items
    
def findmidpoint(first, last):
    return (first + last) // 2

items = [10, 29, 12, 82, 71, 19, 54, 35]

itemslength = len(items)
sortedlist = bubblesort(items, itemslength)

searcheditem = int(input("Enter number to find: "))
found = False

first = 0
last = itemslength-1

while first <= last:
    itemslength = len(sortedlist)
    midpoint = findmidpoint(first, last)
    if searcheditem == sortedlist[midpoint]:
        print("Item found")
        found == True
        break
    elif searcheditem < midpoint:
        first = midpoint + 1
    elif searcheditem > midpoint:
        last = midpoint - 1
 
print(midpoint)
if found == False:
    print("Item not found")

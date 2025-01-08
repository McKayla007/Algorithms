list = ["I", "H", "G", "F", "E", "D", "C", "B", "A", "J"]
searchItem = input("Enter the item to find: ")

found = False
index = 0
while found == False and index <= len(list) - 1:
	if list[index] == searchItem:
		found = True
	else:
	    index += 1

if found == True:
	print("Item found at", index)
else:
	print("Item not found in list.")

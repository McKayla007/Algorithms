def A_Linear_Search (item, thelist):
    # mark the item as not found to start with
    itemfound = False
    # begin at the start of the list, position zero
    index = 0
    # get the length of the list
    listlen = len(thelist)
    
    # iterate through the list to the end
    while index < listlen and not itemfound:
        # if a match is found then change the found flag
        if thelist[index] == item:
            itemfound = True
        index = index + 1    
    
    return itemfound

rainbow = ["red","green","blue","violet","indigo","yellow","orange"]

# get a colour from the user
item = input("Enter a colour : ").lower()
    
# search the list for the item
result = A_Linear_Search(item,rainbow)
    
# inform the user of the result
if result:
    print(item, " is a colour of the rainbow")
else:
    print(item, " is not a colour of the rainbow")
        

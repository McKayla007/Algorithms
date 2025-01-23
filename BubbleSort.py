# Bubble Sort

list = ["Florida", "Georgia", "Delaware", "Alabama", "California"]

n = len(list)
swapped = True
count = 0

while n>0 and swapped == True:
    swapped = False
    n = n-1
    
    for index in range(0, n):
        
        if list[index] > list[index+1]:
            temp = list[index]
            list[index] = list[index+1]
            list[index+1] = temp
            
            swapped = True
        print(list)
        count+=1
        print(count, "pass")
            
        
    
            
n = int(input("Enter number: "))
i = 0
strn = str(n)
nlength = len(strn)

while i<(nlength):
    character = strn[i]
    array1.append(character)
    array2.insert(0, character)
    i+=1

if array1 == array2:
    print(n, "is palindromic.")
else:
    print(n, "is not palindromic.")

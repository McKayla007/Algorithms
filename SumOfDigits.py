n = int(input("Enter number: "))
i = 0
sum = 0
strn = str(n)
nlength = len(strn)

while i<(nlength):
    digit = int(strn[i])
    sum = sum + digit
    i+=1
print(sum)

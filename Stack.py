stack = []

# Declare stack size
stacksize = int(input("Enter stack size: "))

while True:
  option = input("Push or pop?: ")
  option = option.lower()
    
  if option == "push":
    if len(stack) >= stacksize:
     print("STACK OVERFLOW")
    else:
      push = input("Enter value to push onto stack: ")
      stack.append(push)
  elif option == "pop":
    if len(stack) == 0:
      print("STACK UNDERFLOW")
    else:
      stack.pop()
  
  print(stack)

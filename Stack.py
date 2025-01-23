stack = []

# Declare stack size
stacksize = int(input("Enter stack size: "))

while True:
  option = input("Push, pop, view or exit?: ")
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
  elif option == "view":
    print(stack)
  elif option == "exit":
    exit()

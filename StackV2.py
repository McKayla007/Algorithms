# predefined stack size

stack = []

choice = ""

while choice != "quit":
  choice = input("Enter choice (push, pop, peek, quit): ")
  match choice:
    case "push":
      if len(stack) >= 5:
        print("Stack overflow")
      else:
        pushinput = input("Enter value to push: ")
        stack.append(pushinput)
    
    case "pop":
      if len(stack) <= 0:
        print("Stack underflow")
      else:
        stack.pop()
        
    case "peek":
      if len(stack) <= 0:
        print("Stack empty")
      print(stack[len(stack)-1])
    

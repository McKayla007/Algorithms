# predefined queue size

queue = []

choice = ""

while choice != "quit":
  choice = input("Enter choice (enqueue, dequeue, peek, quit): ")
  match choice:
    case "enqueue":
      if len(queue) >= 5:
        print("Queue overflow")
      else:
        enqueueinput = input("Enter value to enqueue: ")
        queue.append(enqueueinput)
    
    case "dequeue":
      if len(queue) <= 0:
        print("Queue underflow")
      else:
        queue.remove(queue[0])
        
    case "peek":
      if len(queue) <= 0:
        print("Queue empty")
      print(queue[0])

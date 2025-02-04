counter = 0

def increaseCounter(counter):
    counter = counter + 1
    return counter

for i in range(0,3):
    counter = increaseCounter(counter)
    print("Counter:", counter)

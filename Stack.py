from queue import LifoQueue

stack = LifoQueue(maxsize=3)

stack.put(1)
stack.put(2)
stack.put(3)

print("Full: ", stack.full()) 
print("Size: ", stack.qsize())
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())
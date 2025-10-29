# Sai

"""
Stack is a linear Data Structure that follows LIFO (Last-in-Fist-out) principle. 
In stack both insertion and deletion takes place at one end, called the Top

Think of a stack of plates - the last plate you added to the stack will be the first one you take out

"""

"""
Available Operations: 
empty() : checks if the stack is empty
size() : Returns the number of elements in the stack
top()/peek() : shows the Top element without removing it
push(a) : adds an element 'a' at the top
pop() : removes the top element

"""

"""
Time: O(1)
Space: O(n)
"""

# Stack Implementation with List

class Stack:
    def __init__(self, stack):
        self.stack = stack if stack is not None else []

    def push(self,item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if len(self.stack) != 0:
            item = self.stack.pop()
            print(f"Popped: {item}")
        else: 
            return "Underflow"

    def top(self):
        return self.stack[-1] if len(self.stack) != 0 else "Empty Stack"

    def empty(self):
        return "Stack Not Empty" if len(self.stack) != 0 else "Empty Stack"

    def size(self):
        print(f"Stack of size: {len(self.stack)}")

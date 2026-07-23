"""
Big O Notation

Time Complexity:
    O(1)       Constant
    O(log n)   Logarithmic
    O(n)       Linear
    O(n log n) Linearithmic
    O(n²)      Quadratic
    O(2ⁿ)      Exponential
    O(n!)      Factorial

Space Complexity:
    O(1) to O(n!) depending on the algorithm.
"""

# no native stack only in py, but list has stack methods

# custom implemntation 
class Stack:
    def __init__(self):
        self.items = []
    def push(self, value):
        self.items.append(value)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def contains(self, value):
        return value in self.items
    def clear(self):
        self.items.clear()
    def __str__(self):
        return str(self.items)

# instatiation 

# Create a stack
stack = Stack()

# Push
stack.push(10)
stack.push(20)
stack.push(30)

print(stack)
# [10, 20, 30]

# Peek
print(stack.peek())
# 30

# Size
print(stack.size())
# 3

# Contains
print(stack.contains(20))
# True

print(stack.contains(99))
# False

# Pop
print(stack.pop())
# 30

print(stack)
# [10, 20]

# Is Empty
print(stack.is_empty())
# False

# Clear
stack.clear()

print(stack)
# []

print(stack.is_empty())
# True
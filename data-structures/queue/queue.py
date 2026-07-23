from collections import deque

"""
Queue (FIFO - First In, First Out)

Implementation:
    Python: collections.deque (recommended)
    Custom: Singly Linked List (head + tail)

Time Complexity:
    Enqueue (append)     O(1)
    Dequeue (popleft)    O(1)
    Peek (front)         O(1)
    Is Empty             O(1)
    Size                 O(1)
    Contains             O(n)
    Clear                O(n)

Space Complexity:
    O(n)
"""
# python native uses deque
queue = deque()

# Enqueue
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")
print(queue)
# deque(['Alice', 'Bob', 'Charlie'])

# Dequeue
first = queue.popleft()
print(first)
# Alice
print(queue)
# deque(['Bob', 'Charlie'])
queue.appendleft("Alice")  # prepend

# custom implmentaion
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value
    
    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

# custom instatiatioon 


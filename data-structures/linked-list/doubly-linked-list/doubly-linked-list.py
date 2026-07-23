"""
Doubly Linked List

Time Complexity:
    Access: O(n)
    Search: O(n)
    Prepend: O(1)
    Append: O(1)
    Insert: O(n)
    Remove: O(n)

Space Complexity:
    O(n)
"""

# no python native version

# custom implementation 
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
    
    def get(self, index):
        self._validate_index(index)
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        return current
    
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(value)
            return 
        if index == self.size:
            self.append(value)
            return
        
        node = Node(value)
        current = self.get(index)
        
        node.prev = current.prev
        node.next = current

        current.prev.next = node
        current.prev = node

        self.size += 1

    def remove(self, index):
        self._validate_index(index)

        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return removed.value
        
        removed = self.get(index)
        removed.prev.next = removed.next
        if removed.next:
            removed.next.prev = removed.prev
        else:
            self.tail = removed.prev

        self.size -= 1
        return removed.value
        
    def _validate_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
    def __len__(self):
        return self.size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return " <-> ".join(str(value) for value in self) + " <-> None"
    
# instantiation 
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(20)
    dll.append(30)
    dll.prepend(10)

    print(dll)                     # 10 <-> 20 <-> 30 <-> None
    print(len(dll))                # 3

    print(dll.get(1).value)        # 20
    print(dll.find(30).value)      # 30

    dll.insert(2, 25)
    print(dll)                     # 10 <-> 20 <-> 25 <-> 30 <-> None

    removed = dll.remove(1)
    print(f"Removed: {removed}")   # 20
    print(dll)                     # 10 <-> 25 <-> 30 <-> None

    for value in dll:
        print(value)
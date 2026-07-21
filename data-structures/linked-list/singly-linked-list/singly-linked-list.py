"""
Singly Linked List
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

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def get(self, index):
        self._validate_index(index)
        current = self.head
        for _ in range(index):
            current = current.next
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
        
        previous = self.get(index - 1)
        node = Node(value)
        node.next = previous.next
        previous.next = node
        self.size += 1

    def remove(self, index):
        self._validate_index(index)
        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return removed.value

        previous = self.get(index - 1)
        removed = previous.next
        previous.next = removed.next
        if removed == self.tail:
            self.tail = previous
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
        return " -> ".join(str(value) for value in self) + " -> None"
    
########################################################################
    
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.prepend(5)

    print(linked_list)
    print(len(linked_list))

    print(linked_list.get(1).value)
    print(linked_list.find(20).value)

    linked_list.insert(2, 15)
    print(linked_list)

    removed = linked_list.remove(1)
    print(f"Removed: {removed}")
    print(linked_list)

    for value in linked_list:
        print(value)
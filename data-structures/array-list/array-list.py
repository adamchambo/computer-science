"""
Dynamic Array (Array List)

Time Complexity:
    Access (index): O(1)
    Update (index): O(1)
    Search (value): O(n)
    Append: O(1) amortized
    Insert: O(n)
    Delete: O(n)

Space Complexity:
    O(n)

Note:
    - Elements are stored contiguously in memory.
    - Insert/Delete require shifting elements.
    - Append may trigger a resize (O(n)), but averages O(1).
"""

lst = [37, 348, 28, 4]

# Access
print(lst[1])   # 348

# Update
lst[2] = 100
print(lst)                      # [37, 348, 100, 4]

# Search
print(348 in lst)               # True
print(lst.index(348))           # 1

# Append
lst.append(10)
print(lst)                      # [37, 348, 100, 4, 10]

# Extend
lst.extend([20, 30])
print(lst)                      # [37, 348, 100, 4, 10, 20, 30]

# Insert
lst.insert(2, 99)
print(lst)                      # [37, 348, 99, 100, 4, 10, 20, 30]

# Count
print(lst.count(20))            # 1

# Remove by value
lst.remove(99)
print(lst)                      # [37, 348, 100, 4, 10, 20, 30]

# Remove last
last = lst.pop()
print(last)                     # 30
print(lst)                      # [37, 348, 100, 4, 10, 20]

# Remove by index
removed = lst.pop(1)
print(removed)                  # 348
print(lst)                      # [37, 100, 4, 10, 20]

# Sort
lst.sort()
print(lst)                      # [4, 10, 20, 37, 100]

# Reverse
lst.reverse()
print(lst)                      # [100, 37, 20, 10, 4]

# Copy
copy = lst.copy()
print(copy)                     # [100, 37, 20, 10, 4]

# Length
print(len(lst))                 # 5

# Clear
lst.clear()
print(lst)                      # []
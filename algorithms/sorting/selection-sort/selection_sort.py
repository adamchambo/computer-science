"""
Sorts an array using Selection Sort.

Time Complexity:
    Best: O(n²)
    Average: O(n²)
    Worst: O(n²)
    
Space Complexity:
    O(1)
"""

## mutative
def selection_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max = None
        for j in range(i + 1):
            if max == None or arr[j] > arr[max]:
                max = j
        temp = arr[max]
        arr[max] = arr[i]
        arr[i] = temp


test = [5,8,2,7,3]
selection_sort(test)
print(test)
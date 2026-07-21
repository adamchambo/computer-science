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

list = [37, 348, 28, 4]
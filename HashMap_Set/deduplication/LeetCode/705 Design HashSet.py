"""
LeetCode 705 - Design HashSet

Build a HashSet without using Python's built-in set. Support add(key),
remove(key), and contains(key). Keys are integers from 0 through 1,000,000.

Methods that do not return a value have expected result None.
"""

# region Inputs
operations = [
    "add",
    "add",
    "contains",
    "contains",
    "add",
    "contains",
    "remove",
    "contains",
]
arguments = [1, 2, 1, 3, 2, 2, 2, 2]
expected = [None, None, True, False, None, True, None, False]
# endregion


# region Methods
class MyHashSet:
    def __init__(self):
        pass

    def add(self, key):
        pass

    def remove(self, key):
        pass

    def contains(self, key):
        pass


# endregion


# region Calls
hash_set = MyHashSet()
result = []
for operation, argument in zip(operations, arguments):
    result.append(getattr(hash_set, operation)(argument))
# endregion


# region Print
print("Result:  ", result)
print("Expected:", expected)
# endregion

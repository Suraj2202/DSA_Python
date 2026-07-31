"""
LeetCode 706 - Design HashMap

Build a HashMap without using Python's built-in dictionary. Support
put(key, value), get(key), and remove(key). get must return -1 when a key does
not exist. Keys and values are integers from 0 through 1,000,000.
"""

# region Inputs
operations = ["put", "put", "get", "get", "put", "get", "remove", "get"]
arguments = [(1, 1), (2, 2), (1,), (3,), (2, 1), (2,), (2,), (2,)]
expected = [None, None, 1, -1, None, 1, None, -1]
# endregion


# region Methods
class MyHashMap:
    def __init__(self):
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass


# endregion


# region Calls
hash_map = MyHashMap()
result = []
for operation, argument in zip(operations, arguments):
    result.append(getattr(hash_map, operation)(*argument))
# endregion


# region Print
print("Result:  ", result)
print("Expected:", expected)
# endregion

"""
LeetCode 380 - Insert Delete GetRandom O(1)

Build a RandomizedSet that stores unique integers. insert(value) returns True
only when the value was absent. remove(value) returns True only when it existed.
get_random() returns a uniformly random stored value. Every method must run in
average O(1) time.
"""

# region Inputs
operations = [
    "insert",
    "remove",
    "insert",
    "get_random",
    "remove",
    "insert",
    "get_random",
]
arguments = [(1,), (2,), (2,), (), (1,), (2,), ()]
expected = [True, False, True, {1, 2}, True, False, {2}]
# For get_random, the expected set contains every valid result at that step.
# endregion


# region Methods
class RandomizedSet:
    def __init__(self):
        pass

    def insert(self, value):
        pass

    def remove(self, value):
        pass

    def get_random(self):
        pass


# endregion


# region Calls
randomized_set = RandomizedSet()
result = []
for operation, argument in zip(operations, arguments):
    result.append(getattr(randomized_set, operation)(*argument))
# endregion


# region Print
print("Result:  ", result)
print("Expected:", expected)
# endregion

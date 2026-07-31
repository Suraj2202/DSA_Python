"""
LeetCode 205 - Isomorphic Strings

Given strings source and target, return True if characters in source can be
replaced to produce target. Every occurrence of a character must map to the
same character, and two source characters cannot map to one target character.
A character may map to itself.
"""

# region Inputs
source1, target1, expected1 = "egg", "add", True
source2, target2, expected2 = "foo", "bar", False
source3, target3, expected3 = "paper", "title", True
# endregion


# region Methods
def is_isomorphic(source, target):
    pass


# endregion


# region Calls
result1 = is_isomorphic(source1, target1)
result2 = is_isomorphic(source2, target2)
result3 = is_isomorphic(source3, target3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

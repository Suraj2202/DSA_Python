"""
LeetCode 242 - Valid Anagram

Given two strings source and target, return True if target is an anagram of
source, and False otherwise. An anagram uses every original character exactly
once, but may arrange the characters in a different order.

Constraints: strings contain lowercase English letters.
"""

# region Inputs
source1, target1, expected1 = "anagram", "nagaram", True
source2, target2, expected2 = "rat", "car", False
source3, target3, expected3 = "aacc", "ccac", False
# endregion


# region Methods
def is_anagram(source, target):
    pass


# endregion


# region Calls
result1 = is_anagram(source1, target1)
result2 = is_anagram(source2, target2)
result3 = is_anagram(source3, target3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

"""
LeetCode 387 - First Unique Character in a String

Given a string text, return the index of its first non-repeating character.
Return -1 if every character repeats.

Constraints: text contains lowercase English letters.
"""

# region Inputs
text1, expected1 = "leetcode", 0
text2, expected2 = "loveleetcode", 2
text3, expected3 = "aabb", -1
# endregion


# region Methods
def first_unique_character(text):
    pass


# endregion


# region Calls
result1 = first_unique_character(text1)
result2 = first_unique_character(text2)
result3 = first_unique_character(text3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

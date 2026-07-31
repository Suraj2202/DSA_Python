"""
LeetCode 383 - Ransom Note

Given strings ransom_note and magazine, return True if ransom_note can be
constructed using letters from magazine. Each magazine letter may be used only
once.

Constraints: strings contain lowercase English letters.
"""

# region Inputs
ransom_note1, magazine1, expected1 = "a", "b", False
ransom_note2, magazine2, expected2 = "aa", "ab", False
ransom_note3, magazine3, expected3 = "aa", "aab", True
# endregion


# region Methods
def can_construct(ransom_note, magazine):
    pass


# endregion


# region Calls
result1 = can_construct(ransom_note1, magazine1)
result2 = can_construct(ransom_note2, magazine2)
result3 = can_construct(ransom_note3, magazine3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

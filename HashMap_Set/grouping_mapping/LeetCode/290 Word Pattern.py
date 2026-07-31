"""
LeetCode 290 - Word Pattern

Given a pattern and a space-separated string text, return True if the pattern
and words follow the same one-to-one mapping. Each pattern character must map
to exactly one word, and each word to exactly one character.
"""

# region Inputs
pattern1, text1, expected1 = "abba", "dog cat cat dog", True
pattern2, text2, expected2 = "abba", "dog cat cat fish", False
pattern3, text3, expected3 = "aaaa", "dog cat cat dog", False
# endregion


# region Methods
def word_pattern(pattern, text):
    pass


# endregion


# region Calls
result1 = word_pattern(pattern1, text1)
result2 = word_pattern(pattern2, text2)
result3 = word_pattern(pattern3, text3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

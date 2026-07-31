"""
LeetCode 451 - Sort Characters By Frequency

Given a string text, sort it in decreasing order based on character frequency.
Return the sorted string. Characters with equal frequencies may appear in any
order.
"""

# region Inputs
text1, expected1 = "tree", ["eert", "eetr"]
text2, expected2 = "cccaaa", ["cccaaa", "aaaccc"]
text3, expected3 = "Aabb", ["bbAa", "bbaA"]
# endregion


# region Methods
def frequency_sort(text):
    pass


# endregion


# region Calls
result1 = frequency_sort(text1)
result2 = frequency_sort(text2)
result3 = frequency_sort(text3)
# endregion


# region Print
print("Case 1:", result1, "Expected one of:", expected1)
print("Case 2:", result2, "Expected one of:", expected2)
print("Case 3:", result3, "Expected one of:", expected3)
# endregion

"""
LeetCode 49 - Group Anagrams

Given an array of strings words, group the anagrams together. Anagrams contain
the same characters with the same frequencies. Groups and words inside each
group may be returned in any order.
"""

# region Inputs
words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

words2, expected2 = [""], [[""]]
words3, expected3 = ["a"], [["a"]]
# endregion


# region Methods
def group_anagrams(words):
    pass


# endregion


# region Calls
result1 = group_anagrams(words1)
result2 = group_anagrams(words2)
result3 = group_anagrams(words3)
# endregion


# region Print
print("Case 1:", result1, "Expected (any group order):", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

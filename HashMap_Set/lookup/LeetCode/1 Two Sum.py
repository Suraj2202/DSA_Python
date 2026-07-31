"""
LeetCode 1 - Two Sum

Given an integer array nums and an integer target, return the indices of two
different numbers whose sum equals target. Exactly one answer exists, and the
indices may be returned in any order.
"""

# region Inputs
nums1, target1, expected1 = [2, 7, 11, 15], 9, [0, 1]
nums2, target2, expected2 = [3, 2, 4], 6, [1, 2]
nums3, target3, expected3 = [3, 3], 6, [0, 1]
# endregion


# region Methods
def two_sum(nums, target):
    pass


# endregion


# region Calls
result1 = two_sum(nums1, target1)
result2 = two_sum(nums2, target2)
result3 = two_sum(nums3, target3)
# endregion


# region Print
print("Case 1:", result1, "Expected (any order):", expected1)
print("Case 2:", result2, "Expected (any order):", expected2)
print("Case 3:", result3, "Expected (any order):", expected3)
# endregion

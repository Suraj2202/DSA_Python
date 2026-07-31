"""
LeetCode 128 - Longest Consecutive Sequence

Given an unsorted integer array nums, return the length of the longest sequence
of consecutive values. The values do not need to be adjacent in the input.

Requirement: the algorithm must run in O(n) time.
"""

# region Inputs
nums1, expected1 = [100, 4, 200, 1, 3, 2], 4
nums2, expected2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9
nums3, expected3 = [], 0
# endregion


# region Methods
def longest_consecutive(nums):
    pass


# endregion


# region Calls
result1 = longest_consecutive(nums1)
result2 = longest_consecutive(nums2)
result3 = longest_consecutive(nums3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

"""
LeetCode 525 - Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray
containing an equal number of 0 values and 1 values.
"""

# region Inputs
nums1, expected1 = [0, 1], 2
nums2, expected2 = [0, 1, 0], 2
nums3, expected3 = [0, 0, 1, 1, 0], 4
# endregion


# region Methods
def find_max_length(nums):
    pass


# endregion


# region Calls
result1 = find_max_length(nums1)
result2 = find_max_length(nums2)
result3 = find_max_length(nums3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

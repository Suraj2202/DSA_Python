"""
LeetCode 349 - Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array containing their
unique common values. The answer may be returned in any order.
"""

# region Inputs
nums1a, nums1b, expected1 = [1, 2, 2, 1], [2, 2], [2]
nums2a, nums2b, expected2 = [4, 9, 5], [9, 4, 9, 8, 4], [4, 9]
nums3a, nums3b, expected3 = [1, 2, 3], [4, 5, 6], []
# endregion


# region Methods
def intersection(nums1, nums2):
    pass


# endregion


# region Calls
result1 = intersection(nums1a, nums1b)
result2 = intersection(nums2a, nums2b)
result3 = intersection(nums3a, nums3b)
# endregion


# region Print
print("Case 1:", result1, "Expected (any order):", expected1)
print("Case 2:", result2, "Expected (any order):", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

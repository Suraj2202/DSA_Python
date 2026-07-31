"""
LeetCode 219 - Contains Duplicate II

Given an integer array nums and integer k, return True when two different
indices i and j contain equal values and abs(i - j) <= k. Otherwise return
False.
"""

# region Inputs
nums1, k1, expected1 = [1, 2, 3, 1], 3, True
nums2, k2, expected2 = [1, 0, 1, 1], 1, True
nums3, k3, expected3 = [1, 2, 3, 1, 2, 3], 2, False
# endregion


# region Methods
def contains_nearby_duplicate(nums, k):
    pass


# endregion


# region Calls
result1 = contains_nearby_duplicate(nums1, k1)
result2 = contains_nearby_duplicate(nums2, k2)
result3 = contains_nearby_duplicate(nums3, k3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

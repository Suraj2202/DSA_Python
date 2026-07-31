"""
LeetCode 454 - 4Sum II

Given four integer arrays of equal length, return the number of index tuples
(i, j, k, l) for which nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.
"""

# region Inputs
nums1a, nums1b = [1, 2], [-2, -1]
nums1c, nums1d, expected1 = [-1, 2], [0, 2], 2

nums2a, nums2b = [0], [0]
nums2c, nums2d, expected2 = [0], [0], 1

nums3a, nums3b = [-1, -1], [-1, 1]
nums3c, nums3d, expected3 = [-1, 1], [1, -1], 6
# endregion


# region Methods
def four_sum_count(nums1, nums2, nums3, nums4):
    pass


# endregion


# region Calls
result1 = four_sum_count(nums1a, nums1b, nums1c, nums1d)
result2 = four_sum_count(nums2a, nums2b, nums2c, nums2d)
result3 = four_sum_count(nums3a, nums3b, nums3c, nums3d)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

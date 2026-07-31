"""
LeetCode 560 - Subarray Sum Equals K

Given an integer array nums and integer k, return the total number of contiguous
non-empty subarrays whose sum equals k. nums may contain negative values, so a
normal shrinking sliding window does not work.
"""

# region Inputs
nums1, k1, expected1 = [1, 1, 1], 2, 2
nums2, k2, expected2 = [1, 2, 3], 3, 2
nums3, k3, expected3 = [1, -1, 0], 0, 3
# endregion


# region Methods
def subarray_sum(nums, k):
    pass


# endregion


# region Calls
result1 = subarray_sum(nums1, k1)
result2 = subarray_sum(nums2, k2)
result3 = subarray_sum(nums3, k3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

"""
LeetCode 974 - Subarray Sums Divisible by K

Given an integer array nums and positive integer k, return the number of
contiguous non-empty subarrays whose sum is divisible by k. A sum is divisible
by k when its remainder is 0.
"""

# region Inputs
nums1, k1, expected1 = [4, 5, 0, -2, -3, 1], 5, 7
nums2, k2, expected2 = [5], 9, 0
nums3, k3, expected3 = [-1, 2, 9], 2, 2
# endregion


# region Methods
def subarrays_div_by_k(nums, k):
    pass


# endregion


# region Calls
result1 = subarrays_div_by_k(nums1, k1)
result2 = subarrays_div_by_k(nums2, k2)
result3 = subarrays_div_by_k(nums3, k3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

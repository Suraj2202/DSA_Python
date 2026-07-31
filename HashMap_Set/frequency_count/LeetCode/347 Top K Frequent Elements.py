"""
LeetCode 347 - Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent
elements. The answer may be returned in any order.

Requirement: solve it faster than O(n log n), where n is len(nums).
"""

# region Inputs
nums1, k1, expected1 = [1, 1, 1, 2, 2, 3], 2, [1, 2]
nums2, k2, expected2 = [1], 1, [1]
nums3, k3, expected3 = [4, 4, 4, 4, 6, 6, 7], 2, [4, 6]
# endregion


# region Methods
def top_k_frequent(nums, k):
    pass


# endregion


# region Calls
result1 = top_k_frequent(nums1, k1)
result2 = top_k_frequent(nums2, k2)
result3 = top_k_frequent(nums3, k3)
# endregion


# region Print
print("Case 1:", result1, "Expected (any order):", expected1)
print("Case 2:", result2, "Expected (any order):", expected2)
print("Case 3:", result3, "Expected (any order):", expected3)
# endregion

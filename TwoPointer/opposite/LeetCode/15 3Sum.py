"""
LeetCode 15 — 3Sum
Problem Statement

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# region Inputs
nums1 = [-1, 0, 1, 2, -1, -4]   # Expected: [[-1, -1, 2], [-1, 0, 1]]
nums2 = [0, 1, 1]               # Expected: []
nums3 = [0, 0, 0]               # Expected: [[0, 0, 0]]
# endregion


# region Methods
def brute_force_three_sum(nums):
    pass


def two_pointer_three_sum(nums):
    pass
# endregion


# region Calls
brute1 = brute_force_three_sum(nums1)
brute2 = brute_force_three_sum(nums2)
brute3 = brute_force_three_sum(nums3)

twoPointer1 = two_pointer_three_sum(nums1)
twoPointer2 = two_pointer_three_sum(nums2)
twoPointer3 = two_pointer_three_sum(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

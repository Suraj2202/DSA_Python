"""
LeetCode 18 — 4Sum
Problem Statement

Given an array nums of n integers and an integer target, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

# region Inputs
# Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
nums1, target1 = [1, 0, -1, 0, -2, 2], 0
nums2, target2 = [2, 2, 2, 2, 2],      8    # Expected: [[2, 2, 2, 2]]
nums3, target3 = [1, 2, 3, 4],         10   # Expected: [[1, 2, 3, 4]]
# endregion


# region Methods
def brute_force_four_sum(nums, target):
    pass


def two_pointer_four_sum(nums, target):
    pass
# endregion


# region Calls
brute1 = brute_force_four_sum(nums1, target1)
brute2 = brute_force_four_sum(nums2, target2)
brute3 = brute_force_four_sum(nums3, target3)

twoPointer1 = two_pointer_four_sum(nums1, target1)
twoPointer2 = two_pointer_four_sum(nums2, target2)
twoPointer3 = two_pointer_four_sum(nums3, target3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

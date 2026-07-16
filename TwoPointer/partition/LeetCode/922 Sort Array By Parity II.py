"""
LeetCode 922 — Sort Array By Parity II
Problem Statement

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
"""

# region Inputs
# Expected: [4, 5, 2, 7]  (any valid even/odd index placement)
nums1 = [4, 2, 5, 7]
nums2 = [2, 3]         # Expected: [2, 3]
# Expected: [0, 1, 2, 3]  (any valid even/odd index placement)
nums3 = [0, 1, 2, 3]
# endregion


# region Methods
def brute_force_sort_array_by_parity_ii(nums):
    pass


def two_pointer_sort_array_by_parity_ii(nums):
    pass
# endregion


# region Calls
brute1 = brute_force_sort_array_by_parity_ii(nums1)
brute2 = brute_force_sort_array_by_parity_ii(nums2)
brute3 = brute_force_sort_array_by_parity_ii(nums3)

twoPointer1 = two_pointer_sort_array_by_parity_ii(nums1)
twoPointer2 = two_pointer_sort_array_by_parity_ii(nums2)
twoPointer3 = two_pointer_sort_array_by_parity_ii(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

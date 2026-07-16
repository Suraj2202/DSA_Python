"""
LeetCode 283 — Move Zeroes
Problem Statement

Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Note: Also a Fast & Slow Pointer pattern — slow tracks insert position, fast finds non-zero elements.
"""

# region Inputs
nums1 = [0, 1, 0, 3, 12]   # Expected: [1, 3, 12, 0, 0]
nums2 = [0]                # Expected: [0]
nums3 = [1, 0, 0, 1]       # Expected: [1, 1, 0, 0]
# endregion


# region Methods
def brute_force_move_zeroes(nums):
    pass


def two_pointer_move_zeroes(nums):
    pass
# endregion


# region Calls
brute1 = brute_force_move_zeroes(nums1)
brute2 = brute_force_move_zeroes(nums2)
brute3 = brute_force_move_zeroes(nums3)

twoPointer1 = two_pointer_move_zeroes(nums1)
twoPointer2 = two_pointer_move_zeroes(nums2)
twoPointer3 = two_pointer_move_zeroes(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

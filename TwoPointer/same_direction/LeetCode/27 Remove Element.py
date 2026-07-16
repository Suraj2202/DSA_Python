"""
LeetCode 27 — Remove Element
Problem Statement

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k.
Change the array nums such that the first k elements contain the elements not equal to val.
The remaining elements of nums are not important, as well as the size of nums.
Return k.

Note: Also a Fast & Slow Pointer pattern — slow tracks insert position, fast scans ahead.
"""

# region Inputs
nums1, val1 = [3, 2, 2, 3],          3   # Expected: 2  (nums = [2, 2, ...])
# Expected: 5  (nums = [0,1,3,0,4,...])
nums2, val2 = [0, 1, 2, 2, 3, 0, 4, 2], 2
nums3, val3 = [1],                   1   # Expected: 0
# endregion


# region Methods
def brute_force_remove_element(nums, val):
    pass


def two_pointer_remove_element(nums, val):
    pass
# endregion


# region Calls
brute1 = brute_force_remove_element(nums1, val1)
brute2 = brute_force_remove_element(nums2, val2)
brute3 = brute_force_remove_element(nums3, val3)

twoPointer1 = two_pointer_remove_element(nums1, val1)
twoPointer2 = two_pointer_remove_element(nums2, val2)
twoPointer3 = two_pointer_remove_element(nums3, val3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

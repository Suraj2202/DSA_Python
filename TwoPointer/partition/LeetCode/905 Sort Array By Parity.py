"""
LeetCode 905 — Sort Array By Parity
Problem Statement

Given an integer array nums, move all the even integers at the beginning of the array
followed by all the odd integers.

Return any array that satisfies this condition.
"""

# region Inputs
nums1 = [3, 1, 2, 4]  # Expected: [2, 4, 3, 1]  (any valid even-first order)
nums2 = [0]  # Expected: [0]
nums3 = [1, 3, 2, 4]  # Expected: [2, 4, 1, 3]  (any valid even-first order)
# endregion


# region Methods
def brute_force_sort_array_by_parity(nums):
    result = [0] * len(nums)

    # Insert will have n complexity, as it will shift that many item
    left, right = 0, -1
    for x in nums:
        if x % 2 == 0:
            result[left] = x
            left += 1
        else:
            result[right] = x
            right -= 1
    return result


def two_pointer_sort_array_by_parity(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


# endregion


# region Calls
brute1 = brute_force_sort_array_by_parity(nums1)
brute2 = brute_force_sort_array_by_parity(nums2)
brute3 = brute_force_sort_array_by_parity(nums3)

twoPointer1 = two_pointer_sort_array_by_parity(nums1)
twoPointer2 = two_pointer_sort_array_by_parity(nums2)
twoPointer3 = two_pointer_sort_array_by_parity(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

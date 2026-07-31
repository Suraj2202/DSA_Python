"""
LeetCode 977 — Squares of a Sorted Array
Problem Statement

Given an integer array nums sorted in non-decreasing order, return an array of the squares
of each number sorted in non-decreasing order.
"""

# region Inputs
nums1 = [-4, -1, 0, 3, 10]  # Expected: [0, 1, 9, 16, 100]
nums2 = [-7, -3, 2, 3, 11]  # Expected: [4, 9, 9, 49, 121]
nums3 = [-3, -1]  # Expected: [1, 9]
# endregion


# region Methods
def brute_force_squares_of_sorted_array(nums):
    res = [0] * len(nums)
    for i in range(len(nums)):
        res[i] = nums[i] ** 2

    res.sort()
    return res


def two_pointer_squares_of_sorted_array(nums):
    print(nums)
    l, r = 0, len(nums) - 1
    res = [0] * len(nums)
    insert_pos = r

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res[insert_pos] = nums[l] ** 2
            l += 1
            insert_pos -= 1
        else:
            res[insert_pos] = nums[r] ** 2
            r -= 1
            insert_pos -= 1

    return res


# endregion


# region Calls
brute1 = brute_force_squares_of_sorted_array(nums1)
brute2 = brute_force_squares_of_sorted_array(nums2)
brute3 = brute_force_squares_of_sorted_array(nums3)

twoPointer1 = two_pointer_squares_of_sorted_array(nums1)
twoPointer2 = two_pointer_squares_of_sorted_array(nums2)
twoPointer3 = two_pointer_squares_of_sorted_array(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

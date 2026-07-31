"""
LeetCode 75 — Sort Colors
Problem Statement

Given an array nums with n objects colored red, white, or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Note: Classic Dutch National Flag problem — uses 3-way partition with two pointers.
"""

# region Inputs
nums1 = [2, 0, 2, 1, 1, 0]  # Expected: [0, 0, 1, 1, 2, 2]
nums2 = [2, 0, 1]  # Expected: [0, 1, 2]
nums3 = [0]  # Expected: [0]
# endregion


# region Methods
# Hint:
# Count how many 0s.
# Count how many 1s.
# Count how many 2s.
# Rewrite the array.
def brute_force_sort_colors(nums):
    count = [0, 0, 0]

    for num in nums:
        count[num] += 1

    index = 0

    for color in range(3):
        while count[color] > 0:
            nums[index] = color
            index += 1
            count[color] -= 1

    return nums


def two_pointer_sort_colors(nums):
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


# endregion


# region Calls
brute1 = brute_force_sort_colors(nums1)
brute2 = brute_force_sort_colors(nums2)
brute3 = brute_force_sort_colors(nums3)

twoPointer1 = two_pointer_sort_colors(nums1)
twoPointer2 = two_pointer_sort_colors(nums2)
twoPointer3 = two_pointer_sort_colors(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

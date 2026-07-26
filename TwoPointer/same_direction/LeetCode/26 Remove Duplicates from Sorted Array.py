"""
LeetCode 26 — Remove Duplicates from Sorted Array
Problem Statement

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
such that each unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k.
Change the array nums such that the first k elements contain the unique elements in the order
they were present in nums originally. The remaining elements are not important.
Return k.

Note: Also a Fast & Slow Pointer pattern — slow marks the last unique position, fast finds the next unique.
"""

# region Inputs
nums1 = [1, 1, 2]  # Expected: 2  (nums = [1, 2, ...])
# Expected: 5  (nums = [0,1,2,3,4,...])
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums3 = [1]  # Expected: 1
# endregion


# region Methods
def brute_force_remove_duplicates(nums):
    res = []

    for x in nums:
        if x not in res:
            res.append(x)
    return len(res), res


def two_pointer_remove_duplicates(nums):
    write = 1
    for current in range(1, len(nums)):
        if nums[current] != nums[write - 1]:
            nums[write]=nums[current]
            write +=1
    return write, nums[:write]


# endregion


# region Calls
brute1 = brute_force_remove_duplicates(nums1)
brute2 = brute_force_remove_duplicates(nums2)
brute3 = brute_force_remove_duplicates(nums3)

twoPointer1 = two_pointer_remove_duplicates(nums1)
twoPointer2 = two_pointer_remove_duplicates(nums2)
twoPointer3 = two_pointer_remove_duplicates(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

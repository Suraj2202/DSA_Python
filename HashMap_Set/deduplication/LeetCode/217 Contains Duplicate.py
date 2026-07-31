"""
LeetCode 217 - Contains Duplicate

Given an integer array nums, return True if any value appears at least twice in
the array. Return False if every element is distinct.

Constraints:
- 1 <= len(nums) <= 100000
- -10^9 <= nums[i] <= 10^9
"""

# region Inputs
nums1 = [1, 2, 3, 1]
expected1 = True

nums2 = [1, 2, 3, 4]
expected2 = False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
expected3 = True
# endregion


# region Methods
def contains_duplicate(nums):
    pass


# endregion


# region Calls
result1 = contains_duplicate(nums1)
result2 = contains_duplicate(nums2)
result3 = contains_duplicate(nums3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion

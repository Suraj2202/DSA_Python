"""
LeetCode 350 — Intersection of Two Arrays II
Problem Statement

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
"""

# region Inputs
nums1_1, nums2_1 = [1, 2, 2, 1], [2, 2]           # Expected: [2, 2]
nums1_2, nums2_2 = [4, 9, 5],    [9, 4, 9, 8, 4]  # Expected: [4, 9]
nums1_3, nums2_3 = [1],          [1]               # Expected: [1]
# endregion


# region Methods
def brute_force_intersection_of_two_arrays_ii(nums1, nums2):
    pass


def two_pointer_intersection_of_two_arrays_ii(nums1, nums2):
    pass
# endregion


# region Calls
brute1 = brute_force_intersection_of_two_arrays_ii(nums1_1, nums2_1)
brute2 = brute_force_intersection_of_two_arrays_ii(nums1_2, nums2_2)
brute3 = brute_force_intersection_of_two_arrays_ii(nums1_3, nums2_3)

twoPointer1 = two_pointer_intersection_of_two_arrays_ii(nums1_1, nums2_1)
twoPointer2 = two_pointer_intersection_of_two_arrays_ii(nums1_2, nums2_2)
twoPointer3 = two_pointer_intersection_of_two_arrays_ii(nums1_3, nums2_3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

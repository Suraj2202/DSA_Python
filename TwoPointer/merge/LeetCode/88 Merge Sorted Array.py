"""
LeetCode 88 — Merge Sorted Array
Problem Statement

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers
m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
"""

# region Inputs
nums1_1, m1, nums2_1, n1 = [1, 2, 3, 0, 0, 0], 3, [
    2, 5, 6], 3   # Expected: [1, 2, 2, 3, 5, 6]
nums1_2, m2, nums2_2, n2 = [
    1],                 1, [],        0   # Expected: [1]
nums1_3, m3, nums2_3, n3 = [0],                 0, [
    1],       1   # Expected: [1]
# endregion


# region Methods
def brute_force_merge_sorted_array(nums1, m, nums2, n):
    pass


def two_pointer_merge_sorted_array(nums1, m, nums2, n):
    pass
# endregion


# region Calls
brute1 = brute_force_merge_sorted_array(nums1_1[:], m1, nums2_1[:], n1)
brute2 = brute_force_merge_sorted_array(nums1_2[:], m2, nums2_2[:], n2)
brute3 = brute_force_merge_sorted_array(nums1_3[:], m3, nums2_3[:], n3)

twoPointer1 = two_pointer_merge_sorted_array(nums1_1[:], m1, nums2_1[:], n1)
twoPointer2 = two_pointer_merge_sorted_array(nums1_2[:], m2, nums2_2[:], n2)
twoPointer3 = two_pointer_merge_sorted_array(nums1_3[:], m3, nums2_3[:], n3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

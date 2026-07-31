"""
LeetCode 349 — Intersection of Two Arrays
Problem Statement

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
"""

# region Inputs
nums1_1, nums2_1 = [1, 2, 2, 1], [2, 2]  # Expected: [2]
nums1_2, nums2_2 = [4, 9, 5], [9, 4, 9, 8, 4]  # Expected: [9, 4]
nums1_3, nums2_3 = [1], [1]  # Expected: [1]
# endregion


# region Methods
def brute_force_intersection_of_two_arrays(nums1, nums2):
    result = []

    for x in nums1:
        for y in nums2:
            if x == y and x not in result:
                result.append(x)
    return result


def two_pointer_intersection_of_two_arrays(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = j = 0
    result = []

    while i < len(nums1) and j < len(nums2):

        if nums1[i] == nums2[j]:
            result.append(nums1[i])

            i += 1
            j += 1

            while i < len(nums1) and i > 0 and nums1[i] == nums1[i - 1]:
                i += 1

            while j < len(nums2) and j > 0 and nums2[j] == nums2[j - 1]:
                j += 1

        elif nums1[i] < nums2[j]:
            i += 1

        else:
            j += 1

    return result


# endregion


# region Calls
brute1 = brute_force_intersection_of_two_arrays(nums1_1, nums2_1)
brute2 = brute_force_intersection_of_two_arrays(nums1_2, nums2_2)
brute3 = brute_force_intersection_of_two_arrays(nums1_3, nums2_3)

twoPointer1 = two_pointer_intersection_of_two_arrays(nums1_1, nums2_1)
twoPointer2 = two_pointer_intersection_of_two_arrays(nums1_2, nums2_2)
twoPointer3 = two_pointer_intersection_of_two_arrays(nums1_3, nums2_3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

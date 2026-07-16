"""
LeetCode 643 — Maximum Average Subarray I
Problem Statement

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value as a float.

Any answer with a calculation error less than 10^-5 will be accepted.
"""

# region Inputs
nums1, k1 = [1, 12, -5, -6, 50, 3], 4   # Expected: 12.75
nums2, k2 = [5],                    1   # Expected: 5.0
nums3, k3 = [0, 4, 0, 3, 2],        1   # Expected: 4.0
# endregion


# region Methods
def brute_force_maximum_average_subarray(nums, k):
    pass


def fixed_sliding_window_maximum_average_subarray(nums, k):
    pass
# endregion


# region Calls
brute1 = brute_force_maximum_average_subarray(nums1, k1)
brute2 = brute_force_maximum_average_subarray(nums2, k2)
brute3 = brute_force_maximum_average_subarray(nums3, k3)

sliding1 = fixed_sliding_window_maximum_average_subarray(nums1, k1)
sliding2 = fixed_sliding_window_maximum_average_subarray(nums2, k2)
sliding3 = fixed_sliding_window_maximum_average_subarray(nums3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

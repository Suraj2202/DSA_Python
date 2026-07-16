"""
LeetCode 2090 — K Radius Subarray Averages
Problem Statement

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k
is the average of all elements in nums between the indices i - k and i + k (inclusive).
If there are fewer than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray
centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division.
"""

# region Inputs
# Expected: [-1, -1, -1, 5, 4, 4, -1, -1, -1]
nums1, k1 = [7, 4, 3, 9, 1, 8, 5, 2, 6], 3
nums2, k2 = [100000],                     0   # Expected: [100000]
nums3, k3 = [8],                     100000   # Expected: [-1]
# endregion


# region Methods
def brute_force_k_radius_subarray_averages(nums, k):
    pass


def fixed_sliding_window_k_radius_subarray_averages(nums, k):
    pass
# endregion


# region Calls
brute1 = brute_force_k_radius_subarray_averages(nums1, k1)
brute2 = brute_force_k_radius_subarray_averages(nums2, k2)
brute3 = brute_force_k_radius_subarray_averages(nums3, k3)

sliding1 = fixed_sliding_window_k_radius_subarray_averages(nums1, k1)
sliding2 = fixed_sliding_window_k_radius_subarray_averages(nums2, k2)
sliding3 = fixed_sliding_window_k_radius_subarray_averages(nums3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

"""
LeetCode 239 — Sliding Window Maximum  (Advanced)
Problem Statement

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window — the maximum value in each window position.
"""

# region Inputs
nums1, k1 = [1, 3, -1, -3, 5, 3, 6, 7], 3   # Expected: [3, 3, 5, 5, 6, 7]
nums2, k2 = [1],                         1   # Expected: [1]
nums3, k3 = [1, -1],                     1   # Expected: [1, -1]
# endregion


# region Methods
def brute_force_sliding_window_maximum(nums, k):
    pass


def fixed_sliding_window_maximum(nums, k):
    pass
# endregion


# region Calls
brute1 = brute_force_sliding_window_maximum(nums1, k1)
brute2 = brute_force_sliding_window_maximum(nums2, k2)
brute3 = brute_force_sliding_window_maximum(nums3, k3)

sliding1 = fixed_sliding_window_maximum(nums1, k1)
sliding2 = fixed_sliding_window_maximum(nums2, k2)
sliding3 = fixed_sliding_window_maximum(nums3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

"""
LeetCode 1004 — Max Consecutive Ones III
Problem Statement

Given a binary array nums and an integer k, return the maximum number of consecutive 1's
in the array if you can flip at most k 0's.
"""

# region Inputs
nums1, k1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2   # Expected: 6
nums2, k2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1,
             1, 0, 0, 0, 1, 1, 1, 1], 3   # Expected: 10
nums3, k3 = [1, 1, 1],                              0   # Expected: 3
# endregion


# region Methods
def brute_force_max_consecutive_ones(nums, k):
    pass


def variable_sliding_window_max_consecutive_ones(nums, k):
    pass
# endregion


# region Calls
brute1 = brute_force_max_consecutive_ones(nums1, k1)
brute2 = brute_force_max_consecutive_ones(nums2, k2)
brute3 = brute_force_max_consecutive_ones(nums3, k3)

sliding1 = variable_sliding_window_max_consecutive_ones(nums1, k1)
sliding2 = variable_sliding_window_max_consecutive_ones(nums2, k2)
sliding3 = variable_sliding_window_max_consecutive_ones(nums3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

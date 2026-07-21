"""
LeetCode 239 — Sliding Window Maximum  (Advanced)
Problem Statement

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window — the maximum value in each window position.
"""

# region Inputs
from collections import deque


nums1, k1 = [1, 3, -1, -3, 5, 3, 6, 7], 3   # Expected: [3, 3, 5, 5, 6, 7]
nums2, k2 = [1],                         1   # Expected: [1]
nums3, k3 = [1, -1],                     1   # Expected: [1, -1]
# endregion


# region Methods
def brute_force_sliding_window_maximum(nums, k):
    numsLength = len(nums)
    if k == 1:
        return nums
    result = []
    for left in range(numsLength - k + 1):
        maxValue = float("-inf")
        right = 0
        while right < k:
            maxValue = max(nums[left+right], maxValue)
            right += 1
        result.append(maxValue)

    return result


def fixed_sliding_window_maximum(nums, k):
    deq = deque()
    left, right = 0, 0
    result = []

    while right < len(nums):

        # Remove Smaller Element
        while deq and nums[right] >= nums[deq[-1]]:
            deq.pop()

        # Add element
        deq.append(right)

        # remove out of window index
        if deq[0] < left:
            deq.popleft()

        # add the result
        if right+1 >= k:
            result.append(nums[deq[0]])
            left += 1

        right += 1

    return result

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

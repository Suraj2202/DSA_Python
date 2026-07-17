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
    n = len(nums)
    window_size = 2 * k + 1
    result = [-1] * n

    if window_size > n:
        return result

    for i in range(k, n - k):
        current_sum = 0

        for j in range(i - k, i + k + 1):
            current_sum += nums[j]

        result[i] = current_sum // window_size

    return result


def fixed_sliding_window_k_radius_subarray_averages(nums, k):
    window = 2*k+1
    length = len(nums)
    result = [-1]*length

    if window > length:
        return result

    sum_num = 0
    left = 0

    for right in range(length):
        sum_num += nums[right]
        if right >= window-1:
            result[right-k] = sum_num//window

            sum_num -= nums[left]
            left += 1

    return result

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

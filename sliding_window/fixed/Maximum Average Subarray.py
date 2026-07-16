# LeetCode 643 — Maximum Average Subarray

"""
Problem

Given an integer array nums and an integer k, return the maximum average of any contiguous subarray of length k.

Example:

nums = [1,12,-5,-6,50,3]
k = 4

Possible windows:

[1,12,-5,-6]
[12,-5,-6,50]
[-5,-6,50,3]

Return the maximum average.
"""

# Lets 1st solve with brute force


def brute_force_max_avg_fixed_window(arr, k):
    max_sum = sum(arr[:k])

    for i in range(1, len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)

    return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print("Brute Force Max Averge Fixed Window",
      brute_force_max_avg_fixed_window(nums, k))


def sliding_window_max_avg(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    print("\nList of values", arr)
    print(f"window values, {arr[:k]}, sum of window {window_sum}")
    for i in range(k, len(arr)):
        print(
            f"{window_sum} - {arr[i-k]} + {arr[i]} = {window_sum - arr[i-k] + arr[i]}")
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    print("Max Sum Value: ", {max_sum}, "Max Avg Value: ", {max_sum}, "/", {k})
    return max_sum/k


print("Slidding Window Max Averge Fixed Window",
      sliding_window_max_avg(nums, k))

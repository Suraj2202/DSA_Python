"""
LeetCode 209 — Minimum Size Subarray Sum
Problem Statement

Given an array of positive integers nums and a positive integer target, return the minimum length of a contiguous subarray whose sum is greater than or equal to target.

If there is no such subarray, return 0.
"""

nums1 = [2, 3, 1, 2, 4, 3]
target1 = 7

nums2 = [1, 4, 4]
target2 = 4

nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
target3 = 11


def brute_force_minimum_size_subarray_sum(nums, target):
    minimum_length = float("inf")
    numsLength = len(nums)
    for i in range(numsLength):
        current_sum = 0
        for j in range(i, numsLength):
            current_sum += nums[j]
            print(i, j, nums[i:j+1], "Sums", current_sum, "Length", j-i+1)
            if current_sum >= target:
                minimum_length = min(minimum_length, j-i+1)
                print("Minimum Sum", minimum_length, "\n================")
                break

    return 0 if minimum_length == float("inf") else minimum_length


nums1 = [2, 3, 1, 2, 4, 3]
target1 = 7


def variable_sliding_window_min_size_subarray_size(nums, target):
    left = 0
    current_sum = 0
    minimum_length = float("inf")
    print(nums, target)
    for right in range(len(nums)):
        current_sum += nums[right]
        print("current sum", current_sum, left, right)
        while current_sum >= target:
            minimum_length = min(minimum_length, right-left+1)
            current_sum -= nums[left]
            print("Inside While", current_sum, left, right)
            left += 1

        print("Minimum Length", minimum_length, "\n=====================")
    return 0 if minimum_length == float("inf") else minimum_length


case1 = brute_force_minimum_size_subarray_sum(nums1, target1)
case2 = brute_force_minimum_size_subarray_sum(nums2, target2)
case3 = brute_force_minimum_size_subarray_sum(nums3, target3)

variablecase1 = variable_sliding_window_min_size_subarray_size(nums1, target1)
variablecase2 = variable_sliding_window_min_size_subarray_size(nums2, target2)
variablecase3 = variable_sliding_window_min_size_subarray_size(nums3, target3)

print("Brute Force Approach: \nCase1", case1,
      "\nCase2", case2, "\nCase3", case3)
print("Variable Sliding Window Approach: \nCase1", variablecase1,
      "\nCase2", variablecase2, "\nCase3", variablecase3)

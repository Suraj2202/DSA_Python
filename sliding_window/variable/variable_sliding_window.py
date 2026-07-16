# Find the longest contiguous subarray whose sum is less than or equal to target.

# region Inputs
nums1,  target1 = [2, 3, 1, 2, 4, 3], 10   # Expected: 4
nums2,  target2 = [1, 2, 3, 4, 5],    15   # Expected: 5
nums3,  target3 = [1, 2, 3, 4, 5],    5    # Expected: 2
nums4,  target4 = [5, 5, 5, 5],       5    # Expected: 1
nums5,  target5 = [2, 2, 2, 2, 2],    6    # Expected: 3
nums6,  target6 = [9, 1, 1, 1, 1],    4    # Expected: 4
nums7,  target7 = [4],                5    # Expected: 1
nums8,  target8 = [4],                4    # Expected: 1
nums9,  target9 = [1],                5    # Expected: 1
nums10, target10 = [1, 1, 1, 1, 1, 1], 3    # Expected: 3
# endregion


# region Methods
def brute_force_maximum_size_subarray_sum(nums, target):
    maximum_size = 0

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum += nums[j]

            if current_sum <= target:
                maximum_size = max(maximum_size, j - i + 1)
            else:
                break

    return maximum_size


def variable_sliding_window_maximum_size_subarray_sum(nums, target):
    left, current_sum = 0, 0
    max_length = 0
    print(nums, target)
    for right in range(len(nums)):
        current_sum += nums[right]
        print("current sum", current_sum, "left", left, "right", right)
        while current_sum > target:
            current_sum -= nums[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
        print("Max Length", max_length, "\n=====================")
    return max_length
# endregion


# region Calls
brute1 = brute_force_maximum_size_subarray_sum(nums1,  target1)
brute2 = brute_force_maximum_size_subarray_sum(nums2,  target2)
brute3 = brute_force_maximum_size_subarray_sum(nums3,  target3)
brute4 = brute_force_maximum_size_subarray_sum(nums4,  target4)
brute5 = brute_force_maximum_size_subarray_sum(nums5,  target5)
brute6 = brute_force_maximum_size_subarray_sum(nums6,  target6)
brute7 = brute_force_maximum_size_subarray_sum(nums7,  target7)
brute8 = brute_force_maximum_size_subarray_sum(nums8,  target8)
brute9 = brute_force_maximum_size_subarray_sum(nums9,  target9)
brute10 = brute_force_maximum_size_subarray_sum(nums10, target10)

variableSliding1 = variable_sliding_window_maximum_size_subarray_sum(
    nums1,  target1)
variableSliding2 = variable_sliding_window_maximum_size_subarray_sum(
    nums2,  target2)
variableSliding3 = variable_sliding_window_maximum_size_subarray_sum(
    nums3,  target3)
variableSliding4 = variable_sliding_window_maximum_size_subarray_sum(
    nums4,  target4)
variableSliding5 = variable_sliding_window_maximum_size_subarray_sum(
    nums5,  target5)
variableSliding6 = variable_sliding_window_maximum_size_subarray_sum(
    nums6,  target6)
variableSliding7 = variable_sliding_window_maximum_size_subarray_sum(
    nums7,  target7)
variableSliding8 = variable_sliding_window_maximum_size_subarray_sum(
    nums8,  target8)
variableSliding9 = variable_sliding_window_maximum_size_subarray_sum(
    nums9,  target9)
variableSliding10 = variable_sliding_window_maximum_size_subarray_sum(
    nums10, target10)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1",  brute1,  "\nCase2",  brute2,  "\nCase3",
      brute3,  "\nCase4",  brute4,  "\nCase5",  brute5)
print("Case6",  brute6,  "\nCase7",  brute7,  "\nCase8",
      brute8,  "\nCase9",  brute9,  "\nCase10", brute10)

print("\nVariable Sliding Window Approach:")
print("Case1",  variableSliding1,  "\nCase2",  variableSliding2,  "\nCase3",
      variableSliding3,  "\nCase4",  variableSliding4,  "\nCase5",  variableSliding5)
print("Case6",  variableSliding6,  "\nCase7",  variableSliding7,  "\nCase8",
      variableSliding8,  "\nCase9",  variableSliding9,  "\nCase10", variableSliding10)
# endregion

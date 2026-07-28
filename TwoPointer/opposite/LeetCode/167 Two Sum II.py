"""
LeetCode 167 — Two Sum II - Input Array Is Sorted
Problem Statement

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

You may not use the same element twice. There is exactly one solution.
"""

# region Inputs
numbers1, target1 = [2, 7, 11, 15], 9  # Expected: [1, 2]
numbers2, target2 = [2, 3, 4], 6  # Expected: [1, 3]
numbers3, target3 = [-1, 0], -1  # Expected: [1, 2]
# endregion


# region Methods
def brute_force_two_sum_ii(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) == target:
                return [i + 1, j + 1]
    return -1


def two_pointer_two_sum_ii(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return -1


# endregion


# region Calls
brute1 = brute_force_two_sum_ii(numbers1, target1)
brute2 = brute_force_two_sum_ii(numbers2, target2)
brute3 = brute_force_two_sum_ii(numbers3, target3)

twoPointer1 = two_pointer_two_sum_ii(numbers1, target1)
twoPointer2 = two_pointer_two_sum_ii(numbers2, target2)
twoPointer3 = two_pointer_two_sum_ii(numbers3, target3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

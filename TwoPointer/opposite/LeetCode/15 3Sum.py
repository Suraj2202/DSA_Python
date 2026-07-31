"""
LeetCode 15 — 3Sum
Problem Statement

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# region Inputs
nums1 = [-1, 0, 1, 2, -1, -4]  # Expected: [[-1, -1, 2], [-1, 0, 1]]
nums2 = [0, 1, 1]  # Expected: []
nums3 = [0, 0, 0]  # Expected: [[0, 0, 0]]
# endregion


# region Methods
def brute_force_three_sum(nums):
    res = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return [list(t) for t in res]


## My Attempt
def two_pointer_three_sum(nums):
    l, r = 0, len(nums) - 1
    nums.sort()  # nlogn sorting?
    result = set()
    for i in range(len(nums)):
        while l < r:
            currentSum = nums[l] + nums[r]
            if i != l and i != r and currentSum == -nums[i]:
                triplet = tuple(sorted([nums[l], nums[r], nums[i]]))  # nlogn sorting ?
                result.add(triplet)
                l += 1
                r -= 1
            elif currentSum < -nums[i]:
                l += 1
            else:
                r -= 1
        l, r = 0, len(nums) - 1
    return [list(x) for x in result]


## AI Attempt
def two_pointer_three_sum_gpt(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        # Skip duplicate fixed elements already found all triplets starting with i-1,
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


# endregion


# region Calls
brute1 = brute_force_three_sum(nums1)
brute2 = brute_force_three_sum(nums2)
brute3 = brute_force_three_sum(nums3)

twoPointer1 = two_pointer_three_sum(nums1)
twoPointer2 = two_pointer_three_sum(nums2)
twoPointer3 = two_pointer_three_sum(nums3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

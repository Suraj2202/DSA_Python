"""
LeetCode 11 — Container With Most Water
Problem Statement

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

# region Inputs
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Expected: 49
height2 = [1, 1]  # Expected: 1
height3 = [4, 3, 2, 1, 4]  # Expected: 16
# endregion


# region Methods
def brute_force_container_with_most_water(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = (j - i) * (min(height[i], height[j]))
            max_area = max(max_area, area)
    return max_area


def two_pointer_container_with_most_water(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


# endregion


# region Calls
brute1 = brute_force_container_with_most_water(height1)
brute2 = brute_force_container_with_most_water(height2)
brute3 = brute_force_container_with_most_water(height3)

twoPointer1 = two_pointer_container_with_most_water(height1)
twoPointer2 = two_pointer_container_with_most_water(height2)
twoPointer3 = two_pointer_container_with_most_water(height3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

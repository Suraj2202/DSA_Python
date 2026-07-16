"""
LeetCode 42 — Trapping Rain Water
Problem Statement

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

# region Inputs
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]   # Expected: 6
height2 = [4, 2, 0, 3, 2, 5]                      # Expected: 9
height3 = [1, 0, 1]                                # Expected: 1
# endregion


# region Methods
def brute_force_trapping_rain_water(height):
    pass


def two_pointer_trapping_rain_water(height):
    pass
# endregion


# region Calls
brute1 = brute_force_trapping_rain_water(height1)
brute2 = brute_force_trapping_rain_water(height2)
brute3 = brute_force_trapping_rain_water(height3)

twoPointer1 = two_pointer_trapping_rain_water(height1)
twoPointer2 = two_pointer_trapping_rain_water(height2)
twoPointer3 = two_pointer_trapping_rain_water(height3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

"""
LeetCode 42 — Trapping Rain Water
Problem Statement

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

# region Inputs
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # Expected: 6
height2 = [4, 2, 0, 3, 2, 5]  # Expected: 9
height3 = [1, 0, 1]  # Expected: 1
# endregion


# region Methods
def brute_force_trapping_rain_water(height):
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    l_wall, r_wall = 0, 0

    for i in range(n):
        j = -i - 1
        current_Lmax = max(l_wall, height[i])
        current_Rmax = max(r_wall, height[j])

        l_wall = current_Lmax
        r_wall = current_Rmax

        max_left[i] = current_Lmax
        max_right[j] = current_Rmax

    rainCollect = 0
    for k in range(n):
        space = min(max_left[k], max_right[k]) - height[k]
        rainCollect += space
    return rainCollect


# def brute_force_trapping_rain_water(height):

#     l_wall = r_wall = 0
#     n = len(height)
#     max_left = [0] * n
#     max_right = [0] * n

#     for i in range(n):
#         j = -i - 1
#         max_left[i] = l_wall
#         max_right[j] = r_wall
#         l_wall = max(l_wall, height[i])
#         r_wall = max(r_wall, height[j])

#     summ = 0
#     for i in range(n):
#         pot = min(max_left[i], max_right[i])
#         summ += max(0, pot - height[i])

#     return summ


def two_pointer_trapping_rain_water(height):
    n = len(height)
    l, r = 0, n - 1
    lMax, rMax = 0, 0
    rainCollect = 0

    while l < r:
        lMax = max(lMax, height[l])
        rMax = max(rMax, height[r])

        if lMax < rMax:
            rainCollect += lMax - height[l]
            l += 1
        else:
            rainCollect += rMax - height[r]
            r -= 1

    return rainCollect


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

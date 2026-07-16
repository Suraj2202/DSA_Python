"""
LeetCode 1652 — Defuse the Bomb
Problem Statement

You have a bomb to defuse, and your time is running out! Your informer will provide you with
a circular array code of length n and a key k.

To decrypt the code, you must replace every number with the sum of the next k numbers.
If k is negative, replace with the sum of the previous |k| numbers.
If k is 0, replace with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element
of code[0] is code[n-1].
"""

# region Inputs
code1, k1 = [5, 7, 1, 4], 3    # Expected: [12, 10, 16, 13]
code2, k2 = [1, 2, 3, 4], 0    # Expected: [0, 0, 0, 0]
code3, k3 = [2, 4, 9, 3], -2   # Expected: [12, 5, 6, 13]
# endregion


# region Methods
def brute_force_defuse_the_bomb(code, k):
    pass


def fixed_sliding_window_defuse_the_bomb(code, k):
    pass
# endregion


# region Calls
brute1 = brute_force_defuse_the_bomb(code1, k1)
brute2 = brute_force_defuse_the_bomb(code2, k2)
brute3 = brute_force_defuse_the_bomb(code3, k3)

sliding1 = fixed_sliding_window_defuse_the_bomb(code1, k1)
sliding2 = fixed_sliding_window_defuse_the_bomb(code2, k2)
sliding3 = fixed_sliding_window_defuse_the_bomb(code3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

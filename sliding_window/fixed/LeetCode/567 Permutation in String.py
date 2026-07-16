"""
LeetCode 567 — Permutation in String
Problem Statement

Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is a substring of s2.
"""

# region Inputs
s1_1, s2_1 = "ab",  "eidbaooo"   # Expected: True
s1_2, s2_2 = "ab",  "eidboaoo"   # Expected: False
s1_3, s2_3 = "adc", "dcda"       # Expected: True
# endregion


# region Methods
def brute_force_permutation_in_string(s1, s2):
    pass


def fixed_sliding_window_permutation_in_string(s1, s2):
    pass
# endregion


# region Calls
brute1 = brute_force_permutation_in_string(s1_1, s2_1)
brute2 = brute_force_permutation_in_string(s1_2, s2_2)
brute3 = brute_force_permutation_in_string(s1_3, s2_3)

sliding1 = fixed_sliding_window_permutation_in_string(s1_1, s2_1)
sliding2 = fixed_sliding_window_permutation_in_string(s1_2, s2_2)
sliding3 = fixed_sliding_window_permutation_in_string(s1_3, s2_3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

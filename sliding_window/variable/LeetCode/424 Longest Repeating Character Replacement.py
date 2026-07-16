"""
LeetCode 424 — Longest Repeating Character Replacement
Problem Statement

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.
"""

# region Inputs
s1, k1 = "ABAB",    2   # Expected: 4
s2, k2 = "AABABBA", 1   # Expected: 4
s3, k3 = "AAAA",    0   # Expected: 4
# endregion


# region Methods
def brute_force_longest_repeating_character_replacement(s, k):
    pass


def variable_sliding_window_longest_repeating_character_replacement(s, k):
    pass
# endregion


# region Calls
brute1 = brute_force_longest_repeating_character_replacement(s1, k1)
brute2 = brute_force_longest_repeating_character_replacement(s2, k2)
brute3 = brute_force_longest_repeating_character_replacement(s3, k3)

sliding1 = variable_sliding_window_longest_repeating_character_replacement(
    s1, k1)
sliding2 = variable_sliding_window_longest_repeating_character_replacement(
    s2, k2)
sliding3 = variable_sliding_window_longest_repeating_character_replacement(
    s3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

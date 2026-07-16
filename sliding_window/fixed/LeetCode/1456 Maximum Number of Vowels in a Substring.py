"""
LeetCode 1456 — Maximum Number of Vowels in a Substring of Given Length
Problem Statement

Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

# region Inputs
s1, k1 = "abciiidef", 3   # Expected: 3
s2, k2 = "aeiou",     2   # Expected: 2
s3, k3 = "leetcode",  3   # Expected: 2
# endregion


# region Methods
def brute_force_max_vowels(s, k):
    pass


def fixed_sliding_window_max_vowels(s, k):
    pass
# endregion


# region Calls
brute1 = brute_force_max_vowels(s1, k1)
brute2 = brute_force_max_vowels(s2, k2)
brute3 = brute_force_max_vowels(s3, k3)

sliding1 = fixed_sliding_window_max_vowels(s1, k1)
sliding2 = fixed_sliding_window_max_vowels(s2, k2)
sliding3 = fixed_sliding_window_max_vowels(s3, k3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

"""
LeetCode 438 — Find All Anagrams in a String
Problem Statement

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An anagram is a string that contains the same characters, only the order of characters can differ.
"""

# region Inputs
s1, p1 = "cbaebabacd", "abc"   # Expected: [0, 6]
s2, p2 = "abab",       "ab"    # Expected: [0, 1, 2]
s3, p3 = "af",         "be"    # Expected: []
# endregion


# region Methods
def brute_force_find_all_anagrams(s, p):
    pass


def fixed_sliding_window_find_all_anagrams(s, p):
    pass
# endregion


# region Calls
brute1 = brute_force_find_all_anagrams(s1, p1)
brute2 = brute_force_find_all_anagrams(s2, p2)
brute3 = brute_force_find_all_anagrams(s3, p3)

sliding1 = fixed_sliding_window_find_all_anagrams(s1, p1)
sliding2 = fixed_sliding_window_find_all_anagrams(s2, p2)
sliding3 = fixed_sliding_window_find_all_anagrams(s3, p3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nFixed Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

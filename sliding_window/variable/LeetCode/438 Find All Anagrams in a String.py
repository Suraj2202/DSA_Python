"""
LeetCode 438 — Find All Anagrams in a String  (Variable Window Approach)
Problem Statement

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An anagram is a string that contains the same characters, only the order can differ.

Note: This problem can be solved with both a Fixed window (window size = len(p))
and a Variable window approach using character frequency matching.
"""

# region Inputs
s1, p1 = "cbaebabacd", "abc"   # Expected: [0, 6]
s2, p2 = "abab",       "ab"    # Expected: [0, 1, 2]
s3, p3 = "af",         "be"    # Expected: []
# endregion


# region Methods
def brute_force_find_all_anagrams(s, p):
    pass


def variable_sliding_window_find_all_anagrams(s, p):
    pass
# endregion


# region Calls
brute1 = brute_force_find_all_anagrams(s1, p1)
brute2 = brute_force_find_all_anagrams(s2, p2)
brute3 = brute_force_find_all_anagrams(s3, p3)

sliding1 = variable_sliding_window_find_all_anagrams(s1, p1)
sliding2 = variable_sliding_window_find_all_anagrams(s2, p2)
sliding3 = variable_sliding_window_find_all_anagrams(s3, p3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

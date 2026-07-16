"""
LeetCode 76 — Minimum Window Substring  (Hard)
Problem Statement

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

# region Inputs
s1, t1 = "ADOBECODEBANC", "ABC"   # Expected: "BANC"
s2, t2 = "a",             "a"    # Expected: "a"
s3, t3 = "a",             "aa"   # Expected: ""
# endregion


# region Methods
def brute_force_minimum_window_substring(s, t):
    pass


def variable_sliding_window_minimum_window_substring(s, t):
    pass
# endregion


# region Calls
brute1 = brute_force_minimum_window_substring(s1, t1)
brute2 = brute_force_minimum_window_substring(s2, t2)
brute3 = brute_force_minimum_window_substring(s3, t3)

sliding1 = variable_sliding_window_minimum_window_substring(s1, t1)
sliding2 = variable_sliding_window_minimum_window_substring(s2, t2)
sliding3 = variable_sliding_window_minimum_window_substring(s3, t3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

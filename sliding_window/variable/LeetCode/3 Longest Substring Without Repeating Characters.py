"""
LeetCode 3 — Longest Substring Without Repeating Characters
Problem Statement

Given a string s, find the length of the longest substring without repeating characters.
"""

# region Inputs
s1 = "abcabcbb"   # Expected: 3
s2 = "bbbbb"      # Expected: 1
s3 = "pwwkew"     # Expected: 3
# endregion


# region Methods
def brute_force_longest_substring_without_repeating(s):
    max_len = 0
    n = len(s)
    checkStr = []

    for l in range(n):
        r = l
        while r < n and s[r] not in checkStr:
            checkStr.append(s[r])
            r += 1
        max_len = max(max_len, len(checkStr))
        checkStr.clear()
    return max_len


def variable_sliding_window_longest_substring_without_repeating(s):
    max_len, left = 0, 0
    n = len(s)
    checkStr = set()
    for right in range(n):
        while s[right] in checkStr:
            checkStr.remove(s[left])
            left += 1
        checkStr.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


def variable_sliding_window_longest_substring_without_repeating_using_list(s):
    max_len = 0
    n = len(s)
    checkStr = []
    for right in range(n):
        if s[right] not in checkStr:
            checkStr.append(s[right])
            max_len = max(max_len, len(checkStr))
        else:
            checkStr.pop(0)

    return max_len
# endregion


# region Calls
brute1 = brute_force_longest_substring_without_repeating(s1)
brute2 = brute_force_longest_substring_without_repeating(s2)
brute3 = brute_force_longest_substring_without_repeating(s3)

sliding1 = variable_sliding_window_longest_substring_without_repeating(s1)
sliding2 = variable_sliding_window_longest_substring_without_repeating(s2)
sliding3 = variable_sliding_window_longest_substring_without_repeating(s3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

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
    n, m = len(s1), len(s2)
    if n > m:
        return False

    # frequency map of s1
    s1Freq = {}
    for ch in s1:
        s1Freq[ch] = s1Freq.get(ch, 0) + 1

    # try every window of length n in s2
    for start in range(m - n + 1):
        windowFreq = {}
        for i in range(start, start + n):
            windowFreq[s2[i]] = windowFreq.get(s2[i], 0) + 1

        if windowFreq == s1Freq:   # same keys AND values
            return True

    return False


def fixed_sliding_window_permutation_in_string(s1, s2):
    s1len, s2Len = len(s1), len(s2)

    if s1len > s2Len:
        return False

    s1Freq = {}
    for x in s1:
        s1Freq[x] = s1Freq.get(x, 0) + 1

    s2Freq = {}
    for i in range(s1len):
        s2Freq[s2[i]] = s2Freq.get(s2[i], 0) + 1

    if s1Freq == s2Freq:
        return True

    for right in range(s1len, s2Len):
        s2Freq[s2[right]] = s2Freq.get(s2[right], 0) + 1

        left = right - s1len
        s2Freq[s2[left]] -= 1
        
        if s2Freq[s2[left]] == 0:
            s2Freq.pop(s2[left])

        if s1Freq == s2Freq:
            return True

    return False

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

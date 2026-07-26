"""
LeetCode 567 — Permutation in String  (Variable Window Approach)
Problem Statement

Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is a substring of s2.

Note: This problem can be solved with both a Fixed window (window size = len(s1))
and a Variable window approach using character frequency matching.
"""

# region Inputs
s1_1, s2_1 = "ab", "eidbaooo"  # Expected: True
s1_2, s2_2 = "ab", "eidboaoo"  # Expected: False
s1_3, s2_3 = "adc", "dcda"  # Expected: True
# endregion


# region Methods
def brute_force_permutation_in_string(s1, s2):
    s1Freq = {}
    for x in s1:
        s1Freq[x] = s1Freq.get(x, 0) + 1
    for i in range(len(s2)):
        r = i
        checkFreq = {}
        while r < len(s2) and (r - i) < len(s1):
            checkFreq[s2[r]] = checkFreq.get(s2[r], 0) + 1
            if checkFreq == s1Freq:
                return True
            r += 1
    return False

def variable_sliding_window_permutation_in_string(s1, s2):
    if len(s1) > len(s2):
        return False

    need = {}
    for ch in s1:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    left = 0

    for right in range(len(s2)):
        ch = s2[right]

        # Character not present in s1 -> reset window
        if ch not in need:
            window.clear()
            left = right + 1
            continue

        # Add current character
        window[ch] = window.get(ch, 0) + 1

        # Shrink until current character frequency is valid
        while window[ch] > need[ch]:
            left_char = s2[left]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            left += 1

        # If frequencies match, permutation found
        if window == need:
            return True

    return False

# endregion


# region Calls
brute1 = brute_force_permutation_in_string(s1_1, s2_1)
brute2 = brute_force_permutation_in_string(s1_2, s2_2)
brute3 = brute_force_permutation_in_string(s1_3, s2_3)

sliding1 = variable_sliding_window_permutation_in_string(s1_1, s2_1)
sliding2 = variable_sliding_window_permutation_in_string(s1_2, s2_2)
sliding3 = variable_sliding_window_permutation_in_string(s1_3, s2_3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

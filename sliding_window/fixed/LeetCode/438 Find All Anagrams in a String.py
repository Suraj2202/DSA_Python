"""
LeetCode 438 — Find All Anagrams in a String
Problem Statement

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An anagram is a string that contains the same characters, only the order of characters can differ.
"""

# region Inputs
from pydoc import plain
from unittest import result


s1, p1 = "cbaebabacd", "abc"   # Expected: [0, 6]
s2, p2 = "abab",       "ab"    # Expected: [0, 1, 2]
s3, p3 = "af",         "be"    # Expected: []
# endregion


# region Methods
def brute_force_find_all_anagrams(s, p):
    s1Len, pLen = len(s), len(p)
    result = []
    if s1Len < pLen:
        return result

    pFreq = {}

    for x in p:
        pFreq[x] = pFreq.get(x, 0) + 1

    # print("================\nP Frequency", pFreq, f"range, {s1Len-pLen-1}")
    for left in range(s1Len-pLen+1):
        matchFreq = {}
        for right in range(pLen):
            # print(left, right)
            matchFreq[s[left + right]] = matchFreq.get(s[left + right], 0) + 1
            # print(matchFreq)

        if pFreq == matchFreq:
            result.append(left)

    return result


def fixed_sliding_window_find_all_anagrams(s, p):
    sLen, pLen, result, pFreq, window_freq, left = len(s), len(p), [
    ], {}, {}, 0

    if sLen < pLen:
        return result

    for x in p:
        pFreq[x] = pFreq.get(x, 0)+1

    print("================\nP Game", s, p)
    for i in range(pLen):
        window_freq[s[i]] = window_freq.get(s[i], 0)+1

    if pFreq == window_freq:
        print(pFreq, window_freq)
        result.append(0)

    for right in range(pLen, sLen):
        window_freq[s[right]] = window_freq.get(s[right], 0)+1

        print(right, left)
        window_freq[s[left]] = window_freq[s[left]] - 1
        if window_freq[s[left]] == 0:
            window_freq.pop(s[left])
        left += 1

        if pFreq == window_freq:
            result.append(right-pLen+1)

    return result

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

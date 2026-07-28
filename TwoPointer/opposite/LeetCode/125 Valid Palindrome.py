"""
LeetCode 125 — Valid Palindrome
Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# region Inputs
s1 = "A man, a plan, a canal: Panama"  # Expected: True
s2 = "race a car"  # Expected: False
s3 = " "  # Expected: True
# endregion


# region Methods
def brute_force_valid_palindrome(s):
    clean = "".join(x.lower() for x in s if x.isalnum())
    rev = []
    for i in range(len(clean) - 1, -1, -1):
        rev.append(clean[i])
    if "".join(rev) == clean:
        return True
    return False


def two_pointer_valid_palindrome(s):
    left, right = 0, len(s) - 1
    print(s)
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


# endregion


# region Calls
brute1 = brute_force_valid_palindrome(s1)
brute2 = brute_force_valid_palindrome(s2)
brute3 = brute_force_valid_palindrome(s3)

twoPointer1 = two_pointer_valid_palindrome(s1)
twoPointer2 = two_pointer_valid_palindrome(s2)
twoPointer3 = two_pointer_valid_palindrome(s3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nTwo Pointer Approach:")
print("Case1", twoPointer1, "\nCase2", twoPointer2, "\nCase3", twoPointer3)
# endregion

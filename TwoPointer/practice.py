# Practice 3 Problems

# 1. Reverse a string in-place (conceptually)
s = list("hello")
# Reverse it using two pointers, without using s[::-1] or reversed()


def reverse_string(s):
    left, right = 0, len(s)-1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1

    return s


rev_str = reverse_string(s[:])
print(f"Original String {''.join(s)}")
print(f"Reverse of string: {''.join(rev_str)}")

# Complexity is O(n)

# 2. Check if a string is a palindrome (ignoring case)


def is_palindrome(s):
    # e.g. "Racecar" -> True, "hello" -> False
    # Use two pointers, don't use s == s[::-1]
    left, right = 0, len(s)-1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


print(f"Racecar, is it a palindrome, {is_palindrome("Racecar")}")
print(f"hello, is it a palindrome, {is_palindrome("hello")}")

# 3. Move all zeroes to the end of an array, in-place,
# keeping relative order of non-zero elements
arr3 = [0, 1, 0, 3, 12]
# should become [1, 3, 12, 0, 0]

# This is having O(n), but space complixity is high due to 1 more list.


def switch_zeros_to_end_space_complex(arr):
    res = [0] * len(arr)
    pos = 0
    for x in arr:
        if x != 0:
            res[pos] = x
            pos += 1
    return res


print(
    f"Switch Zeros to end with high space complexity, {switch_zeros_to_end_space_complex(arr3)}")

# Now lets do it with O(n) inline update.


def switch_zeros_to_end(arr):
    slow = arr[0]
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr

print(f"switch zeros to end, {switch_zeros_to_end(arr3)}")
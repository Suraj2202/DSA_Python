"""
Worked Example: Two Sum on a Sorted Array
Problem:        Given a sorted array arr and a target T, 
                find if there exist two numbers that add up to T.
"""
from ctypes import pointer


arr = [2, 7, 11, 15, 18]
target = 29
print("Printed locations of arr")
# Brute Force (what most people write first)


def two_sum_brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None


# Complexity: O(n²) — nested loop checking every pair.
res = two_sum_brute_force(arr, target)
print(f"Brute Force: {res}")

# Optimized with Two Pointers (Flavor A)
"""
Because the array is sorted, we can be smart:

Start left at 0, right at the end
If arr[left] + arr[right] is too small → we need a bigger sum → move left forward
If it's too big → move right backward
If equal → found it
"""

# Optimized with Two Pointers


def two_sum_two_pointers(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        sum = arr[left]+arr[right]

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return (left, right)
    return None


# Complexity O(n) — each pointer moves at most n times total, no nested loop.
pointer_res = two_sum_two_pointers(arr, target)
print(f"Two Pointer: {pointer_res}")

# Why it works:
"""
because the array is sorted, 
moving left forward can only increase the sum, 
and moving right backward can only decrease it. 

That monotonic property is what lets us safely discard half the "pairs" at each step 
without checking them individually — that's the real reason it beats O(n²).
"""

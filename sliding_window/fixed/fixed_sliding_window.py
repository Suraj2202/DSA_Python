"""
Fixed Sliding Window
A window is simply a continuous portion of an array or string.

Example
Array
2 1 5 1 3 2
Window of size 3
[2 1 5]
Slide
2 [1 5 1]
Slide
2 1 [5 1 3]
Slide
2 1 5 [1 3 2]

The window moves while reusing work from the previous window instead of starting over.

The Three Rules of Sliding Window
Every Sliding Window algorithm follows these ideas:
Expand the window by including a new element (move the right pointer).
Shrink the window when needed by removing elements from the left (move the left pointer).
Maintain the information you care about (sum, frequency, unique characters, maximum, etc.) incrementally instead of recomputing it.

The difference between Fixed and Variable Sliding Window is when you shrink.
"""

# Problem 1
# Find maximum sum of any k consecutive elements.

def max_sum_subarray(nums, k):

    window_sum = sum(nums[:k])      # First window
    maximum = window_sum            # Best answer so far

    for right in range(k, len(nums)):
        window_sum = window_sum - nums[right - k] + nums[right]
        maximum = max(maximum, window_sum)

    return maximum

nums = [2, 1, 5, 1, 3, 2]
k = 3

# Sliding Window
# First understand why it was invented.

# Problem 1: Find the maximum sum of any 3 consecutive elements.
"""
2+1+5 = 8
1+5+1 = 7
5+1+3 = 9
1+3+2 = 6
Answer = 9
"""
nums = [2, 1, 5, 1, 3, 2]


def brute_force_max_k_sum(nums, k):
    maximum = 0
    for i in range(len(nums)-k+1):

        current = 0
        for j in range(i, i+k):
            current += nums[j]

        maximum = max(maximum, current)

    return maximum


print("Maximum sum of any k consecutive elements using Brute Force",
      brute_force_max_k_sum(nums, 3))

"""
Total Operations
Suppose
n = 100000
k = 500
Brute force does roughly
100000 × 500 = 50,000,000 additions
Huge.
"""

"""
nums = [2, 1, 5, 1, 3, 2]

The Important Observation
Instead of recalculating
1+5+1
from scratch,
can we use the previous answer?
Previous
2+1+5 = 8
Next window
1+5+1
"""

"""
New Sum = Old Sum - Outgoing Element + Incoming Element
That is the entire idea behind Sliding Window.
"""

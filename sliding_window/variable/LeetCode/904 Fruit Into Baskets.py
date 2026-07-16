"""
LeetCode 904 — Fruit Into Baskets
Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules:
- You only have two baskets, and each basket can only hold a single type of fruit.
- There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree
  (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.
"""

# region Inputs
fruits1 = [1, 2, 1]         # Expected: 3
fruits2 = [0, 1, 2, 2]      # Expected: 3
fruits3 = [1, 2, 3, 2, 2]   # Expected: 4
# endregion


# region Methods
def brute_force_fruit_into_baskets(fruits):
    pass


def variable_sliding_window_fruit_into_baskets(fruits):
    pass
# endregion


# region Calls
brute1 = brute_force_fruit_into_baskets(fruits1)
brute2 = brute_force_fruit_into_baskets(fruits2)
brute3 = brute_force_fruit_into_baskets(fruits3)

sliding1 = variable_sliding_window_fruit_into_baskets(fruits1)
sliding2 = variable_sliding_window_fruit_into_baskets(fruits2)
sliding3 = variable_sliding_window_fruit_into_baskets(fruits3)
# endregion


# region Print
print("Brute Force Approach:")
print("Case1", brute1, "\nCase2", brute2, "\nCase3", brute3)

print("\nVariable Sliding Window Approach:")
print("Case1", sliding1, "\nCase2", sliding2, "\nCase3", sliding3)
# endregion

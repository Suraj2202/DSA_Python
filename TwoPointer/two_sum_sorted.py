# Two Pointers — Two Sum II (sorted array)
# LeetCode 167 | Difficulty: Medium
#
# Problem:
#   Given a 1-indexed sorted array `numbers` and a target,
#   return indices [i, j] such that numbers[i] + numbers[j] == target.
#
# Approach: Two Pointers — O(n) time, O(1) space

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]   # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []   # no solution (guaranteed by problem constraints)


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9)  == [1, 2]
    assert two_sum([2, 3, 4], 6)       == [1, 3]
    assert two_sum([-1, 0], -1)        == [1, 2]
    print("All tests passed!")

"""Understand why HashMap and Set are useful before solving problems."""


def contains_duplicate_brute_force(nums):
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            if nums[left] == nums[right]:
                return True
    return False


def contains_duplicate_set(nums):
    seen = set()

    for number in nums:
        if number in seen:
            return True
        seen.add(number)

    return False


def count_frequency_brute_force(nums):
    frequency = {}

    for number in nums:
        count = 0
        for candidate in nums:
            if candidate == number:
                count += 1
        frequency[number] = count

    return frequency


def count_frequency_hashmap(nums):
    frequency = {}

    for number in nums:
        frequency[number] = frequency.get(number, 0) + 1

    return frequency


if __name__ == "__main__":
    values = [4, 2, 7, 2, 4, 4]

    assert contains_duplicate_brute_force(values) is True
    assert contains_duplicate_set(values) is True
    assert count_frequency_brute_force(values) == {4: 3, 2: 2, 7: 1}
    assert count_frequency_hashmap(values) == {4: 3, 2: 2, 7: 1}

    print("Set: remember what has already been seen.")
    print("HashMap: remember a value for each key.")
    print("Brute force: O(n^2); HashMap/Set average: O(n).")

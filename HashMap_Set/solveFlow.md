# HashMap / Set — Problem Tracker

## Legend

- ✅ Done
- 🔄 In Progress
- ⬜ Not Started

---

## When to Use HashMap / Set

| Clue in the Problem                         | Start With                      |
| ------------------------------------------- | ------------------------------- |
| Duplicate, unique, already seen             | Set                             |
| Count, frequency, occurrence                | HashMap                         |
| Find a complement or previous value         | HashMap lookup                  |
| Match one value consistently to another     | Two HashMaps                    |
| Group items by a shared property            | HashMap of lists                |
| Follow values until a state repeats         | Set for cycle detection         |
| Find consecutive values regardless of order | Set for O(1) average membership |

### Solve Flow

1. Decide what must be remembered: existence, count, index, or group.
2. Choose a set for existence only; choose a HashMap when a key needs a value.
3. While scanning, ask whether to check before inserting or insert before checking.
4. State the invariant: what does the map or set contain after each iteration?
5. Confirm that keys are hashable and account for O(n) extra space.

Average insert, lookup, and delete are O(1), so one full scan is usually O(n).

---

## Learning Path (Easy → Hard)

| Status | #   | Problem                            | Type             | Difficulty |
| ------ | --- | ---------------------------------- | ---------------- | ---------- |
| ⬜     | 217 | Contains Duplicate                 | Deduplication    | Easy       |
| ⬜     | 242 | Valid Anagram                      | Frequency Count  | Easy       |
| ⬜     | 1   | Two Sum                            | Lookup / Pair    | Easy       |
| ⬜     | 383 | Ransom Note                        | Frequency Count  | Easy       |
| ⬜     | 387 | First Unique Character in a String | Frequency Count  | Easy       |
| ⬜     | 349 | Intersection of Two Arrays         | Deduplication    | Easy       |
| ⬜     | 205 | Isomorphic Strings                 | Mapping          | Easy       |
| ⬜     | 290 | Word Pattern                       | Mapping          | Easy       |
| ⬜     | 202 | Happy Number                       | Cycle Detection  | Easy       |
| ⬜     | 219 | Contains Duplicate II              | Lookup / Index   | Easy       |
| ⬜     | 705 | Design HashSet                     | Implementation   | Easy       |
| ⬜     | 706 | Design HashMap                     | Implementation   | Easy       |
| ⬜     | 49  | Group Anagrams                     | Grouping         | Medium     |
| ⬜     | 36  | Valid Sudoku                       | Lookup           | Medium     |
| ⬜     | 347 | Top K Frequent Elements            | Frequency Count  | Medium     |
| ⬜     | 451 | Sort Characters By Frequency       | Frequency Count  | Medium     |
| ⬜     | 560 | Subarray Sum Equals K              | Prefix Sum + Map | Medium     |
| ⬜     | 525 | Contiguous Array                   | Prefix Sum + Map | Medium     |
| ⬜     | 974 | Subarray Sums Divisible by K       | Prefix Sum + Map | Medium     |
| ⬜     | 454 | 4Sum II                            | Pair Lookup      | Medium     |
| ⬜     | 380 | Insert Delete GetRandom O(1)       | Map + Set Design | Medium     |
| ⬜     | 128 | Longest Consecutive Sequence       | Set Sequence     | Medium     |

---

## Chapter 1 — Frequency Count

Store `item -> count`. Learn manual counting first, then use `Counter` after the pattern is clear.

| Status | #   | Problem                            | Difficulty | File                                                               |
| ------ | --- | ---------------------------------- | ---------- | ------------------------------------------------------------------ |
| ⬜     | 242 | Valid Anagram                      | Easy       | frequency_count/LeetCode/242 Valid Anagram.py                      |
| ⬜     | 383 | Ransom Note                        | Easy       | frequency_count/LeetCode/383 Ransom Note.py                        |
| ⬜     | 387 | First Unique Character in a String | Easy       | frequency_count/LeetCode/387 First Unique Character in a String.py |
| ⬜     | 347 | Top K Frequent Elements            | Medium     | frequency_count/LeetCode/347 Top K Frequent Elements.py            |
| ⬜     | 451 | Sort Characters By Frequency       | Medium     | frequency_count/LeetCode/451 Sort Characters By Frequency.py       |

---

## Chapter 2 — Lookup and Pair Finding

Store information from earlier elements so the current element can find an answer in O(1) average time.

| Status | #   | Problem               | Difficulty | File                                         |
| ------ | --- | --------------------- | ---------- | -------------------------------------------- |
| ⬜     | 1   | Two Sum               | Easy       | lookup/LeetCode/1 Two Sum.py                 |
| ⬜     | 219 | Contains Duplicate II | Easy       | lookup/LeetCode/219 Contains Duplicate II.py |
| ⬜     | 36  | Valid Sudoku          | Medium     | lookup/LeetCode/36 Valid Sudoku.py           |
| ⬜     | 454 | 4Sum II               | Medium     | lookup/LeetCode/454 4Sum II.py               |

---

## Chapter 3 — Deduplication and Design

Use a set when only membership matters. Design problems make the underlying operations explicit.

| Status | #   | Problem                      | Difficulty | File                                                       |
| ------ | --- | ---------------------------- | ---------- | ---------------------------------------------------------- |
| ⬜     | 217 | Contains Duplicate           | Easy       | deduplication/LeetCode/217 Contains Duplicate.py           |
| ⬜     | 349 | Intersection of Two Arrays   | Easy       | deduplication/LeetCode/349 Intersection of Two Arrays.py   |
| ⬜     | 705 | Design HashSet               | Easy       | deduplication/LeetCode/705 Design HashSet.py               |
| ⬜     | 706 | Design HashMap               | Easy       | deduplication/LeetCode/706 Design HashMap.py               |
| ⬜     | 380 | Insert Delete GetRandom O(1) | Medium     | deduplication/LeetCode/380 Insert Delete GetRandom O(1).py |

---

## Chapter 4 — Grouping and Mapping

Use a canonical key for grouping, or maintain a one-to-one relationship with maps in both directions.

| Status | #   | Problem            | Difficulty | File                                                |
| ------ | --- | ------------------ | ---------- | --------------------------------------------------- |
| ⬜     | 205 | Isomorphic Strings | Easy       | grouping_mapping/LeetCode/205 Isomorphic Strings.py |
| ⬜     | 290 | Word Pattern       | Easy       | grouping_mapping/LeetCode/290 Word Pattern.py       |
| ⬜     | 49  | Group Anagrams     | Medium     | grouping_mapping/LeetCode/49 Group Anagrams.py      |

---

## Chapter 5 — Sequence and Cycle Detection

Use set membership to find repeated states or to expand a sequence only from its true starting value.

| Status | #   | Problem                      | Difficulty | File                                                        |
| ------ | --- | ---------------------------- | ---------- | ----------------------------------------------------------- |
| ⬜     | 202 | Happy Number                 | Easy       | sequence_cycle/LeetCode/202 Happy Number.py                 |
| ⬜     | 128 | Longest Consecutive Sequence | Medium     | sequence_cycle/LeetCode/128 Longest Consecutive Sequence.py |

---

## Chapter 6 — Prefix Sum + HashMap

Store information about earlier prefix sums so each current prefix can find the required previous state in O(1) average time.

| Status | #   | Problem                      | Difficulty | File                                                            |
| ------ | --- | ---------------------------- | ---------- | --------------------------------------------------------------- |
| ⬜     | 560 | Subarray Sum Equals K        | Medium     | prefix_sum_hashmap/LeetCode/560 Subarray Sum Equals K.py        |
| ⬜     | 525 | Contiguous Array             | Medium     | prefix_sum_hashmap/LeetCode/525 Contiguous Array.py             |
| ⬜     | 974 | Subarray Sums Divisible by K | Medium     | prefix_sum_hashmap/LeetCode/974 Subarray Sums Divisible by K.py |

"""
CHALLENGE: Two Sum
Difficulty: Intermediate
Teacher: Petra

Pythonic thinking is about elegance and readability!

Problem:
Given a list of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to the target.

You may assume each input has exactly one solution, and you cannot use the same
element twice (i.e., you need two distinct indices).

Examples:
    two_sum([2, 7, 11, 15], 9)  -> (0, 1)
    nums[0] + nums[1] = 2 + 7 = 9

    two_sum([3, 2, 4], 6)       -> (1, 2)
    nums[1] + nums[2] = 2 + 4 = 6

    two_sum([3, 3], 6)          -> (0, 1)
    nums[0] + nums[1] = 3 + 3 = 6 (same value, different indices - valid)

Requirements:
- Return a tuple of two indices
- Aim for O(n) time complexity
- Return None if no solution exists

Approach:
The brute-force solution uses nested loops to check every pair - O(n²) time.

The optimal approach uses a dictionary. For each number, calculate its complement
(target - num). If the complement is already in the dictionary, you've found your
pair. Otherwise, store the current number and its index for future lookups.

This works because dictionary key lookups are O(1), so you only need one pass
through the list.
"""

def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    # Your code here

    groups = {}

    for i, n in enumerate(nums):

        complement = target - n
        if complement in groups:
            return (groups[complement], i)
        else:
            groups[n] = i

    return None




# Test cases - uncomment to verify your solutiondwdadw
print(two_sum([2, 7, 11, 15], 9))  # Expected: (0, 1)
print(two_sum([3, 2, 4], 6))       # Expected: (1, 2)
print(two_sum([3, 3], 6))          # Expected: (0, 1)
print(two_sum([1, 2, 3], 10))      # Expected: None


# ============================================================
# FEEDBACK from Petra
# ============================================================
#
# What worked well:
# - Clean, correct O(n) solution using a hash map — exactly the
#   optimal approach for this classic problem.
# - Good use of enumerate() to track indices without resorting
#   to nums.index(), which would have been O(n) per call.
# - The complement logic is clear and easy to follow.
# - Properly returns None when no solution exists.
#
# Areas for improvement:
# - You can drop the `else` — since the `if` branch returns,
#   the code after it only runs when the condition is false.
#   This is a minor style point but common in idiomatic Python.
# - Clean up the leftover "dwdadw" in the test case comment!
#
# Alternative approaches:
# - Brute force: nested loops checking all pairs — O(n²) time,
#   O(1) space. Simple but doesn't scale.
# - Sorting + two pointers: sort a copy, use left/right pointers
#   moving inward. O(n log n) time, but you'd need to track
#   original indices which adds complexity.
# - Your hash map approach is the standard optimal solution.
#   Well done!
#
# ============================================================

"""
CHALLENGE: Anagram Groups
Difficulty: Intermediate
Teacher: Petra

Good morning! Pythonic thinking is about elegance and readability!

Today we're grouping words by their anagram families. An anagram is a word formed
by rearranging the letters of another word (e.g., "listen" and "silent").

Given a list of words, group them so that all anagrams are together.

Requirements:
- Write a function `group_anagrams(words)` that takes a list of strings
- Return a list of lists, where each inner list contains words that are anagrams
- Words should be compared case-insensitively ("Listen" and "silent" are anagrams)
- Each group should preserve the original casing of the words
- Single words with no anagram partners should still appear in their own group

Example:
    Input: ["listen", "silent", "enlist", "hello", "world", "cat", "act", "tac"]
    Output: [["listen", "silent", "enlist"], ["hello"], ["world"], ["cat", "act", "tac"]]
    (Note: group order may vary, but contents should match)

Hints:
- Think about what makes two words anagrams - what do they have in common?
- Dictionaries are great for grouping things by a common key
- Python's `sorted()` function works on strings too!

Test your solution:
    words = ["listen", "Silent", "enlist", "google", "elgoog", "python", "cat", "Act"]
    print(group_anagrams(words))
"""

# Your code here

def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams = []

    for i in range(len(words)):
        temp = []
        
        for j in range(len(words)):
            if sorted(words[i].lower()) == sorted(words[j].lower()):
                temp.append(words[j])

        if temp is not [] and temp not in anagrams:
            anagrams.append(temp)

    return anagrams






if __name__ == '__main__':
	
    words = ["listen", "silent", "enlist", "hello", "world", "cat", "act", "tac"]
    words_grouped = [["listen", "silent", "enlist"], ["hello"], ["world"], ["cat", "act", "tac"]]
    anagrams = group_anagrams(words)


# ============================================================
# FEEDBACK
# ============================================================
#
# What worked well:
# - Correct use of sorted() + lower() to identify anagrams
# - Preserves original casing in output
# - Type hints are a nice professional touch
# - The logic produces correct results!
#
# Areas for improvement:
# - Line 47: `temp is not []` is a subtle bug! The `is` operator checks
#   object identity, not equality. This always returns True because temp
#   is a different object than the new empty list `[]`. It works here by
#   accident since temp always has at least one item (the word matches itself).
#   Use `if temp:` or `if temp != []` instead.
#
# - The nested loops give O(n²) complexity, and `temp not in anagrams`
#   adds another O(n) check per iteration. For large inputs this gets slow.
#
# - More Pythonic: iterate directly over items instead of indices:
#       for word in words:  # instead of for i in range(len(words))
#
# Alternative approach (O(n) with a dictionary):
#
#   def group_anagrams(words):
#       groups = {}
#       for word in words:
#           key = tuple(sorted(word.lower()))
#           groups.setdefault(key, []).append(word)
#       return list(groups.values())
#
# The dictionary approach uses the sorted letters as a key, so each word
# is processed exactly once. This is the "Pythonic" way - using the right
# data structure makes the code simpler AND faster.
#
# Great job getting a working solution! Now you've seen how dictionaries
# can turn an O(n²) problem into O(n).
# ============================================================

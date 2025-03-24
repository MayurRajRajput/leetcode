# Word Pattern
""" 
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):return False
        word_pattern = {}
        pattern_word = {}
        for p,w in zip(pattern,words):
            if p in pattern_word:
                if pattern_word[p]!=w:
                    return False
            else:
                if w in word_pattern and word_pattern[w]!=p:
                    return False
                pattern_word[p]=w
                word_pattern[w]=p
        return True                    
pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
res = sol.wordPattern(pattern,s)
print(res)
""" 
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false


"""
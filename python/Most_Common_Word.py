# Most Common Word
""" 
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.
"""
from typing import List 
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        split_chars = r"[ !?',;.]"
        words = [word.lower() for word in re.split(split_chars, paragraph) if word and word.lower() not in banned]
        w_dict = {}
        for w in words:
            if w not in w_dict:
                w_dict[w] = 0
            w_dict[w] += 1
        max_so_far = 0
        max_word = ""
        for k, v in w_dict.items():
            if v > max_so_far:
                max_so_far = v
                max_word = k
        return max_word
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
res = sol.mostCommonWord(paragraph,banned)
print(res)
""" 
Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 
"""
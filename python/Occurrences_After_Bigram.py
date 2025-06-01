# Occurrences After Bigram
""" 
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

"""
from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        third = []
        sen = list(text.split())
        for i in range(1, len(sen)-1):
            if sen[i-1] == first and sen[i] == second:
                third.append(sen[i+1])
        return third
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
sol =Solution()
res = sol.findOcurrences(text,first,second)
print(res) 
""" 
Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
 
"""
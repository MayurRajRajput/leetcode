# Letter Combinations of a Phone Number
""" 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            '2':"abc",'3':"def",'4':"ghi",'5':"jkl",
            '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"
        }
        res = []
        def backtrack(index,path):
            if index == len(digits):
                res.append("".join(path))
                return
            for char in phone_map[digits[index]]:
                path.append(char)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return res
digits = "23"
sol =Solution()
res = sol.letterCombinations(digits)
print(res)  
""" 
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
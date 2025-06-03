# Day of the Year
""" 
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
"""
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
        return d + sum(days[:m-1])
date = "2019-01-09"
sol = Solution()
res = sol.dayOfYear(date)
print(res)
""" 
Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
 
"""
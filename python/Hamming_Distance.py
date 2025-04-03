# Hamming Distance
""" 
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 or y >0:
            xbit = x&1
            ybit = y&1
            if xbit != ybit:
                dist +=1
            x>>=1
            y>>=1
        return dist 
x = 1
y = 4
sol = Solution()
res = sol.hammingDistance(x,y)
print(res)
""" 
Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 
"""
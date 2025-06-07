# Restore IP Addresses
""" 
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
"""
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start: int, current: List[str]):
            if len(current) == 4:
                if start == len(s):
                    result.append('.'.join(current))
                return
            for length in range(1, 4):  # 1 to 3 digits
                if start + length > len(s):
                    break
                segment = s[start:start + length]
                if self.is_valid(segment):
                    current.append(segment)
                    backtrack(start + length, current)
                    current.pop()

        result = []
        backtrack(0, [])
        return result

    def is_valid(self, segment: str) -> bool:
        if len(segment) > 1 and segment[0] == '0':
            return False
        return 0 <= int(segment) <= 255

# Example usage
sol = Solution()

s1 = "25525511135"
print(sol.restoreIpAddresses(s1))  # Output: ["255.255.11.135", "255.255.111.35"]

s2 = "0000"
print(sol.restoreIpAddresses(s2))  # Output: ["0.0.0.0"]

s3 = "101023"
print(sol.restoreIpAddresses(s3))  # Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

""" 
Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
"""
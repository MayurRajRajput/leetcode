# Defanging an IP Address
""" 
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address2 = list(address) 
        output = []  
    
        for i in address2:
            if i == ".":
                output.extend(["[", ".", "]"])  
            else:
                output.append(i) 
        return ''.join(output) 
address = "1.1.1.1"
sol =Solution()
res = sol.defangIPaddr(address)
print(res)
""" 
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 
"""